#!/usr/bin/env python3
"""Synthetic geometry smoke test.

This program validates the metric and artifact pipeline against a deliberately
constructed angular route trajectory. It does not train or evaluate MMALS.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from geometry_mmalls.geometry import (  # noqa: E402
    normalized_stress,
    pairwise_fisher_rao,
    procrustes_aligned_drift,
)
from geometry_mmalls.metrics import (  # noqa: E402
    distance_order_correlation,
    neighborhood_preservation,
    pairwise_factor_distance,
    route_entropy,
)


def route_curve(angle_deg: np.ndarray, num_hosts: int = 4) -> np.ndarray:
    """Create smooth host preferences centered on four angular regions."""

    centers = np.linspace(-60.0, 60.0, num_hosts)
    logits = -((angle_deg[:, None] - centers[None, :]) ** 2) / (2.0 * 25.0**2)
    logits -= logits.max(axis=1, keepdims=True)
    probabilities = np.exp(logits)
    return probabilities / probabilities.sum(axis=1, keepdims=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=ROOT / "results" / "smoke")
    args = parser.parse_args()

    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    smoke = config["smoke"]
    angles = np.asarray(config["data"]["train_angles"], dtype=float)
    rng = np.random.default_rng(int(smoke["seed"]))
    n_per = int(smoke["samples_per_angle"])

    observed_angles = np.repeat(angles, n_per)
    # Add within-context variation so neighborhood metrics are not dominated by exact-distance ties.
    observed_angles = observed_angles + rng.uniform(-10.0, 10.0, size=observed_angles.shape)
    observed_angles = np.clip(observed_angles, -75.0, 75.0)
    routes = route_curve(observed_angles, num_hosts=int(config["model"]["num_hosts"]))
    routes += rng.normal(0.0, float(smoke["noise_std"]), size=routes.shape)
    routes = np.clip(routes, 1e-6, None)
    routes /= routes.sum(axis=1, keepdims=True)

    factor_dist = pairwise_factor_distance(observed_angles)
    route_dist = pairwise_fisher_rao(routes)
    rho, p_value = distance_order_correlation(factor_dist, route_dist)
    stress = normalized_stress(factor_dist, route_dist)
    knn = neighborhood_preservation(factor_dist, route_dist, k=min(5, len(routes) - 1))

    context = np.column_stack(
        [
            np.cos(np.deg2rad(observed_angles)),
            np.sin(np.deg2rad(observed_angles)),
        ]
    )
    drifted_context = context + rng.normal(
        0.0, float(smoke["drift_std"]), size=context.shape
    )
    drift = procrustes_aligned_drift(context, drifted_context)

    interpolation_angles = np.asarray(config["data"]["interpolation_angles"], dtype=float)
    interpolation_routes = route_curve(
        interpolation_angles, num_hosts=int(config["model"]["num_hosts"])
    )
    nearest_indices = np.abs(angles[:, None] - interpolation_angles[None, :]).argmin(axis=0)
    nearest_routes = route_curve(
        angles[nearest_indices], num_hosts=int(config["model"]["num_hosts"])
    )
    interpolation_error = float(np.mean(np.linalg.norm(interpolation_routes - nearest_routes, axis=1)))

    args.output.mkdir(parents=True, exist_ok=True)
    sample_df = pd.DataFrame(
        {
            "angle_deg": observed_angles,
            **{f"route_h{i+1}": routes[:, i] for i in range(routes.shape[1])},
            "route_entropy": route_entropy(routes),
        }
    )
    sample_df.to_csv(args.output / "synthetic_routes.csv", index=False)

    metrics = {
        "status": "synthetic_smoke_only",
        "distance_order_spearman_rho": rho,
        "distance_order_p_value": p_value,
        "normalized_stress": stress,
        "knn_preservation_k5": knn,
        "procrustes_drift": drift,
        "nearest_context_interpolation_error": interpolation_error,
        "sample_count": int(len(observed_angles)),
    }
    (args.output / "synthetic_metrics.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8"
    )

    angle_grid = np.linspace(-75, 75, 301)
    smooth_routes = route_curve(angle_grid, num_hosts=routes.shape[1])
    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    for host in range(smooth_routes.shape[1]):
        ax.plot(angle_grid, smooth_routes[:, host], label=f"Host {host + 1}")
    ax.scatter(observed_angles, routes.argmax(axis=1) / max(routes.shape[1] - 1, 1), s=4, alpha=0.12)
    ax.set_xlabel("Known context factor: rotation angle (degrees)")
    ax.set_ylabel("Synthetic route mass")
    ax.set_title("Synthetic smoke trajectory - not an MMALS result")
    ax.legend(ncol=2)
    fig.tight_layout()
    fig.savefig(args.output / "synthetic_route_trajectory.png", dpi=180)
    plt.close(fig)

    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
