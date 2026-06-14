# Geometry-MMALS G1

**From audit-space projections to grounded functional geometry in continual learning.**

Geometry-MMALS G1 is a research specification and implementation scaffold for testing whether MMALS learns a meaningful internal geometry of representations, inferred contexts, routes, host transformations, synthesis states, and memory transport.

> **Status:** v1.0.7 context-bottleneck protocol release. The repository supports a **C0 implementation and protocol-validity claim only**. It does **not** claim successful context mediation or that C1-C6 have passed. Qualification requires frozen thresholds, multi-seed runs, matched controls, archived manifests and hardened baselines.

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

## v1.0.7 primary notebook

`notebooks/Geometry_MMALS_G1_ContextBottleneck_v1_0_7.ipynb`

This protocol tests whether the weak context mediation observed in v1.0.6 was caused by direct sensory shortcutting. It adds a dedicated context-only bottleneck router and a capacity-matched sensory-only router. The primary contrast is context bottleneck with versus without geometry regularization.

The proposed v1.0.6-to-v1.0.7 migration direction is retained, with one scientific correction: a stop-gradient control that still passes `z0` into the router is not diagnostic when the sensory encoder is already frozen. It is replaced by an explicit sensory-only information-path control.

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


## Numerical-stability patch v1.0.2

The v1.0.2 patch fixes the uniform-route NaN gradient in the Fisher-Rao geodesic loss, adds a regression gate, finite-value checks, and a stabilized causal tangent probe.

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

Open `notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb`. The first setup cell verifies package version `1.0.3` and records the active git commit SHA. After publishing this folder, change the repository URL only if the GitHub location differs from:

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


## Current protocol release: v1.0.7

Primary notebook: `notebooks/Geometry_MMALS_G1_ContextBottleneck_v1_0_7.ipynb`

v1.0.7 asks whether the context variable can become a genuine mediator when direct `z0` access is removed. Six equal-compute variants compare standard, uniform-static, context-bottleneck and capacity-matched sensory-bottleneck routes, with and without paired geometry regularization.

The repository also archives the 18-page reviewer status report and its complete LaTeX source under `docs/reports/` and `paper/reviewer_status_v1_0/`.

Scientific status remains **C0 protocol implementation only**. Context mediation, C1-C6 and operational superiority are not claimed.
