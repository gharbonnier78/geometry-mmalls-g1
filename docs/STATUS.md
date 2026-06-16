# Geometry-MMALS G1 Status

## Latest executed evidence: v1.1.2

The five-seed smooth-residual/SPD pilot completed for model seeds
`[0, 1, 2, 3, 4]` under a common frozen sensory encoder, context encoder, host
bank, synthesis layer, classifier, and host-functional cost matrix.

### Protocol integrity

- frozen context and common host bank: **PASS**;
- matched router compute: **PASS**;
- route-swap ordering: **PASS**;
- prediction-identity preservation: **PASS**.

### Primary router decision

The R5 smooth-residual plus continuity router is **not qualified** against the
R1 linear structural reference.

- held-out functional rho effect: `+0.010886`, 95% seed interval
  `[-0.048685, +0.070456]`;
- held-out functional stress effect: `-0.017859`, interval
  `[-0.067115, +0.031396]`;
- continuity non-degradation: **FAIL**;
- functional causal specificity: **FAIL**;
- operational non-degradation versus R0: **FAIL**.

### Secondary router findings

R5 is significantly more ordered and lower-stress than R0 on held-out
common-cost functional geometry:

- rho effect: `+0.049574`, interval `[+0.024319, +0.074828]`;
- stress effect: `-0.039398`, interval `[-0.059165, -0.019631]`.

R5 also removes the severe local-continuity tail of R3, but does not robustly
improve beyond R1.

### SPD diagnostic

Covariance-aware context geometry adds measurable factor information beyond
centroid-only geometry:

- combined stress effect: `-0.044204`;
- 95% seed interval: `[-0.063801, -0.024607]`;
- favorable seeds: `5/5`.

This is diagnostic evidence only. It does not establish a learned Riemannian
manifold or an SPD-aware routing advantage.

## Current scientific claim

Geometry-MMALS has replicated evidence for grounded context geometry and
non-arbitrary route-function structure. Structured low-capacity routing is more
geometrically ordered than a flexible MLP, but the current smooth-residual
router does not improve robustly beyond a linear router and is not operationally
qualified.

## Next executable targets

- **v1.1.3:** route-function memory trajectories and transport;
- **v1.1.4:** selective causal host adaptation, recovery, and host-bank alignment;
- **G2.1:** explicit bottom-up host feedback after host usefulness is causally
  established;
- **TPUT:** goal-conditioned forward-backward control, outside the current G1
  claim scope.


## v1.1.3 C0

Functional memory transport specification and executable limited-replay Colab added. Empirical pilot pending.

## v1.1.3 C0-r2 pre-pilot status

- reviewer corrections integrated: **YES**;
- gradient calibration completed: **NO**;
- pilot lock: **FALSE**;
- five-seed pilot: **BLOCKED until calibration is committed**;
- frozen-host regime: **final planned experiment**;
- next regime after v1.1.3: controlled causal host adaptation, regardless of positive, negative, or partial result.
