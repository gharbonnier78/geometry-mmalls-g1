"""Metrics used by the Geometry-MMALS G1 evidence ladder."""

from __future__ import annotations

from typing import Iterable

import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist, pdist, squareform
from scipy.stats import spearmanr


def pairwise_factor_distance(values: np.ndarray, circular_period: float | None = None) -> np.ndarray:
    """Pairwise scalar factor distances, optionally on a circle."""

    v = np.asarray(values, dtype=np.float64).reshape(-1)
    d = np.abs(v[:, None] - v[None, :])
    if circular_period is not None:
        d = np.minimum(d, float(circular_period) - d)
    return d


def euclidean_distance_matrix(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64)
    if x.ndim != 2:
        raise ValueError("x must be 2-D")
    return squareform(pdist(x, metric="euclidean"))


def distance_order_correlation(
    reference_distances: np.ndarray,
    representation_distances: np.ndarray,
) -> tuple[float, float]:
    """Spearman correlation over upper-triangular pairwise distances."""

    d_ref = np.asarray(reference_distances, dtype=np.float64)
    d_rep = np.asarray(representation_distances, dtype=np.float64)
    if d_ref.shape != d_rep.shape or d_ref.ndim != 2 or d_ref.shape[0] != d_ref.shape[1]:
        raise ValueError("inputs must be equal square distance matrices")
    idx = np.triu_indices(d_ref.shape[0], k=1)
    result = spearmanr(d_ref[idx], d_rep[idx])
    return float(result.statistic), float(result.pvalue)


def neighborhood_preservation(
    reference_distances: np.ndarray,
    representation_distances: np.ndarray,
    k: int = 3,
) -> float:
    """Mean overlap of k-nearest-neighbor sets."""

    d_ref = np.asarray(reference_distances, dtype=np.float64)
    d_rep = np.asarray(representation_distances, dtype=np.float64)
    if d_ref.shape != d_rep.shape or d_ref.ndim != 2:
        raise ValueError("distance matrices must have equal shape")
    n = d_ref.shape[0]
    if not 1 <= k < n:
        raise ValueError("k must satisfy 1 <= k < number of samples")

    overlaps: list[float] = []
    for i in range(n):
        ref_neighbors = set(np.argsort(d_ref[i])[1 : k + 1].tolist())
        rep_neighbors = set(np.argsort(d_rep[i])[1 : k + 1].tolist())
        overlaps.append(len(ref_neighbors & rep_neighbors) / k)
    return float(np.mean(overlaps))


def route_entropy(routes: np.ndarray, normalized: bool = True, eps: float = 1e-12) -> np.ndarray:
    """Per-example Shannon entropy of routing probabilities."""

    p = np.asarray(routes, dtype=np.float64)
    if p.ndim != 2:
        raise ValueError("routes must be 2-D")
    p = np.clip(p, eps, None)
    p = p / p.sum(axis=1, keepdims=True)
    ent = -np.sum(p * np.log(p), axis=1)
    if normalized and p.shape[1] > 1:
        ent = ent / np.log(p.shape[1])
    return ent


def linear_cka(x: np.ndarray, y: np.ndarray, eps: float = 1e-12) -> float:
    """Linear centered-kernel alignment between two representations."""

    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    if x.ndim != 2 or y.ndim != 2 or x.shape[0] != y.shape[0]:
        raise ValueError("x and y must be 2-D with the same number of samples")
    x = x - x.mean(axis=0, keepdims=True)
    y = y - y.mean(axis=0, keepdims=True)
    cross = np.linalg.norm(x.T @ y, ord="fro") ** 2
    xx = np.linalg.norm(x.T @ x, ord="fro")
    yy = np.linalg.norm(y.T @ y, ord="fro")
    return float(cross / max(xx * yy, eps))


