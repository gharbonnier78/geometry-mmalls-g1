# Geometry-MMALS G1 migration: v1.0.8 -> v1.0.9

## Scientific reason

The executed v1.0.8 run produced strong single-seed d4 evidence for context order, route order, cross-source fiber alignment, held-out factor decoding, effective rank, and source-disjoint causal specificity. A post-run audit identified a protocol defect in the legacy route loss: factor gaps were normalized by the largest gap visible at the current continual stage. The same physical relation therefore received different targets as the curriculum expanded.

v1.0.9 freezes the route topology and turns the strongest v1.0.8 result into a five-model-seed pilot.

## Tracked changes

1. **CHG-109-01** - Add `paired_route_geometry_loss_stationary`.
2. **CHG-109-02** - Use the fixed 120-degree chord-compatible target for routes and contexts.
3. **CHG-109-03** - Retain a legacy full-alignment comparator.
4. **CHG-109-04** - Focus the main experiment on context dimension 4.
5. **CHG-109-05** - Add five fixed-split model seeds.
6. **CHG-109-06** - Evaluate a dense 15-degree grid from -75 to +75 degrees.
7. **CHG-109-07** - Add paired source-bootstrap prediction intervals.
8. **CHG-109-08** - Add source-bootstrap causal-specificity intervals.
9. **CHG-109-09** - Add class-evidence and prediction-identity preservation.
10. **CHG-109-10** - Add seed-level Student-t confidence intervals.
11. **CHG-109-11** - Preserve the v1.0.8 source split and frozen sensory boundary.
12. **CHG-109-12** - Separate pilot candidate gates from final qualification.
13. **CHG-109-13** - Archive the complete v1.0.8 result bundle and results report.
14. **CHG-109-14** - Preserve reviewer report v1.1 and LaTeX sources.

## Primary methods

- `d4_no_geo`
- `d4_full_legacy_route`
- `d4_full_stationary_route`

## Primary contrasts

- stationary full alignment vs d4 no geometry;
- stationary route target vs legacy nonstationary route target.

## Non-claims

v1.0.9 does not claim final C1 qualification, predictive superiority, host specialization, memory transport, operational utility, backward transfer, replay-free continual learning, or quantum advantage before execution and review of the five-seed evidence.
