"""Geometry-MMALS G1 research utilities."""

from .geometry import (
    fisher_rao_distance,
    pairwise_fisher_rao,
    route_geodesic_loss,
    normalized_stress,
)
from .metrics import (
    distance_order_correlation,
    neighborhood_preservation,
    linear_cka,
    route_entropy,
)

__all__ = [
    "fisher_rao_distance",
    "pairwise_fisher_rao",
    "route_geodesic_loss",
    "normalized_stress",
    "distance_order_correlation",
    "neighborhood_preservation",
    "linear_cka",
    "route_entropy",
]

__version__ = "1.0.0"

from .memory import ReconstructiveAuditMemory, SyntheticFunctionalMemory, TraceRecord
