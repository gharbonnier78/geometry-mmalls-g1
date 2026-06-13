"""Minimal dual-memory stubs for Geometry-MMALS G1.

The goal is not to implement a production memory system yet. The goal is to
make the dual-memory contract executable and auditable:

- ReconstructiveAuditMemory stores enough route-function trace information to
  replay or inspect what happened.
- SyntheticFunctionalMemory stores compressed prototypes that can be reused
  cheaply.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Mapping, Optional

import numpy as np


@dataclass
class TraceRecord:
    """Serializable trace payload for one sample or batch aggregate."""

    sample_id: str
    stage: int
    context: np.ndarray
    route: np.ndarray
    z0: Optional[np.ndarray] = None
    z_mm: Optional[np.ndarray] = None
    prediction: Optional[int] = None
    metadata: Mapping[str, float | int | str] = field(default_factory=dict)

    def route_entropy(self, eps: float = 1e-12) -> float:
        r = np.asarray(self.route, dtype=np.float64)
        r = np.clip(r, eps, None)
        r = r / r.sum()
        return float(-(r * np.log(r)).sum() / np.log(len(r)))


class ReconstructiveAuditMemory:
    """Append-only in-memory store for reconstructive audit traces."""

    def __init__(self) -> None:
        self._records: Dict[str, TraceRecord] = {}

    def add(self, record: TraceRecord) -> None:
        if record.sample_id in self._records:
            raise ValueError(f"duplicate sample_id: {record.sample_id}")
        self._records[record.sample_id] = record

    def get(self, sample_id: str) -> TraceRecord:
        return self._records[sample_id]

    def __len__(self) -> int:
        return len(self._records)

    def by_stage(self, stage: int) -> List[TraceRecord]:
        return [r for r in self._records.values() if r.stage == stage]

    def reconstruction_fidelity(self, sample_id: str, z_mm_replayed: np.ndarray, eps: float = 1e-12) -> float:
        """Cosine fidelity between stored synthesis and replayed synthesis."""
        record = self.get(sample_id)
        if record.z_mm is None:
            raise ValueError("record does not contain z_mm")
        a = np.asarray(record.z_mm, dtype=np.float64).reshape(-1)
        b = np.asarray(z_mm_replayed, dtype=np.float64).reshape(-1)
        if a.shape != b.shape:
            raise ValueError("stored and replayed vectors must have the same shape")
        return float(np.dot(a, b) / max(np.linalg.norm(a) * np.linalg.norm(b), eps))


class SyntheticFunctionalMemory:
    """Small prototype bank for compiled functional reuse."""

    def __init__(self) -> None:
        self._prototypes: Dict[str, np.ndarray] = {}
        self._counts: Dict[str, int] = {}

    def update(self, key: str, vector: np.ndarray, momentum: float = 0.9) -> None:
        if not 0.0 <= momentum < 1.0:
            raise ValueError("momentum must be in [0, 1)")
        v = np.asarray(vector, dtype=np.float64)
        if key not in self._prototypes:
            self._prototypes[key] = v.copy()
            self._counts[key] = 1
        else:
            if self._prototypes[key].shape != v.shape:
                raise ValueError("prototype shape mismatch")
            self._prototypes[key] = momentum * self._prototypes[key] + (1.0 - momentum) * v
            self._counts[key] += 1

    def get(self, key: str) -> np.ndarray:
        return self._prototypes[key].copy()

    def keys(self) -> Iterable[str]:
        return self._prototypes.keys()

    def count(self, key: str) -> int:
        return self._counts[key]
