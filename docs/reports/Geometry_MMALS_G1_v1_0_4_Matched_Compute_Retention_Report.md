# Geometry-MMALS G1 v1.0.4
## Matched Initialization, Matched Compute, and Retention Anchors

**Archive status:** protocol correction report and executable development design.

**Accepted claim:** C0 pipeline/protocol integrity only.

**Not claimed:** C1-C6 qualification, quantum advantage, backward transfer, replay-free continual learning, or domain-general geometry.

## Executive decision

The v1.0.3 cross-angle paired experiment was the first informative Geometry-MMALS G1 run. It showed stronger local route/context ordering and improved average interpolation, but three attribution problems remained: paired and unpaired methods did not start from the same MMALS parameters, paired training used more image-forward compute than the current-only control, and the geometry condition increased forgetting on earlier angles.

v1.0.4 is designed to isolate these effects before any additional qualification run. The primary scientific comparison is now `paired_geometry` versus `paired_compute_matched_no_geometry`. These methods receive identical multi-angle tensors, share one immutable initial state, use the same source order, and execute the same number of image forwards and optimizer steps. A separate `paired_geometry_anchor_010` variant tests whether a small old-angle classification anchor can reduce forgetting without extra forward passes.

## Research history

| Version | Main question | Outcome |
|---|---|---|
| v1.0.0 | Can functional MMALS geometry be specified and falsified? | Article, evidence ladder, and C0 scaffold. |
| v1.0.1 | Can claims, gates, notation, and memory contracts be audited? | C0-only status and pilot gates formalized. |
| v1.0.2 | Can the route loss and Colab pipeline run without NaNs? | Numerical stability passed. |
| v1.0.3 | Does the optimization unit contain real cross-angle evidence? | Same-source paired protocol; first informative development result. |
| v1.0.4 | Does geometry add value at matched initialization/compute, and can an anchor reduce forgetting? | Implemented in the new notebook; no qualification claim yet. |

## v1.0.3 development evidence carried forward

The seed-0 development run reported:

- route source-level order: 0.378 without geometry versus 0.492 with paired geometry;
- context source-level order: 0.289 versus 0.497;
- mean held-out interpolation accuracy: 0.278 versus 0.346;
- mean trained-angle forgetting: 0.059 versus 0.105;
- causal specificity ratio: approximately 0.17 versus 0.66-0.74, still below one.

The result was promising but non-qualifying. The synthesis geometry did not improve, interpolation gains were asymmetric, and causal specificity remained weaker than matched orthogonal directions.

## Why v1.0.4 is necessary

### Initialization confound

In v1.0.3 each method instantiated a new context network, router, host bank, and classifier. Even with the same sensory encoder, the methods began from different MMALS parameters. v1.0.4 creates one base state, hashes it, and reloads it for every method.

### Compute confound

The v1.0.3 current-only control processed one view per source while paired geometry processed all angles seen so far. v1.0.4 keeps the current-only method as a cost reference but adds a paired compute-matched control using identical multi-angle batches with geometry weight zero.

### Stability-plasticity trade-off

Paired geometry improved final/interpolation accuracy while increasing forgetting. v1.0.4 adds an old-angle classification anchor computed from views already present in the paired batch, so it adds no image-forward compute.

## Method matrix

| Method | Inputs at stage t | Geometry loss | Old-angle CE anchor | Role |
|---|---|---:|---:|---|
| current_only_no_geometry | current angle only | 0 | 0 | cheaper external reference |
| paired_compute_matched_no_geometry | all seen angles | 0 | 0 | primary compute-matched control |
| paired_geometry | all seen angles | enabled | 0 | geometry treatment |
| paired_geometry_anchor_010 | all seen angles | enabled | 0.10 | retention treatment |

The primary geometry attribution is the difference between the second and third rows. The primary retention contrast is the difference between the third and fourth rows.

## Experimental invariants

1. One deterministic train/test source split is shared by all methods.
2. One immutable MMALS initialization is shared by all methods and recorded by SHA-256.
3. Paired variants share method-independent DataLoader seeds for each stage and epoch.
4. Paired variants must match exactly on image forwards, source examples, and optimizer steps.
5. Interpolation and extrapolation angles never enter training or checkpoint selection.
6. The true angle is available only to the declared controlled geometry loss and evaluator, never to the deployable router.
7. The sensory encoder is frozen before MMALS training.
8. Qualification mode is blocked when the sensory acceptance gate fails.

## Measurements and exported evidence

The notebook exports:

- staged losses and compute accounting;
- staged accuracy and trained-angle forgetting;
- source-block and factor-centroid geometry for sensory, context, route, and synthesis spaces;
- held-out interpolation accuracy, NLL, route interpolation error, and nearest-route control;
- route mass and host ablation mean, median, and positive fraction;
- signed causal route effects, matched orthogonal effects, causal specificity ratio, and class-evidence change;
- method-level summaries and explicit geometry/retention contrasts;
- an immutable run manifest with package version, git SHA, split hashes, initial-state hash, method specifications, and non-claims.

## Gate interpretation

The notebook does not auto-promote a development run. Candidate evidence must be interpreted through two contrasts:

**Geometry effect at matched compute**

- positive route/context order delta;
- no unacceptable synthesis degradation;
- improved held-out interpolation relative to the paired control;
- compute audit passed;
- no hidden difference in initialization or source order.

**Retention anchor effect**

- reduced forgetting relative to paired geometry;
- retained or improved final/interpolation accuracy;
- limited degradation of route/context geometry;
- no additional image-forward compute.

C3 still requires cross-seed host-role matching. C4 still requires bootstrap confidence intervals and a causal specificity ratio above the frozen threshold. C5 requires explicit memory-transport and dual-memory experiments.

## Sensory acceptance boundary

The development notebook uses a larger sensory pretraining subset than v1.0.3 and measures held-out 0-degree accuracy before MMALS training. Development mode records a warning below 0.85; qualification mode stops below 0.95. This prevents claims about MMALS geometry from being built on an immature identity representation.

## Archive layout

Recommended GitHub paths:

- `notebooks/Geometry_MMALS_G1_MatchedCompute_Retention_v1_0_4.ipynb`
- `docs/reports/Geometry_MMALS_G1_v1_0_4_Matched_Compute_Retention_Report.pdf`
- `docs/reports/Geometry_MMALS_G1_v1_0_4_Matched_Compute_Retention_Report.md`
- `docs/changes/Geometry_MMALS_G1_v1_0_3_to_v1_0_4.md`

A completed run should additionally archive `results/v1_0_4/seed_<n>/` with all CSVs and `run_manifest.json`.

## Qualification path after v1.0.4 development

1. Run the development mode and inspect budget assertions.
2. Reject the run if the sensory gate or finite-value guards fail.
3. Confirm that all paired variants have exactly matched forwards and steps.
4. Examine the two explicit contrasts before looking at broader baselines.
5. Freeze thresholds and anchor weight before multi-seed qualification.
6. Run at least five pilot seeds, then ten final seeds.
7. Add tuned EWC, replay, sparse-MoE, oracle-angle, and joint upper-bound controls for broader continual-learning claims.
8. Add cross-seed host-role matching, memory transport, dual-memory qualification, and a second controlled factor before C3-C5.

## Epistemic conclusion

v1.0.4 does not assert that Geometry-MMALS works. It repairs the attribution design needed to decide whether the cross-angle result observed in v1.0.3 was caused by the geometry objective itself, by extra compute, by initialization, or by a stability-plasticity trade-off. The next acceptable scientific statement must be based on the matched paired contrast, not on the cheaper current-only baseline alone.
