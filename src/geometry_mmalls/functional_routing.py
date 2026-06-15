"""Functional routing primitives for Geometry-MMALS G1 v1.1.x.

The module keeps architecture, geometry and evaluation primitives explicit so
that the v1.1.0 notebook can test the bridge ``context -> route -> hosts``
without hiding protocol assumptions inside a trainer.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, Sequence

import numpy as np
import torch
from torch import nn
import torch.nn.functional as F


class MLPContextRouter(nn.Module):
    """Flexible context-only router used as the R0 baseline."""

    def __init__(self, context_dim: int, num_hosts: int, hidden_dim: int = 64) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(context_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, num_hosts),
        )

    def forward(self, context: torch.Tensor, temperature: float = 1.0) -> torch.Tensor:
        if temperature <= 0:
            raise ValueError("temperature must be positive")
        return torch.softmax(self.net(context) / float(temperature), dim=-1)


class LinearContextRouter(nn.Module):
    """Low-capacity R1 router testing simple transmission of context order."""

    def __init__(self, context_dim: int, num_hosts: int) -> None:
        super().__init__()
        self.linear = nn.Linear(context_dim, num_hosts)

    def forward(self, context: torch.Tensor, temperature: float = 1.0) -> torch.Tensor:
        if temperature <= 0:
            raise ValueError("temperature must be positive")
        return torch.softmax(self.linear(context) / float(temperature), dim=-1)


class PrototypeEnergyRouter(nn.Module):
    """R2 geometric router with one learnable context prototype per host.

    The first energy term of the broader MMALS Energy-Guided Router is

    ``E_h(c) = d_C(c, mu_h)^2 / (2 sigma_h^2) + b_h``

    where ``d_C`` is half the Euclidean chord on the unit sphere.
    """

    def __init__(
        self,
        context_dim: int,
        num_hosts: int,
        *,
        sigma_min: float = 0.05,
        temperature: float = 1.0,
    ) -> None:
        super().__init__()
        if context_dim < 2:
            raise ValueError("context_dim must be at least 2")
        if num_hosts < 2:
            raise ValueError("num_hosts must be at least 2")
        if sigma_min <= 0:
            raise ValueError("sigma_min must be positive")
        if temperature <= 0:
            raise ValueError("temperature must be positive")
        self.context_dim = int(context_dim)
        self.num_hosts = int(num_hosts)
        self.sigma_min = float(sigma_min)
        self.default_temperature = float(temperature)
        initial = F.normalize(torch.randn(num_hosts, context_dim), dim=-1)
        self.prototype_raw = nn.Parameter(initial)
        self.bandwidth_raw = nn.Parameter(torch.zeros(num_hosts))
        self.bias = nn.Parameter(torch.zeros(num_hosts))

    @property
    def prototypes(self) -> torch.Tensor:
        return F.normalize(self.prototype_raw, p=2, dim=-1)

    @property
    def bandwidths(self) -> torch.Tensor:
        return self.sigma_min + F.softplus(self.bandwidth_raw)

    def energies(self, context: torch.Tensor) -> torch.Tensor:
        context = F.normalize(context, p=2, dim=-1)
        delta = context[:, None, :] - self.prototypes[None, :, :]
        half_chord_sq = 0.25 * torch.square(delta).sum(dim=-1)
        sigma_sq = torch.square(self.bandwidths)[None, :]
        return half_chord_sq / (2.0 * sigma_sq) + self.bias[None, :]

    def forward(self, context: torch.Tensor, temperature: float | None = None) -> torch.Tensor:
        tau = self.default_temperature if temperature is None else float(temperature)
        if tau <= 0:
            raise ValueError("temperature must be positive")
        return torch.softmax(-self.energies(context) / tau, dim=-1)

    @torch.no_grad()
    def project_prototypes_(self) -> None:
        self.prototype_raw.copy_(F.normalize(self.prototype_raw, p=2, dim=-1))

    @torch.no_grad()
    def initialize_from_contexts(
        self,
        contexts: torch.Tensor,
        *,
        seed: int = 0,
        iterations: int = 50,
    ) -> dict[str, float]:
        centers, assignments = spherical_kmeans(
            contexts,
            self.num_hosts,
            seed=seed,
            iterations=iterations,
        )
        self.prototype_raw.copy_(centers.to(self.prototype_raw))
        distances = half_chord_distance(
            F.normalize(contexts, dim=-1)[:, None, :],
            centers.to(contexts)[None, :, :],
        )
        selected = distances.gather(1, assignments[:, None]).squeeze(1)
        global_scale = selected.median().clamp_min(self.sigma_min * 1.5)
        scales = []
        for host in range(self.num_hosts):
            values = selected[assignments == host]
            scales.append(values.median() if values.numel() else global_scale)
        sigma = torch.stack(scales).clamp_min(self.sigma_min * 1.01)
        # inverse softplus(sigma - sigma_min)
        raw = torch.log(torch.expm1((sigma - self.sigma_min).clamp_min(1e-6)))
        self.bandwidth_raw.copy_(raw.to(self.bandwidth_raw))
        return {
            "mean_assignment_distance": float(selected.mean().cpu()),
            "min_cluster_count": int(torch.bincount(assignments, minlength=self.num_hosts).min()),
        }


class UniformRouter(nn.Module):
    """Parameter-free router used to construct a neutral common host bank."""

    def __init__(self, num_hosts: int) -> None:
        super().__init__()
        if num_hosts < 2:
            raise ValueError("num_hosts must be at least 2")
        self.num_hosts = int(num_hosts)

    def forward(self, context: torch.Tensor, temperature: float = 1.0) -> torch.Tensor:
        if temperature <= 0:
            raise ValueError("temperature must be positive")
        return torch.full(
            (context.shape[0], self.num_hosts),
            1.0 / self.num_hosts,
            dtype=context.dtype,
            device=context.device,
        )


class HybridDirectionalPrototypeRouter(PrototypeEnergyRouter):
    """R3 router combining local prototype territories and global directions.

    ``E_h(c) = alpha*d_C(c,mu_h)^2/(2*sigma_h^2) - beta*<a_h,c> + b_h``.
    """

    def __init__(
        self,
        context_dim: int,
        num_hosts: int,
        *,
        sigma_min: float = 0.05,
        temperature: float = 1.0,
        prototype_weight: float = 1.0,
        directional_weight: float = 1.0,
        learnable_mixture: bool = True,
    ) -> None:
        super().__init__(context_dim, num_hosts, sigma_min=sigma_min, temperature=temperature)
        if prototype_weight <= 0 or directional_weight <= 0:
            raise ValueError("energy mixture weights must be positive")
        self.direction_raw = nn.Parameter(F.normalize(torch.randn(num_hosts, context_dim), dim=-1))
        self.learnable_mixture = bool(learnable_mixture)
        p_raw = torch.tensor(math.log(math.expm1(float(prototype_weight))), dtype=torch.float32)
        d_raw = torch.tensor(math.log(math.expm1(float(directional_weight))), dtype=torch.float32)
        if self.learnable_mixture:
            self.prototype_weight_raw = nn.Parameter(p_raw)
            self.directional_weight_raw = nn.Parameter(d_raw)
        else:
            self.register_buffer("prototype_weight_raw", p_raw)
            self.register_buffer("directional_weight_raw", d_raw)

    @property
    def directions(self) -> torch.Tensor:
        return F.normalize(self.direction_raw, p=2, dim=-1, eps=1e-8)

    @property
    def prototype_weight(self) -> torch.Tensor:
        return F.softplus(self.prototype_weight_raw).clamp_min(1e-6)

    @property
    def directional_weight(self) -> torch.Tensor:
        return F.softplus(self.directional_weight_raw).clamp_min(1e-6)

    def energy_components(self, context: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        context = F.normalize(context, p=2, dim=-1, eps=1e-8)
        delta = context[:, None, :] - self.prototypes[None, :, :]
        half_chord_sq = 0.25 * torch.square(delta).sum(dim=-1)
        sigma_sq = torch.square(self.bandwidths)[None, :]
        local = half_chord_sq / (2.0 * sigma_sq)
        directional = context @ self.directions.T
        return local, directional

    def energies(self, context: torch.Tensor) -> torch.Tensor:
        local, directional = self.energy_components(context)
        return self.prototype_weight * local - self.directional_weight * directional + self.bias[None, :]

    @torch.no_grad()
    def project_parameters_(self) -> None:
        self.project_prototypes_()
        self.direction_raw.copy_(F.normalize(self.direction_raw, p=2, dim=-1))

    @torch.no_grad()
    def initialize_from_contexts(self, contexts: torch.Tensor, *, seed: int = 0, iterations: int = 50) -> dict[str, float]:
        diagnostics = super().initialize_from_contexts(contexts, seed=seed, iterations=iterations)
        generator = torch.Generator(device=contexts.device)
        generator.manual_seed(int(seed) + 73)
        noise = 0.05 * torch.randn(self.prototypes.shape, generator=generator, device=contexts.device, dtype=contexts.dtype)
        self.direction_raw.copy_(F.normalize(self.prototypes.to(contexts) + noise, dim=-1).to(self.direction_raw))
        diagnostics.update({
            "prototype_weight": float(self.prototype_weight.detach().cpu()),
            "directional_weight": float(self.directional_weight.detach().cpu()),
        })
        return diagnostics


class SmoothSimplexResidualRouter(PrototypeEnergyRouter):
    """Linear-first router with a bounded, centered prototype residual.

    The route logits are

    ``l(c) = Wc + b + g(c) * s_max * tanh(delta_proto(c))``.

    The linear path carries the global direction. The prototype residual is
    zero-centered across hosts and bounded by ``residual_cap`` so local
    territories cannot dominate the route map as they did in v1.1.1.
    """

    def __init__(
        self,
        context_dim: int,
        num_hosts: int,
        *,
        sigma_min: float = 0.05,
        temperature: float = 1.0,
        residual_cap: float = 0.35,
        gate_hidden_dim: int = 16,
        learnable_cap: bool = False,
    ) -> None:
        super().__init__(
            context_dim=context_dim,
            num_hosts=num_hosts,
            sigma_min=sigma_min,
            temperature=temperature,
        )
        if residual_cap <= 0:
            raise ValueError("residual_cap must be positive")
        self.linear = nn.Linear(context_dim, num_hosts)
        self.gate = nn.Sequential(
            nn.Linear(context_dim, gate_hidden_dim),
            nn.Tanh(),
            nn.Linear(gate_hidden_dim, 1),
        )
        cap_logit = math.log(0.5 / 0.5)
        if learnable_cap:
            self.cap_logit = nn.Parameter(torch.tensor(cap_logit, dtype=torch.float32))
        else:
            self.register_buffer("cap_logit", torch.tensor(cap_logit, dtype=torch.float32))
        self.residual_cap_max = float(residual_cap)
        self.learnable_cap = bool(learnable_cap)

    @property
    def residual_cap(self) -> torch.Tensor:
        return self.residual_cap_max * torch.sigmoid(self.cap_logit)

    def prototype_residual(self, context: torch.Tensor) -> torch.Tensor:
        context = F.normalize(context, p=2, dim=-1, eps=1e-8)
        delta = context[:, None, :] - self.prototypes[None, :, :]
        half_chord_sq = 0.25 * torch.square(delta).sum(dim=-1)
        sigma_sq = torch.square(self.bandwidths)[None, :]
        score = -half_chord_sq / (2.0 * sigma_sq) - self.bias[None, :]
        score = score - score.mean(dim=-1, keepdim=True)
        scale = score.detach().std(dim=-1, keepdim=True).clamp_min(1e-4)
        return torch.tanh(score / scale)

    def components(self, context: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        normalized = F.normalize(context, p=2, dim=-1, eps=1e-8)
        base_logits = self.linear(normalized)
        gate = torch.sigmoid(self.gate(normalized))
        residual = self.residual_cap * gate * self.prototype_residual(normalized)
        return base_logits, residual, gate

    def forward(self, context: torch.Tensor, temperature: float | None = None) -> torch.Tensor:
        tau = self.default_temperature if temperature is None else float(temperature)
        if tau <= 0:
            raise ValueError("temperature must be positive")
        base_logits, residual, _ = self.components(context)
        return torch.softmax((base_logits + residual) / tau, dim=-1)

    @torch.no_grad()
    def project_parameters_(self) -> None:
        self.project_prototypes_()

    @torch.no_grad()
    def initialize_from_contexts(
        self,
        contexts: torch.Tensor,
        *,
        seed: int = 0,
        iterations: int = 50,
    ) -> dict[str, float]:
        diagnostics = super().initialize_from_contexts(
            contexts,
            seed=seed,
            iterations=iterations,
        )
        diagnostics.update({
            "residual_cap": float(self.residual_cap.detach().cpu()),
            "learnable_cap": int(self.learnable_cap),
        })
        return diagnostics


def simplex_continuity_hinge_loss(
    routes: torch.Tensor,
    contexts: torch.Tensor,
    *,
    kappa: float = 1.0,
    margin: float = 0.0,
) -> torch.Tensor:
    """Context-only Lipschitz hinge on route-simplex movement.

    ``routes`` has shape ``[batch, views, hosts]`` and ``contexts`` has shape
    ``[batch, views, context_dim]``. No external factor label is used.
    """
    if routes.ndim != 3 or contexts.ndim != 3:
        raise ValueError("routes and contexts must be rank-3 tensors")
    if routes.shape[:2] != contexts.shape[:2]:
        raise ValueError("routes and contexts must share batch/view dimensions")
    if kappa <= 0 or margin < 0:
        raise ValueError("kappa must be positive and margin non-negative")
    n_views = routes.shape[1]
    if n_views < 2:
        return routes.sum() * 0.0
    index = torch.triu_indices(n_views, n_views, offset=1, device=routes.device)
    route_a, route_b = routes[:, index[0]], routes[:, index[1]]
    context_a, context_b = contexts[:, index[0]], contexts[:, index[1]]
    d_route = root_simplex_chord(route_a, route_b)
    d_context = half_chord_distance(context_a, context_b)
    violation = d_route - float(kappa) * d_context - float(margin)
    return torch.relu(violation).square().mean()


@dataclass
class FunctionalRoutingTrace:
    z0: torch.Tensor
    context: torch.Tensor
    route: torch.Tensor
    host_outputs: torch.Tensor
    z_mm: torch.Tensor
    logits: torch.Tensor
    context_raw: torch.Tensor | None = None


class FunctionalRoutingMMALS(nn.Module):
    """MMALS model with a frozen sensory/context representation and pluggable router."""

    def __init__(
        self,
        encoder: nn.Module,
        context_net: nn.Module,
        router: nn.Module,
        hosts: Sequence[nn.Module],
        synthesis_norm: nn.Module,
        classifier: nn.Module,
        *,
        freeze_encoder: bool = True,
        freeze_context: bool = True,
    ) -> None:
        super().__init__()
        self.encoder = encoder
        self.context_net = context_net
        self.router = router
        self.hosts = nn.ModuleList(hosts)
        self.synthesis_norm = synthesis_norm
        self.classifier = classifier
        self.freeze_encoder = bool(freeze_encoder)
        self.freeze_context = bool(freeze_context)
        if self.freeze_encoder:
            for parameter in self.encoder.parameters():
                parameter.requires_grad_(False)
        if self.freeze_context:
            for parameter in self.context_net.parameters():
                parameter.requires_grad_(False)

    def encode(self, x: torch.Tensor) -> torch.Tensor:
        if self.freeze_encoder:
            self.encoder.eval()
            with torch.no_grad():
                return self.encoder(x)
        return self.encoder(x)

    def infer_context(self, z0: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        if self.freeze_context:
            self.context_net.eval()
            with torch.no_grad():
                raw = self.context_net(z0)
        else:
            raw = self.context_net(z0)
        return raw, F.normalize(raw, p=2, dim=-1, eps=1e-8)

    def route_context(self, context: torch.Tensor, temperature: float = 1.0) -> torch.Tensor:
        return self.router(context, temperature=temperature)

    def synthesize(
        self,
        z0: torch.Tensor,
        context: torch.Tensor,
        route: torch.Tensor,
        *,
        context_raw: torch.Tensor | None = None,
    ) -> FunctionalRoutingTrace:
        host_outputs = torch.stack([host(z0) for host in self.hosts], dim=1)
        z_mm = torch.einsum("bh,bhd->bd", route, host_outputs)
        z_mm = self.synthesis_norm(z_mm)
        logits = self.classifier(z_mm)
        return FunctionalRoutingTrace(
            z0=z0,
            context=context,
            route=route,
            host_outputs=host_outputs,
            z_mm=z_mm,
            logits=logits,
            context_raw=context_raw,
        )

    def forward(self, x: torch.Tensor, temperature: float = 1.0) -> FunctionalRoutingTrace:
        z0 = self.encode(x)
        raw, context = self.infer_context(z0)
        route = self.route_context(context, temperature=temperature)
        return self.synthesize(z0, context, route, context_raw=raw)



def parameter_count(module: nn.Module, *, trainable_only: bool = True) -> int:
    params = module.parameters()
    if trainable_only:
        params = (p for p in params if p.requires_grad)
    return int(sum(p.numel() for p in params))


def half_chord_distance(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """Half Euclidean chord between unit-normalized context vectors."""
    a = F.normalize(a, p=2, dim=-1, eps=1e-8)
    b = F.normalize(b, p=2, dim=-1, eps=1e-8)
    return 0.5 * torch.linalg.vector_norm(a - b, dim=-1)


def root_simplex_chord(a: torch.Tensor, b: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    """Stable normalized chord between categorical routes."""
    a = a.clamp_min(eps); a = a / a.sum(dim=-1, keepdim=True)
    b = b.clamp_min(eps); b = b / b.sum(dim=-1, keepdim=True)
    return torch.linalg.vector_norm(torch.sqrt(a) - torch.sqrt(b), dim=-1) / math.sqrt(2.0)


def usage_balance_loss(routes: torch.Tensor) -> torch.Tensor:
    """Penalize deviation of mean host use from a uniform allocation."""
    if routes.ndim < 2:
        raise ValueError("routes must end with a host dimension")
    mean_route = routes.reshape(-1, routes.shape[-1]).mean(dim=0)
    target = torch.full_like(mean_route, 1.0 / mean_route.numel())
    return torch.square(mean_route - target).sum()


def host_functional_diversity_loss(host_outputs: torch.Tensor) -> torch.Tensor:
    """Squared off-diagonal cosine similarity; minimizing encourages diversity."""
    if host_outputs.ndim != 3:
        raise ValueError("host_outputs must have shape [batch, hosts, dim]")
    normalized = F.normalize(host_outputs, p=2, dim=-1, eps=1e-8)
    similarity = torch.einsum("bhd,bkd->bhk", normalized, normalized)
    mask = ~torch.eye(similarity.shape[-1], dtype=torch.bool, device=similarity.device)
    return torch.square(similarity[:, mask]).mean()


def spherical_kmeans(
    contexts: torch.Tensor,
    clusters: int,
    *,
    seed: int = 0,
    iterations: int = 50,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Deterministic spherical k-means without factor labels."""
    x = F.normalize(contexts.detach(), p=2, dim=-1, eps=1e-8)
    if x.ndim != 2:
        raise ValueError("contexts must have shape [samples, context_dim]")
    if not 1 < clusters <= len(x):
        raise ValueError("clusters must be between 2 and the sample count")
    generator = torch.Generator(device=x.device)
    generator.manual_seed(int(seed))
    first = int(torch.randint(len(x), (1,), generator=generator, device=x.device))
    chosen = [first]
    min_distance = 1.0 - (x @ x[first]).clamp(-1.0, 1.0)
    for _ in range(1, clusters):
        probabilities = min_distance.clamp_min(1e-12)
        probabilities = probabilities / probabilities.sum()
        index = int(torch.multinomial(probabilities, 1, generator=generator))
        chosen.append(index)
        distance = 1.0 - (x @ x[index]).clamp(-1.0, 1.0)
        min_distance = torch.minimum(min_distance, distance)
    centers = x[torch.tensor(chosen, device=x.device)].clone()
    assignments = torch.zeros(len(x), dtype=torch.long, device=x.device)
    for _ in range(int(iterations)):
        assignments = torch.argmax(x @ centers.T, dim=1)
        updated = []
        for cluster in range(clusters):
            members = x[assignments == cluster]
            if members.numel() == 0:
                farthest = torch.argmin(torch.max(x @ centers.T, dim=1).values)
                updated.append(x[farthest])
            else:
                updated.append(F.normalize(members.mean(dim=0), dim=0))
        new_centers = torch.stack(updated)
        if torch.allclose(new_centers, centers, atol=1e-6, rtol=0.0):
            centers = new_centers
            break
        centers = new_centers
    assignments = torch.argmax(x @ centers.T, dim=1)
    return centers, assignments


