# Geometry-MMALS G1

**From grounded context geometry to functional routing in continual learning.**

Geometry-MMALS G1 is a falsifiable research program for testing whether MMALS learns meaningful internal geometry across inferred contexts, routes, host transformations, synthesized states, and continual-memory transport.

> **Latest executed evidence:** v1.0.9 five-seed matched-compute pilot.  
> **Latest executable protocol:** v1.1.0 functional routing, complete C0 implementation and not yet executed.  
> **Current scientific status:** candidate replicated context geometry; functional and operational geometry remain unqualified.

## What the system builds

A frozen sensory encoder transforms a rotated handwritten digit into `z0`. A four-dimensional inferred context `c` summarizes the situation. A route `r` distributes probability mass over four functional hosts. Their weighted outputs form `zM`, which is classified.

```text
image x -> frozen sensory z0 -> inferred context c -> route r
        -> host transformations -> synthesis zM -> prediction
```

The central question is whether nearby rotation angles produce nearby contexts, whether unseen angles interpolate, and whether this geometry then controls routes and hosts.

## v1.0.9 result

Across model seeds `[0,1,2,3,4]`, stationary full alignment versus no geometry produces:

- context rho effect `+0.107`, 95% seed CI `[+0.029,+0.185]`;
- context stress effect `-0.042`, CI `[-0.084,-0.001]`;
- held-out-source context decoding improvement of about `+0.132 R²`;
- held-out angle MAE improvement of about `5°`.

Every seed shows a positive context-order effect. The result generalizes across held-out source identities.

The following do **not** replicate or improve reliably:

- route geometry;
- synthesis geometry;
- prediction accuracy;
- forgetting;
- causal specificity;
- stationary-route superiority over the legacy route target.

The result is therefore representational, not yet functional or operational.

## English article

The 21-page article explains the program at two levels: an intuitive path for non-specialists and a complete mathematical account.

```text
docs/reports/Geometry_MMALS_G1_v1_0_9_Results_and_v1_1_0_Specification.pdf
paper/results_v1_0_9_and_spec_v1_1_0/
releases/Geometry_MMALS_G1_v1_0_9_Results_and_v1_1_0_Specification_LaTeX.zip
```

## v1.1.0 functional-routing implementation

v1.1.0 freezes the successful `z0 -> c` representation and compares:

1. `R0`: current MLP context router;
2. `R1`: low-capacity linear router;
3. `R2`: prototype-energy router.

For the prototype router:

```text
E_geo_h(c) = half_chord(c, mu_h)^2 / (2 sigma_h^2) + bias_h
r_h(c) proportional to exp(-E_geo_h(c) / temperature)
```

This is the first geometric component of the broader Energy-Guided Router. Future energy terms add host uncertainty, cost, memory risk, stability, and goals.

v1.1.0 also introduces:

- nominal root-simplex route geometry;
- functional route geometry using an optimal-transport cost over measured host functions;
- held-out low-capacity context-to-route probes;
- Jacobian and finite tangent-versus-orthogonal interventions;
- host territory, specialization, overlap, diversity, ablation, and resilience;
- matched-compute, source-bootstrap, and seed-level gates.

Implementation and specification files:

```text
notebooks/Geometry_MMALS_G1_FunctionalRouting_v1_1_0.ipynb
src/geometry_mmalls/functional_routing.py
configs/rotated_mnist_g1_v110.yaml
docs/specs/Geometry_MMALS_G1_v1_1_0_Functional_Routing_Specification.md
configs/rotated_mnist_g1_v110_spec.yaml
tests/test_functional_routing.py
```

## Repository map

```text
notebooks/                 Executable Colab protocols through v1.1.0
src/geometry_mmalls/       PyTorch models, geometric/functional routing, metrics, memory stubs
configs/                   Frozen protocols and v1.1.0 specification
results/v1_0_9/            Complete executed five-seed evidence
paper/                     Article and reviewer LaTeX sources
docs/reports/              Compiled archival reports
docs/specs/                Complete v1.1.0 mathematical specification
docs/changes/              Version and design history
releases/                  Distributable LaTeX packages
tests/                     Numerical and structural regression tests
```


## Run v1.1.0

After publishing this package to the existing repository, open:

```text
notebooks/Geometry_MMALS_G1_FunctionalRouting_v1_1_0.ipynb
```

The default `pilot` profile runs seeds `[0,1,2,3,4]`. Set the Colab environment variable `G1_PROFILE=development` for a one-seed development run or `G1_PROFILE=qualification` for the preregistered ten-seed profile. The notebook reproduces and freezes one v1.0.9-aligned context checkpoint per seed before training the three routing treatments.

## Validation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```

The canonical v1.1.0 C0 implementation passes 40 package tests. The five-seed v1.1.0 experiment remains unexecuted.

## Claim discipline

The repository does not claim:

- final C1–C6 qualification;
- predictive superiority from geometry;
- replicated route geometry or host specialization;
- memory transport or backward transfer;
- operational utility;
- domain-general geometry;
- replay-free continual learning;
- quantum computation or quantum advantage.

The planned progression is:

```text
G1.1 geometry-mediated routing
 -> G1.2 host ecology
 -> G1.3 memory transport
 -> G2 full energy-guided and goal-conditioned control
 -> G3 phase-aware / quantum-inspired routing
```

Code is released under the MIT License. See `CITATION.cff` for citation metadata.