def match_host_roles(cost_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """Hungarian matching for host roles across seeds or checkpoints."""

    cost = np.asarray(cost_matrix, dtype=np.float64)
    if cost.ndim != 2:
        raise ValueError("cost_matrix must be 2-D")
    rows, cols = linear_sum_assignment(cost)
    return rows, cols, float(cost[rows, cols].mean())


def contribution_locality(
    context_values: np.ndarray,
    contribution: np.ndarray,
    bins: Iterable[float],
) -> dict[str, float]:
    """Summarize mean host contribution over declared context bins."""

    u = np.asarray(context_values, dtype=np.float64).reshape(-1)
    c = np.asarray(contribution, dtype=np.float64).reshape(-1)
    edges = np.asarray(list(bins), dtype=np.float64)
    if u.shape != c.shape:
        raise ValueError("context_values and contribution must have equal length")
    if edges.size < 2:
        raise ValueError("at least two bin edges are required")

    result: dict[str, float] = {}
    for left, right in zip(edges[:-1], edges[1:]):
        mask = (u >= left) & (u < right)
        result[f"[{left:g},{right:g})"] = float(np.mean(c[mask])) if np.any(mask) else float("nan")
    return result


def bootstrap_mean_ci(
    values: np.ndarray,
    samples: int = 1000,
    confidence: float = 0.95,
    seed: int = 0,
) -> tuple[float, float, float]:
    """Block-bootstrap confidence interval for a vector of group-level scores."""

    x = np.asarray(values, dtype=np.float64).reshape(-1)
    x = x[np.isfinite(x)]
    if x.size == 0:
        return float("nan"), float("nan"), float("nan")
    if samples < 1:
        raise ValueError("samples must be positive")
    if not 0.0 < confidence < 1.0:
        raise ValueError("confidence must lie in (0, 1)")

    rng = np.random.default_rng(seed)
    boot = np.empty(samples, dtype=np.float64)
    for index in range(samples):
        boot[index] = np.mean(rng.choice(x, size=x.size, replace=True))
    alpha = 1.0 - confidence
    return (
        float(np.mean(x)),
        float(np.quantile(boot, alpha / 2.0)),
        float(np.quantile(boot, 1.0 - alpha / 2.0)),
    )


def grouped_geometry_scores(
    factor_values: np.ndarray,
    representations: np.ndarray,
    group_ids: np.ndarray,
    metric: str = "euclidean",
) -> dict[str, np.ndarray]:
    """Compute geometry scores independently inside each source block.

    This avoids treating millions of dependent cross-sample pairs as
    independent observations. ``group_ids`` should normally be the original
    image identifier, so every group contains the same source image observed
    under several angles.
    """

    from .geometry import normalized_stress, pairwise_fisher_rao

    factors = np.asarray(factor_values, dtype=np.float64).reshape(-1)
    reps = np.asarray(representations, dtype=np.float64)
    groups = np.asarray(group_ids).reshape(-1)
    if reps.ndim != 2 or len(factors) != len(reps) or len(groups) != len(reps):
        raise ValueError("factors, representations and group_ids must align")

    rhos: list[float] = []
    stresses: list[float] = []
    group_values: list[object] = []

    for group in np.unique(groups):
        mask = groups == group
        if np.count_nonzero(mask) < 3:
            continue
        u = factors[mask]
        x = reps[mask]
        d_ref = pairwise_factor_distance(u)
        if metric == "euclidean":
            d_rep = euclidean_distance_matrix(x)
        elif metric == "fisher_rao":
            d_rep = pairwise_fisher_rao(x)
        else:
            raise ValueError("metric must be 'euclidean' or 'fisher_rao'")
        rho, _ = distance_order_correlation(d_ref, d_rep)
        rhos.append(rho)
        stresses.append(normalized_stress(d_ref, d_rep))
        group_values.append(group)

    return {
        "group_ids": np.asarray(group_values),
        "rho": np.asarray(rhos, dtype=np.float64),
        "stress": np.asarray(stresses, dtype=np.float64),
    }


def centroid_geometry_scores(
    factor_values: np.ndarray,
    representations: np.ndarray,
    metric: str = "euclidean",
) -> dict[str, float]:
    """Geometry scores on factor-level centroids, avoiding nearest-neighbor ties."""

    from .geometry import normalized_stress, pairwise_fisher_rao

    factors = np.asarray(factor_values, dtype=np.float64).reshape(-1)
    reps = np.asarray(representations, dtype=np.float64)
    if reps.ndim != 2 or len(factors) != len(reps):
        raise ValueError("factor_values and representations must align")

    unique = np.sort(np.unique(factors))
    centroids = np.stack([reps[factors == value].mean(axis=0) for value in unique])
    d_ref = pairwise_factor_distance(unique)
    if metric == "euclidean":
        d_rep = euclidean_distance_matrix(centroids)
    elif metric == "fisher_rao":
        d_rep = pairwise_fisher_rao(centroids)
    else:
        raise ValueError("metric must be 'euclidean' or 'fisher_rao'")
    rho, _ = distance_order_correlation(d_ref, d_rep)
    return {
        "rho": float(rho),
        "stress": float(normalized_stress(d_ref, d_rep)),
        "factor_count": int(len(unique)),
    }
