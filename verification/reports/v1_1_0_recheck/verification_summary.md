# MMALS Verification Summary

- Experiment: `geometry_mmalls_g1_v1_1_0`
- Verification engine: `0.2.0`
- PDF pages: 67
- ZIP files inventoried: 538

## Claims

| Claim | Status | Statement |
|---|---|---|
| `CONTEXT_GEOMETRY` | **PASS** | The inferred context has replicated representational geometry. |
| `HELDOUT_NOMINAL_ROUTE_MEDIATION` | **PARTIAL** | The tested router improves held-out nominal route order. |
| `HELDOUT_FUNCTIONAL_ROUTE_MEDIATION` | **PARTIAL** | The tested router improves held-out functional route order under a common cost matrix. |
| `LOCAL_STABILITY` | **PARTIAL** | The router reduces high-tail local sensitivity without route collapse. |
| `CAUSAL_SPECIFICITY` | **FAIL** | Factor-tangent interventions are functionally more specific than orthogonal controls. |
| `HOST_SPECIALIZATION` | **FAIL** | Stable functional host specialization is established. |
| `OPERATIONAL_NON_DEGRADATION` | **PASS** | The routing intervention stays within the preregistered non-degradation margin. |
| `OPERATIONAL_SUPERIORITY` | **FAIL** | The routing intervention improves operational performance. |
| `MEMORY_TRANSPORT` | **FAIL** | Route-function memory transport is demonstrated. |

## Protocol findings

| Rule | Status | Finding |
|---|---|---|
| `ZIP_SAFE_PATHS` | **PASS** | ZIP extraction completed without unsafe paths. |
| `RESULTS_PRESENT` | **PASS** | A results manifest or gate summary is present. |
| `RUN_MANIFEST` | **PASS** | Run manifest parsed. |
| `CLAIM_MANIFEST` | **PASS** | Claim manifest parsed. |
| `SEED_COUNT` | **PASS** | Detected 5 model seeds; minimum is 5. |
| `PDF_PARSE` | **PASS** | Execution PDF has 67 pages. |
| `PDF_NO_TRACEBACK` | **PASS** | No Python traceback detected. |
| `PDF_EXECUTION_MARKERS` | **PASS** | Completed-seed and export markers checked. |
| `MATCHED_COMPUTE` | **PASS** | Matched compute checked. |
| `FROZEN_CONTEXT` | **PASS** | Frozen-context audit checked. |
| `SOURCE_PARTITION_SEPARATION` | **PASS** | Partition hashes checked for accidental identity. |
| `CLAIM_MANIFEST_FRESHNESS` | **FAIL** | Claim state compared with execution evidence. |
| `ARCHIVE_HYGIENE` | **PARTIAL** | Archive hygiene checked. |
| `EXPERIMENT_GATE::C0_context_frozen_and_preserved` | **PASS** | Imported experiment gate C0_context_frozen_and_preserved. |
| `EXPERIMENT_GATE::C0_equal_compute` | **PASS** | Imported experiment gate C0_equal_compute. |
| `EXPERIMENT_GATE::C1_nominal_route_mediation` | **PASS** | Imported experiment gate C1_nominal_route_mediation. |
| `EXPERIMENT_GATE::C1_functional_route_mediation` | **PASS** | Imported experiment gate C1_functional_route_mediation. |
| `EXPERIMENT_GATE::C1_probe_generalization` | **PASS** | Imported experiment gate C1_probe_generalization. |
| `EXPERIMENT_GATE::C4_functional_causal_specificity` | **FAIL** | Imported experiment gate C4_functional_causal_specificity. |
| `EXPERIMENT_GATE::C3_host_ecology` | **FAIL** | Imported experiment gate C3_host_ecology. |
| `EXPERIMENT_GATE::C4_identity_preservation` | **FAIL** | Imported experiment gate C4_identity_preservation. |
| `EXPERIMENT_GATE::C6_operational_non_degradation` | **PASS** | Imported experiment gate C6_operational_non_degradation. |
| `EXPERIMENT_GATE::C5_memory_transport` | **FAIL** | Imported experiment gate C5_memory_transport. |
| `EXPERIMENT_GATE::operational_superiority` | **FAIL** | Imported experiment gate operational_superiority. |
| `EXPERIMENT_GATE::C3_mature_host_specialization` | **FAIL** | Canonical gate C3_mature_host_specialization mapped from C3_host_ecology. |
