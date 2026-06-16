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

from .functional_routing import (
    FunctionalRoutingMMALS,
    FunctionalRoutingTrace,
    LinearContextRouter,
    MLPContextRouter,
    PrototypeEnergyRouter,
    entropic_transport_cost,
    half_chord_distance,
    host_functional_diversity_loss,
    host_output_cost_matrix,
    host_specialization,
    host_territory,
    pairwise_functional_route_distances,
    parameter_count,
    reconstruct_route_from_root_probe,
    root_simplex_chord,
    spherical_kmeans,
    territory_overlap,
    usage_balance_loss,
)

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
    "FunctionalRoutingMMALS",
    "FunctionalRoutingTrace",
    "LinearContextRouter",
    "MLPContextRouter",
    "PrototypeEnergyRouter",
    "entropic_transport_cost",
    "half_chord_distance",
    "host_functional_diversity_loss",
    "host_output_cost_matrix",
    "host_specialization",
    "host_territory",
    "pairwise_functional_route_distances",
    "parameter_count",
    "reconstruct_route_from_root_probe",
    "root_simplex_chord",
    "spherical_kmeans",
    "territory_overlap",
    "usage_balance_loss",
]


from .functional_routing import (
    HybridDirectionalPrototypeRouter,
    UniformRouter,
    local_continuity_ratio,
    permute_hosts_and_routes,
    route_weighted_synthesis,
)


from .functional_routing import SmoothSimplexResidualRouter, simplex_continuity_hinge_loss
from .spd_geometry import (
    affine_invariant_distance,
    bures_wasserstein_distance,
    log_euclidean_distance,
    pairwise_spd_distances,
    regularized_covariance,
)

# The verification stack is intentionally not imported here.
# It is an optional layer and may require pypdf. Import it explicitly with:
#     from geometry_mmalls.verification import verify_evidence_bundle

__version__ = "1.1.3"

from .memory_transport import (
    PathStatistics,
    RootGaussianMemory,
    compile_root_gaussian,
    cross_functional_route_costs,
    distributional_functional_transport,
    distillation_kl,
    functional_path_statistics,
    functional_transport_anchor_loss,
    latent_anchor_loss,
    root_gaussian_nll,
    root_route_anchor_loss,
    uniform_empirical_transport,
)
