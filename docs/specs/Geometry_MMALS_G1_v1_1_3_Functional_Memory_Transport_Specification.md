# Geometry-MMALS G1 v1.1.3

## Functional Memory Transport under Matched Remembered-Source Access

**Status:** corrected C0 specification and executable Colab; gradient-scale calibration required before the five-seed pilot.  
**Build revision:** `functional-memory-transport-c0-r2`.  
**Program decision:** v1.1.3 is the final planned experiment in the fully frozen-host regime.

## Abstract

Geometry-MMALS G1 v1.1.1 isolated the context-to-route bridge under one frozen host ecosystem. Version 1.1.2 repaired the sharp local tails of prototype routing but did not outperform the low-capacity linear router on the preregistered held-out functional contrast. Covariance-aware context geometry nevertheless added stable information beyond centroid-only geometry.

Version 1.1.3 therefore stops adding router capacity. It fixes one linear router and asks which memory object should constrain that router during sequential learning. The experiment compares current-only learning, limited replay, nominal route anchoring, functional transport under a frozen host-cost matrix, and joint functional memory. Treatments receive the same remembered identities, the same access to old images, the same memory batches, and matched compute. They do **not** store the same number of bytes: richer treatments deliberately preserve richer targets for the same remembered sources. A byte-matched analysis is optional and secondary.

The protocol measures paired nominal and functional drift, old-angle forgetting, distributional transport, mediated-latent drift, output drift, prediction identity, and accumulated regularized transport cost along the learning path. A diagnostic compiled memory compares a covariance-aware Gaussian with a precisely defined isotropic Gaussian in root-simplex coordinates.

The central claims are narrow. v1.1.3 can test whether functional transport preserves old route-function behavior better than nominal route anchoring under matched remembered-source access, and whether joint functional memory reduces old-angle forgetting beyond replay. It cannot establish mature host specialization, positive backward transfer, transport optimality, a learned Riemannian manifold, or the central co-adaptive MMALS hypothesis.

## 1. Why v1.1.3 follows v1.1.2

The v1.1.2 pilot produced three relevant observations:

1. structured low-capacity routing improved functional geometry over the flexible MLP baseline, but the bounded residual did not robustly beat the linear router;
2. the continuity repair removed the very large local tails of the prototype family without creating a qualified functional bridge;
3. context covariance added stable factor information beyond centroid geometry.

The next experiment therefore changes the memory objective, not the router architecture. This is a closure experiment for the frozen-host regime: after v1.1.3, the program either retains a narrow functional-memory result or records that ordered routing and richer memory remain insufficient with a neutral frozen host bank.

## 2. Frozen ecosystem and reconstruction acceptance

For every model seed, all treatments reconstruct the same ecosystem from the same code, seeds, data partitions, and training protocol:

\[
z_0=P(x),\qquad c=C_\phi(z_0),\qquad u_h=g_h(z_0),
\]

\[
z_M(r)=\sum_{h=1}^{H}r_hu_h,\qquad \hat y=Q(z_M).
\]

The sensory encoder \(P\), context encoder \(C_\phi\), host bank \(\{g_h\}\), synthesis normalization, classifier \(Q\), and common host-cost matrix \(C^\star\) are frozen during the memory-treatment comparison. Only a linear router is trainable:

\[
r_\theta(c)=\operatorname{softmax}(Wc+b).
\]

Every treatment starts from the same newly initialized router for a given model seed:

\[
\text{router seed}=\text{model seed}+1300.
\]

No treatment loads a trained v1.1.2 router.

Exact parameter hashes are recorded for traceability but are **not** a portability gate because deterministic floating-point reconstruction can vary across software and hardware stacks. Reconstruction acceptance is metric-based:

- sensory test accuracy must be at least \(0.92\);
- the reference v1.1.2 sensory accuracy is \(0.942\);
- all reconstructed component hashes are exported;
- frozen-component deltas after each memory treatment must be at most \(10^{-6}\).

## 3. Remembered-source access budget

At each curriculum stage, every treatment receives:

