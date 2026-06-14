# Geometry-MMALS G1 v1.0.7 Release Checklist

- [x] Package version is 1.0.7 in `pyproject.toml` and `geometry_mmalls.__version__`.
- [x] Notebook version guard requires 1.0.7.
- [x] `ContextBottleneckRouter` and `SensoryBottleneckRouter` are in the canonical source package.
- [x] Context and sensory bottleneck routers have shape, gradient and parameter-isolation tests.
- [x] Six core variants share initialization, inputs, forward counts, steps and anchor weight.
- [x] C1, C2 and extrapolation geometry are exported separately.
- [x] Mediation summary exports route shifts, accuracy drops, dependency ratio and `context_is_primary`.
- [x] The 18-page reviewer report is archived under `docs/reports/`.
- [x] The complete reviewer LaTeX source is archived under `paper/reviewer_status_v1_0/`.
- [x] The original reviewer LaTeX ZIP is archived under `releases/`.
- [x] Protocol report PDF was compiled, rendered and visually checked.
- [x] Clean package excludes `.git`, datasets, runtime results, caches, bytecode and local environments.
- [x] C1-C6 and successful mediation remain unclaimed.
