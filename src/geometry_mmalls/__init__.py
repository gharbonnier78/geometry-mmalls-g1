"""Geometry-MMALS G1 research utilities."""

from .geometry import (
    fisher_rao_distance,
    pairwise_fisher_rao,
    route_geodesic_loss,
    paired_route_geometry_loss,
    paired_route_geometry_loss_stationary,
    stationary_route_target,
    normalize_functional_context,
    context_chord_target,
    paired_context_geometry_loss,
    context_path_spread_loss,
    factor_centroid_geometry_loss,
    cross_source_fiber_alignment_loss,
    normalized_stress,
)
from .metrics import (
    distance_order_correlation,
    neighborhood_preservation,
    linear_cka,
    route_entropy,
    bootstrap_mean_ci,
    grouped_geometry_scores,
    centroid_geometry_scores,
    fiber_alignment_scores,
    ridge_factor_probe,
    effective_rank,
    context_collapse_diagnostics,
)
from .model import ContextBottleneckRouter, SensoryBottleneckRouter
from .memory import ReconstructiveAuditMemory, SyntheticFunctionalMemory, TraceRecord

__all__ = [
    "fisher_rao_distance",
    "pairwise_fisher_rao",
    "route_geodesic_loss",
    "paired_route_geometry_loss",
    "paired_route_geometry_loss_stationary",
    "stationary_route_target",
    "normalize_functional_context",
    "context_chord_target",
    "paired_context_geometry_loss",
    "context_path_spread_loss",
    "factor_centroid_geometry_loss",
    "cross_source_fiber_alignment_loss",
    "normalized_stress",
    "distance_order_correlation",
    "neighborhood_preservation",
    "linear_cka",
    "route_entropy",
    "bootstrap_mean_ci",
    "grouped_geometry_scores",
    "centroid_geometry_scores",
    "fiber_alignment_scores",
    "ridge_factor_probe",
    "effective_rank",
    "context_collapse_diagnostics",
    "ContextBottleneckRouter",
    "SensoryBottleneckRouter",
    "ReconstructiveAuditMemory",
    "SyntheticFunctionalMemory",
    "TraceRecord",
]

__version__ = "1.0.9"
