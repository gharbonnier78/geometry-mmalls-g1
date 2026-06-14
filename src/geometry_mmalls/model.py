"""Minimal PyTorch architecture for Geometry-MMALS G1.

This is an implementation scaffold, not a claim of benchmark performance.
"""

from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn
import torch.nn.functional as F


class SmallConvEncoder(nn.Module):
    """Compact sensory grove for MNIST-scale inputs."""

    def __init__(self, latent_dim: int = 128) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64 * 7 * 7, latent_dim),
            nn.LayerNorm(latent_dim),
            nn.ReLU(),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.features(x)


class ResidualHost(nn.Module):
    """A small residual transformation field over the sensory representation."""

    def __init__(self, latent_dim: int, hidden_dim: int) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, latent_dim),
        )
        self.norm = nn.LayerNorm(latent_dim)

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        return self.norm(z + self.net(z))


class ContextBottleneckRouter(nn.Module):
    """Capacity-controlled router that receives inferred context only.

    The direct sensory representation ``z0`` is never accepted by this module.
    Any instance-specific route geometry must therefore pass through the
    context encoder. Two hidden layers avoid giving the bottleneck an obvious
    capacity disadvantage relative to the standard concatenated router.
    """

    def __init__(self, context_dim: int, num_hosts: int, hidden_dim: int = 64) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(context_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, num_hosts),
        )

    def forward(self, context: torch.Tensor) -> torch.Tensor:
        return self.net(context)


class SensoryBottleneckRouter(nn.Module):
    """Capacity-matched control router that receives the sensory state only."""

    def __init__(self, latent_dim: int, num_hosts: int, hidden_dim: int = 64) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, num_hosts),
        )

    def forward(self, z0: torch.Tensor) -> torch.Tensor:
        return self.net(z0)


@dataclass
class MMALSTrace:
    z0: torch.Tensor
    context: torch.Tensor
    route: torch.Tensor
    host_outputs: torch.Tensor
    z_mm: torch.Tensor
    logits: torch.Tensor
    context_raw: torch.Tensor | None = None


class GeometryMMALS(nn.Module):
    """Context-inferred, host-routed MMALS scaffold.

    The default route uses both the sensory representation and inferred
    context. G1 v1.0.7 additionally exposes dedicated context-only and
    sensory-only bottleneck routers for controlled mediation experiments.
    Losses remain outside the module so protocol assumptions stay visible.
    """

    def __init__(
        self,
        encoder: nn.Module,
        latent_dim: int = 128,
        context_dim: int = 2,
        num_hosts: int = 4,
        host_hidden_dim: int = 128,
        num_classes: int = 10,
        freeze_encoder: bool = True,
        bottleneck_hidden_dim: int = 64,
    ) -> None:
        super().__init__()
        if num_hosts < 2:
            raise ValueError("num_hosts must be at least 2")
        self.encoder = encoder
        self.freeze_encoder = freeze_encoder
        self.context_net = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.GELU(),
            nn.Linear(64, context_dim),
        )
        self.router = nn.Sequential(
            nn.Linear(latent_dim + context_dim, 64),
            nn.GELU(),
            nn.Linear(64, num_hosts),
        )
        self.context_bottleneck_router = ContextBottleneckRouter(
            context_dim=context_dim,
            num_hosts=num_hosts,
            hidden_dim=bottleneck_hidden_dim,
        )
        self.sensory_bottleneck_router = SensoryBottleneckRouter(
            latent_dim=latent_dim,
            num_hosts=num_hosts,
            hidden_dim=bottleneck_hidden_dim,
        )
        self.hosts = nn.ModuleList(
            [ResidualHost(latent_dim, host_hidden_dim) for _ in range(num_hosts)]
        )
        self.synthesis_norm = nn.LayerNorm(latent_dim)
        self.classifier = nn.Linear(latent_dim, num_classes)

        if freeze_encoder:
            for parameter in self.encoder.parameters():
                parameter.requires_grad_(False)

    def encode(self, x: torch.Tensor) -> torch.Tensor:
        if self.freeze_encoder:
            self.encoder.eval()
            with torch.no_grad():
                return self.encoder(x)
        return self.encoder(x)

    @staticmethod
    def normalize_context(context_raw: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
        """Return the functional unit-sphere context used by G1 v1.0.8.

        Keeping this operation inside the model makes it harder for training,
        metrics and causal probes to accidentally use incompatible context
        representations. The raw context can still be retained in the trace.
        """
        return F.normalize(context_raw, p=2, dim=-1, eps=eps)

    def infer_context(self, z0: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Return ``(raw_context, functional_normalized_context)``."""
        raw = self.context_net(z0)
        return raw, self.normalize_context(raw)

    def synthesize(
        self,
        z0: torch.Tensor,
        context: torch.Tensor,
        route: torch.Tensor,
        context_raw: torch.Tensor | None = None,
    ) -> MMALSTrace:
        """Run hosts, synthesis and classifier for a declared route."""
        host_outputs = torch.stack([host(z0) for host in self.hosts], dim=1)
        z_mm = torch.einsum("bh,bhd->bd", route, host_outputs)
        z_mm = self.synthesis_norm(z_mm)
        logits = self.classifier(z_mm)
        return MMALSTrace(
            z0=z0,
            context=context,
            route=route,
            host_outputs=host_outputs,
            z_mm=z_mm,
            logits=logits,
            context_raw=context_raw,
        )

    def forward(self, x: torch.Tensor, temperature: float = 1.0) -> MMALSTrace:
        if temperature <= 0:
            raise ValueError("temperature must be positive")
        z0 = self.encode(x)
        context_raw, context = self.infer_context(z0)
        route_logits = self.router(torch.cat([z0, context], dim=-1))
        route = torch.softmax(route_logits / temperature, dim=-1)
        return self.synthesize(z0, context, route, context_raw=context_raw)
