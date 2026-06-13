# Geometry-MMALS G1 v1.0.2 Artifact Manifest

Numerical-stability patch generated after the first real Colab development run exposed a Fisher-Rao backward singularity.

## Scientific status

Accepted package claim: C0 pipeline validity only.

C1-C5 are specified as future experimental claims and require real per-seed runs, frozen gates, hardened baselines and claim manifests.

## Main artifacts

- `paper/Geometry_MMALS_G1_Article.pdf` - compiled specification article, v1.0.1, 31 pages (unchanged in this code-only patch).
- `paper/main.tex` - LaTeX source.
- `paper/references.bib` - bibliography.
- `notebooks/Geometry_MMALS_G1_Colab.ipynb` - Colab-ready v1.0.2 scaffold with stable route loss, finite guards and robust export discovery.
- `src/geometry_mmalls/` - executable scaffold.
- `docs/CLAIMS_AND_GATES.md` - numeric pilot gates and non-claims.
- `docs/NOTATION_BRIDGE.md` - MMALS-TPUT to Geometry-G1 notation bridge.
- `docs/STATUS.md` - current claim status.

## Validation performed

- `pytest -q`: 13 tests passed.
- `scripts/run_synthetic_smoke.py`: synthetic metric smoke completed.
- LaTeX compiled to PDF with bibliography using pdfTeX + BibTeX.
- PDF rendered to 31 PNG pages for visual inspection.

## Key patch items

- C0-only status clarified.
- Notebook leakage risk annotated: G1-A supervised/grounded variant.
- Fisher-Rao simplex utilities hardened near boundaries and at the identity-gradient singularity.
- Uniform-route backward regression test added.
- Colab finite guards and ridge-stabilized causal tangent probe added.
- Dual memory stubs added for reconstructive audit and synthetic functional memory.
- TPUT/G1 notation mismatch addressed.
- Numeric gates added for CSR, ablation locality, kNN preservation, stress and seed counts.
