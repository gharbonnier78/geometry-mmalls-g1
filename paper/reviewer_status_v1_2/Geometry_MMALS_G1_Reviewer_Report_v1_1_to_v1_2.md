# Geometry-MMALS G1 reviewer report v1.1 -> v1.2

## Evidence update

v1.2 replaces the single-seed v1.0.7 evidence snapshot with the completed v1.0.9 five-seed matched-compute pilot.

## Main changes

1. Reframe the strongest result as replicated candidate context geometry, not route geometry.
2. Add five-seed context correlation and stress intervals.
3. Add held-out-source factor-decoding R2 and angular-MAE evidence.
4. Record the negative result that the stationary route target does not outperform the legacy target.
5. Downgrade route geometry and source-disjoint causal specificity from promising single-seed evidence to failed/inconclusive replicated evidence.
6. Preserve the distinction between representational geometry and functional geometry.
7. Update the gate table through C6.
8. Redirect next work toward causal coupling from context to routes, hosts, synthesis, and memory transport.
9. Add numerical-stability history for non-negative RNG seeds and coincident-route gradients.
10. Include selected v1.0.9 CSV evidence and figures in the archival package.

## Reviewer-safe core statement

Across five matched-compute model seeds on controlled RotatedMNIST, the d4 globally aligned objective increases trained-angle context distance-order correlation by 0.107 and decreases context stress by 0.042 relative to a no-geometry control. It also improves held-out-source factor decoding by 0.132 R2 and reduces angular MAE by approximately 5 degrees. These improvements do not extend reliably to route geometry, synthesis geometry, predictive accuracy, forgetting, or causal specificity.
