# Geometry-MMALS G1 v1.1.1 and 1.1.x roadmap

## Reusable formalization

The routing branch is treated as an operator

\[
R_\theta:\mathcal P(Z\times M)\longrightarrow \mathcal P(H)\cong\Delta^{K-1}.
\]

For an empirical input state,

\[
\mu_t=\frac1N\sum_{j=1}^N\delta_{(z_j,m_j)},\qquad
\pi_H=R_\theta(\mu_t).
\]

The executed v1.1.0 protocol is a controlled special case in which memory is fixed or omitted and the frozen four-dimensional context is the router input. The goal-conditioned extension

\[
R_\theta:\mathcal P(Z\times M)\times G\to\mathcal P(H)
\]

belongs primarily to TPUT and must not be duplicated here.

## v1.1.1 - Local stability and bridge isolation

- Freeze the aligned context, a common host bank, the classifier, and a common functional cost matrix \(C^\star\).
- Compare MLP, linear, prototype-energy, and hybrid directional-prototype routers.
- Promote held-out functional mediation to the primary gate.
- Measure the distribution, not only the mean, of

\[
L_{\mathrm{local}}(\mu_1,\mu_2)=
\frac{d_H(R(\mu_1),R(\mu_2))}{d_{ZM}(\mu_1,\mu_2)+\varepsilon}.
\]

- Add latent/context noise, ambiguity, progressive drift, partial corruption, candidate permutation, route swap, and matched tangent/orthogonal perturbations.
- Export route-sensitivity maps and calibration curves.

A hybrid router is preregistered as

\[
E_h(c)=\alpha\frac{d_C(c,\mu_h)^2}{2\sigma_h^2}-\beta a_h^\top c+b_h,
\qquad
r_h(c)=\frac{e^{-E_h(c)/\tau}}{\sum_k e^{-E_k(c)/\tau}}.
\]

The prototype term creates local territories; the directional term can preserve the global factor direction that the linear router transmitted well in v1.1.0.

## v1.1.2 - SPD covariance geometry and drift

Compare Euclidean, log-Euclidean, affine-invariant SPD, and simple covariance metrics for context and host-activation covariances. Retain SPD geometry only if it improves context separation, route prediction, stability, drift detection, or host specialization relative to Euclidean controls.

## v1.1.3 - Route-function memory and transport

Study whether route-function relations persist, deform, or can be reconstructed across continual stages. Measure path reconstruction, old-region drift, neighborhood retention, route-function stability, and memory-deletion sensitivity. Do not use the term parallel transport unless the required geometric structure is explicitly defined and tested.

## v1.1.4 - Causal host specialization qualification

Require non-trivial route entropy, host contribution gain, localized ablation impact, route-swap impact, representation separation, route-function stability, and cross-seed role reproducibility after matching. Hub-and-partner ecologies are allowed; raw dominance is insufficient.

## G2 and TPUT boundary

Geometry studies \(R_\theta:\mathcal P(Z\times M)\to\mathcal P(H)\). TPUT adds goal and future conditioning:

\[
R_\theta:\mathcal P(Z\times M)\times G\to\mathcal P(H).
\]

The prototype energy from G1 can become the geometric term of the full energy-guided router:

\[
E_h=\alpha E_h^{\mathrm{geo}}+\beta E_h^{\mathrm{host}}+
\gamma E_h^{\mathrm{memory}}+\delta E_h^{\mathrm{cost}}+
\eta E_h^{\mathrm{stability}}+\zeta E_h^{\mathrm{goal}}.
\]

## Mandatory verification stack

Every release should emit versioned metric, protocol, claim, and evidence reports with PASS, PARTIAL, FAIL, or NOT_TESTED status. The verifier must reject test leakage, missing seeds, incomparable budgets, synthetic-as-real claims, route-change-without-goal-gain claims, and specialization claims without ablation evidence.
