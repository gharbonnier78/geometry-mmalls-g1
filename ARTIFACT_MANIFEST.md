# Geometry-MMALS G1 v1.0.9 Artifact Manifest

## Build revision

`stationary-route-qualification-pilot-r1`

## Primary v1.0.9 protocol

- `notebooks/Geometry_MMALS_G1_StationaryGeometry_Pilot_v1_0_9.ipynb`
- `configs/rotated_mnist_g1_v109.yaml`
- `docs/reports/Geometry_MMALS_G1_v1_0_9_Stationary_Geometry_Pilot_Protocol_Report.pdf`
- `docs/reports/Geometry_MMALS_G1_v1_0_9_Stationary_Geometry_Pilot_Protocol_Report.tex`
- `docs/reports/Geometry_MMALS_G1_v1_0_9_Stationary_Geometry_Pilot_Protocol_Report.md`
- `docs/changes/Geometry_MMALS_G1_v1_0_8_to_v1_0_9.md`

## Stationary mathematical implementation

- `src/geometry_mmalls/geometry.py`
  - `paired_route_geometry_loss_stationary`;
  - fixed 120-degree chord-compatible route target;
  - stable square-root-simplex optimization.
- `tests/test_stationary_route_geometry.py`
  - finite backward;
  - collapsed-route penalty;
  - permutation equivariance;
  - curriculum-span stationarity check.

## Archived v1.0.8 executed evidence

- `results/v1_0_8/seed_0/`
- `notebooks/Geometry_MMALS_G1_DirectContext_GlobalAlignment_v1_0_8_REVISED_PATCHED.ipynb`
- `docs/changes/Geometry_MMALS_G1_v1_0_8_synthesis_column_patch.md`

## v1.0.8 Results and Interpretation report

- `docs/reports/Geometry_MMALS_G1_v1_0_8_Results_and_Interpretation_Report.pdf`
- `docs/reports/Geometry_MMALS_G1_v1_0_8_Results_and_Interpretation_Report.tex`
- `paper/results_v1_0_8/`
- `releases/Geometry_MMALS_G1_v1_0_8_Results_Report_LaTeX.zip`

## Reviewer package retained

- `docs/reports/Geometry_MMALS_G1_Status_and_Perspective_Reviewer_Report_v1_1.pdf`
- `paper/reviewer_status_v1_1/`
- `releases/Geometry_MMALS_G1_Status_and_Perspective_LaTeX_v1_1.zip`

## Build validation

- package version: `1.0.9`;
- notebook Python syntax: pass;
- package tests: 31 passed;
- v1.0.8 results report: 6 pages, openable, rendered and inspected;
- v1.0.9 protocol report: 3 pages, openable, rendered and inspected.

## Status

The v1.0.8 seed-0 result is archived as development evidence. The v1.0.9 five-seed pilot has not been executed in this package. Final C1-C6 qualification remains unclaimed.
