# Geometry-MMALS G1 v1.0.5
## Context Mediation, Curriculum Order, and Paired Delta Evidence

**Document status:** archival protocol report  
**Scientific status:** C0 protocol implementation only  
**Date:** 13 June 2026

## 1. Purpose

Geometry-MMALS G1 asks whether MMALS learns a functional internal geometry rather than only a geometry of external audit indicators. v1.0.5 narrows the question further: is route geometry genuinely mediated by inferred context, is it stable to curriculum order, and is the treatment effect supported by paired source-level uncertainty?

The release does not claim that C1-C6 have passed. It defines a controlled experiment and the evidence bundle required to decide those gates later.

## 2. Evidence motivating v1.0.5

The v1.0.4 seed-0 development run corrected initialization and paired-compute confounds. Its main observations were:

- the explicit geometry term changed local route order only modestly, but improved global route-centroid order;
- geometry alone added almost no interpolation or retention benefit at matched compute;
- a 0.10 old-angle classification anchor improved interpolation, final accuracy, forgetting, global route alignment, and absolute causal specificity;
- context order did not improve, while route order did, suggesting that the router may bypass context through its direct sensory input;
- absolute causal specificity could look strong even when the signed route effect was reversed;
- only an ascending angle curriculum had been tested.

These are development observations, not qualified claims.

## 3. v1.0.5 research questions

1. **Context mediation:** Does the inferred context materially affect route choice and prediction, beyond direct access to the sensory representation?
2. **Geometry attribution:** Does the explicit route geometry term improve trained-angle and interpolation geometry under matched initialization, source order, image forwards, and optimizer steps?
3. **Curriculum robustness:** Are route geometry, interpolation, retention, and causal direction stable under ascending, descending, and fixed-permuted angle orders?
4. **Paired evidence:** Do treatment-control deltas remain positive when computed for each source image and bootstrapped as paired blocks?
5. **Signed causality:** Does increasing the learned context coordinate move routes in the expected increasing-angle direction with monotonic magnitude and preserved class evidence?

## 4. Experimental variants

| Variant | Input views | Router input | Geometry | Retention anchor | Primary purpose |
|---|---|---|---:|---:|---|
| current_only_step_matched | current angle | z0 + context | 0 | 0 | optimizer-step-matched simple reference |
| paired_compute_matched_no_geometry | all seen angles | z0 + context | 0 | 0 | paired compute control |
| paired_geometry | all seen angles | z0 + context | 0.10 | 0 | geometry attribution |
| paired_geometry_anchor_010 | all seen angles | z0 + context | 0.10 | 0.10 | retention trade-off |
| paired_anchor_context_only | all seen angles | context only | 0.10 | 0.10 | context mediation training control |
| paired_anchor_direct_z0 | all seen angles | z0 only | 0.10 | 0.10 | direct sensory bypass control |

## 5. Context mediation interventions

The anchored standard model is evaluated without retraining under five conditions:

- standard: router receives z0 and inferred context;
- context zeroed: context is replaced by zero;
- context shuffled: context is borrowed from another source in the batch;
- z0 router zeroed: only inferred context reaches the router;
- both zeroed: neither sample-specific input reaches the router.

The report exports accuracy drop, class log-probability drop, and route shift. A context-mediated route requires non-trivial sensitivity to context removal or shuffling. If direct-z0 removal has a much larger effect than context interventions, the route is likely dominated by a sensory bypass.

## 6. Evidence partitioning

- **C1 trained geometry:** only -60, -30, 0, 30, 60 degrees.
- **C2 interpolation:** only -45, -15, 15, 45 degrees.
- **Extrapolation:** -75 and 75 degrees, reported separately.

No global all-pairs p-value is used. Same-source geometry is calculated inside source blocks. Treatment-control differences are paired by source ID and bootstrapped across sources.

## 7. Curriculum controls

The anchored standard method is trained with the same immutable initialization and budgets under:

- ascending: -60, -30, 0, 30, 60;
- descending: 60, 30, 0, -30, -60;
- fixed permuted: 0, -60, 60, -30, 30.

The protocol reports order sensitivity in final trained-angle accuracy, interpolation accuracy, forgetting, route geometry, and signed causal direction.

## 8. Signed causal gate

A candidate C4 result requires all of the following:

1. mean causal specificity ratio greater than the frozen threshold;
2. positive intervention scale produces positive route movement along the increasing-angle route direction;
3. negative scale produces negative movement;
4. magnitude at absolute scale 2 exceeds magnitude at absolute scale 1;
5. class evidence remains within the identity-preservation bound;
6. source-block confidence intervals and multi-seed replication.

Absolute CSR alone is not sufficient.

## 9. Tracked changes

CHG-105-01 through CHG-105-15 add version guards, step-matched current-only control, explicit router modes, inference mediation interventions, C1/C2 separation, source-paired bootstrap deltas, curriculum controls, signed causal orientation, context dependency summaries, clean export, clean release packaging, strict epistemic labels, and qualification blocks.

## 10. Archive layout

- `notebooks/Geometry_MMALS_G1_ContextMediation_Curriculum_v1_0_5.ipynb`
- `docs/reports/Geometry_MMALS_G1_v1_0_5_Context_Mediation_Curriculum_Report.pdf`
- `docs/reports/Geometry_MMALS_G1_v1_0_5_Context_Mediation_Curriculum_Report.md`
- `docs/changes/Geometry_MMALS_G1_v1_0_4_to_v1_0_5.md`
- `configs/rotated_mnist_g1_v105.yaml`

The clean GitHub archive excludes `.git`, datasets, runtime results, caches, bytecode, editable-install metadata, and local environments.

## 11. Qualification boundary

v1.0.5 is ready for smoke and development execution. It is not ready for C1-C6 promotion until numeric gates are frozen, the sensory gate passes, at least five pilot seeds and ten final seeds are run, failed seeds are reported, context mediation and curriculum robustness are bounded, causal orientation is validated, and a second controlled transformation is replicated.
