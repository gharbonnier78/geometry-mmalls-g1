# Geometry-MMALS G1 v1.1.2 Results Release Notes

## Execution status

The five-seed pilot completed for model seeds `[0, 1, 2, 3, 4]` using build
revision `smooth-residual-spd-diagnostics-c0-r1`.

The original claim manifest retained the stale pre-execution status
`pilot_pending`. The corrected release changes metadata only. No numerical
result, split, checkpoint hash, host-cost matrix, or gate outcome changed.

## Final router decision

Primary treatment: `r5_smooth_residual_continuity`.

Primary structural reference: `r1_linear`.

Primary operational reference: `r0_mlp`.

Final decision: `r5_smooth_residual_router_not_qualified`.

The primary R5-versus-R1 held-out functional effects were favorable on average
but not robust:

- functional rho: `+0.010886`, 95% seed interval
  `[-0.048685, +0.070456]`;
- functional stress: `-0.017859`, interval
  `[-0.067115, +0.031396]`.

Local continuity q95 was nearly equal on average for R5 and R1, but the paired
seed interval exceeded the preregistered tolerance. Functional causal
specificity and operational non-degradation also failed.

## Secondary positive results

R5 significantly improved held-out common-cost functional geometry relative to
R0:

- functional rho: `+0.049574`, interval
  `[+0.024319, +0.074828]`;
- functional stress: `-0.039398`, interval
  `[-0.059165, -0.019631]`.

R5 also reduced the severe R3 held-out functional continuity q95 by `1.675537`
on average. Route-swap ordering and prediction-identity preservation passed.

## SPD diagnostic

The covariance-aware context diagnostic passed as candidate diagnostic
evidence. The combined centroid-plus-Log-Euclidean metric reduced stress by
`-0.044204`, with interval `[-0.063801, -0.024607]` and all five seeds
favorable.

This does not establish a learned Riemannian manifold and does not show that the
router uses covariance information.

## Verification

The independent Verification Stack v0.2.1 passes:

- safe ZIP extraction;
- result and manifest presence;
- five-seed count;
- clean 47-page execution PDF without traceback;
- completed-seed and export markers;
- matched compute;
- frozen context and host bank;
- source-partition separation;
- claim-manifest freshness;
- archive hygiene.

Experiment claims remain FAIL or NOT_TESTED exactly where the scientific gates
do not pass.

## Next stage

Do not add another increasingly complex router. The next stages are:

- v1.1.3 route-function memory trajectories and transport;
- v1.1.4 selective causal host adaptation and recovery;
- G2.1 bottom-up host feedback only after host usefulness is causally measured.
