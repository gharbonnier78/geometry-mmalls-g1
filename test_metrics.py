# Geometry-MMALS G1 v1.1.0 — Functional Routing Specification

**Status:** specification only; not yet executed  
**Depends on:** executed Geometry-MMALS G1 v1.0.9 five-seed evidence  
**Primary objective:** test whether the replicated context geometry can causally and functionally mediate routing and host allocation.

## 1. Plain-language purpose

Version 1.0.9 showed that the four-dimensional inferred context can reflect rotation order and can transfer angle information to source identities not used to fit the decoder. The next problem is that the route over hosts does not show the same replicated order, and prediction does not improve.

The v1.1.0 experiment freezes the successful context representation and changes only the mechanism that turns context into a route. The central comparison is:

1. the current flexible MLP router;
2. a low-capacity linear router;
3. a prototype-energy router whose routing is structurally based on distance in context space.

The prototype-energy router is the first controlled geometric term of the broader Energy-Guided MMALS router. It is not a separate research direction.

## 2. Internal chain

\[
x \rightarrow z_0 \rightarrow c \rightarrow r
\rightarrow \{g_h(z_0)\}_{h=1}^H
\rightarrow z_M \rightarrow \hat y.
\]

- `z0`: frozen sensory representation;
- `c`: normalized four-dimensional context;
- `r`: probability distribution over four hosts;
- `g_h`: host transformations;
- `z_M`: weighted host synthesis;
- `y_hat`: digit prediction.

## 3. Frozen modules and matched initialization

For every model seed:

1. reproduce or load the corresponding aligned d4 v1.0.9 context checkpoint;
2. freeze the sensory encoder `P` and context encoder `C_phi`;
3. initialize hosts and classifier from one seed-specific state shared by all router treatments;
4. use identical source splits, curriculum, batches, optimizer steps, replay/anchor schedule, and evaluation partitions.

The true angle is not supplied to the router during the routing phase. It is used only for evaluation and for fitting causal tangent probes on designated fit identities.

## 4. Router treatments

### R0 — current MLP router

\[
\ell^{(0)}(c)=W_2\phi(W_1c+b_1)+b_2,
\qquad
r^{(0)}(c)=\operatorname{softmax}(\ell^{(0)}(c)/\tau).
\]

This is the flexible baseline. It can use information in the context without preserving its metric structure.

### R1 — linear router

\[
\ell^{(1)}(c)=Wc+b,
\qquad
r^{(1)}(c)=\operatorname{softmax}(\ell^{(1)}(c)/\tau).
\]

This tests whether a simple transformation is sufficient to transmit context order. Parameter counts must be reported. A supplementary parameter-matched MLP is allowed as a sanity check but is not a primary treatment.

### R2 — prototype-energy router

Each host has a normalized context prototype and a positive bandwidth:

\[
\|\mu_h\|_2=1,
\qquad
\sigma_h=\sigma_{\min}+\operatorname{softplus}(s_h).
\]

The geometric energy is

\[
E_h^{\mathrm{geo}}(c)
=
\frac{d_C(c,\mu_h)^2}{2\sigma_h^2}+b_h,
\qquad
 d_C(a,b)=\tfrac12\|a-b\|_2.
\]

The route is

\[
r_h^{(2)}(c)
=
\frac{\exp[-E_h^{\mathrm{geo}}(c)/\tau]}
{\sum_k\exp[-E_k^{\mathrm{geo}}(c)/\tau]}.
\]

Prototype initialization uses spherical k-means on training contexts without angle labels. Bandwidth initialization uses within-cluster distances. Prototypes and bandwidths remain trainable, with prototype projection back to the unit sphere after each optimizer step.

## 5. Connection to the full Energy-Guided Router

The long-term MMALS energy is

\[
E_h(c,m,g,s_h)=
\alpha E_h^{\mathrm{geo}}(c)
+\beta E_h^{\mathrm{host}}(s_h)
+\gamma E_h^{\mathrm{memory}}(m)
+\delta E_h^{\mathrm{cost}}(s_h)
+\eta E_h^{\mathrm{stability}}(m,s_h)
+\zeta E_h^{\mathrm{goal}}(g).
\]

v1.1.0 implements only `E_geo`. Later G2 versions add host uncertainty, saturation, cost, memory risk, stability, and goal conditioning. Reinforcement learning and forward–backward control then optimize future consequences of route choices.

## 6. Common routing-phase objective

Because context is frozen, all primary treatments use the same objective:

\[
\mathcal L
=
\mathcal L_{\mathrm{CE}}
+\lambda_A\mathcal L_{\mathrm{anchor}}
+\lambda_B\mathcal L_{\mathrm{balance}}
+\lambda_D\mathcal L_{\mathrm{host-div}}.
\]

