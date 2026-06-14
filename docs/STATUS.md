# Status

## Current release: Geometry-MMALS G1 v1.0.9
### Stationary route geometry qualification pilot `r1`

The repository now contains two distinct evidence layers:

1. **Executed v1.0.8 seed-0 development evidence** - archived under `results/v1_0_8/seed_0/` and summarized in `docs/reports/Geometry_MMALS_G1_v1_0_8_Results_and_Interpretation_Report.pdf`.
2. **Unexecuted v1.0.9 five-seed pilot protocol** - implemented in `notebooks/Geometry_MMALS_G1_StationaryGeometry_Pilot_v1_0_9.ipynb`.

The v1.0.8 run found strong single-seed candidate evidence for d4 context and route geometry, fiber consistency, held-out factor decoding, effective rank, and source-disjoint causal specificity. It did not demonstrate material predictive or operational benefit. A post-run audit found that the legacy route target depended on the largest factor gap visible in the current continual stage.

v1.0.9 fixes that defect with a stationary chord-compatible route target and tests replication across five model seeds while keeping the v1.0.8 source split and frozen sensory boundary fixed.

Accepted status:

- v1.0.8: development evidence, not final qualification;
- v1.0.9: C0 implementation only until execution;
- C1-C6: unqualified.
