
import torch

from geometry_mmalls.spd_geometry import (
    affine_invariant_distance,
    bures_wasserstein_distance,
    log_euclidean_distance,
    pairwise_spd_distances,
    regularized_covariance,
)


def test_regularized_covariance_is_spd():
    samples = torch.randn(64, 4, dtype=torch.float64)
    covariance = regularized_covariance(samples)
    eigenvalues = torch.linalg.eigvalsh(covariance)
    assert torch.all(eigenvalues > 0)


def test_spd_distances_are_symmetric_and_zero_on_identity():
    a = regularized_covariance(torch.randn(64, 4, dtype=torch.float64))
    b = regularized_covariance(torch.randn(64, 4, dtype=torch.float64) + 0.2)
    for function in [log_euclidean_distance, affine_invariant_distance, bures_wasserstein_distance]:
        assert torch.allclose(function(a, a), torch.tensor(0.0, dtype=a.dtype), atol=1e-6)
        assert torch.allclose(function(a, b), function(b, a), atol=1e-6)


def test_pairwise_spd_distances_shape():
    matrices = torch.stack([
        regularized_covariance(torch.randn(32, 4, dtype=torch.float64))
        for _ in range(3)
    ])
    distances = pairwise_spd_distances(matrices, metric='airm')
    assert distances.shape == (3, 3)
    assert torch.allclose(distances, distances.T, atol=1e-6)
