"""Minimal PyTorch architecture for Geometry-MMALS G1.

This is an implementation scaffold, not a claim of benchmark performance.
"""

from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn


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


@dataclass
class MMALSTrace:
    z0: torch.Tensor
    context: torch.Tensor
    route: torch.Tensor
    host_outputs: torch.Tensor
    z_mm: torch.Tensor
    logits: torch.Tensor


class GeometryMMALS(nn.Module):
    """Context-inferred, host-routed MMALS scaffold.

    The context coordinate is continuous. A softmax route maps the context and
    sensory representation to host weights. G1 losses are applied outside the
    module so every assumption remains visible in the training loop.
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

    def forward(self, x: torch.Tensor, temperature: float = 1.0) -> MMALSTrace:
        if temperature <= 0:
            raise ValueError("temperature must be positive")
        z0 = self.encode(x)
        context = self.context_net(z0)
        route_logits = self.router(torch.cat([z0, context], dim=-1))
        route = torch.softmax(route_logits / temperature, dim=-1)
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
        )