Usage balancing is

\[
\mathcal L_{\mathrm{balance}}
=
\sum_{h=1}^H
\left(\mathbb E_x[r_h(x)]-\frac1H\right)^2.
\]

No angle-supervised route-geometry loss is used in the primary comparison. This isolates structural mediation from direct target imposition.

## 7. Nominal route geometry

Historical comparability uses the root-simplex chord:

\[
d_R(r_a,r_b)
=
\frac{\|\sqrt{r_a}-\sqrt{r_b}\|_2}{\sqrt2}.
\]

Report:

- source-level distance-order Spearman correlation;
- normalized stress;
- dense held-out interpolation order;
- route entropy and usage balance;
- local transition smoothness;
- per-seed and source-bootstrap effects.

## 8. Functional route geometry

A coordinate-wise route metric assumes all host indices are equally different. v1.1.0 builds a host-function cost matrix:

\[
v_h(x)=g_h(z_0(x)),
\]

\[
C_{hk}
=
\mathbb E_{x\in\mathcal D_{\mathrm{metric}}}
\left[
\frac{\|v_h(x)-v_k(x)\|_2^2}{d_M}
\right].
\]

`C` is symmetrized and normalized by its nonzero median. The functional distance between routes is entropic optimal transport:

\[
W_C^\varepsilon(r_a,r_b)
=
\min_{\Pi\ge0}
\langle \Pi,C\rangle
+\varepsilon\operatorname{KL}(\Pi\|r_ar_b^\top)
\]

subject to

\[
\Pi\mathbf 1=r_a,
\qquad
\Pi^\top\mathbf 1=r_b.
\]

This metric is evaluation-only in v1.1.0. It is not optimized, avoiding circular evidence.

A supplementary ablation cost may be evaluated:

\[
C^{\mathrm{abl}}_{hk}
=
\mathbb E_x|\Delta\ell_h(x)-\Delta\ell_k(x)|.
\]

## 9. Low-capacity mediation probe

Fit a low-capacity map from context to root-route coordinates:

\[
\widehat q=Ac+b,
\qquad
\widehat r
=
\frac{[\widehat q]_+^2}
{\sum_h[\widehat q_h]_+^2+\varepsilon}.
\]

Train on designated source identities and trained angles. Evaluate on held-out identities and dense unseen angles. Report:

- root-route `R²`;
- root-chord error;
- functional transport error;
- angle-shuffled control;
- tangent-removed and orthogonal-context controls.

High in-sample reconstruction is not sufficient.

## 10. Differential and finite causal mediation

Estimate a local unit tangent `t(c)` associated with increasing rotation from a fit source partition. Construct matched orthogonal directions `v_j(c)`.

The root-route Jacobian is

\[
J_q(c)=\frac{\partial\sqrt{r(c)}}{\partial c}.
\]

Define

\[
S_t(c)=\|J_q(c)t(c)\|_2,
\qquad
S_\perp(c)=\frac1J\sum_j\|J_q(c)v_j(c)\|_2,
\]

\[
\mathrm{DMR}
=
\frac{\mathbb E[S_t]}
{\mathbb E[S_\perp]+\varepsilon}.
\]

Finite interventions are

\[
c_t^\pm=\operatorname{normalize}(c\pm\epsilon t),
\qquad
c_{\perp,j}=\operatorname{normalize}(c+\epsilon v_j).
\]

Report nominal and functional causal-specificity ratios:

\[
\mathrm{CSR}_{\mathrm{nom}}
=
\frac{\mathbb E[d_R(r(c_t^+),r(c))]}
{\mathbb E_j[d_R(r(c_{\perp,j}),r(c))]+\varepsilon},
\]

\[
\mathrm{CSR}_{\mathrm{func}}
=
\frac{\mathbb E[W_C^\varepsilon(r(c_t^+),r(c))]}
{\mathbb E_j[W_C^\varepsilon(r(c_{\perp,j}),r(c))]+\varepsilon}.
\]

Also report signed consistency between positive and negative tangent moves, prediction identity preservation, and true-class log-probability change.

## 11. Host ecology measurements

Host territory across factor values is

\[
A_h(u)=\mathbb E_s[r_h(c_{s,u})].
\]

Normalize

\[
p_h(u)=\frac{A_h(u)}{\sum_{u'}A_h(u')+\varepsilon}.
\]

Specialization is

\[
\operatorname{Spec}_h
=1-\frac{H(p_h)}{\log|U|}.
\]

Territory overlap is

\[
O_{hk}=\sum_u\min(p_h(u),p_k(u)).
\]

