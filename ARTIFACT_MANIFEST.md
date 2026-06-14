# Artifact Manifest - Geometry-MMALS G1 v1.0.7

## Primary protocol artifacts

- `notebooks/Geometry_MMALS_G1_ContextBottleneck_v1_0_7.ipynb` - Colab-ready context-bottleneck experiment with complete research history and CHG-107 tracking.
- `configs/rotated_mnist_g1_v107.yaml` - hypothesis, falsification condition, controls and non-claims.
- `src/geometry_mmalls/model.py` - canonical context- and sensory-bottleneck router implementations.
- `docs/reports/Geometry_MMALS_G1_v1_0_7_Context_Bottleneck_Protocol_Report.pdf` - archival protocol report.
- `docs/reports/Geometry_MMALS_G1_v1_0_7_Context_Bottleneck_Protocol_Report.md` - editable report source.
- `docs/reports/Geometry_MMALS_G1_v1_0_7_Context_Bottleneck_Protocol_Report.tex` - LaTeX report source.
- `docs/changes/Geometry_MMALS_G1_v1_0_6_to_v1_0_7.md` - tracked protocol delta.
- `docs/changes/MIGRATION_v1_0_6_to_v1_0_7.md` - supplied migration proposal archived verbatim.
- `docs/RELEASE_CHECKLIST_v1_0_7.md` - release and claim-discipline checklist.
- `docs/V1_0_7_BUILD_VALIDATION.json` - machine-readable build validation.

## Reviewer synthesis archived in the repository

- `docs/reports/Geometry_MMALS_G1_Status_and_Perspective_Reviewer_Report_v1_0.pdf` - previously generated 18-page reviewer status report covering evidence through v1.0.6.
- `paper/reviewer_status_v1_0/` - complete LaTeX source tree, bibliography, figures and report manifest.
- `releases/Geometry_MMALS_G1_Status_and_Perspective_LaTeX_v1_0.zip` - original complete LaTeX source package.

## Core v1.0.7 controls

- standard route with retention anchor;
- uniform static route;
- context bottleneck with and without geometry;
- capacity-matched sensory bottleneck with and without geometry;
- equal initialization, data order, image forwards, optimizer steps and anchor weight;
- trained/interpolation/extrapolation evidence partitions;
- context and z0 intervention diagnostics;
- optional same-final-task curricula for the primary treatment only.

## Validation

- notebook JSON and Python syntax: PASS;
- package tests: 19 passed;
- protocol PDF: 3 pages, openable, unencrypted and visually inspected;
- reviewer PDF: included from the verified 18-page report package;
- package version: 1.0.7;
- clean archive hygiene: `.git`, datasets, runtime results, caches, bytecode, egg-info and local environments excluded.

## Scientific status

C0 protocol implementation only. The full v1.0.7 experiment was not executed during package generation. No C1-C6, context-mediation, adaptive-route, backward-transfer or quantum claim is included.
