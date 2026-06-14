# Geometry-MMALS G1

**From audit-space projections to grounded functional geometry in continual learning.**

Geometry-MMALS G1 is a falsifiable research program for testing whether MMALS learns a meaningful internal geometry of inferred contexts, routes, host transformations, synthesized states, and continual-memory transport.

> **Current release:** v1.0.9, build `stationary-route-qualification-pilot-r1`.  
> **Scientific status:** v1.0.8 seed-0 development evidence is archived; v1.0.9 is an unexecuted five-seed pilot protocol. Final C1-C6 qualification is not claimed.

## Current scientific question

The executed v1.0.8 study found that local context geometry alone was insufficient. Full alignment in context dimension 4 substantially improved source-level context order, route order, fiber consistency, effective rank, held-out factor decoding, and source-disjoint causal specificity. These improvements remained weakly coupled to prediction and forgetting.

A post-run audit identified a route-loss defect: the same angle gap received different targets as the visible curriculum span grew. v1.0.9 asks:

> Does the d4 full-alignment result replicate across five model seeds after replacing the curriculum-dependent route target with a fixed chord-compatible topology?

## Stationary route geometry

For route probabilities `r`, use square-root simplex coordinates `q = sqrt(r)` and normalized chord distance:

```text
d_route = sqrt(1 - <q_a, q_b>)
```

The fixed target is:

```text
target = sin((pi / 2) * clip(|angle_a-angle_b| / 120, 0, 1))
```

The target is independent of continual stage, curriculum order, and the number of visible angles.

## Primary v1.0.9 notebook

```text
notebooks/Geometry_MMALS_G1_StationaryGeometry_Pilot_v1_0_9.ipynb
```

The pilot compares:

1. `d4_no_geo`;
2. `d4_full_legacy_route`;
3. `d4_full_stationary_route`.

The pilot profile uses model seeds `[0,1,2,3,4]` with a fixed source split and a common frozen sensory grove. It adds:

- a dense 15-degree evaluation grid;
- paired source-bootstrap prediction intervals;
- source-bootstrap causal CSR intervals;
- class-log-probability and prediction-identity preservation;
- model-seed confidence intervals and positive-seed fractions.

## v1.0.8 archived result

The repository now includes the complete executed v1.0.8 seed-0 evidence under:

```text
results/v1_0_8/seed_0/
```

The archival interpretation is available as:

```text
docs/reports/Geometry_MMALS_G1_v1_0_8_Results_and_Interpretation_Report.pdf
paper/results_v1_0_8/
releases/Geometry_MMALS_G1_v1_0_8_Results_Report_LaTeX.zip
```

The defensible v1.0.8 conclusion is that full alignment with context dimension 4 produced strong single-seed candidate geometry, but direct context geometry alone failed and operational benefit remained small.

## Reviewer material retained

- `docs/reports/Geometry_MMALS_G1_Status_and_Perspective_Reviewer_Report_v1_1.pdf`
- `paper/reviewer_status_v1_1/`
- `releases/Geometry_MMALS_G1_Status_and_Perspective_LaTeX_v1_1.zip`

The reviewer report predates the v1.0.8 execution and is retained as a historical status document.

## Repository map

```text
notebooks/                  Colab protocols
src/geometry_mmalls/        PyTorch model, losses, metrics, memory stubs
configs/                    Frozen protocol configurations
docs/reports/               Archival PDFs, TeX and Markdown reports
docs/changes/               Version-to-version tracked changes
paper/                      G1 article and report LaTeX sources
results/v1_0_8/seed_0/      Executed v1.0.8 evidence
releases/                   Archived LaTeX source bundles
tests/                      Numerical and structural regression tests
```

## Quick validation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```

Expected package validation for v1.0.9:

```text
31 passed
```

## Claim discipline

v1.0.9 does **not** claim:

- final C1-C6 qualification;
- predictive advantage from geometry;
- reproducible host specialization;
- memory transport or backward transfer;
- operational utility;
- domain-general geometry;
- replay-free continual learning;
- quantum advantage.

The scientific progression remains:

```text
G1 grounded functional geometry
  -> G2 energy-guided manifold routing
  -> G3 phase-aware / quantum-inspired routing
```

Code is released under the MIT License. See `CITATION.cff` for citation metadata.

## v1.0.9 canonical stable build

The current canonical notebook and Python functions include both execution
corrections directly:

- non-negative uint32 RNG seed normalization for dense negative angles;
- root-space stationary route distance with finite gradients for coincident
  and near-coincident routes.

Build revision: `stationary-route-qualification-pilot-r3`. No runtime monkey-patch is required.
