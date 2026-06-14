# Geometry-MMALS G1 v1.1.0 to v1.1.1 implementation

## Scientific change

v1.1.0 trained a different host bank under each router, so each treatment also
induced a different functional host-cost matrix. v1.1.1 isolates the
context-to-route bridge by freezing one common host bank, classifier, synthesis
layer, and functional cost matrix within each model seed.

## New treatment

The hybrid directional-prototype energy router is:

\[
E_h(c)=
\alpha\frac{d_C(c,\mu_h)^2}{2\sigma_h^2}
-\beta a_h^\top c+b_h.
\]

It combines prototype territories with a global linear direction.

## New required evidence

- held-out nominal route mediation;
- held-out functional mediation under the common cost matrix;
- local continuity distributions and tail quantiles;
- context-noise sensitivity;
- route-swap near/far ordering;
- source-disjoint causal specificity;
- operational equivalence.

## Verification Stack v0.2

A reusable notebook and Python engine parse execution PDFs and result ZIPs and
produce:

- `metric_report.json`
- `protocol_report.json`
- `claim_report.json`
- `evidence_bundle.json`
- `verification_summary.md`
- `verification_gate_summary.csv`

The verifier can reject a high-performing experiment when critical protocol
checks fail.
