# Geometry-MMALS G1 v1.0.6 -> v1.0.7

## Scientific trigger

The executed v1.0.6 run showed that paired geometry regularization improved route ordering but not prediction, while the standard router depended mainly on direct sensory access. Context zeroing and shuffling had nearly no effect; router `z0` removal produced a much larger shift.

## Core correction

v1.0.7 tests context mediation with a hard information bottleneck. The context-bottleneck router accepts only inferred context. A capacity-matched sensory-only router controls for route capacity and for geometry already available in perception.

## Deviation from the attached migration draft

The draft proposed a stop-gradient variant that detached `z0` but continued to concatenate `z0` into the standard router. Because the sensory encoder is already frozen, this does not stop router weights from using `z0`. It is therefore not a valid test of the shortcut. The release replaces it with explicit information-path controls.

## Tracked changes

1. CHG-107-01 - Added `ContextBottleneckRouter`.
2. CHG-107-02 - Added `SensoryBottleneckRouter`.
3. CHG-107-03 - Removed the non-diagnostic stop-gradient control.
4. CHG-107-04 - Reduced core methods to six targeted variants.
5. CHG-107-05 - Added bottleneck and sensory geometry contrasts.
6. CHG-107-06 - Added extended mediation table and `context_is_primary`.
7. CHG-107-07 - Added route-policy capacity audit.
8. CHG-107-08 - Kept C1, C2 and extrapolation partitions separate.
9. CHG-107-09 - Limited counterbalanced curricula to the primary bottleneck method.
10. CHG-107-10 - Added reviewer-report and LaTeX-source archive references.
11. CHG-107-11 - Added package/source/version integrity checks.
12. CHG-107-12 - Preserved C0-only claim discipline.

## Primary falsification condition

The architectural-shortcut hypothesis is supported only if all of the following hold:

- `context_bottleneck_geo` is context-primary under intervention;
- the context-to-z0 route-shift ratio exceeds 1;
- context zeroing reduces predictive evidence more than z0 zeroing;
- `bottleneck_geo_effect` improves trained context-space order with a paired-source confidence interval above zero;
- causal specificity and identity-preservation gates are not violated.

Otherwise, context representation or supervision remains the more likely bottleneck.
