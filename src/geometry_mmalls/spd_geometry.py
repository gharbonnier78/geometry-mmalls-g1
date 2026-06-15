
"""Covariance and SPD geometry diagnostics for Geometry-MMALS G1 v1.1.2."""
from __future__ import annotations

import torch


def _symmetrize(matrix: torch.Tensor) -> torch.Tensor:
    return 0.5 * (matrix + matrix.transpose(-1, -2))


def _eigh_spd(matrix: torch.Tensor, eps: float = 1e-6) -> tuple[torch.Tensor, torch.Tensor]:
    values, vectors = torch.linalg.eigh(_symmetrize(matrix))
    return values.clamp_min(eps), vectors


def regularized_covariance(
    samples: torch.Tensor,
    *,
    shrinkage: float = 0.05,
    eps: float = 1e-4,
) -> torch.Tensor:
    """Estimate a strictly positive-definite covariance matrix."""
    if samples.ndim != 2 or samples.shape[0] < 2:
        raise ValueError("samples must have shape [n>=2, d]")
    if not 0.0 <= shrinkage <= 1.0:
        raise ValueError("shrinkage must lie in [0,1]")
    centered = samples - samples.mean(dim=0, keepdim=True)
    covariance = centered.T @ centered / float(samples.shape[0] - 1)
    dimension = covariance.shape[0]
    isotropic = torch.trace(covariance) / float(dimension) * torch.eye(
        dimension, dtype=samples.dtype, device=samples.device
    )
    covariance = (1.0 - float(shrinkage)) * covariance + float(shrinkage) * isotropic
    covariance = _symmetrize(covariance) + float(eps) * torch.eye(
        dimension, dtype=samples.dtype, device=samples.device
    )
    return covariance


def matrix_log_spd(matrix: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
    values, vectors = _eigh_spd(matrix, eps=eps)
    return vectors @ torch.diag_embed(torch.log(values)) @ vectors.transpose(-1, -2)


def matrix_sqrt_spd(matrix: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
    values, vectors = _eigh_spd(matrix, eps=eps)
    return vectors @ torch.diag_embed(torch.sqrt(values)) @ vectors.transpose(-1, -2)


def matrix_inv_sqrt_spd(matrix: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
    values, vectors = _eigh_spd(matrix, eps=eps)
    return vectors @ torch.diag_embed(torch.rsqrt(values)) @ vectors.transpose(-1, -2)


def log_euclidean_distance(a: torch.Tensor, b: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
    return torch.linalg.matrix_norm(matrix_log_spd(a, eps) - matrix_log_spd(b, eps), ord='fro')


def affine_invariant_distance(a: torch.Tensor, b: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
    inv_sqrt = matrix_inv_sqrt_spd(a, eps)
    middle = _symmetrize(inv_sqrt @ b @ inv_sqrt)
    return torch.linalg.matrix_norm(matrix_log_spd(middle, eps), ord='fro')


def bures_wasserstein_distance(a: torch.Tensor, b: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
    sqrt_a = matrix_sqrt_spd(a, eps)
    middle = _symmetrize(sqrt_a @ b @ sqrt_a)
    trace_term = torch.trace(a) + torch.trace(b) - 2.0 * torch.trace(matrix_sqrt_spd(middle, eps))
    return torch.sqrt(trace_term.clamp_min(0.0))


def pairwise_spd_distances(matrices: torch.Tensor, metric: str = 'log_euclidean') -> torch.Tensor:
    if matrices.ndim != 3 or matrices.shape[-1] != matrices.shape[-2]:
        raise ValueError("matrices must have shape [n,d,d]")
    functions = {
        'log_euclidean': log_euclidean_distance,
        'airm': affine_invariant_distance,
        'bures': bures_wasserstein_distance,
    }
    if metric not in functions:
        raise ValueError(f"unsupported SPD metric: {metric}")
    n = matrices.shape[0]
    output = torch.zeros(n, n, dtype=matrices.dtype, device=matrices.device)
    for i in range(n):
        for j in range(i + 1, n):
            value = functions[metric](matrices[i], matrices[j])
            output[i, j] = output[j, i] = value
    return output