- the full current-stage training subset;
- exactly 64 remembered source identities for each previously learned angle;
- the same old-image accesses and memory-batch schedule;
- the same current and memory forward counts;
- the same number of optimizer steps;
- no access to the remaining historical training examples.

This is a **matched remembered-source and replay-access budget**, not a matched byte budget.

M1 stores or reconstructs labels for replay. M2 and M3 additionally preserve route targets. M4 additionally preserves mediated-latent and output targets. The richer information object is intentional: the main question compares what is preserved for the same remembered identities.

The notebook exports, for every treatment:

- remembered identity count;
- target fields and dimensions;
- estimated auxiliary target bytes per remembered source;
- current and memory forward counts;
- optimizer-step counts.

An optional secondary sensitivity analysis may equalize estimated bytes by reducing the number of M4 identities. It is disabled in the primary pilot and cannot replace the main contrast.

Memory identities are selected deterministically from the fixed split permutation and are identical across treatments.

## 4. Acquisition snapshot contract

Let \(a\) denote an angle, \(\tau(a)\) the stage at which angle \(a\) is first learned, \(s\) a later evaluation stage, and \(T\) the final stage.

The acquisition contract is exact:

1. complete the final optimizer step of stage \(\tau(a)\);
2. deep-copy the router state immediately;
3. instantiate a frozen teacher from that copied state;
4. compute and store teacher targets for the remembered identities of angle \(a\);
5. evaluate the end of stage \(\tau(a)\);
6. only then begin any data loading or optimizer operation for stage \(\tau(a)+1\).

Two distinct artifacts are exported:

- `router_snapshot_at_acquisition`;
- `teacher_targets_at_acquisition`.

Teacher targets are never recomputed from a later model.

## 5. Treatments

| Treatment | Current CE | Replay CE | Route anchor | Functional OT | Latent anchor | Output KL |
|---|---:|---:|---:|---:|---:|---:|
| M0 current only | yes | zero-weight matched pass | no | no | no | no |
| M1 replay CE | yes | yes | no | no | no | no |
| M2 route anchor | yes | yes | yes | no | no | no |
| M3 functional transport | yes | yes | no | yes | no | no |
| M4 joint functional memory | yes | yes | no | yes | yes | yes |

M0 still performs the matched memory forward pass, but old-memory losses receive zero weight.

## 6. Exact memory losses

### 6.1 Nominal route anchor

The nominal route loss uses root-simplex coordinates:

\[
\mathcal L_R
=
\frac{1}{2B}\sum_{n=1}^{B}
\left\|
\sqrt{r_s^{(n)}}-\sqrt{r_{\mathrm{ref}}^{(n)}}
\right\|_2^2.
\]

### 6.2 Common functional host cost

Let \(d_z\) be the host-output dimension. The unnormalized cost is

\[
\widetilde C_{hk}
=
\frac{1}{d_z}
\mathbb E_x
\left[
\left\|g_h(P(x))-g_k(P(x))\right\|_2^2
\right].
\]

The common cost used by every treatment is median-normalized:

\[
C^\star_{hk}
=
\frac{\widetilde C_{hk}}
{\operatorname{median}_{i<j}\widetilde C_{ij}},
\qquad C^\star_{hh}=0.
\]

### 6.3 Paired functional transport

\[
\mathcal L_F
=
\frac{1}{B}\sum_{n=1}^{B}
\operatorname{OT}_{C^\star,\epsilon_r}
\left(r_s^{(n)},r_{\mathrm{ref}}^{(n)}\right),
\]

with route Sinkhorn regularization

\[
\epsilon_r=0.05,
\qquad K_r=100\text{ iterations}.
\]

### 6.4 Latent and output preservation

\[
\mathcal L_Z
=
\frac{1}{B}\sum_n
\left\|z_{M,s}^{(n)}-z_{M,\mathrm{ref}}^{(n)}\right\|_2^2,
\]

