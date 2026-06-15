# MMALS Metric, Protocol and Claim Verification Stack v0.2

This layer is independent of training and routing. It reads an execution PDF,
a results ZIP, and versioned YAML definitions, then emits the same six files:

- `metric_report.json`
- `protocol_report.json`
- `claim_report.json`
- `evidence_bundle.json`
- `verification_summary.md`
- `verification_gate_summary.csv`

Supported statuses are `PASS`, `PARTIAL`, `FAIL`, and `NOT_TESTED`.

The Colab notebook accepts reusable environment variables:

- `MMALS_EXPERIMENT_ID`
- `MMALS_EXECUTION_PDF`
- `MMALS_RESULTS_ZIP`
- `MMALS_VERIFICATION_OUTPUT`

Critical protocol failures stop positive claim validation, even when performance
metrics are favorable.
