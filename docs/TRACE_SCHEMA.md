# Trace Schema

A Geometry-MMALS trace must make the internal chain reconstructible without storing raw private data unnecessarily.

## Required identifiers

- `run_id`, `seed`, `checkpoint_id`, `continual_stage`;
- `sample_id` or a salted/reproducible surrogate;
- dataset split and transform identifier;
- true class and controlled context factor for evaluation only.

## Internal tensors

- `z0`: frozen sensory representation;
- `context`: inferred context coordinate or distribution;
- `route`: normalized host weights;
- `host_outputs`: one transformed representation per host, or declared compressed summaries;
- `z_mm`: route-function synthesis;
- logits/prediction and calibration outputs.

## Functional and resource fields

- per-host contribution and ablation estimates;
- active host count and route entropy;
- latency, FLOP and memory-access proxies;
- reconstructive-memory references;
- compiled-memory/prototype identifiers;
- drift and out-of-support indicators.

## Storage policy

Large tensor traces may be sharded in Parquet, NumPy or Zarr files. CSV tables should contain artifact paths and stable hashes rather than embedding high-dimensional arrays as text. Every compression must preserve enough information to reproduce the metric being claimed.
