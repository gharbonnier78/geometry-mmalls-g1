import math

import numpy as np
import torch

from geometry_mmalls.geometry import (
    context_chord_target,
    context_path_spread_loss,
    cross_source_fiber_alignment_loss,
    factor_centroid_geometry_loss,
    normalize_functional_context,
    paired_context_geometry_loss,
)
from geometry_mmalls.metrics import (
    context_collapse_diagnostics,
    fiber_alignment_scores,
    ridge_factor_probe,
)


def test_context_geometry_backward_is_finite():
    context = torch.randn(8, 5, 4, requires_grad=True)
    factors = torch.tensor([-60.0, -30.0, 0.0, 30.0, 60.0])
    loss = (
        paired_context_geometry_loss(context, factors)
        + 0.05 * context_path_spread_loss(context)
        + 0.05 * cross_source_fiber_alignment_loss(context, factors)
        + 0.05 * factor_centroid_geometry_loss(context, factors)
    )
    loss.backward()
    assert torch.isfinite(loss)
    assert context.grad is not None and torch.isfinite(context.grad).all()


def test_context_loss_is_scale_invariant():
    context = torch.randn(6, 5, 4)
    factors = torch.tensor([-60.0, -30.0, 0.0, 30.0, 60.0])
    base = paired_context_geometry_loss(context, factors)
    scaled = paired_context_geometry_loss(17.0 * context, factors)
    assert torch.allclose(base, scaled, atol=1e-6, rtol=1e-6)


def test_chord_target_maps_full_span_to_one():
    gap = torch.tensor([0.0, 60.0, 120.0])
    target = context_chord_target(gap, max_factor_span=120.0)
    expected = torch.tensor([0.0, math.sin(math.pi / 4.0), 1.0])
    assert torch.allclose(target, expected, atol=1e-6)


def test_collapsed_context_is_penalized():
    context = torch.ones(8, 5, 4)
    factors = torch.tensor([-60.0, -30.0, 0.0, 30.0, 60.0])
    geo = paired_context_geometry_loss(context, factors)
    spread = context_path_spread_loss(context, spread_floor=0.05)
    assert geo > 0.05
    assert spread > 0.0


def test_normalized_context_has_unit_norm():
    context = torch.randn(7, 4)
    normalized = normalize_functional_context(context)
    assert torch.allclose(
        torch.linalg.vector_norm(normalized, dim=-1),
        torch.ones(7),
        atol=1e-6,
    )


def test_fiber_alignment_prefers_shared_direction():
    factors = np.array([-1.0, 0.0, 1.0])
    rows, groups, values = [], [], []
    for group in range(12):
        for factor in factors:
            rows.append([factor, 0.1 * group])
            groups.append(group)
            values.append(factor)
    score = fiber_alignment_scores(np.array(values), np.array(rows), np.array(groups))
    assert score["mean_resultant_length"] > 0.99


def test_context_collapse_diagnostics_detect_separation():
    factors = np.tile(np.array([-60.0, -30.0, 60.0]), 4)
    groups = np.repeat(np.arange(4), 3)
    rows = []
    for group in range(4):
        rows.extend([[1.0, 0.0], [0.0, 1.0], [-1.0, 0.0]])
    normalized = np.asarray(rows, dtype=float)
    raw = 3.0 * normalized
    report = context_collapse_diagnostics(factors, normalized, raw, groups)
    assert report["mean_path_variance"] > 0.1
    assert report["far_to_near_ratio"] > 1.0
    assert report["effective_rank"] > 1.0


def test_ridge_probe_recovers_linear_factor():
    rng = np.random.default_rng(4)
    x = rng.normal(size=(100, 3))
    y = 2.0 * x[:, 0] - x[:, 1]
    result = ridge_factor_probe(x[:70], y[:70], x[70:], y[70:])
    assert result["r2"] > 0.99
