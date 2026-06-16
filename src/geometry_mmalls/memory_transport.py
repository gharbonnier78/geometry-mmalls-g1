"""Functional memory transport utilities for Geometry-MMALS G1 v1.1.3.

The module isolates memory objectives from router architecture. It supports:
- nominal route anchoring on the probability simplex;
- functional route transport under a frozen host-cost matrix;
- latent/output preservation;
- empirical distribution transport between route clouds;
- path-length and path-excess diagnostics;
- compact root-simplex Gaussian summaries.

All functions are classical and deterministic given their inputs. No claim of
optimality or Riemannian learning is implied by using these diagnostics.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import torch
import torch.nn.functional as F

from .functional_routing import entropic_transport_cost


def root_route_anchor_loss(current: torch.Tensor, reference: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    """Mean squared root-simplex distance between paired routes."""
    if current.shape != reference.shape:
        raise ValueError("current and reference routes must have identical shapes")
    a = torch.sqrt(current.clamp_min(eps))
    b = torch.sqrt(reference.clamp_min(eps))
    return 0.5 * torch.square(a - b).sum(dim=-1).mean()


def functional_transport_anchor_loss(
    current: torch.Tensor,
    reference: torch.Tensor,
    host_cost: torch.Tensor,
    *,
    epsilon: float = 0.05,
    iterations: int = 100,
) -> torch.Tensor:
    """Mean paired functional transport under a frozen host-cost matrix."""
    return entropic_transport_cost(
        current,
        reference,
        host_cost,
        epsilon=epsilon,
        iterations=iterations,
    ).mean()


def latent_anchor_loss(current: torch.Tensor, reference: torch.Tensor) -> torch.Tensor:
    """Mean squared error between paired mediated latent states."""
    if current.shape != reference.shape:
        raise ValueError("current and reference latent states must have identical shapes")
    return F.mse_loss(current, reference)


def distillation_kl(
    current_logits: torch.Tensor,
    reference_logits: torch.Tensor,
    *,
    temperature: float = 2.0,
) -> torch.Tensor:
    """Teacher-to-current KL divergence with standard temperature scaling."""
    if temperature <= 0:
        raise ValueError("temperature must be positive")
    if current_logits.shape != reference_logits.shape:
        raise ValueError("logit tensors must have identical shapes")
    tau = float(temperature)
    teacher = torch.softmax(reference_logits.detach() / tau, dim=-1)
    student = torch.log_softmax(current_logits / tau, dim=-1)
    return F.kl_div(student, teacher, reduction="batchmean") * (tau * tau)


def cross_functional_route_costs(
    routes_a: torch.Tensor,
    routes_b: torch.Tensor,
    host_cost: torch.Tensor,
    *,
    epsilon: float = 0.05,
    iterations: int = 100,
) -> torch.Tensor:
    """Pairwise functional costs between two route clouds."""
    if routes_a.ndim != 2 or routes_b.ndim != 2:
        raise ValueError("route clouds must have shape [items, hosts]")
    if routes_a.shape[1] != routes_b.shape[1]:
        raise ValueError("route clouds must use the same host dimension")
    left = routes_a[:, None, :].expand(-1, routes_b.shape[0], -1)
    right = routes_b[None, :, :].expand(routes_a.shape[0], -1, -1)
    return entropic_transport_cost(
        left,
        right,
        host_cost,
        epsilon=epsilon,
        iterations=iterations,
    )


def uniform_empirical_transport(
    ground_cost: torch.Tensor,
    *,
    epsilon: float = 0.05,
    iterations: int = 100,
    eps: float = 1e-12,
) -> torch.Tensor:
    """Entropic OT between two uniform empirical measures given a cost matrix."""
    if ground_cost.ndim != 2:
        raise ValueError("ground_cost must be a matrix")
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    n, m = ground_cost.shape
    a = torch.full((n,), 1.0 / n, dtype=ground_cost.dtype, device=ground_cost.device)
    b = torch.full((m,), 1.0 / m, dtype=ground_cost.dtype, device=ground_cost.device)
    kernel = torch.exp(-ground_cost / float(epsilon)).clamp_min(eps)
    u = torch.ones_like(a)
    v = torch.ones_like(b)
    for _ in range(int(iterations)):
        u = a / (kernel @ v).clamp_min(eps)
        v = b / (kernel.T @ u).clamp_min(eps)
    plan = u[:, None] * kernel * v[None, :]
    return (plan * ground_cost).sum()


def distributional_functional_transport(
    routes_a: torch.Tensor,
    routes_b: torch.Tensor,
    host_cost: torch.Tensor,
    *,
    route_epsilon: float = 0.05,
    route_iterations: int = 100,
    cloud_epsilon: float = 0.05,
    cloud_iterations: int = 100,
) -> torch.Tensor:
    """Transport between empirical route distributions under functional ground cost."""
    ground = cross_functional_route_costs(
        routes_a,
        routes_b,
        host_cost,
        epsilon=route_epsilon,
        iterations=route_iterations,
    )
    return uniform_empirical_transport(
        ground,
        epsilon=cloud_epsilon,
        iterations=cloud_iterations,
    )


@dataclass(frozen=True)
class PathStatistics:
    cumulative_length: float
    endpoint_distance: float
    path_excess: float
    steps: int


def functional_path_statistics(
    stage_routes: Sequence[torch.Tensor],
    host_cost: torch.Tensor,
    *,
    epsilon: float = 0.05,
    iterations: int = 100,
) -> PathStatistics:
    """Paired mean path length, endpoint drift, and excess across stage snapshots."""
    if len(stage_routes) < 2:
        raise ValueError("at least two stage route tensors are required")
    first_shape = stage_routes[0].shape
    if any(routes.shape != first_shape for routes in stage_routes):
        raise ValueError("all stage route tensors must have identical shapes")
    segments = []
    for left, right in zip(stage_routes[:-1], stage_routes[1:]):
        segments.append(float(entropic_transport_cost(left, right, host_cost, epsilon=epsilon, iterations=iterations).mean()))
    endpoint = float(entropic_transport_cost(stage_routes[0], stage_routes[-1], host_cost, epsilon=epsilon, iterations=iterations).mean())
    total = float(sum(segments))
    return PathStatistics(
        cumulative_length=total,
        endpoint_distance=endpoint,
        path_excess=total / max(endpoint, 1e-12),
        steps=len(segments),
    )


@dataclass(frozen=True)
class RootGaussianMemory:
    mean: torch.Tensor
    covariance: torch.Tensor
    count: int


def compile_root_gaussian(
    routes: torch.Tensor,
    *,
    shrinkage: float = 0.05,
    eps: float = 1e-4,
) -> RootGaussianMemory:
    """Compile a route cloud into a mean/covariance summary in root coordinates."""
    if routes.ndim != 2 or routes.shape[0] < 2:
        raise ValueError("routes must have shape [items, hosts] with at least two items")
    if not 0.0 <= shrinkage <= 1.0:
        raise ValueError("shrinkage must lie in [0,1]")
    roots = torch.sqrt(routes.clamp_min(1e-12))
    mean = roots.mean(dim=0)
    centered = roots - mean
    covariance = centered.T @ centered / float(max(len(roots) - 1, 1))
    scale = torch.trace(covariance) / covariance.shape[0]
    covariance = (1.0 - shrinkage) * covariance + shrinkage * scale * torch.eye(
        covariance.shape[0], dtype=covariance.dtype, device=covariance.device
    )
    covariance = covariance + float(eps) * torch.eye(
        covariance.shape[0], dtype=covariance.dtype, device=covariance.device
    )
    return RootGaussianMemory(mean=mean, covariance=covariance, count=len(routes))


def root_gaussian_nll(routes: torch.Tensor, memory: RootGaussianMemory) -> torch.Tensor:
    """Average Gaussian negative log-likelihood in root-route coordinates."""
    roots = torch.sqrt(routes.clamp_min(1e-12))
    delta = roots - memory.mean.to(roots)
    covariance = memory.covariance.to(roots)
    sign, logdet = torch.linalg.slogdet(covariance)
    if float(sign) <= 0:
        raise ValueError("memory covariance must be positive definite")
    solved = torch.linalg.solve(covariance, delta.T).T
    quadratic = (delta * solved).sum(dim=-1)
    dimension = roots.shape[-1]
    return 0.5 * (quadratic + logdet + dimension * torch.log(torch.tensor(2.0 * torch.pi, dtype=roots.dtype, device=roots.device))).mean()
