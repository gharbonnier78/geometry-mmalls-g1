# Geometry-MMALS G1 v1.1.3 C0-r1 to C0-r2

This patch implements the pre-pilot reviewer corrections without changing the scientific version or adding a new router.

## Contract corrections

- `fixed memory budget` becomes `matched remembered-source and replay-access budget`;
- M4 is not described as byte-efficient;
- the acquisition snapshot order is executable and exported;
- the functional host cost and both Sinkhorn layers are fully specified;
- the compiled baseline is one trace-matched isotropic Gaussian;
- reconstruction hashes are audit-only and metric acceptance is preregistered;
- M3-versus-M2 forgetting is reported separately from endpoint functional drift.

## Numerical interpretation correction

The path quantity is renamed `path_to_endpoint_regularized_cost_ratio`. Raw entropic OT is a regularized dissimilarity, so the ratio is not a geodesic excess and is not guaranteed to be at least one.

## Calibration lock

Before the pilot, run `G1_PROFILE=development_calibration`. The notebook estimates median unweighted router-gradient norms and proposes

`lambda_F = clip(lambda_R * median_grad_R / median_grad_F, 0.05, 2.0)`.

Commit the selected value and calibration report SHA-256 to the YAML, set `status: locked` and `pilot_lock: true`, then run the five-seed pilot. No adaptive rescaling is allowed during the pilot.

## Program-level stopping rule

v1.1.3 is the final fully frozen-host experiment. The next scientific regime tests controlled host adaptation irrespective of the v1.1.3 outcome.
