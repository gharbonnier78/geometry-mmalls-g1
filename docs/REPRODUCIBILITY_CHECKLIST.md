# Reproducibility Checklist

## Before training

- [ ] Commit hash recorded.
- [ ] Configuration file copied into the run directory.
- [ ] Python, CUDA, PyTorch and hardware versions recorded.
- [ ] All random seeds declared.
- [ ] Dataset source, transforms, checksums and splits recorded.
- [ ] Validation budget equalized across methods.
- [ ] Oracle/task identifiers excluded from deployable inputs.
- [ ] Baseline sanity checks pass.

## During training

- [ ] Per-stage checkpoints stored.
- [ ] Learning rates, losses and router statistics logged.
- [ ] Route collapse and host starvation alarms monitored.
- [ ] Active compute and memory-access proxies logged.
- [ ] Old-context evaluation performed only through the declared protocol.

## Geometry evidence

- [ ] Sensory geometry reported as a baseline.
- [ ] Distances use the declared metric for each space.
- [ ] UMAP/PCA are not treated as primary evidence.
- [ ] Permutation/null controls included.
- [ ] Interpolation angles were never used for fitting or model selection.
- [ ] Causal interventions include matched-norm orthogonal controls.
- [ ] Cross-seed host roles are matched before comparison.

## Continual-learning evidence

- [ ] Final average accuracy and forgetting reported per seed.
- [ ] Retention evaluated after subsequent stages, not only immediately.
- [ ] Joint training marked as an upper bound, not a fair online baseline.
- [ ] EWC/replay/MoE hyperparameters selected on validation data.
- [ ] Failed baselines investigated before public comparison.

## Publication package

- [ ] Raw per-seed CSV files included.
- [ ] Aggregation script included.
- [ ] Figures reproducible from CSV files.
- [ ] Claim manifest points to exact artifacts.
- [ ] Synthetic results labeled clearly.
- [ ] Limitations and failed hypotheses retained.
- [ ] LaTeX source and compiled PDF match.
