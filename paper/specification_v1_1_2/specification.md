# Geometry-MMALS G1 v1.1.2

## Smooth Simplex-Residual Routing and Covariance-Aware Context Diagnostics

### Status

Complete experimental specification and executable Colab. No v1.1.2 empirical
claim has been made.

## 1. Motivation from v1.1.1

The five-seed bridge-isolation pilot passed its protocol-integrity gates and
showed that far route swaps have larger functional effects than near swaps.
However, the prototype-dominated hybrid R3 router did not qualify: held-out
order intervals crossed zero, local-continuity tails were large, functional
causal specificity failed, and operational non-degradation failed.

The next experiment must preserve the common frozen context, host bank,
classifier, and cost matrix while reducing local route sharpness.

## 2. Primary router repair

The new router is linear first:

\[
\ell^{\mathrm{base}}(c)=Wc+b.
\]

A prototype branch produces a centered bounded residual:

\[
\delta_h(c)=\tanh\left(
\frac{s_h^{\mathrm{proto}}(c)-\overline{s}^{\mathrm{proto}}(c)}
{\operatorname{Std}_k s_k^{\mathrm{proto}}(c)+\varepsilon}
\right).
\]

A scalar gate controls its amplitude:

\[
g(c)=\sigma(u^\top\phi(c)+\beta),\qquad
0\le s_{\max}g(c)\le s_{\max}.
\]

The final logits and route are

\[
\ell_h(c)=w_h^\top c+b_h+s_{\max}g(c)\delta_h(c),
\qquad
r(c)=\operatorname{softmax}(\ell(c)/\tau).
\]

The cap is preregistered at \(s_{\max}=0.35\).

## 3. Context-only continuity control

The continuity regularizer uses only inferred contexts and routes:

\[
\mathcal L_{\mathrm{cont}}=
\mathbb E_{a<b}
\left[
\max\left(0,d_R(r_a,r_b)-\kappa d_C(c_a,c_b)-m\right)^2
\right].
\]

It does not use angle labels. R4 tests the architecture alone; R5 tests the same
architecture with the continuity term.

## 4. Covariance and SPD diagnostics

For each factor value \(u\), contexts across source identities define a
regularized covariance

\[
\Sigma_u=(1-\lambda)\widehat{\operatorname{Cov}}(c\mid u)
+\lambda\frac{\operatorname{tr}(\widehat\Sigma_u)}{d}I+\epsilon I.
\]

The diagnostic compares

\[
d_{\mathrm{LE}}(\Sigma_u,\Sigma_v)=
\|\log\Sigma_u-\log\Sigma_v\|_F,
\]

\[
d_{\mathrm{AIRM}}(\Sigma_u,\Sigma_v)=
\left\|\log\left(\Sigma_u^{-1/2}\Sigma_v\Sigma_u^{-1/2}\right)\right\|_F,
\]

and the Bures-Wasserstein distance. A combined context distance adds normalized
centroid and covariance terms. This is a diagnostic candidate, not a claim that
the model learned a Riemannian manifold.

## 5. Treatments

- R0: flexible MLP;
- R1: linear router;
- R2: prototype energy;
- R3: v1.1.1 directional-prototype hybrid;
- R4: smooth bounded residual;
- R5: R4 plus context-only continuity.

All treatments share the same frozen sensory encoder, context encoder, host
bank, synthesis layer, classifier, and functional cost matrix within each seed.

## 6. Primary gates

1. R5 reduces held-out common-cost functional stress versus R1.
2. R5 improves held-out functional order versus R1.
3. R5 functional q95 continuity remains within 0.10 of R1.
4. Far route swaps exceed near route swaps in at least four of five seeds.
5. Functional CSR and prediction-identity gates pass.
6. R5 remains within the one-point operational equivalence margin versus R0.
7. The combined centroid-plus-SPD diagnostic reduces stress versus centroid-only.

## 7. Non-claims

v1.1.2 does not claim operational superiority, mature host specialization,
memory transport, full Energy-Guided control, RL control, a learned Riemannian
manifold, or quantum advantage.

## 8. Next stages

- v1.1.3: route-function memory distributions and transport;
- v1.1.4: selective causal host adaptation and recovery;
- G2.1: explicit bottom-up host feedback;
- TPUT: goal-conditioned forward-backward control.
