"""Geometry-MMALS G1 research utilities."""

from .geometry import (
    fisher_rao_distance,
    pairwise_fisher_rao,
    route_geodesic_loss,
    paired_route_geometry_loss,
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
)
from .model import ContextBottleneckRouter, SensoryBottleneckRouter
from .memory import ReconstructiveAuditMemory, SyntheticFunctionalMemory, TraceRecord

__all__ = [
    "fisher_rao_distance",
    "pairwise_fisher_rao",
    "route_geodesic_loss",
    "paired_route_geometry_loss",
    "normalized_stress",
    "distance_order_correlation",
    "neighborhood_preservation",
    "linear_cka",
    "route_entropy",
    "bootstrap_mean_ci",
    "grouped_geometry_scores",
    "centroid_geometry_scores",
    "ContextBottleneckRouter",
    "SensoryBottleneckRouter",
    "ReconstructiveAuditMemory",
    "SyntheticFunctionalMemory",
    "TraceRecord",
]

__version__ = "1.0.7"
