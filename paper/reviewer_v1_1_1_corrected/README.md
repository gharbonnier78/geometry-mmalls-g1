# Geometry-MMALS G1 v1.1.1 Reviewer Article

This package contains the reviewer-facing arXiv-style results manuscript for the five-seed Geometry-MMALS G1 v1.1.1 bridge-isolation pilot.

## Contents

- `main.tex`: complete LaTeX manuscript
- `main.pdf`: compiled 17-page manuscript
- `figures/`: vector PDF and PNG figures generated from the archived CSV evidence
- `data/`: aggregate and audit files copied from the `v1_1_1` result bundle

## Scientific status

The protocol-integrity gates passed. The hybrid directional-prototype router did not qualify on held-out mediation, local continuity, causal specificity, or operational non-degradation. Route-swap ordering and prediction-identity preservation passed.

## Build

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
