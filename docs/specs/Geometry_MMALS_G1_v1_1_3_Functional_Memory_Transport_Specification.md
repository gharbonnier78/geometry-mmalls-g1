# Geometry-MMALS G1 v1.1.3

## Functional Memory Transport, Route-Path Diagnostics, and Limited-Replay Retention

**Status:** complete C0 specification and executable Colab; empirical pilot pending.  
**Build revision:** `functional-memory-transport-c0-r1`.

## Abstract

Geometry-MMALS G1 v1.1.1 isolated the context-to-route bridge under one frozen host ecosystem. The hybrid prototype router did not qualify, although route-swap ordering showed that the frozen ecosystem contained non-arbitrary functional structure. Version 1.1.2 repaired the sharp local tails of the prototype family with a bounded smooth residual and a context-only continuity hinge. The repair succeeded mechanically but did not outperform the low-capacity linear router on held-out functional order or stress. At the same time, covariance-aware context geometry improved stress over centroid-only geometry by -0.0442 with a five-seed confidence interval entirely below zero.

Version 1.1.3 therefore stops adding router capacity. It fixes one linear router architecture and asks a different question: **what memory object should constrain a route as learning proceeds?** The experiment compares current-only learning, limited replay, nominal route anchoring, functional transport anchoring under a frozen host-cost matrix, and a joint functional-memory objective. It measures paired route drift, paired functional drift, distributional transport, latent drift, output drift, identity preservation, path length, endpoint drift, and path excess. A separate compiled-memory diagnostic compares barycentric and covariance-aware summaries in root-simplex coordinates.

The central claim is deliberately narrow: v1.1.3 can establish whether functional route transport preserves old behavior more efficiently than nominal route anchoring under a fixed ecosystem and fixed memory budget. It cannot establish mature host specialization, positive backward transfer, optimality of the transport plan, or a learned Riemannian manifold.

## 1. Why v1.1.3 follows v1.1.2

The v1.1.2 five-seed pilot produced three important observations:

1. R5 was better than the MLP baseline on held-out functional geometry, but not robustly better than the linear router.
2. R5 reduced the large local-continuity tails of R2/R3, showing that smoothness can be repaired without proving a better bridge.
3. covariance-aware context geometry added stable information beyond centroids.

These findings suggest that the next bottleneck is not another routing architecture. The next falsifiable question is whether the system is preserving the correct **route-function memory object** over time.

## 2. Frozen experimental ecosystem

For every model seed, v1.1.3 reconstructs and freezes the same objects used by all memory treatments:

\[
z_0=P(x),\qquad c=C_\phi(z_0),\qquad u_h=g_h(z_0),
\]

\[
z_M(r)=\sum_{h=1}^{H}r_hu_h,\qquad \hat y=Q(z_M).
\]

The sensory encoder \(P\), context encoder \(C_\phi\), host bank \(\{g_h\}\), synthesis normalization, classifier \(Q\), and functional host-cost matrix \(C^\star\) are frozen. Only a linear router is trained:

\[
r_\theta(c)=\operatorname{softmax}(Wc+b).
\]

This removes router architecture as a confound. Differences among treatments come only from the memory objective.

## 3. Memory object

For source \(x\), factor regime \(u\), and stage \(t\), the route-function state is

\[
\Phi_t(x,u)=\bigl(r_t,\;z_{M,t},\;p_t\bigr),
\]

where

\[
r_t=r_{\theta_t}(C_\phi(P(x_u))),\qquad
z_{M,t}=\sum_h r_{t,h}g_h(P(x_u)),\qquad
p_t=\operatorname{softmax}(Q(z_{M,t})).
\]

A route vector is therefore only one coordinate of memory. Two identical-looking routes can differ functionally when the host ecosystem changes; conversely, in this frozen-ecosystem protocol, a route change has a measurable functional interpretation through \(C^\star\).

## 4. Limited replay protocol

At each curriculum stage, the model receives:

- the full current-stage training subset;
- a fixed memory of 64 source identities per previously learned angle;
- no access to the remaining historical training examples.

Memory source IDs are selected once by the split seed and are identical across treatments. For each newly learned angle, the experiment stores the original router snapshot. Later memory targets are always computed from that original snapshot, not from the immediately preceding stage. This prevents a slowly drifting teacher from redefining old memory.

Evaluation uses source-disjoint test partitions. Therefore the principal drift metrics compare the final model with the original stage snapshot on identities never used to fit the memory objectives.

## 5. Treatments

| Treatment | Current CE | Replay CE | Route anchor | Functional OT | Latent anchor | Output KL |
|---|---:|---:|---:|---:|---:|---:|
| M0 current only | yes | no | no | no | no | no |
| M1 replay CE | yes | yes | no | no | no | no |
| M2 route anchor | yes | yes | yes | no | no | no |
| M3 functional transport | yes | yes | no | yes | no | no |
| M4 joint functional memory | yes | yes | no | yes | yes | yes |

All treatments use the same linear router initialization, optimizer, current-stage batches, memory batches, number of optimizer steps, and frozen ecosystem.

## 6. Losses

### 6.1 Nominal route anchoring

The nominal anchor acts on square-root simplex coordinates:

\[
\mathcal L_R
=
\frac{1}{2B}\sum_{n=1}^{B}
\left\|
\sqrt{r_t^{(n)}}-\sqrt{r_{\mathrm{ref}}^{(n)}}
\right\|_2^2.
\]

