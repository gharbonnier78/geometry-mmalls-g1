import json
from pathlib import Path
import zipfile

import pandas as pd
import pytest
import yaml

from geometry_mmalls.verification import safe_extract_zip, verify_evidence_bundle, write_verification_outputs


def test_safe_extract_rejects_path_traversal(tmp_path):
    archive = tmp_path / "bad.zip"
    with zipfile.ZipFile(archive, "w") as handle:
        handle.writestr("../escape.txt", "bad")
    with pytest.raises(ValueError):
        safe_extract_zip(archive, tmp_path / "out")


def test_verifier_generates_standard_outputs(tmp_path):
    result_root = tmp_path / "fixture"
    result_dir = result_root / "results" / "v_test"
    result_dir.mkdir(parents=True)
    pd.DataFrame([
        {"model_seed": 0, "method": "a", "total_forward_images": 10, "total_optimizer_steps": 2},
        {"model_seed": 0, "method": "b", "total_forward_images": 10, "total_optimizer_steps": 2},
    ]).to_csv(result_dir / "compute_summary.csv", index=False)
    pd.DataFrame([{"gate": "C0_equal_compute", "passed": True, "status": "protocol_integrity"}]).to_csv(result_dir / "gate_summary.csv", index=False)
    pd.DataFrame([{"contrast": "b_vs_a", "partition": "heldout", "geometry": "nominal", "metric": "rho", "seed_ci_low": 0.1, "seed_ci_high": 0.2}]).to_csv(result_dir / "aggregate_seed_effects.csv", index=False)
    pd.DataFrame([{"method": "a", "metric": "accuracy", "mean": 0.5}]).to_csv(result_dir / "aggregate_method_summary.csv", index=False)
    pd.DataFrame([{"model_seed": 0, "method": "a"}]).to_csv(result_dir / "causal_seed_summary.csv", index=False)
    pd.DataFrame([{"model_seed": 0, "method": "a"}]).to_csv(result_dir / "route_swap_effects.csv", index=False)
    pd.DataFrame([{"method": "b", "max_abs_context_delta": 0.0}]).to_csv(result_dir / "context_preservation.csv", index=False)
    (result_dir / "run_manifest.json").write_text(json.dumps({
        "notebook_version": "test", "build_revision": "test", "model_seeds": [0],
        "split_manifest": {"a_sha256": "a", "b_sha256": "b"},
    }), encoding="utf-8")
    (result_dir / "claim_manifest.json").write_text(json.dumps({"version": "test", "status": "executed", "non_claims": []}), encoding="utf-8")
    archive = tmp_path / "results.zip"
    with zipfile.ZipFile(archive, "w") as handle:
        for path in result_root.rglob("*"):
            if path.is_file():
                handle.write(path, path.relative_to(result_root))

    from pypdf import PdfWriter
    pdf = tmp_path / "run.pdf"
    writer = PdfWriter(); writer.add_blank_page(width=200, height=200)
    with pdf.open("wb") as stream: writer.write(stream)

    metric = tmp_path / "metrics.yaml"; protocol = tmp_path / "protocol.yaml"; claims = tmp_path / "claims.yaml"
    metric.write_text(yaml.safe_dump({"schema_version": "0.2.0", "metrics": [{"id": "COMPUTE_SUMMARY", "file_patterns": ["**/compute_summary.csv"], "required_columns": ["model_seed", "method", "total_forward_images", "total_optimizer_steps"]}]}), encoding="utf-8")
    protocol.write_text(yaml.safe_dump({"schema_version": "0.2.0", "minimum_model_seeds": 1, "rules": [{"id": "MATCHED_COMPUTE", "severity": "critical"}]}), encoding="utf-8")
    claims.write_text(yaml.safe_dump({"schema_version": "0.2.0", "claims": [{"id": "TEST", "statement": "fixture", "required_metrics": ["COMPUTE_SUMMARY"], "required_protocol_rules": ["MATCHED_COMPUTE"]}]}), encoding="utf-8")

    bundle = verify_evidence_bundle(experiment_id="fixture", execution_pdf=pdf, results_zip=archive, metric_definitions=metric, protocol_rules=protocol, claim_rules=claims)
    outputs = write_verification_outputs(bundle, tmp_path / "reports")
    for value in outputs.values():
        assert Path(value).exists()


def test_non_tested_experiment_gate_maps_to_not_tested(tmp_path):
    result_root = tmp_path / "fixture"
    result_dir = result_root / "results" / "v_test"
    result_dir.mkdir(parents=True)
    pd.DataFrame([
        {
            "gate": "C3_mature_host_specialization",
            "passed": False,
            "status": "not_tested_hosts_frozen",
        }
    ]).to_csv(result_dir / "gate_summary.csv", index=False)
    (result_dir / "run_manifest.json").write_text(
        json.dumps({
            "notebook_version": "test",
            "build_revision": "test",
            "model_seeds": [0],
            "split_manifest": {"a_sha256": "a", "b_sha256": "b"},
        }),
        encoding="utf-8",
    )
    (result_dir / "claim_manifest.json").write_text(
        json.dumps({"version": "test", "status": "executed", "non_claims": []}),
        encoding="utf-8",
    )
    archive = tmp_path / "results.zip"
    with zipfile.ZipFile(archive, "w") as handle:
        for path in result_root.rglob("*"):
            if path.is_file():
                handle.write(path, path.relative_to(result_root))

    from pypdf import PdfWriter
    pdf = tmp_path / "run.pdf"
    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    with pdf.open("wb") as stream:
        writer.write(stream)

    metric = tmp_path / "metrics.yaml"
    protocol = tmp_path / "protocol.yaml"
    claims = tmp_path / "claims.yaml"
    metric.write_text(yaml.safe_dump({"metrics": []}), encoding="utf-8")
    protocol.write_text(
        yaml.safe_dump({
            "minimum_model_seeds": 1,
            "rules": [],
        }),
        encoding="utf-8",
    )
    claims.write_text(
        yaml.safe_dump({
            "claims": [{
                "id": "HOST_SPECIALIZATION",
                "statement": "fixture",
                "required_experiment_gates": ["C3_mature_host_specialization"],
            }]
        }),
        encoding="utf-8",
    )

    bundle = verify_evidence_bundle(
        experiment_id="fixture",
        execution_pdf=pdf,
        results_zip=archive,
        metric_definitions=metric,
        protocol_rules=protocol,
        claim_rules=claims,
    )
    claim = bundle["claim_report"]["claims"][0]
    assert claim["status"] == "NOT_TESTED"
