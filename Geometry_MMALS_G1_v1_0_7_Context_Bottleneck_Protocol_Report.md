# Geometry-MMALS G1 v1.0.3
## Cross-Angle Paired Geometry Protocol Correction Report

**Date:** 2026-06-13  
**Status:** protocol release; C0 only; C1-C6 remain unqualified.

### Executive conclusion

v1.0.2 repaired the Fisher-Rao numerical singularity and produced finite traces,
but its geometry loss was applied inside fixed-angle batches. Every factor value
inside a batch was identical, so the loss could not learn or test an ordered
cross-angle geometry. v1.0.3 changes the optimization and measurement unit to
the same source image observed at several angles.

### Version history

- v1.0.0: functional geometry specification and falsification ladder.
- v1.0.1: claim gates, audit patch, notation bridge and memory stubs.
- v1.0.2: numerical stability, finite guards and Colab execution.
- v1.0.3: cross-angle paired protocol and source-block measurement.

### v1.0.2 development evidence

The finite development run reported distance-order correlations close to zero:
sensory -0.0334, context -0.0383, route 0.0272 and synthesis 0.0118. These values
do not support C1. They are not considered a decisive falsification because the
training loss never compared different angles.

Host ablations suggested two useful general hosts and two nearly inactive hosts,
not yet localized, reproducible host specialization.

The tangent probe showed symmetric route sensitivity in absolute norm, but it
did not establish a signed angle-specific causal effect.

### v1.0.3 scientific corrections

1. Same-source cross-angle batches.
2. Geometry anchors restricted to angles already seen in the continual sequence.
3. Classification applied to the current angle by default.
4. Stable square-root-simplex chordal loss for optimization.
5. Fisher-Rao retained for evaluation.
6. Source indices retained in traces.
7. Source-block bootstrap instead of all-pairs p-values.
8. Factor-centroid geometry instead of tie-fragile sample kNN.
9. Held-out context and route interpolation controls.
10. Staged accuracy and forgetting.
11. Signed causal route projection with orthogonal controls.
12. Package version and git SHA in every run manifest.

### Mathematical protocol

For source image x_i and seen angles u_1,...,u_A, the model produces routes
r_i,a. The loss is:

L_pair = L_local + lambda_far L_far + lambda_match L_match.

Distances are optimized in square-root simplex coordinates. This distance is
monotonic with the Fisher-Rao route distance but avoids arccos instability.

### Claim discipline

The new notebook makes C1-C4 measurable. It does not make them true. C5 still
requires explicit memory transport and dual-memory experiments. C6 requires
tuned baselines and secondary-dataset replication.

### GitHub placement

- notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb
- docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.pdf
- docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.md
- configs/rotated_mnist_g1.yaml
- src/geometry_mmalls/data.py
- src/geometry_mmalls/geometry.py
- src/geometry_mmalls/metrics.py
- tests/test_geometry.py
- tests/test_metrics.py