def host_output_cost_matrix(
    host_outputs: torch.Tensor,
    *,
    normalize: bool = True,
    eps: float = 1e-12,
) -> torch.Tensor:
    """Build the evaluation-only host-function cost matrix ``C``.

    ``host_outputs`` has shape ``[samples, hosts, representation_dim]``.
    """
    if host_outputs.ndim != 3:
        raise ValueError("host_outputs must have shape [samples, hosts, dim]")
    dim = max(host_outputs.shape[-1], 1)
    delta = host_outputs[:, :, None, :] - host_outputs[:, None, :, :]
    cost = torch.square(delta).sum(dim=-1).mean(dim=0) / float(dim)
    cost = 0.5 * (cost + cost.T)
    cost.fill_diagonal_(0.0)
    if normalize:
        nonzero = cost[cost > eps]
        if nonzero.numel():
            cost = cost / nonzero.median().clamp_min(eps)
    return cost


def entropic_transport_cost(
    a: torch.Tensor,
    b: torch.Tensor,
    cost: torch.Tensor,
    *,
    epsilon: float = 0.05,
    iterations: int = 100,
    eps: float = 1e-12,
) -> torch.Tensor:
    """Batched Sinkhorn transport cost between route distributions.

    The returned quantity is ``<Pi, C>`` for the entropically regularized
    transport plan. ``a`` and ``b`` may have arbitrary shared leading shape.
    """
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    if cost.ndim != 2 or cost.shape[0] != cost.shape[1]:
        raise ValueError("cost must be a square matrix")
    if a.shape != b.shape or a.shape[-1] != cost.shape[0]:
        raise ValueError("route shapes and cost size are inconsistent")
    leading = a.shape[:-1]
    hosts = a.shape[-1]
    a2 = a.reshape(-1, hosts).clamp_min(eps)
    b2 = b.reshape(-1, hosts).clamp_min(eps)
    a2 = a2 / a2.sum(dim=-1, keepdim=True)
    b2 = b2 / b2.sum(dim=-1, keepdim=True)
    kernel = torch.exp(-cost.to(a2) / float(epsilon)).clamp_min(eps)
    u = torch.ones_like(a2)
    v = torch.ones_like(b2)
    for _ in range(int(iterations)):
        u = a2 / (v @ kernel.T).clamp_min(eps)
        v = b2 / (u @ kernel).clamp_min(eps)
    plan = u[:, :, None] * kernel[None, :, :] * v[:, None, :]
    value = (plan * cost.to(plan)[None, :, :]).sum(dim=(1, 2))
    return value.reshape(leading)


