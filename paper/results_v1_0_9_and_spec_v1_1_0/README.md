# Geometry-MMALS G1 — v1.0.9 Results and v1.1.0 Functional Routing Specification

This source package contains the English technical article, the exact v1.0.9 aggregate evidence used in the article, all included figures, and the complete v1.1.0 functional-routing specification in Markdown and YAML.

## Build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The document uses `biblatex` with `biber`; `latexmk` handles the complete build.

## Scientific status

- v1.0.9: executed five-seed matched-compute pilot.
- Replicated candidate result: context geometry and held-out-source factor decoding.
- Not replicated: route geometry, synthesis geometry, causal specificity, predictive advantage, forgetting improvement.
- v1.1.0: specification only; not yet executed.

## Main v1.1.0 question

Can a geometry-mediated router convert the learned context geometry into ordered, causally specific, and functionally meaningful host allocation?

The primary comparison is an MLP router, a linear router, and a prototype-energy router. The package also defines a functional optimal-transport metric over routes using measured host-function costs.
