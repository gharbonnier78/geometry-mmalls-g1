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
]

__version__ = "1.0.5"

from .memory import ReconstructiveAuditMemory, SyntheticFunctionalMemory, TraceRecord
