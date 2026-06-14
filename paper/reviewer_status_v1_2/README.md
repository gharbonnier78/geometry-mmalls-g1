# Geometry-MMALS G1 - Reviewer Status and Perspective v1.2

This package contains the reviewer-oriented arXiv-style status report updated through the completed Geometry-MMALS G1 v1.0.9 five-seed pilot.

## Scientific status

The strongest supported statement is a replicated candidate C1 context-geometry result. Across five matched-compute model seeds, four-dimensional full alignment improves trained-angle context distance-order correlation and held-out-source factor decoding. Route geometry, synthesis geometry, predictive accuracy, forgetting, and causal specificity remain unqualified.

The stationary route target is curriculum independent and numerically stable, but it does not outperform the legacy route target in this pilot.

## Contents

- `source/main.tex` - report source
- `source/references.bib` - bibliography
- `figures/` - vector and raster figures
- `data/` - selected immutable v1.0.9 CSV evidence and run manifest
- `rendered/` - internal visual-QA pages
- `REPORT_MANIFEST.json` - artifact identity and validation

## Build

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

The report is a status and perspective synthesis, not a completed C1-C6 qualification paper.
