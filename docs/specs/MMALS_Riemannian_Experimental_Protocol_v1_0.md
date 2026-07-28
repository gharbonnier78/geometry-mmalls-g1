# MMALS Riemannian Experimental Protocol v1.0

**Status:** preregistration-ready specification; not an executed result.  
**Article:** `docs/reports/MMALS_Riemannian_Learning_Architecture_v1_0.pdf`  
**Date:** 28 July 2026

## 1. Decision question

Does an intrinsic geometry of MMALS route distributions and functional-memory descriptors explain or improve continual-learning behaviour beyond Euclidean diagnostics, output distillation, replay, and fixed-metric controls at matched parameter, compute, and remembered-source budgets?

The protocol is deliberately asymmetric: a diagnostic can qualify without becoming a training mechanism. A geometry enters the objective only after it adds held-out explanatory value and survives null controls.

## 2. Frozen prerequisites

1. Reuse the validated Geometry-MMALS G1 v1.1.x sensory encoder, context checkpoints, host bank, and functional-routing traces.
2. Freeze train/validation/test partitions, seed lists, remembered-source access, and preprocessing before comparing metrics.
3. Preserve raw per-seed outputs and failed runs.
4. Do not select a geometry on the final test stream.
5. Record exact source and code commit hashes.

## 3. Stage A — Post-hoc metric qualification

No model retraining is allowed.

### A1. Route metrics

For route distributions `r, s` compare:

- Euclidean distance;
- Hellinger distance;
- Jensen–Shannon divergence;
- Fisher–Rao distance with an explicitly declared treatment of zero probabilities.

### A2. Functional descriptors

For each context and host/synthesis state, construct:

- raw latent mean vectors;
- shrinkage covariance matrices;
- normalized full-rank correlation matrices;
- low-rank-plus-diagonal SPD descriptors.

Compare:

- latent MSE;
- fixed Log-Euclidean SPD distance;
- Cholesky product distance;
- affine-invariant SPD distance where computationally feasible.

### A3. Primary explanatory endpoint

Use nested seed-held-out regression to predict context-level forgetting or functional-output drift. Report incremental out-of-sample `R²`, calibration, coefficient uncertainty, and residual diagnostics relative to the Euclidean-only model.

### A4. Qualification gate

A candidate metric qualifies for Stage B only when all conditions hold:

- positive held-out incremental explanatory value;
- same effect direction in at least 4 of 5 pilot seeds;
- no dependence on one pathological seed;
- superiority over shuffled descriptors and random orthogonal coordinate controls;
- stable numerical behaviour and declared computational cost.

At most one route metric and one functional descriptor advance.

## 4. Stage B — Fixed intrinsic geometry ablation

Add the qualified fixed metric to training without changing architecture capacity.

Treatments:

1. output distillation only;
2. latent MSE functional memory;
3. fixed Log-Euclidean or qualified SPD memory;
4. Cholesky stability control;
5. shuffled-metric control;
6. random pullback-map control;
7. replay baseline with the same remembered-source budget.

Primary endpoints:

- final average accuracy;
- average forgetting;
- intransigence/new-context accuracy;
- expected calibration error and NLL;
- active FLOPs, wall time, peak memory, and stored bytes.

A lower geometric drift is not success when new-context learning degrades.

## 5. Stage C — Learnable pullback geometry

Only run after a fixed intrinsic metric qualifies.

### C1. Parameterization

Use a constrained, smooth, monotone spectral map with a low-dimensional parameter budget. Add explicit conditioning and identity-neighbourhood regularization. Preserve permutation invariance near repeated eigenvalues or use grouped/isotropic parameters.

### C2. Controls

- fixed qualified metric;
- same number of unconstrained scalar parameters attached to a non-geometric baseline;
- frozen random pullback map;
- Cholesky product geometry;
- identity pullback.

### C3. Selection rule

Select hyperparameters on validation streams using a utility frontier, not final accuracy alone. Report the full Pareto surface for retention, intransigence, calibration, compute, and memory.

### C4. Promotion gate

The learnable geometry qualifies only if it improves at least one preregistered operational objective without materially worsening the others, replicates over seeds, and exceeds the parameter-matched non-geometric control.

## 6. Stage D — Intrinsic context classification and normalization

Riemannian multinomial logistic regression is admissible only when the context object has a declared manifold and valid logarithmic map. LieBN or GyroBN is admissible only at interfaces satisfying the required Lie-group or gyrogroup structure.

Required ablations:

- Euclidean classifier on coordinates;
- tangent-space classifier;
- intrinsic RMLR;
- intrinsic normalization on/off;
- matched affine layer with equal parameter count.

Do not place manifold normalization on the route simplex merely by analogy.

## 7. Stage E — Continual transport

Test memory transport only after Stage B or C qualifies.

Compare:

- direct Euclidean comparison of old/current descriptors;
- fixed-map transport;
- parallel transport under the qualified metric;
- learned transport with cycle-consistency;
- replay-only and distillation-only controls.

Transport must improve old-context functional prediction, not merely reduce an internal distance.

## 8. Secondary hierarchy branch

Hyperbolic or Proper Velocity networks are deferred until a benchmark has a grounded hierarchical or branching factor. Required controls are Euclidean, spherical, Poincaré/Lorentz, and Proper Velocity representations, with distortion, stability, gradient, and behavioural metrics reported together.

RotatedMNIST is not a valid primary justification because its grounded factor is circular rather than hierarchical.

## 9. Statistical plan

- Development: one seed, integrity only; no claims.
- Pilot: five seeds, confidence intervals and seed-level direction checks.
- Qualification: ten preregistered seeds when the pilot passes.
- Nested model selection by seed or source identity.
- Bootstrap confidence intervals over seeds and remembered-source units.
- Report raw values, effect sizes, and uncertainty; do not rely only on p-values.
- Multiple primary endpoints require a declared correction or a single composite gate fixed before execution.

## 10. Falsification conditions

Stop or defer the Riemannian branch when any of the following occurs:

1. intrinsic metrics add no held-out explanatory value over Euclidean controls;
2. gains disappear under parameter or remembered-source matching;
3. the metric improves its own loss but not behaviour;
4. covariance noise dominates the descriptor;
5. learned spectral maps become ill-conditioned or identity-ambiguous;
6. geometry reduces forgetting by suppressing plasticity;
7. manifold assumptions are not satisfied;
8. route or host roles are not reproducible across seeds;
9. the simplest fixed metric remains equal or better.

## 11. Required output bundle

- frozen configuration and data manifests;
- per-seed raw metrics;
- route and descriptor tables;
- numerical-stability report;
- compute/memory accounting;
- null-control results;
- claim-to-artifact manifest;
- executed notebook or script logs;
- compiled result report with explicit negative evidence.