\[
\mathcal L_Y
=
T_d^2
\operatorname{KL}
\left(
\operatorname{softmax}(\ell_{\mathrm{ref}}/T_d)
\;\|\;
\operatorname{softmax}(\ell_s/T_d)
\right),
\]

where

\[
T_d=2.0,
\qquad \tau_{\mathrm{route}}=1.0.
\]

## 7. Pre-pilot gradient-scale calibration

Equal scalar coefficients do not imply equal optimization pressure. Before the five-seed pilot, one development calibration is mandatory.

The calibration uses:

- model seed 0;
- the development data profile;
- eight preregistered probe batches;
- the same linear router and frozen ecosystem;
- identical old-memory examples for both losses.

After inducing limited current-task drift, the notebook measures unweighted router-gradient norms

\[
g_R=\operatorname{median}\|\nabla_\theta\mathcal L_R\|_2,
\qquad
g_F=\operatorname{median}\|\nabla_\theta\mathcal L_F\|_2.
\]

The route-anchor coefficient is fixed at

\[
\lambda_R=0.5.
\]

The functional coefficient is proposed once as

\[
\lambda_F
=
\operatorname{clip}
\left(
\lambda_R\frac{g_R}{g_F},
0.05,
2.0
\right).
\]

The calibration report, selected \(\lambda_F\), and its SHA-256 checksum must be committed to the YAML before the pilot. Pilot and qualification profiles refuse to start while calibration status is not `locked`. Coefficients are never adapted during the pilot.

## 8. Distributional transport

For angle \(a\) after stage \(s\), define the empirical route law

\[
\mu_{a,s}
=
\frac{1}{N}\sum_{n=1}^{N}
\delta_{r_s(x_n,a)}.
\]

The inner functional ground cost is

\[
D^{(r)}_{ij}
=
\operatorname{OT}_{C^\star,\epsilon_r}(r_i,r_j).
\]

The outer cloud transport is

\[
\mathcal T_a^{s-1\rightarrow s}
=
\operatorname{OT}_{D^{(r)},\epsilon_c}
\left(\mu_{a,s-1},\mu_{a,s}\right),
\]

with

\[
\epsilon_c=0.05,
\qquad K_c=100\text{ iterations}.
\]

This complements source-matched drift. It does not prove optimal transport optimality or identify a unique causal transport plan.

## 9. Regularized route-path diagnostics

For angle \(a\), the accumulated regularized path cost is

\[
L_a
=
\sum_{s=\tau(a)+1}^{T}
\delta_F\left(\mu_{a,s-1},\mu_{a,s}\right),
\]

and the direct endpoint cost is

\[
D_a
=
\delta_F\left(\mu_{a,\tau(a)},\mu_{a,T}\right),
\]

where \(\delta_F\) is the entropically regularized functional transport dissimilarity used by the implementation.

The reported ratio is

\[
E_a
=
\frac{L_a}{D_a+\varepsilon}.
\]

This is a **path-to-endpoint regularized cost ratio**, not a geodesic excess. Because raw entropic OT is not guaranteed to be a metric, \(E_a\ge 1\) is not guaranteed and values below one are possible. The quantity is used only as a comparative diagnostic under an identical computation rule.

## 10. Compiled-memory diagnostic

For the root routes \(y=\sqrt r\), the covariance-aware summary is

\[
q_a^{\mathrm{cov}}
=
\mathcal N(m_a,\Sigma_a),
\qquad
m_a=\mathbb E[y].
\]

The single preregistered baseline is the trace-matched isotropic Gaussian

\[
q_a^{\mathrm{iso}}
=
\mathcal N(m_a,\sigma_a^2 I),
\qquad
\sigma_a^2
=
\frac{1}{d_r}\operatorname{tr}(\Sigma_a).
\]

The diagnostic contrast is

\[
\Delta\mathrm{NLL}
=
\mathrm{NLL}(q^{\mathrm{cov}})
-
\mathrm{NLL}(q^{\mathrm{iso}}),
\]

where negative values favor covariance-aware compilation. This branch is diagnostic only and does not replace replay.

