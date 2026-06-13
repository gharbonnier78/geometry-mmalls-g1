"""Trace schema helpers."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class RunManifest:
    run_id: str
    seed: int
    config_path: str
    git_commit: str
    data_fingerprint: str
    torch_version: str
    device: str
    status: str = "development"

    def save(self, path: str | Path) -> None:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")


def json_safe(value: Any) -> Any:
    """Convert common numerical values to JSON-safe Python objects."""

    if hasattr(value, "tolist"):
        return value.tolist()
    if hasattr(value, "item"):
        return value.item()
    return value
