# Geometry-MMALS G1 v1.0.6
## Static Route Controls and Counterbalanced Curriculum

**Document status:** archival protocol report  
**Scientific status:** C0 protocol implementation only  
**Date:** 14 June 2026

## 1. Purpose

Geometry-MMALS G1 tests whether MMALS develops an internal functional geometry that is predictive, causally meaningful, and operationally useful. v1.0.6 focuses on a narrower engineering question exposed by the v1.0.5 development run:

> Does instance-adaptive routing add value beyond a uniform or learned global static mixture, and are curriculum effects still present when every curriculum ends on the same final task?

The release defines a falsifiable experiment. It does not claim that C1-C6 or adaptive-route superiority have passed.

## 2. Evidence motivating v1.0.6

The v1.0.5 seed-0 development archive showed:

- the explicit geometry term produced a small positive context-order effect but no predictive gain;
- a 0.10 retention anchor improved interpolation, final trained accuracy, and forgetting;
- standard adaptive routing achieved about 0.521 accuracy across the mediation evaluation, while router-z0 zeroing reached about 0.617 and both-input zeroing about 0.611;
- context-induced route displacement was only about 0.148 of the direct-z0 displacement;
- a non-monotone curriculum reached about 0.704 interpolation accuracy, but it ended on a different final angle than the monotone curricula;
- principal adaptive variants had mean causal specificity ratios below one.

These observations are development evidence from one seed. They motivate controls; they are not claims.

## 3. New research questions

1. Does an adaptive standard router outperform a fixed uniform route under equal paired inputs, anchor weight, image forwards, and optimizer steps?
2. Does it outperform a learned global static route initialized at the uniform simplex point?
3. Does adding the geometry term improve an anchored adaptive route relative to the same adaptive route without geometry?
4. Do router intervention effects have source-paired bootstrap intervals that exclude zero?
5. Do curriculum effects persist across four cyclic orders that all end at 30 degrees and balance every other angle across pre-final positions?

## 4. Route-policy variants

| Variant | Route policy | Geometry | Anchor | Main purpose |
|---|---|---:|---:|---|
| current_only_step_matched | adaptive z0 + context | 0 | 0 | cheaper step-matched reference |
| paired_compute_matched_no_geometry | adaptive z0 + context | 0 | 0 | paired compute control |
| paired_geometry | adaptive z0 + context | 0.10 | 0 | geometry attribution |
| paired_anchor_adaptive_no_geometry | adaptive z0 + context | 0 | 0.10 | adaptive route utility control |
| paired_geometry_anchor_010 | adaptive z0 + context | 0.10 | 0.10 | geometry plus retention |
| paired_anchor_context_only | adaptive context only | 0 | 0.10 | context sufficiency |
| paired_anchor_direct_z0 | adaptive z0 only | 0 | 0.10 | sensory bypass |
| paired_anchor_uniform_static | fixed uniform route | 0 | 0.10 | simplest static control |
| paired_anchor_learned_static | learned global route | 0 | 0.10 | optimized static control |

The learned static logits start at zero, so the initial route is exactly uniform.

## 5. Counterbalanced curricula

All primary curricula contain the same five angles and end at 30 degrees:

- cb_a: -60, -30, 0, 60, 30
- cb_b: -30, 0, 60, -60, 30
- cb_c: 0, 60, -60, -30, 30
- cb_d: 60, -60, -30, 0, 30

Across the first four positions, each non-final angle appears once in every position. This removes the terminal-task confound and balances serial position.

## 6. Router intervention evidence

The anchored standard model is evaluated without retraining under:

- adaptive_standard;
- router_context_zeroed;
- router_context_shuffled;
- router_z0_zeroed;
- router_both_inputs_zeroed.

Accuracy, class-log-probability change, and route displacement are averaged per source image. Treatment-control differences are then bootstrapped across source IDs.

## 7. Evidence partitions and gates

- C1 trained geometry uses only -60, -30, 0, 30, 60.
- C2 interpolation uses only -45, -15, 15, 45.
- Extrapolation uses -75 and 75 and is reported separately.
- Static routes are excluded from C4 because they cannot demonstrate context causality.
- Adaptive-route utility requires superiority over both uniform and learned-static routes at equal compute.
- Curriculum robustness requires bounded variation across the four same-final-task orders.

## 8. Tracked changes

CHG-106-01 through CHG-106-16 add release integrity, uniform and learned-static route controls, adaptive utility contrasts, clear intervention names, source-paired intervention intervals, same-final-task cyclic curricula, position-balance assertions, static host evidence, and clean archival exports.

## 9. Archive layout

- `notebooks/Geometry_MMALS_G1_StaticRoutes_CounterbalancedCurriculum_v1_0_6.ipynb`
- `docs/reports/Geometry_MMALS_G1_v1_0_6_Static_Routes_Counterbalanced_Curriculum_Report.pdf`
- `docs/reports/Geometry_MMALS_G1_v1_0_6_Static_Routes_Counterbalanced_Curriculum_Report.md`
- `docs/changes/Geometry_MMALS_G1_v1_0_5_to_v1_0_6.md`
- `configs/rotated_mnist_g1_v106.yaml`

The clean package declares version 1.0.6 and excludes `.git`, datasets, runtime results, caches, bytecode, editable-install metadata, and local environments.

## 10. Qualification boundary

v1.0.6 is ready for smoke and development execution. No C1-C6 or adaptive-route claim is permitted until the exact release is executed, numeric gates are frozen, the sensory gate passes, at least five pilot seeds and ten final seeds are aggregated, failed runs are reported, adaptive routing beats both static controls, curriculum effects are bounded under the counterbalance, and a second transformation is replicated.
