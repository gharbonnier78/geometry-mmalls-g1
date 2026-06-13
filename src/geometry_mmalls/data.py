"""RotatedMNIST data utilities for the controlled G1 protocol."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import torch
from torch.utils.data import Dataset
from torchvision.datasets import MNIST
from torchvision.transforms import functional as TF


class FixedAngleMNIST(Dataset):
    """MNIST view rotated by one declared angle.

    Returns ``(image, label, angle, source_index)``. The angle is retained for
    evaluation and geometry losses in controlled experiments; it must not be
    supplied to the deployable router.
    """

    def __init__(
        self,
        root: str | Path,
        angle: float,
        train: bool,
        download: bool = True,
    ) -> None:
        self.base = MNIST(root=str(root), train=train, download=download)
        self.angle = float(angle)

    def __len__(self) -> int:
        return len(self.base)

    def __getitem__(self, index: int):
        image, label = self.base[index]
        image = TF.to_tensor(TF.rotate(image, angle=self.angle, fill=0))
        return image, int(label), torch.tensor(self.angle, dtype=torch.float32), int(index)


class MultiAngleMNIST(Dataset):
    """Return multiple rotated views of the same MNIST source image.

    Each item is ``(views, label, angles, source_index)`` where ``views`` has
    shape ``[n_angles, 1, 28, 28]``. This is the canonical data primitive for
    the G1-A cross-angle paired protocol. The true angle is available only to
    the controlled loss and evaluator; it is never passed to the deployable
    router.
    """

    def __init__(
        self,
        root: str | Path,
        angles: Sequence[float],
        train: bool,
        indices: Sequence[int] | None = None,
        download: bool = True,
    ) -> None:
        self.base = MNIST(root=str(root), train=train, download=download)
        self.angles = tuple(float(angle) for angle in angles)
        if not self.angles:
            raise ValueError("angles must contain at least one value")
        if indices is None:
            self.indices = tuple(range(len(self.base)))
        else:
            self.indices = tuple(int(index) for index in indices)
            if not self.indices:
                raise ValueError("indices must not be empty")
            if min(self.indices) < 0 or max(self.indices) >= len(self.base):
                raise IndexError("indices contain values outside the MNIST split")

    def __len__(self) -> int:
        return len(self.indices)

    def __getitem__(self, position: int):
        source_index = self.indices[position]
        image, label = self.base[source_index]
        views = torch.stack(
            [
                TF.to_tensor(TF.rotate(image, angle=angle, fill=0))
                for angle in self.angles
            ],
            dim=0,
        )
        factors = torch.tensor(self.angles, dtype=torch.float32)
        return views, int(label), factors, int(source_index)


@dataclass(frozen=True)
class AngleProtocol:
    train_angles: Sequence[float]
    interpolation_angles: Sequence[float]
    extrapolation_angles: Sequence[float]