def pairwise_functional_route_distances(
    routes: torch.Tensor,
    cost: torch.Tensor,
    *,
    epsilon: float = 0.05,
    iterations: int = 100,
) -> torch.Tensor:
    """Full pairwise functional route-distance matrix for ``[items, hosts]``."""
    if routes.ndim != 2:
        raise ValueError("routes must have shape [items, hosts]")
    n = routes.shape[0]
    left = routes[:, None, :].expand(n, n, -1)
    right = routes[None, :, :].expand(n, n, -1)
    matrix = entropic_transport_cost(
        left,
        right,
        cost,
        epsilon=epsilon,
        iterations=iterations,
    )
    matrix = 0.5 * (matrix + matrix.T)
    matrix.fill_diagonal_(0.0)
    return matrix


def route_entropy(routes: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    p = routes.clamp_min(eps)
    p = p / p.sum(dim=-1, keepdim=True)
    return -(p * torch.log(p)).sum(dim=-1)


def host_territory(routes: torch.Tensor, factors: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    """Return sorted factors and mean host activation ``A_h(u)``."""
    factors = factors.reshape(-1)
    if routes.ndim != 2 or len(routes) != len(factors):
        raise ValueError("routes and factors must share the sample dimension")
    unique = torch.unique(factors, sorted=True)
    territory = torch.stack([routes[factors == value].mean(dim=0) for value in unique])
    return unique, territory


def host_specialization(territory: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    """Entropy-normalized specialization for territory ``[factors, hosts]``."""
    if territory.ndim != 2:
        raise ValueError("territory must have shape [factors, hosts]")
    p = territory / territory.sum(dim=0, keepdim=True).clamp_min(eps)
    entropy = -(p.clamp_min(eps) * torch.log(p.clamp_min(eps))).sum(dim=0)
    return 1.0 - entropy / math.log(max(territory.shape[0], 2))


def territory_overlap(territory: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    """Pairwise overlap of normalized host territories."""
    p = territory / territory.sum(dim=0, keepdim=True).clamp_min(eps)
    overlap = torch.minimum(p[:, :, None], p[:, None, :]).sum(dim=0)
    overlap.fill_diagonal_(1.0)
    return overlap


def reconstruct_route_from_root_probe(root_prediction: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    positive = np.clip(np.asarray(root_prediction, dtype=np.float64), 0.0, None)
    squared = positive ** 2
    return squared / np.clip(squared.sum(axis=-1, keepdims=True), eps, None)



def local_continuity_ratio(
    context_a: torch.Tensor,
    context_b: torch.Tensor,
    route_distance: torch.Tensor,
    *,
    eps: float = 1e-8,
) -> torch.Tensor:
    """Output/input distance ratio for local routing continuity audits."""
    return route_distance / half_chord_distance(context_a, context_b).clamp_min(eps)


def permute_hosts_and_routes(
    routes: torch.Tensor,
    host_outputs: torch.Tensor,
    permutation: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Apply the same host permutation to routes and host outputs."""
    if permutation.ndim != 1:
        raise ValueError("permutation must be one-dimensional")
    if routes.shape[-1] != len(permutation) or host_outputs.shape[-2] != len(permutation):
        raise ValueError("permutation size does not match the host dimension")
    return routes[..., permutation], host_outputs[..., permutation, :]


def route_weighted_synthesis(routes: torch.Tensor, host_outputs: torch.Tensor) -> torch.Tensor:
    """Synthesize host outputs for arbitrary leading sample dimensions."""
    if routes.shape[:-1] != host_outputs.shape[:-2]:
        raise ValueError("route and host-output leading dimensions do not match")
    return torch.einsum("...h,...hd->...d", routes, host_outputs)
