# Geometry-MMALS G1 v1.0.5 -> v1.0.6
## Static route controls and same-final-task counterbalanced curriculum

### Motivation

The v1.0.5 seed-0 development run showed that explicit geometry produced small ordering gains but no prediction gain. More importantly, zeroing router inputs improved prediction and curriculum order dominated architectural effects. The previous curriculum comparison was confounded because the curricula ended on different final tasks.

### Protocol changes

| Change ID | Change | Scientific reason |
|---|---|---|
| CHG-106-01 | Require package/notebook version 1.0.6 | Prevent execution against stale v1.0.3-v1.0.5 source states |
| CHG-106-02 | Add equal uniform static route | Test whether adaptive routing beats the simplest host mixture |
| CHG-106-03 | Add learned global static route | Test whether instance-specific routing beats one optimized global mixture |
| CHG-106-04 | Add adaptive no-geometry anchor control | Match anchor and paired compute across adaptive/static route policies |
| CHG-106-05 | Export adaptive-route utility contrasts | Separate route usefulness from geometric order |
| CHG-106-06 | Audit learned-static zero-logit initialization | Ensure uniform starting point and reproducibility |
| CHG-106-07 | Rename router interventions | Remove ambiguity between router-input and host-input ablations |
| CHG-106-08 | Pair intervention deltas by source | Provide dependency-aware uncertainty |
| CHG-106-09 | Hold final task at 30 degrees | Remove terminal-task confounding |
| CHG-106-10 | Add four cyclic counterbalanced orders | Balance each non-final angle across pre-final positions |
| CHG-106-11 | Assert curriculum balance | Fail early on protocol drift |
| CHG-106-12 | Preserve C1/C2/extrapolation partitions | Avoid mixing descriptive and predictive evidence |
| CHG-106-13 | Restrict C4 to adaptive policies | Static routes cannot demonstrate context causality |
| CHG-106-14 | Extend host bundle to static controls | Compare functional mixtures, not route mass alone |
| CHG-106-15 | Export utility/intervention/curriculum evidence | Archive the new decision variables |
| CHG-106-16 | Keep C1-C6 unqualified | Prevent single-seed protocol results from becoming claims |

### Primary contrasts

1. `paired_anchor_adaptive_no_geometry` versus `paired_anchor_uniform_static`.
2. `paired_anchor_adaptive_no_geometry` versus `paired_anchor_learned_static`.
3. `paired_geometry_anchor_010` versus `paired_anchor_adaptive_no_geometry`.
4. `cb_a`, `cb_b`, `cb_c`, and `cb_d`, all ending at 30 degrees.

### Promotion boundary

No adaptive-route or curriculum claim is allowed until source-paired intervals are aggregated across at least five pilot seeds, failed runs are reported, and the route-policy advantage remains positive against both static controls.