### 6.2 Functional route transport

The frozen host-cost matrix is

\[
C^\star_{hk}
=
\mathbb E_x
\frac{\|g_h(P(x))-g_k(P(x))\|_2^2}{d_M}.
\]

For paired routes, the functional transport loss is

\[
\mathcal L_F
=
\frac{1}{B}\sum_{n=1}^{B}
\operatorname{OT}_{C^\star}
\left(r_t^{(n)},r_{\mathrm{ref}}^{(n)}\right).
\]

This penalizes movement between functionally dissimilar hosts more than movement between redundant hosts.

### 6.3 Latent and output preservation

\[
\mathcal L_Z
=
\frac{1}{B}\sum_n
\|z_{M,t}^{(n)}-z_{M,\mathrm{ref}}^{(n)}\|_2^2,
\]

\[
\mathcal L_Y
=
T^2\operatorname{KL}
\left(
\operatorname{softmax}(\ell_{\mathrm{ref}}/T)
\;\|\;
\operatorname{softmax}(\ell_t/T)
\right).
\]

M4 combines functional transport, latent preservation, and output distillation. The joint objective is a stronger memory treatment, not a claim that all components are necessary.

## 7. Distributional transport

For an old angle \(u\), let

\[
\mu_{u,t}=\frac{1}{N}\sum_{n=1}^{N}\delta_{r_t(x_n,u)}.
\]

The distributional memory movement between stages is

\[
\mathcal T_{u}^{t-1\to t}
=
\inf_{\gamma\in\Pi(\mu_{u,t-1},\mu_{u,t})}
\sum_{ij}\gamma_{ij}
\,d_{C^\star}(r_i,r_j).
\]

This measure does not require source-by-source matching. It asks whether the whole route distribution moved, complementing paired drift.

## 8. Route-path diagnostics

For an old regime \(u\), let \(\mu_{u,s}\) denote its route distribution after stage \(s\). The cumulative path length is

\[
L_u=\sum_{s=u+1}^{T}d_F(\mu_{u,s-1},\mu_{u,s}),
\]

and the endpoint drift is

\[
D_u=d_F(\mu_{u,u},\mu_{u,T}).
\]

The path-excess ratio is

\[
E_u=\frac{L_u}{D_u+\varepsilon}.
\]

A large \(E_u\) indicates oscillatory or wasteful memory motion: the route moved far during learning even if the final endpoint returned near its origin.

## 9. Compiled memory diagnostic

The reconstructive memory stores exact per-source route-function traces. A smaller compiled memory stores a Gaussian summary of the square-root routes:

\[
q_u=\mathcal N(m_u,\Sigma_u),
\qquad
m_u=\mathbb E[\sqrt r],
\qquad
\Sigma_u=\operatorname{Cov}(\sqrt r)+\epsilon I.
\]

The diagnostic compares held-out negative log-likelihood under:

1. an isotropic or barycenter-only summary;
2. the covariance-aware compiled summary.

This is a compression diagnostic only. It does not replace replay in the primary v1.1.3 experiment.

## 10. Primary contrasts and gates

### Primary contrast A: M3 versus M2

Does functional transport preserve old functional state better than nominal route anchoring?

Primary gate:

\[
\Delta D_F=D_F(M3)-D_F(M2)<0
\]

with the upper bound of the five-seed 95% confidence interval below zero and at least four of five favorable seeds.

### Primary contrast B: M4 versus M1

Does joint functional memory reduce old-angle forgetting beyond limited replay alone?

Primary gate:

\[
\Delta F=F(M4)-F(M1)<0
\]

with the upper confidence bound below zero and at least four of five favorable seeds.

### Safety gates

- equal compute and identical memory budget;
- frozen context, host bank, classifier, and \(C^\star\);
- final-versus-original prediction identity lower bound at least 0.95;
- new-angle accuracy within 0.01 of M1 in at least four of five seeds;
- no full old-dataset access.

### Secondary gates

- M4 reduces functional path excess versus M1;
- covariance-aware compiled memory improves held-out root-route NLL in at least four of five seeds;
- distributional transport agrees directionally with paired functional drift.

## 11. Required exports

The notebook exports per-seed and aggregate evidence for:

- split and memory-budget manifests;
- context and common-bank hashes;
- staged accuracy, NLL, and forgetting;
- paired nominal route drift;
- paired functional drift;
- latent drift;
- output KL and prediction identity;
- distributional functional transport;
- cumulative path length, endpoint drift, and path excess;
- compiled-memory fit and held-out diagnostics;
- compute counts;
- gate summary;
- run and claim manifests;
- environment capture.

## 12. Interpretation discipline

A successful v1.1.3 pilot would support the narrow statement that, under a fixed functional ecosystem and fixed limited-memory budget, functional transport preserves old route-function behavior better than nominal route anchoring or replay alone.

It would not establish:

- mature host specialization;
- positive backward transfer;
- operational superiority;
- optimality of the chosen entropic transport;
- a learned Riemannian manifold;
- reinforcement-learning control;
- quantum advantage.

## 13. Roadmap after v1.1.3

- **v1.1.4:** selective causal host adaptation, host contribution, recovery, and cross-seed qualification;
- **G2.1:** explicit bottom-up host state reporting to the router;
- **TPUT:** goal-conditioned forward-backward control after the memory and causal host layers are independently qualified.