## 11. Preregistered constants

| Element | Value |
|---|---:|
| Remembered identities | 64 per previous angle |
| Identity selection | fixed split permutation, first 64 memory indices |
| Router initialization | `model_seed + 1300` |
| Route temperature | 1.0 |
| Distillation temperature | 2.0 |
| Route Sinkhorn | \(\epsilon=0.05\), 100 iterations |
| Cloud Sinkhorn | \(\epsilon=0.05\), 100 iterations |
| New-angle equivalence margin | 0.01 |
| Seed confidence | 95% t interval |
| Favorable-seed requirement | at least 4/5 |
| Sensory acceptance floor | 0.92 |
| Calibration seed / batches | 0 / 8 |
| \(\lambda_R\) | 0.5 |
| \(\lambda_F\) | locked after development calibration |
| Profiles | development calibration / development / pilot / qualification |

## 12. Contrasts, metrics, and directions

| ID | Treatment - control | Metric | Favorable direction | Role |
|---|---|---|---|---|
| A1 | M3 - M2 | endpoint functional drift \(D_F\) | \(<0\) | primary functional-memory gate |
| A2 | M3 - M2 | old-angle forgetting | \(<0\) | secondary operational alignment |
| B1 | M4 - M1 | old-angle forgetting | \(<0\) | primary retention gate |
| B2 | M4 - M1 | path-to-endpoint cost ratio | \(<0\) | secondary path diagnostic |
| S1 | M4 - M1 | new-angle accuracy difference | \(|\Delta|\le0.01\) | safety equivalence |
| D1 | covariance - isotropic | held-out root-route NLL | \(<0\) | diagnostic candidate only |

A1 qualifies only if the upper bound of the five-seed 95% confidence interval is below zero and at least four of five seeds are favorable. B1 uses the same decision rule. A2 is reported regardless of outcome but is not substituted for A1.

Mandatory safety gates are:

- frozen ecosystem;
- matched current and memory compute;
- exact remembered-source count and no full historical access;
- source-disjoint evaluation;
- acquisition snapshot ordering;
- locked pre-pilot gradient calibration;
- prediction-identity preservation;
- new-angle non-degradation.

Failure of a protocol-integrity gate blocks the corresponding scientific claim.

## 13. Required exports

The notebook exports:

- split and remembered-source manifests;
- metric-based reconstruction acceptance and audit hashes;
- acquisition snapshot event logs;
- memory-information budget summary;
- gradient calibration report and lock metadata;
- common host-cost matrix definition and tensor;
- staged accuracy, NLL, and forgetting;
- paired nominal and functional drift;
- M3-versus-M2 forgetting alignment;
- latent drift, output KL, and prediction identity;
- distributional functional transport;
- accumulated regularized path cost, endpoint cost, and ratio;
- covariance and isotropic compiled-memory NLL;
- aggregate seed effects and gate summary;
- run manifest, claim manifest, and environment capture.

## 14. Interpretation and stopping rule

A positive A1 result would support only:

> Functional transport preserves old route-function behavior better than nominal route anchoring under matched remembered-source access and matched compute in a frozen host ecosystem.

A positive B1 result would support only:

> Richer joint functional memory reduces old-angle forgetting beyond replay for the same remembered identities and old-image access.

Neither result answers whether context geometry can organize useful host specialization. Therefore v1.1.3 is the final fully frozen-host experiment:

- if A1 or B1 passes, retain the narrow memory claim and proceed to controlled host adaptation;
- if both fail, record the frozen-regime limit and proceed to controlled host adaptation;
- if results are mixed, classify them as partial and still leave the fully frozen regime.

No additional router, distance, or frozen-bank memory variant is planned after v1.1.3.

## 15. Non-claims

v1.1.3 does not establish:

- mature host specialization;
- positive backward transfer;
- operational superiority;
- byte efficiency of richer memory objects;
- optimality or metricity of entropic transport;
- geodesic route motion;
- a learned Riemannian manifold;
- reinforcement-learning control;
- quantum advantage.