Factor-specific host ablation is

\[
\Delta\operatorname{Acc}_h(u)
=
\operatorname{Acc}(u)-\operatorname{Acc}_{-h}(u).
\]

Report territory curves, specialization, overlap, functional cost, route entropy, ablation profiles, top-host ablation, random-host ablation, and resilience under removal. Specialization must be functional, not only route-mass differentiation.

## 12. Primary experimental matrix

For seeds `[0,1,2,3,4]`:

- fixed sensory and context checkpoints;
- four hosts;
- identical host and classifier initial states per seed;
- identical continual curriculum `[-60,-30,0,60,30]`;
- dense evaluation `[-75,-60,-45,-30,-15,0,15,30,45,60,75]`;
- matched forward images and optimizer steps;
- identical anchor and balance schedules;
- source-disjoint metric, probe, and causal partitions.

Primary contrasts:

- `R2 prototype-energy - R0 MLP`;
- `R2 prototype-energy - R1 linear`;
- `R1 linear - R0 MLP`.

A ten-seed qualification run is allowed only after the five-seed pilot passes the functional mediation gate.

## 13. Statistics

Within each seed, source identity is the bootstrap unit. Across seeds, report paired mean effect, Student-t 95% confidence interval, seed standard deviation, and positive-seed fraction.

Angle-wise secondary tests use false-discovery-rate correction. Partitions used for tangent fitting, prototype diagnostics, host cost construction, and final causal evaluation must be disjoint where their reuse would leak information.

## 14. Candidate gates

| Gate | Requirement |
|---|---|
| Context preservation | frozen geometry and held-out decoding remain within numerical tolerance |
| Nominal route mediation | R2–R0 route-order seed CI lower bound > 0 and at least 4/5 positive seeds |
| Functional route mediation | R2–R0 functional-order or tangent-transport CI lower bound > 0 |
| Causal specificity | source lower bound of functional CSR > 1 and seed mean target > 1.5 |
| Probe generalization | held-out error beats shuffled and orthogonal controls |
| Host ecology | specialization or factor-dependent ablation increases without route collapse |
| Identity preservation | source lower bound ≥ 0.95 |
| Operational non-degradation | accuracy and forgetting remain within a preregistered 1 percentage-point equivalence margin |

## 15. Falsification logic

- If R2 improves neither nominal nor functional route mediation, structural prototype routing fails to build the bridge.
- If functional geometry improves while nominal geometry does not, the previous simplex metric was incomplete.
- If route mediation improves but host ablation and synthesis do not, the bridge stops at routing.
- If host effects improve but prediction and retention remain neutral, v1.1.0 reaches functional but not operational geometry.
- If accuracy improves without mediation evidence, the result is useful but does not validate the geometric mechanism.

## 16. Preregistered secondary arm

Only after the architecture-only result is reported, a separate mediation-trained arm may use

\[
\mathcal L_{\mathrm{med}}
=
\operatorname{ReLU}
\left(
 m_{\mathrm{med}}
 -d_{\mathrm{func}}(r(c+\epsilon t),r(c))
 +d_{\mathrm{func}}(r(c+\epsilon v_\perp),r(c))
\right).
\]

This must remain a separate claim: it asks whether mediation can be trained directly, not whether it emerges from architecture.

## 17. Required artifacts

Every seed and method must export:

- checkpoint and initial-state hashes;
- compute summaries;
- nominal and functional geometry metrics;
- host cost matrices;
- mediation probes and controls;
- Jacobian and finite causal results;
- host territory and ablation tables;
- accuracy, NLL, forgetting, and retention;
- source-bootstrap and seed aggregate effects;
- gate summary, run manifest, environment capture, and claim manifest.

## 18. Non-claims

v1.1.0 does not by itself claim:

- operational superiority;
- final host specialization;
- memory transport or backward transfer;
- distributed/mycelial routing;
- multi-objective energy control;
- reinforcement-learning control;
- quantum or quantum-inspired advantage.

## 19. Roadmap after v1.1.0

- **G1.2 Host ecology:** heterogeneous roles, overlap, redundancy, ablation, recovery.
- **G1.3 Memory transport:** preserve or controllably move geometric and functional relations through continual updates.
- **G2 Full Energy-Guided Router:** geometry + uncertainty + cost + memory + stability + goal.
- **G2.1 Bottom-up host feedback:** hosts report confidence, novelty, saturation, capacity, and error.
- **G2.2 RL / predictive control:** optimize future consequences and reachable goal states.
- **G3 Phase-aware / quantum-inspired routing:** amplitudes, phases, interference, and density matrices only after functional geometry is established.
