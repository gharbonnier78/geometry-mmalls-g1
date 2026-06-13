# Geometry-MMALS G1

<p align="center">
  <a href="./paper/paper/Geometry_MMALS_G1_Article_v1_0_1.pdf">
    <img src="https://img.shields.io/badge/Open-Article-0B5FFF?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Open PDF">
  </a>
</p>

**From audit-space projections to grounded functional geometry in continual learning.**

Geometry-MMALS G1 is a research specification and implementation scaffold for testing whether MMALS learns a meaningful internal geometry of representations, inferred contexts, routes, host transformations, synthesis states, and memory transport.

> **Status:** research protocol and executable scaffold, patched as v1.0.1 after release audit. The repository currently supports a **C0 pipeline-validity claim only**. It does **not** claim that the proposed G1 experiments have succeeded. Included smoke outputs are synthetic and validate only the software and metric flow. C2+ claims require real runs, fixed numeric gates, seed reports, and hardened baselines.

## Why this repository exists

Earlier MMALS work organized audit and control variables in a geometric decision space. That is useful for governance, but it is not evidence that the learning system itself has discovered a functional geometry. G1 separates these two layers:

- **External audit/control geometry:** observable traces, costs, objectives, stability and policy indicators.
- **Internal functional geometry:** sensory representations, inferred contexts, route distributions, host functions, synthesized representations and their evolution through continual learning.

A G1 claim is admissible only if the geometry passes four levels of evidence:

1. **Descriptive:** known context order and neighborhoods are preserved.
2. **Predictive:** unseen intermediate contexts can be interpolated.
3. **Causal:** controlled latent interventions produce specific functional changes.
4. **Operational:** geometry improves accuracy, retention, cost, drift stability or host specialization against hardened baselines.

## Primary experiment

The first protocol uses continuous **RotatedMNIST** because the angle is an observable ground-truth factor. A frozen sensory encoder isolates geometry already present in perception. MMALS then learns:

- an inferred context coordinate;
- a route trajectory on the probability simplex;
- host-specific transformation fields;
- a synthesized functional representation;
- a transport map between continual-learning stages;
- reconstructive audit memory and synthetic/compiled functional memory.

The scientific progression is intentionally ordered:

```text
G1 grounded functional geometry
  -> G2 energy-guided manifold routing
  -> G3 phase-aware / quantum-inspired routing
```

No quantum-computing or quantum-advantage claim is made here.

## Repository map

```text
paper/                      LaTeX article, references, figures and compiled PDF
src/geometry_mmalls/        PyTorch model and geometry/metric utilities
notebooks/                  Colab-ready experimental scaffold
configs/                    Declared experiment configurations
docs/                       Protocol, gates, reproducibility and French summary
results/templates/          Empty result schemas for real experiments
results/smoke/              Synthetic smoke outputs only
scripts/                    Figure, smoke and paper-build scripts
tests/                      Unit tests for geometric primitives
```


## Release-audit patch v1.0.1

This patch addresses the main methodological risks identified during package review:

- the notebook labels the angle-supervised route geometry loss as the **G1-A supervised/grounded variant**;
- Fisher-Rao utilities explicitly clip and normalize probability vectors near simplex boundaries;
- numeric pilot gates are stated in `docs/CLAIMS_AND_GATES.md`;
- TPUT-to-G1 notation is bridged in `docs/NOTATION_BRIDGE.md`;
- reconstructive audit memory and synthetic functional memory have minimal executable stubs;
- core smoke tests cover model traces, metrics, memory stubs and package imports.

## Quick start

### Synthetic smoke test

This test does not train MMALS. It creates a known angular route trajectory and verifies that the metric pipeline detects order, interpolation and drift.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python scripts/run_synthetic_smoke.py --config configs/rotated_mnist_g1.yaml
pytest -q
```

For local inspection without installation, `pytest` also works from the repository root because `pyproject.toml` declares `src` as a pytest pythonpath.

### Build the paper

A TeX distribution with `latexmk` and BibTeX is required.

```bash
make paper
```

The compiled article is available directly at:

- `paper/Geometry_MMALS_G1_Article.pdf`

### Run in Colab

Open `notebooks/Geometry_MMALS_G1_Colab.ipynb`. After publishing this folder, change the repository URL in the first setup cell if the GitHub location differs from:

```text
https://github.com/gharbonnier78/geometry-mmalls-g1
```

## Evidence and claim discipline

The implementation logs per-sample or per-batch traces for:

- `z0`: frozen sensory representation;
- `context`: inferred context coordinate;
- `route`: host probability vector;
- `host_outputs`: each host transformation;
- `z_mm`: synthesized MMALS representation;
- predictions, losses, task stage, true angle and resource estimates.

Host specialization is not accepted from route frequency alone. It requires converging evidence from contribution gain, ablation locality, representation separation, route-function stability and cross-seed role matching.

See:

- [`docs/EXPERIMENT_PROTOCOL.md`](docs/EXPERIMENT_PROTOCOL.md)
- [`docs/CLAIMS_AND_GATES.md`](docs/CLAIMS_AND_GATES.md)
- [`docs/REPRODUCIBILITY_CHECKLIST.md`](docs/REPRODUCIBILITY_CHECKLIST.md)
- [`docs/RESUME_FR.md`](docs/RESUME_FR.md)

## Licensing and citation

Code is released under the MIT License. The article and documentation may be reused with attribution; see `CITATION.cff` for the preferred citation.
