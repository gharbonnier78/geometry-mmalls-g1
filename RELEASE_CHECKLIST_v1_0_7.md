# TPUT ↔ Geometry-MMALS G1 notation bridge

This file prevents the operational TPUT specification and the G1 geometry paper from looking like two unrelated mathematical systems.

## Different levels, same stack

| Layer | TPUT object | G1 object | Interpretation |
|---|---|---|---|
| input representation | `z` | `z0 = P(x)` | frozen or controlled sensory representation |
| context | `c` or inferred context state | `c = q_phi(z0)` | learned context coordinate / chart |
| route | `r` | `r in Delta^(H-1)` | distribution over hosts on the simplex |
| host function | host/action module | `g_h(z0)` | functional transformation field |
| synthesis | route-selected output | `z_M = sum_h r_h g_h(z0)` | MMALS synthesized representation |
| memory | `m = (m_rec, m_syn)` | reconstructive + synthetic memory | trace replay versus compiled reuse |
| objective | `g` | goal vector `(accuracy, retention, cost, drift, specialization)` | deployment or experiment goal |
| audit state | trace/evidence vector | `a(x,t)` | external control geometry, not internal geometry |

## Energy terms versus G1 losses

TPUT writes the route energy as a deployment/control functional:

```text
E_theta(r; z, m, g) = fit + mem + ret + cost + drift + spec + audit
```

G1 writes a training/evidence objective:

```text
L_G1 = CE + distill + route_geo + stress + far + transport + host_div + carbon
```

They are related but not identical:

| TPUT energy term | Closest G1 term | Difference |
|---|---|---|
| fit | CE / NLL / calibration | task performance at train/eval time |
| mem | reconstructive fidelity + synthetic memory reuse | G1 measures trace replay and compiled memory explicitly |
| ret | forgetting / transport / old-region preservation | G1 separates representation transport from accuracy forgetting |
| cost | carbon / active FLOPs / memory bytes | same control goal, lower priority in G1 proof ladder |
| drift | stress drift / Procrustes drift / Hydro diagnostics | G1 distinguishes geometric drift from deployment drift |
| spec | host_div, contribution gain, ablation locality, CKA | specialization is ecological, not route entropy alone |
| audit | trace completeness, m_rec reconstruction | G1 keeps audit as evidence support, not as geometry proof |

## Practical rule

Use TPUT notation when discussing **policy selection and deployment control**. Use G1 notation when discussing **whether an internal geometry exists and is useful**. A single experiment may export both: internal tensors for G1 and audit traces for TPUT/RC2O.
