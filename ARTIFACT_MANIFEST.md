# Geometry-MMALS G1 v1.0.3 Artifact Manifest

## Scientific status

Accepted claim: C0 implementation and protocol correction only.

C1-C6 remain unqualified until frozen-gate, multi-seed, controlled runs are
archived.

## Main artifacts

- `notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb`
- `docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.pdf`
- `docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.md`
- `src/geometry_mmalls/data.py` with `MultiAngleMNIST`
- `src/geometry_mmalls/geometry.py` with `paired_route_geometry_loss`
- `src/geometry_mmalls/metrics.py` with source-block and centroid metrics
- `configs/rotated_mnist_g1.yaml` with paired-protocol settings
- `docs/changes/Geometry_MMALS_G1_v1_0_2_to_v1_0_3.patch`

## Core correction

v1.0.2 used a single factor value inside each geometry batch. v1.0.3 uses
same-source cross-angle views and evaluates geometry inside source blocks.

## Validation performed during package generation

- Notebook JSON and Python syntax validation.
- Unit test suite: 16 tests passed.
- Same-source multi-angle dataset smoke using locally available MNIST data.
- Paired route-loss forward/backward smoke.
- PDF render verification.
