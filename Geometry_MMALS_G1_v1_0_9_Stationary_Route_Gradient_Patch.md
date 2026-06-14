# Geometry-MMALS G1 v1.0.9 — non-negative RNG seed patch

## Failure

The dense held-out evaluation includes negative angles. The prediction bootstrap
previously constructed its seed as:

```python
SPLIT_SEED + int(angle * 10) + 101
```

At `angle = -75°` and `SPLIT_SEED = 0`, this becomes `-649`.
`numpy.random.default_rng()` rejects negative integer entropy and raises:

```text
ValueError: expected non-negative integer
```

## Correction

The notebook now maps every deterministic integer seed into NumPy's uint32
seed domain:

```python
UINT32_MODULUS = 2 ** 32

def nonnegative_rng_seed(seed):
    return int(seed) % UINT32_MODULUS
```

This normalization is applied inside `bootstrap_delta()` and the other local
RNG helpers, so future negative offsets cannot recreate the failure.

A regression gate explicitly tests the `-75°` case.

## Recovery in an active Colab session

The exception occurs after all three seed-0 models have trained, but before
`run_seed(0)` returns. Its local results are therefore not appended to
`all_runs`.

Rerun:

1. the helper/analysis cell containing `bootstrap_delta`;
2. the cell beginning with `all_runs = []`.

The sensory grove, source split, and earlier setup cells do not need to be
rerun while they remain in memory. Seed 0 itself will train again.
