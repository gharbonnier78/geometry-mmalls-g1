# Geometry-MMALS G1 v1.0.8 — synthesis column patch

## Problem

The paired-delta cell iterated over the semantic space name `synthesis`, while
`collect_trace()` stored the corresponding vectors in the DataFrame column
`z_mm`. Calling `stack(sub, "synthesis")` therefore raised:

```text
KeyError: 'synthesis'
```

## Correction

The patched notebook introduces an explicit mapping:

```python
SPACE_TO_TRACE_COLUMN = {
    "sensory": "z0",
    "context": "context",
    "route": "route",
    "synthesis": "z_mm",
}
```

`source_geometry()` now validates the requested space, resolves the physical
trace column, checks required columns, and rejects empty method/angle subsets.

## Run recovery

The failure occurs after training and trace collection. In the active Colab
session, replace the `source_geometry()` helper with the corrected version and
rerun the failed paired-delta cell and all following cells. Retraining is not
required while `models` and `trace_df` remain in memory.
