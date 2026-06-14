# Geometry-MMALS G1 v1.0.9 — stationary-route gradient patch

## Failure observed

The five-seed pilot completed seeds 0–3, then failed for model seed 4 while
training `d4_full_stationary_route` at the `+60°` stage:

```text
FloatingPointError: Non-finite gradient norm
```

The legacy-route method completed under the same seed and stage, isolating
the problem to the stationary route-distance implementation.

## Root cause

The stationary loss computed:

```python
affinity = <sqrt(p), sqrt(q)>
observed = sqrt(1 - affinity)
```

When two routes are identical or nearly identical in float32, `affinity`
can become exactly `1`. The forward distance is then zero, but the
derivative of `sqrt(x)` is singular at `x = 0`, creating `NaN` or infinite
gradients.

## Stable equivalent

For normalized square-root route coordinates:

```text
||sqrt(p) - sqrt(q)||² = 2(1 - affinity)
```

Therefore the same normalized chord distance can be computed as:

```python
root_delta = sqrt(p) - sqrt(q)
observed = ||root_delta||₂ / sqrt(2)
```

This avoids cancellation in `1 - affinity` and gives a finite zero
subgradient for coincident routes.

## Regression coverage

The patch adds backward tests for:

- random routes;
- exactly uniform/collapsed routes;
- nearly identical routes.

## Recovery in the active Colab session

Seeds 0–3 are already present in `all_runs`. The failed seed 4 was never
appended. After loading the patched source, run only:

```python
seed4_result = run_seed(4)
all_runs.append((4, seed4_result))
print("Completed seeds:", [seed for seed, _ in all_runs])
```

If the runtime or Python module is restarted, rerun the notebook normally.
The scientific version remains `1.0.9`; this is execution-stability change
`CHG-109-14`.
