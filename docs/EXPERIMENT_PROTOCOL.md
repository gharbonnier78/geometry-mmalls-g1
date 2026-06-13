# Geometry-MMALS G1 Experimental Protocol

## 1. Research question

Can MMALS learn a grounded internal geometry in which context proximity, route transitions, host contributions and memory transport are coherent, predictive, causally testable and operationally useful?

## 2. Primary controlled factor

Use image rotation angle `u` as a known continuous factor. The evaluator retains the angle as ground truth, but the deployable model receives no task or angle identifier.

Recommended initial schedule:

- training contexts: `[-60, -30, 0, 30, 60]` degrees;
- held-out interpolation contexts: `[-45, -15, 15, 45]` degrees;
- optional extrapolation contexts: `[-75, 75]` degrees;
- continual stages: one declared sequence and its reversed control;
- seeds: at least five for qualification, three only for development smoke runs.

## 3. Model boundary

The primary experiment freezes a declared sensory encoder after a reference pretraining stage. This separates:

- geometry already present in the perceptual representation `z0`;
- geometry learned by MMALS in context, route, host and synthesis layers.

The frozen encoder is not automatically counted as an adaptive host. A later ablation may promote it to a host only if it participates in routing and exhibits contribution-defined specialization.

## 4. Compared systems

Minimum baselines:

1. frozen backbone plus linear classifier;
2. fine-tuning classifier;
3. EWC with validation-selected regularization;
4. replay with validation-selected memory size;
5. sparse mixture-of-experts with capacity/load sanity checks;
6. MMALS with the current softmax router;
7. MMALS with route-geometry regularization;
8. MMALS full G1 with route geometry, host-functional separation and transport;
9. oracle-angle diagnostic upper bound;
10. joint-training upper bound, clearly marked as non-continual.

Baseline hyperparameters must be selected using the same validation budget. Failed baselines are diagnostic until implementation and tuning checks pass.

## 5. Required traces

For each evaluation sample or declared aggregate, store:

- input identifier and continual stage;
- true class and known evaluation angle;
- `z0`, inferred context `c`, route `r`;
- every host output `g_h(z0)` or a reproducible summary;
- synthesized representation `z_mm`;
- prediction, loss and calibration quantities;
- active host count, latency proxy, FLOP proxy and memory access;
- model/config/data hashes and seed.

## 6. Geometry metrics

### Grounding

Compare pairwise factor distances `d_U(u_i,u_j)` with internal distances in:

- sensory space;
- inferred-context space;
- route simplex using Fisher-Rao distance;
- synthesized representation space;
- host function space.

Report Spearman distance correlation, normalized stress and neighborhood preservation. Report the sensory baseline alongside every downstream layer.

### Prediction

For held-out angles, report:

- context-coordinate error;
- route interpolation error against neighboring learned contexts;
- accuracy, NLL and calibration;
- error as a function of angular distance to the nearest trained context.

### Causal intervention

Estimate a tangent direction associated with increasing angle. Apply matched-norm interventions:

- along the estimated tangent;
- in random orthogonal directions;
- in class-sensitive nuisance directions when available;
- with a zero-intervention control.

Measure monotonic route/context movement, output identity preservation and a causal specificity ratio.

### Continual transport

At each learning stage, compare old-context geometries before and after training using:

- Procrustes-aligned drift;
- neighborhood retention;
- CKA or another representation-similarity metric;
- route drift on the simplex;
- optimal-transport alignment cost;
- change in contribution and ablation maps.

## 7. Host-specialization metrics

Host specialization requires a bundle:

- route entropy and dominance;
- contribution gain relative to removal or replacement;
- context-localized ablation impact;
- functional distance/CKA between hosts;
- route-function stability across time;
- Hungarian-matched role reproducibility across seeds.

A high route frequency without localized contribution is dominance, not specialization.

## 8. Operational outcomes

Report accuracy and forgetting together with:

- active computation and memory access;
- stability under controlled drift;
- calibration and out-of-support detection;
- host specialization bundle;
- reconstructive memory fidelity;
- compiled-memory cost reduction.

No single scalar should hide a failed safety or retention gate.

## 9. Statistical policy

- publish per-seed values and mean with confidence interval;
- bootstrap pairwise and intervention metrics by example or context block;
- correct or clearly group multiple primary comparisons;
- distinguish exploratory metrics from preregistered gates;
- never select a seed or checkpoint using the final test set.

## 10. Falsification outcomes

G1 is considered unsupported if one or more core findings persist after correction and replication:

- geometry exists only in the frozen backbone;
- route smoothness collapses hosts or erases useful boundaries;
- held-out interpolation is no better than nearest-context routing;
- tangent interventions are no more specific than controls;
- apparent host roles permute or disappear across seeds without role-level matching;
- operational gains vanish against tuned baselines;
- geometry improves plots but worsens retention, cost or calibration.
