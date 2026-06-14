# Geometry-MMALS G1

**From audit-space projections to grounded functional geometry in continual learning.**

Geometry-MMALS G1 is a falsifiable research program for testing whether MMALS learns a meaningful internal geometry of sensory representations, inferred contexts, routes, host transformations, synthesized states, and continual-memory transport.

> **Current release:** v1.0.8, reviewer-loss-design revision `r2`.  
> **Scientific status:** C0 protocol implementation only. C1-C6 remain unqualified.

## Current scientific question

The executed v1.0.7 context-bottleneck study showed that inferred context can mediate competitive and causally specific routing when direct sensory access is blocked. It also showed that the prior route-geometry objective did not significantly organize context coordinates and could improve local source trajectories while weakening global centroid alignment.

v1.0.8 therefore asks:

> Can a scale-fixed, chord-compatible context objective produce local context order, prevent compressed trajectories, align source-specific fibers globally, and preserve functional usefulness?

## Revised v1.0.8 mathematical design

The context encoder produces a raw vector `context_raw`. The functional context is

```text
context = L2_normalize(context_raw)
```

The same normalized context is used by:

- the context-bottleneck router;
- context geometry losses;
- geometry metrics;
- held-out factor decoding;
- causal interventions.

For unit contexts, the observed half-chord distance is

```text
d_context = 0.5 * ||context_a - context_b||_2
```

and the factor target is

```text
target = sin((pi / 2) * clip(|angle_a-angle_b| / 120, 0, 1))
```

The total protocol separates:

- route geometry;
- local context geometry;
- far-pair separation;
- per-source path-spread anti-collapse;
- interval-wise cross-source fiber alignment;
- factor-centroid grounding;
- retention and host-function terms.

See the full equations in:

- `docs/reports/Geometry_MMALS_G1_v1_0_8_Direct_Context_Global_Alignment_Protocol_Report.pdf`
- `docs/reports/Geometry_MMALS_G1_v1_0_8_Direct_Context_Global_Alignment_Protocol_Report.tex`

## Primary notebook

```text
notebooks/Geometry_MMALS_G1_DirectContext_GlobalAlignment_v1_0_8.ipynb
```

The focused ablation family is:

1. context bottleneck, no geometry;
2. route geometry only;
3. context geometry plus path spread;
4. route plus context geometry;
5. full route/context/fiber/centroid alignment;
6. dimension-4 full alignment as a capacity probe.

Dimension 2 remains the primary geometric test. Dimension 4 is not interpreted as a parameter-matched causal contrast.

## Evidence outputs

The notebook exports:

- trained, interpolation, and extrapolation geometry separately;
- source-block Spearman correlation and normalized stress;
- factor-centroid geometry;
- fiber resultant length;
- held-out-source factor decoding;
- raw-context norm, path variance, effective rank, and near/far separation;
- paired treatment-control deltas for both correlation and stress;
- staged accuracy, NLL, forgetting, and compute audits;
- source-disjoint spherical causal probes.

## Preserved evidence and reviewer material

The repository includes:

- complete executed v1.0.7 seed-0 results under `results/v1_0_7/seed_0/`;
- the 22-page reviewer-oriented Status and Perspective report v1.1;
- its complete LaTeX source and figures;
- the v1.0.7 protocol report and migration history.

## Repository map

```text
notebooks/                  Colab protocols
src/geometry_mmalls/        PyTorch model, losses, metrics, memory stubs
configs/                    Frozen protocol configurations
docs/reports/               Archival PDFs, TeX and Markdown reports
docs/changes/               Version-to-version tracked changes
paper/                      G1 article and reviewer-status LaTeX sources
results/v1_0_7/seed_0/      Executed historical evidence
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

## Claim discipline

v1.0.8 does **not** claim:

- C1-C6 qualification;
- globally aligned context geometry;
- predictive advantage from geometry;
- causal qualification;
- reproducible host specialization;
- memory transport or backward transfer;
- domain-general geometry;
- quantum advantage.

The scientific progression remains:

```text
G1 grounded functional geometry
  -> G2 energy-guided manifold routing
  -> G3 phase-aware / quantum-inspired routing
```

Code is released under the MIT License. See `CITATION.cff` for citation metadata.
