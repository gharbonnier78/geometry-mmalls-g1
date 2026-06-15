"""Reusable Metric, Protocol and Claim Verification engine.

The engine is notebook-independent. It parses an execution PDF and a result ZIP,
applies versioned YAML rules, and emits stable PASS/PARTIAL/FAIL/NOT_TESTED
reports.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
from typing import Any, Iterable
import zipfile

import pandas as pd
import yaml

STATUSES = {"PASS", "PARTIAL", "FAIL", "NOT_TESTED"}


@dataclass
class GateResult:
    id: str
    status: str
    message: str
    evidence: dict[str, Any]

    def __post_init__(self) -> None:
        if self.status not in STATUSES:
            raise ValueError(f"Unsupported verification status: {self.status}")


def sha256_file(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_yaml(path: str | Path) -> dict[str, Any]:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}


def safe_extract_zip(zip_path: str | Path, destination: str | Path) -> list[str]:
    destination = Path(destination).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    extracted: list[str] = []
    with zipfile.ZipFile(zip_path) as archive:
        for info in archive.infolist():
            member = PurePosixPath(info.filename)
            if member.is_absolute() or ".." in member.parts:
                raise ValueError(f"Unsafe ZIP member: {info.filename}")
            target = (destination / Path(*member.parts)).resolve()
            if destination not in target.parents and target != destination:
                raise ValueError(f"ZIP member escapes destination: {info.filename}")
            if info.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(info) as source, target.open("wb") as sink:
                    shutil.copyfileobj(source, sink)
                extracted.append(str(target))
    return extracted


def pdf_report(pdf_path: str | Path) -> dict[str, Any]:
    """Parse an execution PDF.

    ``pypdf`` is loaded lazily so the MMALS core package remains importable
    in training notebooks that do not use the independent verifier.
    """
    try:
        from pypdf import PdfReader
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "The Verification Stack requires the optional dependency 'pypdf'. "
            "Install it with: pip install 'pypdf>=4.0'"
        ) from exc

    path = Path(pdf_path)
    reader = PdfReader(str(path))
    pages = [(page.extract_text() or "") for page in reader.pages]
    text = "\n".join(pages)
    completed = re.search(r"Completed seeds:\s*\[[^\]]+\]", text)
    return {
        "path": str(path),
        "sha256": sha256_file(path),
        "page_count": len(reader.pages),
        "metadata": {str(k): str(v) for k, v in (reader.metadata or {}).items()},
        "text_length": len(text),
        "contains_traceback": "Traceback (most recent call last)" in text,
        "contains_completed_seeds": completed is not None,
        "contains_export_marker": "Exported" in text and "evidence" in text,
        "completed_seed_line": completed.group(0) if completed else None,
        "text": text,
    }


def inventory(root: str | Path) -> list[dict[str, Any]]:
    root = Path(root)
    return [
        {
            "relative_path": path.relative_to(root).as_posix(),
            "size_bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in sorted(root.rglob("*")) if path.is_file()
    ]


def find_first(root: Path, patterns: Iterable[str]) -> Path | None:
    for pattern in patterns:
        matches = sorted(root.glob(pattern))
        if matches:
            return matches[0]
    return None


def resolve_results_root(extracted_root: Path, experiment_id: str) -> Path:
    """Select the intended result directory from a multi-version archive.

    Geometry-MMALS execution archives contain historical results and paper
    copies. Searching the entire archive can therefore select an older
    manifest. The experiment id is used to scope all metric and protocol
    searches to the requested ``results/vX_Y_Z`` directory.
    """
    match = re.search(r"(v\d+(?:_\d+)+)", str(experiment_id))
    version_token = match.group(1) if match else None
    candidates: list[Path] = []
    if version_token:
        candidates.extend(sorted(extracted_root.glob(f"**/results/{version_token}")))
    candidates.extend(sorted(extracted_root.glob("**/results")))
    for candidate in candidates:
        if candidate.is_dir() and (candidate / "run_manifest.json").exists():
            return candidate
    # Last resort for simple result-only archives.
    manifests = sorted(extracted_root.glob("**/run_manifest.json"))
    if len(manifests) == 1:
        return manifests[0].parent
    return extracted_root


def summarize_csv(path: Path) -> dict[str, Any]:
    frame = pd.read_csv(path)
    numeric = frame.select_dtypes(include="number")
    result: dict[str, Any] = {
        "path": str(path),
        "sha256": sha256_file(path),
        "rows": int(len(frame)),
        "columns": list(map(str, frame.columns)),
        "null_cells": int(frame.isna().sum().sum()),
    }
    if not numeric.empty:
        result["numeric_mean"] = {str(k): float(v) for k, v in numeric.mean().items()}
        result["numeric_min"] = {str(k): float(v) for k, v in numeric.min().items()}
        result["numeric_max"] = {str(k): float(v) for k, v in numeric.max().items()}
    return result


def metric_report(extracted_root: Path, definitions: dict[str, Any]) -> dict[str, Any]:
    results = []
    for metric in definitions.get("metrics", []):
        metric_id = metric.get("id") or metric.get("name")
        path = find_first(extracted_root, metric.get("file_patterns", []))
        if path is None:
            results.append(asdict(GateResult(metric_id, "NOT_TESTED", "No matching artifact found.", {"patterns": metric.get("file_patterns", [])})))
            continue
        if path.suffix.lower() == ".csv":
            summary = summarize_csv(path)
            missing = [c for c in metric.get("required_columns", []) if c not in summary["columns"]]
            status = "PASS" if not missing and summary["rows"] > 0 else "FAIL"
            results.append(asdict(GateResult(metric_id, status, "CSV structure checked.", summary | {"missing_columns": missing})))
        elif path.suffix.lower() == ".json":
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                payload = {}
            missing = [k for k in metric.get("required_keys", []) if k not in payload]
            status = "PASS" if payload and not missing else "FAIL"
            results.append(asdict(GateResult(metric_id, status, "JSON structure checked.", {"path": str(path), "sha256": sha256_file(path), "missing_keys": missing, "top_level_keys": sorted(payload)})))
        else:
            results.append(asdict(GateResult(metric_id, "PASS", "Artifact is present.", {"path": str(path), "sha256": sha256_file(path)})))
    return {"schema_version": definitions.get("schema_version", "0.2.0"), "metrics": results}


def _json(root: Path, patterns: list[str]) -> tuple[Path | None, dict[str, Any]]:
    path = find_first(root, patterns)
    if path is None:
        return None, {}
    try:
        return path, json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return path, {}


def _csv(root: Path, patterns: list[str]) -> tuple[Path | None, pd.DataFrame | None]:
    path = find_first(root, patterns)
    if path is None:
        return None, None
    try:
        return path, pd.read_csv(path)
    except Exception:
        return path, None


def protocol_report(extracted_root: Path, pdf: dict[str, Any], rules: dict[str, Any], archive_inventory: list[dict[str, Any]], profile: dict[str, Any] | None = None) -> dict[str, Any]:
    run_path, run = _json(extracted_root, ["**/run_manifest.json"])
    claim_path, claim = _json(extracted_root, ["**/claim_manifest.json"])
    compute_path, compute = _csv(extracted_root, ["**/compute_summary.csv"])
    context_path, context = _csv(extracted_root, ["**/preservation.csv", "**/context_preservation.csv"])
    gate_path, gate = _csv(extracted_root, ["**/gate_summary.csv"])

    banned = rules.get("archive_hygiene", {}).get("banned_path_fragments", ["/.git/", "__pycache__", ".pytest_cache", ".pyc"])
    dirty = [row["relative_path"] for row in archive_inventory if any(item in row["relative_path"] for item in banned)]
    minimum_seeds = int(rules.get("minimum_model_seeds", 1))
    seed_count = len(run.get("model_seeds", [])) if run else 0

    matched = False
    if compute is not None and {"model_seed", "method", "total_forward_images", "total_optimizer_steps"}.issubset(compute.columns):
        matched = all(
            block.total_forward_images.nunique() == 1 and block.total_optimizer_steps.nunique() == 1
            for _, block in compute.groupby("model_seed")
        )

    frozen = False
    frozen_evidence: dict[str, Any] = {"path": str(context_path) if context_path else None}
    if context is not None and "max_abs_context_delta" in context.columns:
        value = float(context.max_abs_context_delta.max())
        frozen = value <= float(rules.get("context_tolerance", 1e-6))
        frozen_evidence["max_abs_context_delta"] = value

    split_manifest = run.get("split_manifest", {}) if run else {}
    hashes = [value for key, value in split_manifest.items() if key.endswith("sha256")]
    split_ok = bool(hashes) and len(hashes) == len(set(hashes))

    stale = False
    if claim:
        status = str(claim.get("status", "")).lower()
        stale = pdf["contains_completed_seeds"] and any(token in status for token in ["pending execution", "not yet executed"])

    builtins: dict[str, GateResult] = {
        "ZIP_SAFE_PATHS": GateResult("ZIP_SAFE_PATHS", "PASS", "ZIP extraction completed without unsafe paths.", {}),
        "RESULTS_PRESENT": GateResult("RESULTS_PRESENT", "PASS" if run_path or gate_path else "FAIL", "A results manifest or gate summary is present.", {"run_manifest": str(run_path) if run_path else None, "gate_summary": str(gate_path) if gate_path else None}),
        "RUN_MANIFEST": GateResult("RUN_MANIFEST", "PASS" if run else "FAIL", "Run manifest parsed." if run else "Run manifest missing or invalid.", {"path": str(run_path) if run_path else None, "keys": sorted(run)}),
        "CLAIM_MANIFEST": GateResult("CLAIM_MANIFEST", "PASS" if claim else "FAIL", "Claim manifest parsed." if claim else "Claim manifest missing or invalid.", {"path": str(claim_path) if claim_path else None, "keys": sorted(claim)}),
        "SEED_COUNT": GateResult("SEED_COUNT", "PASS" if seed_count >= minimum_seeds else "FAIL", f"Detected {seed_count} model seeds; minimum is {minimum_seeds}.", {"seed_count": seed_count, "minimum": minimum_seeds}),
        "PDF_PARSE": GateResult("PDF_PARSE", "PASS" if pdf["page_count"] > 0 else "FAIL", f"Execution PDF has {pdf['page_count']} pages.", {k: v for k, v in pdf.items() if k != "text"}),
        "PDF_NO_TRACEBACK": GateResult("PDF_NO_TRACEBACK", "FAIL" if pdf["contains_traceback"] else "PASS", "No Python traceback detected." if not pdf["contains_traceback"] else "A Python traceback is present in the PDF.", {}),
        "PDF_EXECUTION_MARKERS": GateResult("PDF_EXECUTION_MARKERS", "PASS" if pdf["contains_completed_seeds"] and pdf["contains_export_marker"] else "PARTIAL", "Completed-seed and export markers checked.", {"completed_seeds": pdf["contains_completed_seeds"], "export_marker": pdf["contains_export_marker"], "line": pdf["completed_seed_line"]}),
        "ARCHIVE_HYGIENE": GateResult("ARCHIVE_HYGIENE", "PASS" if not dirty else "PARTIAL", "Archive hygiene checked.", {"dirty_count": len(dirty), "examples": dirty[:20]}),
        "MATCHED_COMPUTE": GateResult("MATCHED_COMPUTE", "PASS" if matched else ("NOT_TESTED" if compute is None else "FAIL"), "Matched compute checked.", {"path": str(compute_path) if compute_path else None}),
        "FROZEN_CONTEXT": GateResult("FROZEN_CONTEXT", "PASS" if frozen else ("NOT_TESTED" if context is None else "FAIL"), "Frozen-context audit checked.", frozen_evidence),
        "SOURCE_PARTITION_SEPARATION": GateResult("SOURCE_PARTITION_SEPARATION", "PASS" if split_ok else ("NOT_TESTED" if not hashes else "FAIL"), "Partition hashes checked for accidental identity.", {"hash_count": len(hashes), "unique_count": len(set(hashes))}),
        "CLAIM_MANIFEST_FRESHNESS": GateResult("CLAIM_MANIFEST_FRESHNESS", "FAIL" if stale else ("NOT_TESTED" if not claim else "PASS"), "Claim state compared with execution evidence.", {"claim_status": claim.get("status") if claim else None}),
    }
    if gate is not None and {"gate", "passed"}.issubset(gate.columns):
        imported: dict[str, GateResult] = {}
        for _, row in gate.iterrows():
            raw = row["passed"]
            passed = raw.strip().lower() in {"true", "1", "yes"} if isinstance(raw, str) else bool(raw)
            gate_name = str(row["gate"])
            result = GateResult(
                f"EXPERIMENT_GATE::{gate_name}",
                "PASS" if passed else "FAIL",
                f"Imported experiment gate {gate_name}.",
                {"source": str(gate_path), "status": row.get("status")},
            )
            builtins[result.id] = result
            imported[gate_name] = result
        # Version profiles may map a stable canonical claim gate to a
        # historical experiment-specific gate name.
        for canonical, aliases in (profile or {}).get("gate_aliases", {}).items():
            if isinstance(aliases, str):
                aliases = [aliases]
            matched_alias = next((alias for alias in aliases if alias in imported), None)
            if matched_alias is not None:
                source_result = imported[matched_alias]
                builtins[f"EXPERIMENT_GATE::{canonical}"] = GateResult(
                    f"EXPERIMENT_GATE::{canonical}",
                    source_result.status,
                    f"Canonical gate {canonical} mapped from {matched_alias}.",
                    source_result.evidence | {"mapped_from": matched_alias},
                )

    results = []
    for rule in rules.get("rules", []):
        result = builtins.get(rule["id"], GateResult(rule["id"], "NOT_TESTED", "No evaluator registered for this rule.", {}))
        evidence = dict(result.evidence)
        evidence["severity"] = rule.get("severity", "major")
        results.append(asdict(GateResult(result.id, result.status, result.message, evidence)))
    listed = {item["id"] for item in results}
    for key, result in builtins.items():
        if key not in listed:
            results.append(asdict(result))
    return {"schema_version": rules.get("schema_version", "0.2.0"), "rules": results}


def claim_report(metric: dict[str, Any], protocol: dict[str, Any], claims: dict[str, Any]) -> dict[str, Any]:
    metric_status = {item["id"]: item["status"] for item in metric.get("metrics", [])}
    protocol_status = {item["id"]: item["status"] for item in protocol.get("rules", [])}
    output = []
    for claim in claims.get("claims", []):
        statuses = [metric_status.get(item, "NOT_TESTED") for item in claim.get("required_metrics", [])]
        statuses += [protocol_status.get(item, "NOT_TESTED") for item in claim.get("required_protocol_rules", [])]
        statuses += [protocol_status.get(f"EXPERIMENT_GATE::{item}", "NOT_TESTED") for item in claim.get("required_experiment_gates", [])]
        if not statuses or all(item == "NOT_TESTED" for item in statuses):
            status = "NOT_TESTED"
        elif any(item == "FAIL" for item in statuses):
            status = "FAIL"
        elif any(item == "NOT_TESTED" for item in statuses):
            status = "NOT_TESTED"
        elif all(item == "PASS" for item in statuses):
            status = "PASS"
        else:
            status = "PARTIAL"
        output.append({
            "id": claim["id"],
            "statement": claim.get("statement", ""),
            "status": status,
            "required_metrics": claim.get("required_metrics", []),
            "required_protocol_rules": claim.get("required_protocol_rules", []),
            "required_experiment_gates": claim.get("required_experiment_gates", []),
            "resolved_statuses": statuses,
        })
    return {"schema_version": claims.get("schema_version", "0.2.0"), "claims": output}


def verification_summary_markdown(bundle: dict[str, Any]) -> str:
    lines = [
        "# MMALS Verification Summary", "",
        f"- Experiment: `{bundle['experiment_id']}`",
        f"- Verification engine: `{bundle['verification_version']}`",
        f"- PDF pages: {bundle['pdf_report']['page_count']}",
        f"- ZIP files inventoried: {len(bundle['archive_inventory'])}", "",
        "## Claims", "", "| Claim | Status | Statement |", "|---|---|---|",
    ]
    for item in bundle["claim_report"]["claims"]:
        lines.append(f"| `{item['id']}` | **{item['status']}** | {item['statement']} |")
    lines += ["", "## Protocol findings", "", "| Rule | Status | Finding |", "|---|---|---|"]
    for item in bundle["protocol_report"]["rules"]:
        lines.append(f"| `{item['id']}` | **{item['status']}** | {item['message']} |")
    return "\n".join(lines) + "\n"


def verify_evidence_bundle(*, experiment_id: str, execution_pdf: str | Path, results_zip: str | Path, metric_definitions: str | Path, protocol_rules: str | Path, claim_rules: str | Path, experiment_profile: str | Path | None = None, extraction_dir: str | Path | None = None) -> dict[str, Any]:
    temporary = None
    if extraction_dir is None:
        temporary = tempfile.TemporaryDirectory(prefix="mmals_verify_")
        extracted = Path(temporary.name)
    else:
        extracted = Path(extraction_dir)
        if extracted.exists():
            shutil.rmtree(extracted)
        extracted.mkdir(parents=True)
    safe_extract_zip(results_zip, extracted)
    pdf = pdf_report(execution_pdf)
    archive_inventory = inventory(extracted)
    selected_results_root = resolve_results_root(extracted, experiment_id)
    profile = load_yaml(experiment_profile) if experiment_profile is not None else {}
    metric = metric_report(selected_results_root, load_yaml(metric_definitions))
    protocol = protocol_report(
        selected_results_root,
        pdf,
        load_yaml(protocol_rules),
        archive_inventory,
        profile=profile,
    )
    claims = claim_report(metric, protocol, load_yaml(claim_rules))
    bundle = {
        "schema_version": "0.2.1",
        "verification_version": "0.2.1",
        "experiment_id": experiment_id,
        "selected_results_root": str(selected_results_root.relative_to(extracted)),
        "experiment_profile": str(experiment_profile) if experiment_profile is not None else None,
        "inputs": {
            "execution_pdf": str(execution_pdf),
            "execution_pdf_sha256": sha256_file(execution_pdf),
            "results_zip": str(results_zip),
            "results_zip_sha256": sha256_file(results_zip),
        },
        "pdf_report": {key: value for key, value in pdf.items() if key != "text"},
        "archive_inventory": archive_inventory,
        "metric_report": metric,
        "protocol_report": protocol,
        "claim_report": claims,
    }
    if temporary is not None:
        temporary.cleanup()
    return bundle


def write_verification_outputs(bundle: dict[str, Any], output_dir: str | Path) -> dict[str, str]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    files = {
        "metric_report": output / "metric_report.json",
        "protocol_report": output / "protocol_report.json",
        "claim_report": output / "claim_report.json",
        "evidence_bundle": output / "evidence_bundle.json",
        "verification_summary": output / "verification_summary.md",
        "verification_gate_summary": output / "verification_gate_summary.csv",
    }
    files["metric_report"].write_text(json.dumps(bundle["metric_report"], indent=2), encoding="utf-8")
    files["protocol_report"].write_text(json.dumps(bundle["protocol_report"], indent=2), encoding="utf-8")
    files["claim_report"].write_text(json.dumps(bundle["claim_report"], indent=2), encoding="utf-8")
    files["evidence_bundle"].write_text(json.dumps(bundle, indent=2), encoding="utf-8")
    files["verification_summary"].write_text(verification_summary_markdown(bundle), encoding="utf-8")
    rows = []
    for category, key, plural in [("metric", "metric_report", "metrics"), ("protocol", "protocol_report", "rules"), ("claim", "claim_report", "claims")]:
        for item in bundle[key][plural]:
            rows.append({"category": category, "id": item["id"], "status": item["status"], "message": item.get("message", item.get("statement", ""))})
    pd.DataFrame(rows).to_csv(files["verification_gate_summary"], index=False)
    return {key: str(value) for key, value in files.items()}
