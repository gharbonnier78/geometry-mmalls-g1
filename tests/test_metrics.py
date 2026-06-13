import numpy as np

from geometry_mmalls.metrics import (
    distance_order_correlation,
    linear_cka,
    neighborhood_preservation,
    pairwise_factor_distance,
    route_entropy,
)


def test_distance_order_correlation_for_exact_order():
    factor = np.arange(8, dtype=float)
    distances = pairwise_factor_distance(factor)
    rho, _ = distance_order_correlation(distances, distances)
    assert rho > 0.999


def test_neighborhood_preservation_for_identical_geometry():
    factor = np.arange(10, dtype=float)
    distances = pairwise_factor_distance(factor)
    assert neighborhood_preservation(distances, distances, k=3) == 1.0


def test_linear_cka_invariance_to_isotropic_scaling():
    rng = np.random.default_rng(2)
    x = rng.normal(size=(40, 6))
    assert linear_cka(x, 3.0 * x) > 0.999999


def test_route_entropy_bounds():
    routes = np.array([[1.0, 0.0], [0.5, 0.5]])
    ent = route_entropy(routes)
    assert ent[0] < 1e-8
    assert np.isclose(ent[1], 1.0)
