# v1.1.3 gradient-scale calibration workflow

1. Keep the canonical YAML at `status: pending`, `pilot_lock: false`, and `calibrated_functional_transport_weight: null`.
2. In Colab, set `G1_PROFILE=development_calibration` before running the notebook.
3. Execute through the calibration section.
4. Archive:
   - `results/v1_1_3_calibration/gradient_norm_probes.csv`;
   - `results/v1_1_3_calibration/gradient_scale_calibration.json`;
   - `results/v1_1_3_calibration/gradient_scale_calibration.sha256`.
5. Copy the proposed coefficient and SHA-256 into `configs/rotated_mnist_g1_v113.yaml`.
6. Set `gradient_scale_calibration.status: locked` and `pilot_lock: true`.
7. Commit the YAML and calibration report before running `G1_PROFILE=pilot`.
8. Do not change coefficients after observing pilot outcomes.

The route-anchor weight remains 0.5. The functional-transport coefficient is clipped to [0.05, 2.0].
