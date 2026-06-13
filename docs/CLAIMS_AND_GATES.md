# Claims and Evidence Gates

This document prevents a visualization or a single favorable run from becoming a scientific claim.

## Pilot numeric gates v1.0.1

These are **pilot preregistration thresholds**, not final universal constants. They must be frozen before any qualification run and reported even if failed. A final paper may tighten them only before the final run, never after observing the qualification result.

| Gate | Pilot threshold | Notes |
|---|---:|---|
| C1 distance-order | Spearman rho CI lower > permutation-null 95th percentile and rho >= 0.25 | Report separately for context, route and synthesis; compare against frozen sensory z0. |
| C1 stress | normalized stress <= 0.70 or improves z0 by >= 10% | Stress alone cannot pass the gate. |
| C1 kNN | kNN preservation >= matched-dimensional random control + 0.10 | k fixed before run; default k=5. |
| C2 interpolation | beats nearest-context and unconstrained-router controls on held-out angles; trained-angle drop <= 2 percentage points | Report accuracy, NLL and calibration. |
| C3 specialization | at least two hosts with positive local contribution gain, ablation locality ratio >= 1.5, and cross-seed role CKA >= 0.50 after Hungarian matching | Hub-and-partner ecology is allowed; raw dominance is not enough. |
| C4 causality | CSR > 1.5 and bootstrap 95% CI lower > 1.0; class-identity log-prob drop <= 0.05 nats or <= 1 percentage point accuracy drop | Orthogonal controls must be matched norm. |
| C5 transport | old-region Procrustes/OT drift <= softmax baseline by 10% and forgetting not worse than baseline by > 0.5 percentage point | Must use matched compute and memory. |
| C6 robustness | pilot: >=5 seeds; final: >=10 seeds; no single seed may determine the conclusion | Report failed seeds. |

## C0 - Pipeline integrity

**Statement:** the experiment is reproducible and traces the intended internal objects.

Required evidence:

- deterministic seed manifest and environment record;
- dataset split hashes;
- train/validation/test separation audit;
- tensor-shape and normalization tests;
- successful synthetic smoke test;
- no oracle angle or task identifier in deployable inference.

## C1 - Grounded descriptive geometry

**Statement:** at least one MMALS internal layer preserves meaningful order or neighborhoods of the known context factor beyond chance.

Required evidence:

- positive distance-order correlation with confidence interval excluding the permutation null;
- normalized stress below the preregistered threshold;
- neighborhood preservation above a matched-dimensional random control;
- comparison with the frozen sensory representation.

A 2-D UMAP or PCA figure is illustration only.

## C2 - Predictive interpolation

**Statement:** the learned geometry predicts unseen intermediate contexts.

Required evidence:

- held-out-angle context and route interpolation error;
- better performance than nearest-trained-context and unconstrained-router controls;
- no unacceptable loss of class identity or calibration.

## C3 - Host functional specialization

**Statement:** hosts form reproducible, complementary functional regions.

Required evidence:

- non-trivial contribution gain;
- localized ablation impact;
- functional separation without forced arbitrary fragmentation;
- role stability through continual stages;
- role-level reproducibility after optimal cross-seed matching.

Route dominance alone fails this claim.

## C4 - Causal geometric direction

**Statement:** a measured latent direction corresponding to the context factor has a specific causal effect.

Required evidence:

- monotonic shift in inferred context or route under tangent intervention;
- effect larger than matched-norm orthogonal controls;
- class identity preserved within a declared margin;
- bootstrap lower confidence bound for the causal specificity ratio above the preregistered null.

## C5 - Continual geometric transport

**Statement:** old route-function structures are transported with controlled deformation rather than reconstructed accidentally after each stage.

Required evidence:

- neighborhood and functional alignment retained on old contexts;
- lower geometric drift than the no-transport ablation;
- lower forgetting or better recovery for equivalent compute/memory;
- stored reconstructive traces can reproduce the declared route-function path within tolerance.

## C6 - Operational utility

**Statement:** grounded geometry improves a concrete MMALS objective.

Required evidence:

- comparison with tuned and sanity-checked baselines;
- improvement on at least one preregistered objective;
- no violation of declared retention, cost, calibration or stability guardrails;
- reproducibility across seeds and at least one secondary dataset before generalization claims.

## Prohibited claims at G1

G1 does not establish:

- quantum computation or quantum advantage;
- physical superposition or entanglement inside a classical neural network;
- positive backward transfer unless measured and statistically supported;
- universal intelligence;
- consciousness;
- domain-general manifold discovery from a single synthetic benchmark.
