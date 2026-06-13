import numpy as np
import torch

from geometry_mmalls.geometry import (
    fisher_rao_distance,
    normalized_stress,
    pairwise_fisher_rao,
    procrustes_aligned_drift,
    route_geodesic_loss,
)


def test_fisher_rao_identity_and_symmetry():
    p = np.array([0.2, 0.3, 0.5])
    q = np.array([0.6, 0.2, 0.2])
    assert fisher_rao_distance(p, p) < 1e-7
    assert np.isclose(fisher_rao_distance(p, q), fisher_rao_distance(q, p))


def test_pairwise_fisher_rao_shape_and_diagonal():
    routes = np.array([[0.9, 0.1], [0.5, 0.5], [0.1, 0.9]])
    distances = pairwise_fisher_rao(routes)
    assert distances.shape == (3, 3)
    assert np.allclose(np.diag(distances), 0.0, atol=1e-7)


def test_normalized_stress_is_zero_for_scaled_copy():
    d = np.array([[0.0, 1.0, 2.0], [1.0, 0.0, 1.0], [2.0, 1.0, 0.0]])
    assert normalized_stress(d, 2.5 * d) < 1e-10


def test_procrustes_is_invariant_to_rotation():
    rng = np.random.default_rng(1)
    x = rng.normal(size=(50, 2))
    theta = 0.7
    rotation = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    y = x @ rotation
    assert procrustes_aligned_drift(x, y) < 1e-10


def test_route_geodesic_loss_is_finite_and_differentiable():
    logits = torch.randn(16, 4, requires_grad=True)
    routes = torch.softmax(logits, dim=-1)
    factor = torch.linspace(-60, 60, 16)
    loss = route_geodesic_loss(routes, factor)
    assert torch.isfinite(loss)
    loss.backward()
    assert logits.grad is not None
