"""Geometric primitives for route, context and transport analysis.

The functions in this module are deliberately small and testable. They do not
claim that a neural representation is a manifold; they provide measurements
used by the G1 evidence protocol.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import torch


def _normalize_probabilities_np(p: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    p = np.asarray(p, dtype=np.float64)
    if p.ndim == 1:
        p = p[None, :]
    p = np.clip(p, eps, None)
    return p / p.sum(axis=-1, keepdims=True)


def fisher_rao_distance(p: np.ndarray, q: np.ndarray, eps: float = 1e-12) -> float:
    """Fisher-Rao distance between two categorical distributions.

    The simplex is embedded through square-root coordinates. The returned
    distance is ``2 * arccos(sum(sqrt(p_i q_i)))`` and lies in ``[0, pi]``.
    """

    p_n = _normalize_probabilities_np(np.asarray(p), eps=eps)[0]
    q_n = _normalize_probabilities_np(np.asarray(q), eps=eps)[0]
    affinity = float(np.sum(np.sqrt(p_n * q_n)))
    affinity = float(np.clip(affinity, -1.0, 1.0))
    return float(2.0 * np.arccos(affinity))


def pairwise_fisher_rao(routes: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """Return the full pairwise Fisher-Rao distance matrix."""

    r = _normalize_probabilities_np(routes, eps=eps)
    roots = np.sqrt(r)
    affinity = np.clip(roots @ roots.T, 0.0, 1.0)
    distances = 2.0 * np.arccos(affinity)
    np.fill_diagonal(distances, 0.0)
    return distances


def route_geodesic_loss(
    routes: torch.Tensor,
    factor: torch.Tensor,
    bandwidth: float = 20.0,
    margin: float = 0.35,
    far_weight: float = 0.25,
    eps: float = 1e-8,
) -> torch.Tensor:
    """Encourage local route continuity without forcing global collapse.

    Nearby factor values are penalized for large Fisher-Rao distance. Far pairs
    receive a contrastive margin so that a constant route is not optimal.
    ``factor`` is expected to contain the observed training factor, such as
    rotation angle, and is used only in the controlled G1 experiment.
    """

    if routes.ndim != 2:
        raise ValueError("routes must have shape [batch, hosts]")
    factor = factor.reshape(-1).to(routes.device, routes.dtype)
    if factor.shape[0] != routes.shape[0]:
        raise ValueError("factor and routes must have the same batch length")

    p = routes.clamp_min(eps)
    p = p / p.sum(dim=-1, keepdim=True)
    roots = torch.sqrt(p)
    affinity = torch.clamp(roots @ roots.T, eps, 1.0 - eps)
    d_route = 2.0 * torch.arccos(affinity)

    d_factor = torch.abs(factor[:, None] - factor[None, :])
    near_w = torch.exp(-torch.square(d_factor / max(float(bandwidth), eps)))
    eye = torch.eye(routes.shape[0], dtype=torch.bool, device=routes.device)
    near_w = near_w.masked_fill(eye, 0.0)

    smooth = (near_w * torch.square(d_route)).sum() / near_w.sum().clamp_min(eps)

    far_mask = d_factor >= float(bandwidth)
    far_mask = far_mask & (~eye)
    if torch.any(far_mask):
        far_penalty = torch.relu(float(margin) - d_route[far_mask]).square().mean()
    else:
        far_penalty = torch.zeros((), dtype=routes.dtype, device=routes.device)

    return smooth + float(far_weight) * far_penalty


def normalized_stress(
    reference_distances: np.ndarray,
    representation_distances: np.ndarray,
    mask: Optional[np.ndarray] = None,
    eps: float = 1e-12,
) -> float:
    """Kruskal-style normalized stress after optimal scalar rescaling."""

    d_ref = np.asarray(reference_distances, dtype=np.float64)
    d_rep = np.asarray(representation_distances, dtype=np.float64)
    if d_ref.shape != d_rep.shape:
        raise ValueError("distance matrices must share the same shape")

    if mask is None:
        mask = np.triu(np.ones_like(d_ref, dtype=bool), k=1)
    x = d_ref[mask]
    y = d_rep[mask]
    if x.size == 0:
        raise ValueError("no distance pairs selected")

    scale = float(np.dot(x, y) / max(np.dot(y, y), eps))
    residual = x - scale * y
    return float(np.sqrt(np.dot(residual, residual) / max(np.dot(x, x), eps)))


def procrustes_aligned_drift(
    reference: np.ndarray,
    current: np.ndarray,
    eps: float = 1e-12,
) -> float:
    """Orthogonal-Procrustes drift normalized by reference energy."""

    x = np.asarray(reference, dtype=np.float64)
    y = np.asarray(current, dtype=np.float64)
    if x.shape != y.shape or x.ndim != 2:
        raise ValueError("reference and current must be 2-D arrays with equal shape")

    x0 = x - x.mean(axis=0, keepdims=True)
    y0 = y - y.mean(axis=0, keepdims=True)
    u, _, vt = np.linalg.svd(y0.T @ x0, full_matrices=False)
    rotation = u @ vt
    y_aligned = y0 @ rotation
    return float(np.linalg.norm(x0 - y_aligned) / max(np.linalg.norm(x0), eps))
