# MMALS Verification Summary

- Experiment: `geometry_mmalls_g1_v1_1_1`
- Verification engine: `0.2.1`
- PDF pages: 44
- ZIP files inventoried: 140

## Claims

| Claim | Status | Statement |
|---|---|---|
| `CONTEXT_GEOMETRY` | **PASS** | The inferred context has replicated representational geometry. |
| `HELDOUT_NOMINAL_ROUTE_MEDIATION` | **FAIL** | The tested router improves held-out nominal route order. |
| `HELDOUT_FUNCTIONAL_ROUTE_MEDIATION` | **FAIL** | The tested router improves held-out functional route order under a common cost matrix. |
| `LOCAL_STABILITY` | **FAIL** | The router reduces high-tail local sensitivity without route collapse. |
| `CAUSAL_SPECIFICITY` | **FAIL** | Factor-tangent interventions are functionally more specific than orthogonal controls. |
| `HOST_SPECIALIZATION` | **FAIL** | Stable functional host specialization is established. |
| `OPERATIONAL_NON_DEGRADATION` | **FAIL** | The routing intervention stays within the preregistered non-degradation margin. |
| `OPERATIONAL_SUPERIORITY` | **FAIL** | The routing intervention improves operational performance. |
| `MEMORY_TRANSPORT` | **FAIL** | Route-function memory transport is demonstrated. |
| `HELDOUT_FUNCTIONAL_STRESS_REDUCTION` | **NOT_TESTED** | The primary smooth residual treatment reduces held-out common-cost functional stress. |
| `SPD_COVARIANCE_VALUE` | **NOT_TESTED** | Regularized covariance geometry adds factor-discrimination value beyond centroid-only context geometry. |

## Protocol findings

| Rule | Status | Finding |
|---|---|---|
| `ZIP_SAFE_PATHS` | **PASS** | ZIP extraction completed without unsafe paths. |
| `RESULTS_PRESENT` | **PASS** | A results manifest or gate summary is present. |
| `RUN_MANIFEST` | **PASS** | Run manifest parsed. |
| `CLAIM_MANIFEST` | **PASS** | Claim manifest parsed. |
| `SEED_COUNT` | **PASS** | Detected 5 model seeds; minimum is 5. |
| `PDF_PARSE` | **PASS** | Execution PDF has 44 pages. |
| `PDF_NO_TRACEBACK` | **PASS** | No Python traceback detected. |
| `PDF_EXECUTION_MARKERS` | **PASS** | Completed-seed and export markers checked. |
| `MATCHED_COMPUTE` | **PASS** | Matched compute checked. |
| `FROZEN_CONTEXT` | **PASS** | Frozen-context audit checked. |
| `SOURCE_PARTITION_SEPARATION` | **PASS** | Partition hashes checked for accidental identity. |
| `CLAIM_MANIFEST_FRESHNESS` | **PASS** | Claim state compared with execution evidence. |
| `ARCHIVE_HYGIENE` | **PASS** | Archive hygiene checked. |
| `EXPERIMENT_GATE::C0_context_and_common_bank_frozen` | **PASS** | Imported experiment gate C0_context_and_common_bank_frozen. |
| `EXPERIMENT_GATE::C0_equal_router_compute` | **PASS** | Imported experiment gate C0_equal_router_compute. |
| `EXPERIMENT_GATE::C1_heldout_nominal_mediation` | **FAIL** | Imported experiment gate C1_heldout_nominal_mediation. |
| `EXPERIMENT_GATE::C1_heldout_functional_mediation_common_cost` | **FAIL** | Imported experiment gate C1_heldout_functional_mediation_common_cost. |
| `EXPERIMENT_GATE::C1_local_continuity_tail` | **FAIL** | Imported experiment gate C1_local_continuity_tail. |
| `EXPERIMENT_GATE::C2_route_swap_order` | **PASS** | Imported experiment gate C2_route_swap_order. |
| `EXPERIMENT_GATE::C4_functional_causal_specificity` | **FAIL** | Imported experiment gate C4_functional_causal_specificity. |
| `EXPERIMENT_GATE::C4_identity_preservation` | **PASS** | Imported experiment gate C4_identity_preservation. |
| `EXPERIMENT_GATE::C6_operational_non_degradation` | **FAIL** | Imported experiment gate C6_operational_non_degradation. |
| `EXPERIMENT_GATE::C3_mature_host_specialization` | **FAIL** | Imported experiment gate C3_mature_host_specialization. |
| `EXPERIMENT_GATE::C5_memory_transport` | **FAIL** | Imported experiment gate C5_memory_transport. |
| `EXPERIMENT_GATE::operational_superiority` | **FAIL** | Imported experiment gate operational_superiority. |
