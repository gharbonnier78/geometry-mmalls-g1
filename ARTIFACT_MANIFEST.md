# Artifact Manifest - Geometry-MMALS G1 v1.0.6

## Primary artifacts

- `notebooks/Geometry_MMALS_G1_StaticRoutes_CounterbalancedCurriculum_v1_0_6.ipynb` - Colab protocol with research history and CHG-106 tracking.
- `docs/reports/Geometry_MMALS_G1_v1_0_6_Static_Routes_Counterbalanced_Curriculum_Report.pdf` - archival protocol report.
- `docs/reports/Geometry_MMALS_G1_v1_0_6_Static_Routes_Counterbalanced_Curriculum_Report.md` - editable report source.
- `docs/changes/Geometry_MMALS_G1_v1_0_5_to_v1_0_6.md` - v1.0.5 to v1.0.6 tracked changes.
- `configs/rotated_mnist_g1_v106.yaml` - static-route and counterbalanced-curriculum declaration.
- `docs/V1_0_6_VALIDATION.json` - build and preflight status.

## Key controls

- adaptive standard route;
- context-only and direct-z0 adaptive routes;
- uniform static route;
- learned global static route;
- four cyclic curricula ending at 30 degrees;
- source-paired router intervention confidence intervals.

## Validation

- notebook JSON and Python syntax: PASS;
- package tests: 16 passed;
- PDF: 5 pages, openable, unencrypted, visually rendered;
- clean archive hygiene: `.git`, datasets, runtime results, caches, bytecode, egg-info, and local environments excluded.

## Scientific status

C0 protocol implementation only. The full v1.0.6 experiment was not executed during artifact generation. No C1-C6 or adaptive-route claim is included.
