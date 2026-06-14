# Changelog

## v1.0.7 - Context-bottleneck mediation experiment

- Added a dedicated `ContextBottleneckRouter` that never receives `z0`.
- Added a capacity-matched `SensoryBottleneckRouter` control.
- Replaced the non-diagnostic stop-gradient proposal with explicit information-path controls.
- Reduced the core run to six targeted equal-compute variants.
- Added bottleneck, sensory, standard and static paired contrasts.
- Added context/z0 route-shift and accuracy-drop mediation diagnostics with `context_is_primary`.
- Preserved trained, interpolation and extrapolation geometry partitions.
- Restricted counterbalanced curriculum reruns to the primary context-bottleneck treatment.
- Added 19 passing package tests, including bottleneck router shape, gradient and parameter-isolation tests.
- Archived the reviewer status PDF and complete LaTeX source inside the GitHub package.
- Kept C1-C6, successful context mediation and operational superiority explicitly unqualified.

## v1.0.6 - Static route controls and counterbalanced curriculum

- Added uniform and learned global static route controls.
- Added an adaptive no-geometry anchored control for clean route-policy attribution.
- Added explicit adaptive-route utility contrasts.
- Renamed router interventions and added source-paired bootstrap intervals.
- Replaced terminal-confounded curricula with four same-final-task cyclic counterbalances.
- Added curriculum position-balance assertions and exports.
- Added package/notebook version equality and source-hash evidence.
- Restricted causal geometry gates to adaptive route policies.
- Extended host ablation evidence to static mixtures.
- Kept C1-C6 and adaptive-route superiority explicitly unqualified.

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
