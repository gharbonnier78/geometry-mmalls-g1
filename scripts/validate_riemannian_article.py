#!/usr/bin/env python3
"""Validate the MMALS Riemannian article package using only the Python standard library."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "LICENSE",
    "CITATION.cff",
    "paper/riemannian_learning_architecture/main.tex",
    "paper/riemannian_learning_architecture/Makefile",
    "docs/reports/MMALS_Riemannian_Learning_Architecture_v1_0.pdf",
    "docs/specs/MMALS_Riemannian_Experimental_Protocol_v1_0.md",
    "governance/riemannian_learning_architecture/source_tiers.yaml",
    "governance/riemannian_learning_architecture/claim_manifest.yaml",
    "governance/riemannian_learning_architecture/uploaded_source_hashes.txt",
    ".github/workflows/riemannian-article.yml",
]

FORBIDDEN_MARKERS = ("TBD", "TODO_REPLACE", "INSERT RESULT", "PLACEHOLDER CLAIM")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing required file: {relative}")
        if path.stat().st_size == 0:
            fail(f"empty required file: {relative}")

    pdf = ROOT / "docs/reports/MMALS_Riemannian_Learning_Architecture_v1_0.pdf"
    if pdf.stat().st_size < 100_000:
        fail("compiled PDF is unexpectedly small")
    if pdf.read_bytes()[:5] != b"%PDF-":
        fail("compiled report does not have a PDF header")

    text_paths = [
        ROOT / "README.md",
        ROOT / "paper/riemannian_learning_architecture/main.tex",
        ROOT / "docs/specs/MMALS_Riemannian_Experimental_Protocol_v1_0.md",
        ROOT / "governance/riemannian_learning_architecture/source_tiers.yaml",
        ROOT / "governance/riemannian_learning_architecture/claim_manifest.yaml",
    ]
    for path in text_paths:
        text = path.read_text(encoding="utf-8")
        for marker in FORBIDDEN_MARKERS:
            if marker in text:
                fail(f"forbidden marker {marker!r} in {path.relative_to(ROOT)}")

    tiers = (ROOT / "governance/riemannian_learning_architecture/source_tiers.yaml").read_text(encoding="utf-8")
    for tier in ("T1:", "T2:", "T3:", "T4:", "T5:"):
        if tier not in tiers:
            fail(f"source tier missing: {tier}")

    claims = (ROOT / "governance/riemannian_learning_architecture/claim_manifest.yaml").read_text(encoding="utf-8")
    claim_ids = re.findall(r"^  (C\d+_[a-z0-9_]+):$", claims, flags=re.MULTILINE)
    if len(claim_ids) < 10:
        fail(f"expected at least 10 governed claims, found {len(claim_ids)}")

    hash_lines = [
        line.strip()
        for line in (ROOT / "governance/riemannian_learning_architecture/uploaded_source_hashes.txt").read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]
    if len(hash_lines) < 6:
        fail("source-hash ledger is incomplete")
    for line in hash_lines:
        if not re.search(r"\b[0-9a-f]{64}\b", line):
            fail(f"invalid SHA-256 ledger line: {line}")

    print("MMALS Riemannian article package: VALID")
    print(f"PDF bytes: {pdf.stat().st_size}")
    print(f"PDF SHA-256: {sha256(pdf)}")
    print(f"Governed claims: {len(claim_ids)}")
    print(f"Recorded source artifacts: {len(hash_lines)}")


if __name__ == "__main__":
    main()
