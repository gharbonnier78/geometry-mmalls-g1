# Geometry-MMALS G1 v1.0.7 -> v1.0.8
## Revised direct-context loss design (`reviewer-loss-design-r2`)

## Scientific motivation

v1.0.7 established that forced context mediation is operationally viable and can produce a specific causal route response. It also showed that route regularization did not significantly improve context-space rank order and could strengthen local source trajectories while weakening global centroid alignment.

The first v1.0.8 draft therefore proposed direct context geometry and cross-source alignment. Reviewer feedback identified four additional requirements:

1. use the same scale-fixed context for routing and measurement;
2. make the factor target compatible with spherical chord distance;
3. separate local geometry, far separation and anti-collapse regularization;
4. align source fibers transition by transition and ground centroids separately.

## Tracked changes

### CHG-108-01 - Functional context normalization

The context encoder still emits `context_raw`, but the functional context is

```text
context = L2_normalize(context_raw)
```

This normalized context is passed to the context-bottleneck router.

### CHG-108-02 - Raw context retained for audit

`MMALSTrace` now retains both `context` and `context_raw`. Raw norm statistics are exported to detect hidden scale use.

### CHG-108-03 - Chord-compatible context distance

Direct context geometry uses normalized half-chord distance:

```text
0.5 * ||context_a - context_b||_2
```

### CHG-108-04 - Semicircle-compatible factor target

For a declared factor span of 120 degrees:

```text
target = sin((pi / 2) * clip(|angle_a-angle_b| / 120, 0, 1))
```

### CHG-108-05 - Explicit far-pair separation

Far factor pairs receive a separately logged minimum-distance margin.

### CHG-108-06 - Separate path-spread anti-collapse

Per-source normalized trajectory variance is required to exceed a declared floor. The term has its own weight and diagnostics.

### CHG-108-07 - Interval-wise fiber alignment

Adjacent context displacements are aligned only across matching factor intervals. Curved trajectories are not forced toward one global tangent.

### CHG-108-08 - Separate factor-centroid grounding

Factor centroids receive the same chord-compatible geometry objective as a distinct global-alignment term.

### CHG-108-09 - Focused ablation family

The primary dimension-2 methods are:

- no geometry;
- route geometry only;
- context geometry plus spread;
- route plus context geometry;
- full route/context/fiber/centroid alignment.

### CHG-108-10 - Dimension 4 as a capacity probe

Dimension 2 remains the primary minimal-context experiment. Dimension 4 is reported separately and is not treated as a parameter-matched treatment.

### CHG-108-11 - Collapse diagnostics

The notebook exports:

- mean and minimum path variance;
- effective rank;
- mean raw-context norm and dispersion;
- near and far half-chord distances;
- far-to-near separation ratio.

### CHG-108-12 - Paired correlation and stress deltas

Source-paired bootstrap tables now report treatment-control changes for both Spearman distance order and normalized stress.

### CHG-108-13 - Spherical causal interventions

Causal directions are projected into the local tangent plane of the unit sphere, applied, and renormalized. Fitting and evaluation source identities remain disjoint.

### CHG-108-14 - Historical evidence retained

The complete v1.0.7 seed-0 result bundle and reviewer report v1.1, including LaTeX source and figures, remain archived.

### CHG-108-15 - Strict claim boundary

v1.0.8 remains a C0 protocol release. No C1-C6 qualification, predictive advantage, global manifold, host specialization, memory transport, backward transfer or quantum advantage is claimed.

## Decision logic

A local context-geometry candidate requires:

- positive source-level context-rho delta with a positive bootstrap lower bound;
- negative context-stress delta.

A global alignment candidate additionally requires:

- improved factor-centroid order;
- improved fiber resultant length;
- improved held-out-source factor decoding;
- non-collapse diagnostics.

Geometry without predictive improvement remains a representational result only.
