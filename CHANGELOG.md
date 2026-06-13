# Changelog


## [1.0.5] - 2026-06-13

### Added
- Context mediation training and inference controls.
- Ascending, descending, and fixed-permuted curricula.
- Current-only optimizer-step-matched reference.
- C1/C2 evidence partitioning and source-paired bootstrap deltas.
- Signed causal orientation and monotonicity gates.
- Clean archive and exact-location notebook PDF export.

### Status
- Protocol implementation only. C1-C6 remain unqualified.


## v1.0.3 - Cross-angle paired protocol correction

- Replaced single-angle geometry batches with same-source multi-angle batches.
- Added `MultiAngleMNIST` and a stable square-root-simplex paired geometry loss.
- Preserved the continual sequence while using only previously seen angles as geometry anchors.
- Added source identifiers to traces and source-block bootstrap metrics.
- Replaced global pairwise significance and tie-fragile kNN evidence with paired-source and centroid geometry.
- Added held-out interpolation accuracy, NLL, context interpolation and route interpolation controls.
- Added staged accuracy matrices and trained-angle forgetting estimates.
- Added signed causal route-direction probes with matched-norm orthogonal controls.
- Added strict package version and git-SHA recording.
- Kept C1-C6 explicitly unqualified pending multi-seed runs and hardened baselines.

## v1.0.2 - Numerical-stability and Colab execution patch

- Fixed NaN gradients in `route_geodesic_loss` for identical or nearly identical routes.
- Added a dtype-aware interior clamp and diagonal masking before `arccos`.
- Added a regression test for uniform-route backward stability.
- Consolidated the Colab setup around the active kernel interpreter and `src/` layout.
- Added finite-value guards, stage diagnostics, and a ridge-stabilized causal tangent probe.
- Replaced brittle hard-coded PDF export paths with notebook discovery and explicit nbconvert arguments.

## v1.0.1 - Release-audit patch

- Clarified C0-only package status and C1-C5 non-claims.
- Added numeric pilot gates and C4 CSR threshold.
- Added TPUT-to-G1 notation bridge.
- Labeled the notebook route-geodesic loss as the G1-A supervised/grounded variant.
- Added dual-memory executable stubs and tests.
- Added core model trace tests.
- Made pytest work from the repository root through `pythonpath = ["src"]`.
- Hardened Fisher-Rao pairwise distances near simplex boundaries.


## 1.0.0 - 2026-06-13

- Formalized the distinction between external audit/control geometry and internal functional geometry.
- Added the full Geometry-MMALS G1 LaTeX article and compiled PDF.
- Added a RotatedMNIST protocol, PyTorch architecture scaffold and route-simplex geometry utilities.
- Added host ablation, geometry, drift and cross-seed role-matching metrics.
- Added a Colab-ready notebook scaffold.
- Added synthetic smoke outputs, claim gates and reproducibility documentation.
- Reserved energy-guided routing for G2 and phase-aware/quantum-inspired routing for G3.
