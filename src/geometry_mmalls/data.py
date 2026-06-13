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


@dataclass(frozen=True)
class AngleProtocol:
    train_angles: Sequence[float]
    interpolation_angles: Sequence[float]
    extrapolation_angles: Sequence[float]
