# Geometry-MMALS G1: v1.0.4 to v1.0.5

## Purpose

v1.0.5 addresses the remaining attribution issues identified after the matched-compute v1.0.4 development run: possible direct sensory bypass of inferred context, curriculum-order dependence, and the absence of paired source-level confidence intervals for treatment-control deltas.

## Added

1. Current-only optimizer-step-matched control.
2. Explicit standard, context-only, and direct-z0 router modes.
3. Context-zero, context-shuffle, z0-router-zero, and both-zero inference interventions.
4. C1 trained-angle geometry separated from C2 interpolation evidence.
5. Source-paired geometry and prediction deltas with paired bootstrap intervals.
6. Ascending, descending, and fixed-permuted curriculum controls.
7. Signed causal orientation and monotonicity gates in addition to CSR.
8. Context dependency, curriculum sensitivity, and mediation summaries.
9. Exact notebook/package/git/state/split provenance in the manifest.
10. Clean release packaging and non-recursive PDF export.

## Scientific non-claims

This release implements a stricter experiment. It does not claim that context mediation, curriculum robustness, causal geometry, host specialization, memory transport, or operational utility have passed qualification.
