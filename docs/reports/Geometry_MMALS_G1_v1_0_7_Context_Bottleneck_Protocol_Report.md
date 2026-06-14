# Geometry-MMALS G1 v1.0.7
## Context-Bottleneck Mediation Protocol

**Author:** Guillaume Harbonnier  
**Date:** 2026-06-14  
**Scientific status:** C0 protocol implementation only; C1-C6 remain unqualified.

## Purpose

The v1.0.6 development run established a reproducible route-ordering effect under paired geometry regularization, but it also showed that the standard router depended overwhelmingly on the direct sensory representation `z0`. Context zeroing and shuffling had negligible effects, while suppressing `z0` at the router caused a substantial route and accuracy change. The unresolved question is whether context mediation failed because the standard router took an architectural shortcut or because the inferred context was itself insufficient.

v1.0.7 introduces a hard context bottleneck. The dedicated router never receives `z0`; any sample-specific route must pass through the inferred context. A capacity-matched sensory-only bottleneck provides the decisive control.

## Correction to the attached migration proposal

The attached migration note correctly identifies the next scientific direction. One proposed control, however, is not diagnostic: detaching `z0` before the context network while still concatenating `z0` into the standard router does not prevent the router parameters from exploiting `z0`. The sensory encoder is already frozen, so this stop-gradient mainly changes nothing relevant to the shortcut hypothesis.

v1.0.7 replaces that control with a capacity-matched sensory-only router. This isolates the information path rather than only the gradient path.

## Six equal-compute variants

| Method | Router information | Geometry | Retention anchor | Purpose |
|---|---|---:|---:|---|
| `standard_anchor_no_geo` | `z0 + context` | no | 0.10 | v1.0.6 operational reference |
| `uniform_static_anchor` | none | no | 0.10 | static floor |
| `context_bottleneck_no_geo` | context only | no | 0.10 | hard bottleneck baseline |
| `context_bottleneck_geo` | context only | yes | 0.10 | primary treatment |
| `sensory_bottleneck_no_geo` | `z0` only | no | 0.10 | capacity-matched shortcut control |
| `sensory_bottleneck_geo` | `z0` only | yes | 0.10 | tests whether geometry is recoverable directly from perception |

All six methods use the same initial MMALS state, source order, multi-angle tensors, image-forward count, optimizer-step count, curriculum, and retention-anchor weight.

## Primary contrasts

1. **Bottleneck geometry effect:** `context_bottleneck_geo - context_bottleneck_no_geo`.
2. **Bottleneck versus standard:** `context_bottleneck_geo - standard_anchor_no_geo`.
3. **Sensory geometry effect:** `sensory_bottleneck_geo - sensory_bottleneck_no_geo`.
4. **Context versus sensory geometry:** `context_bottleneck_geo - sensory_bottleneck_geo`.
5. **Bottleneck versus static floor:** `context_bottleneck_geo - uniform_static_anchor`.

The primary representational success condition is a positive paired-source change in trained context-space order for the bottleneck geometry effect, with a confidence interval above zero. The mediation success condition requires context interventions to affect route and prediction more than `z0` interventions.

## Mediation diagnostics

For every method, the notebook exports:

- context-zeroing and context-shuffling route shifts;
- `z0`-zeroing and `z0`-shuffling route shifts;
- prediction changes under each intervention;
- context-to-`z0` route-shift ratio;
- context and `z0` accuracy drops;
- a reviewer-readable `context_is_primary` flag.

For a true context bottleneck, `z0` interventions at the router should have no direct effect, while context interventions should produce a measurable change. This is necessary but not sufficient: geometry and causal specificity must also improve.

## Evidence partitions

The notebook keeps three distinct partitions:

- **C1 trained geometry:** `-60, -30, 0, 30, 60` degrees;
- **C2 interpolation:** `-45, -15, 15, 45` degrees;
- **extrapolation evidence:** `-75, 75` degrees.

No held-out angle enters training, checkpoint selection, or the paired geometry loss.

## Causal gate

The signed causal probe is retained for standard, context-bottleneck, and sensory-bottleneck adaptive policies. A candidate C4 result requires all of:

- signed orientation consistent with intervention direction;
- monotonic effect magnitude;
- mean causal specificity ratio above 1.5;
- bounded class-evidence change;
- later multi-seed and source-bootstrap confirmation.

## Curriculum control

The primary curriculum remains `cb_a` for direct comparison with v1.0.6. Optional same-final-task counterbalanced reruns are restricted to `context_bottleneck_geo`, reducing compute while testing whether a context-mediated route remains curriculum-sensitive.

## Reviewer scenarios

### Architectural-shortcut success

Context is primary under the bottleneck and geometry improves context order with a positive lower confidence bound. The next step is a regularized soft bottleneck that reintroduces sensory information only under evidence of benefit.

### Representational failure

The bottleneck is context-dependent by construction, but context geometry and causal specificity remain weak. The context encoder or its supervision must be redesigned before G2 energy-guided routing.

### Geometry-function trade-off

Context geometry improves but predictive accuracy drops relative to the sensory-only control. This shows that the context contains partial structure but is not yet sufficient for host selection.

## Archive integration

The v1.0.7 GitHub package includes:

- the new Colab notebook;
- this protocol report in PDF and Markdown;
- the v1.0.6 to v1.0.7 migration and tracked-change documents;
- the previously generated 18-page reviewer status report;
- the complete reviewer-report LaTeX source tree and original LaTeX ZIP;
- updated package source, configuration, tests, release checklist, and checksums.

## Claim boundary

v1.0.7 is a falsifiable experiment, not a positive result. Successful execution can support C0 protocol integrity only. Any claim that the context bottleneck solves mediation, improves geometry, or produces operational benefit requires the exported evidence and multi-seed replication.
