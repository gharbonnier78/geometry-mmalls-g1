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


## v1.0.3 measurement policy amendment

For RotatedMNIST G1 qualification:

- distance-order and stress statistics must be computed inside same-source
  cross-angle blocks and summarized across source images;
- factor-centroid geometry must be reported as a complementary tie-free view;
- uncertainty must use source-block bootstrap or permutation;
- ordinary pairwise p-values over all sample pairs are descriptive only;
- ordinary sample-level kNN is not a primary gate when the reference factor has
  large tied neighborhoods;
- a geometry-trained model must be compared with the same architecture without
  paired geometry regularization.

## v1.0.8 direct-context geometry amendment

For the revised direct-context protocol:

- the functional context used by the context-bottleneck router, losses, metrics and causal interventions must be the same L2-normalized vector;
- raw context may be logged only for audit and scale diagnostics;
- local context geometry must report both source-level distance-order correlation and normalized stress;
- a local candidate requires a positive paired-bootstrap rho delta and a negative stress delta;
- anti-collapse evidence must include per-source path variance, effective rank, raw norm statistics and near/far half-chord separation;
- global alignment requires factor-centroid order, interval-wise fiber resultant length and held-out-source factor decoding to improve together;
- dimension 4 is a capacity probe and must not be interpreted as a parameter-matched treatment against dimension 2;
- source-disjoint causal interventions must remain on the normalized context sphere;
- geometry without predictive or retention benefit remains C1 representational evidence only and cannot promote C6.

## v1.0.9 stationary-geometry pilot amendment

For the v1.0.9 pilot:

- route-factor targets must be independent of current continual-stage span;
- the primary comparison is `d4_full_stationary_route` versus `d4_no_geo`;
- `d4_full_legacy_route` is retained only to diagnose the effect of the target correction;
- the source split and sensory boundary are fixed across model seeds to isolate MMALS initialization and training-order variability;
- within-seed uncertainty uses source bootstrap; across-pilot replication uses model seed as the statistical unit;
- candidate C1 promotion requires a positive model-seed confidence interval and at least 80% positive seeds for the primary effect;
- dense held-out angles must remain absent from training and checkpoint selection;
- causal evidence must include source-bootstrap CSR intervals and prediction-identity preservation;
- passing the pilot does not establish final C1 qualification or C2-C6 claims.

## v1.0.9 replicated candidate evidence

- Candidate pass: context geometry across five seeds.
- Candidate pass: held-out-source context factor decoding.
- Fail/inconclusive: route geometry.
- Fail/inconclusive: synthesis geometry.
- Fail: predictive superiority and forgetting improvement.
- Fail: causal specificity threshold.
- Diagnostic negative: stationary route target does not beat legacy target.

## v1.1.0 implementation gates

The v1.1.0 gates are defined in:

- `docs/specs/Geometry_MMALS_G1_v1_1_0_Functional_Routing_Specification.md`
- `configs/rotated_mnist_g1_v110_spec.yaml`

The protocol is fully implemented in `notebooks/Geometry_MMALS_G1_FunctionalRouting_v1_1_0.ipynb`, but no v1.1.0 empirical gate has been executed or passed.


## v1.1.0 executed evidence amendment

- Protocol integrity: PASS.
- Prototype nominal route mediation: candidate pass on trained and held-out factors.
- Prototype functional route mediation: candidate pass on trained factors only.
- Held-out functional mediation: not established.
- Low-capacity linear routing: equally competitive; strongest exploratory causal and ablation signals.
- Prototype causal specificity and identity preservation: fail.
- Host ecology: route territories observed, functional specialization not qualified.
- Operational non-degradation: pass as equivalence, not superiority.
- Memory transport: not implemented.

No final geometry claim may rely on PCA/UMAP alone, and no Riemannian-manifold claim is allowed without explicit structural tests and metric comparisons.

## v1.1.1 final gate record

The completed pilot qualifies protocol integrity, route-swap ordering, and
prediction-identity preservation. It does not qualify R3 held-out mediation,
local continuity, functional causal specificity, or operational non-degradation.

## v1.1.2 candidate gates

The primary R5 treatment must pass held-out common-cost functional stress,
functional order, q95 continuity non-degradation, route-swap ordering, causal
specificity, identity preservation, and operational equivalence. The SPD axis is
a separate diagnostic candidate and cannot promote a router claim by itself.
