# Geometry-MMALS G1 v1.0.3 -> v1.0.4 tracked changes

## Release purpose

v1.0.4 removes the two main attribution confounds in the first cross-angle paired development run and adds a controlled retention mechanism.

## Added

- `current_only_no_geometry` external cost reference.
- `paired_compute_matched_no_geometry` as the primary geometry control.
- `paired_geometry` as the geometry treatment.
- `paired_geometry_anchor_010` as the no-extra-forward retention treatment.
- One immutable initial MMALS state shared by all methods.
- SHA-256 digest for the initial state and each source split.
- Deterministic, method-independent DataLoader ordering.
- Per-stage image-forward, source-example, optimizer-step, and wall-time accounting.
- Hard assertions that all paired variants have identical compute budgets.
- Sensory acceptance gate before MMALS qualification.
- Explicit geometry-attribution and retention-anchor contrast tables.
- Route mass in the host ablation bundle.
- Smoke/development/qualification run modes.

## Changed

- The primary scientific comparison is no longer paired geometry versus the cheaper current-only model.
- Geometry attribution is now paired geometry versus a paired compute-matched control.
- Retention is tested using old-angle classification evidence already present in paired batches.
- The development sensory grove uses a larger pretraining subset than v1.0.3.
- The manifest now records method specifications, initial-state hash, compute-audit status, and sensory-gate result.

## Preserved

- Same-source multi-angle training primitive.
- Held-out interpolation and extrapolation angles.
- Source-block bootstrap and centroid geometry metrics.
- Signed causal probe with matched orthogonal controls.
- Strict C0-only accepted status and C1-C6 non-claims.

## Scientific decision rule

The geometry objective is attributable only if `paired_geometry` improves the matched paired control under identical initialization, tensors, source order, forwards, and optimizer steps.

The retention anchor is useful only if it reduces forgetting without erasing most of the geometry/interpolation gain and without adding image-forward compute.
