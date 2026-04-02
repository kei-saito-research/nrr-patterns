#!/usr/bin/env python3
from __future__ import annotations

import csv
import io
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
ANALYSIS_DIR = RESULTS_DIR / "analysis"

RUNS = [
    (
        "stage1_main",
        RESULTS_DIR / "paper7_results_allproviders_clean.zip",
        "results/analysis/paper7_allproviders_pattern_summary_robust_t00.csv",
    ),
    (
        "stage1_rep2",
        RESULTS_DIR / "paper7_results_stage1_t00_rep2.zip",
        "results/analysis/paper7_allproviders_pattern_summary_robust_t00.csv",
    ),
    (
        "stage2_t03",
        RESULTS_DIR / "paper7_results_stage2_t03.zip",
        "results/analysis/paper7_allproviders_pattern_summary_robust_t03.csv",
    ),
]

PATTERN_ORDER = [
    "hierarchical",
    "delta",
    "lazy",
    "conditional",
    "branch",
]

OUTPUT_PATH = ANALYSIS_DIR / "paper7_integrated_comparison_headline_summary_v2_2026-03-31.csv"


def read_csv_from_zip(zip_path: Path, member_path: str) -> list[dict[str, str]]:
    with zipfile.ZipFile(zip_path) as zf:
        with zf.open(member_path) as f:
            return list(csv.DictReader(io.TextIOWrapper(f, encoding="utf-8")))


def main() -> int:
    per_run: dict[str, dict[str, dict[str, str]]] = {}
    for run_label, zip_path, member_path in RUNS:
        rows = read_csv_from_zip(zip_path, member_path)
        per_run[run_label] = {row["pattern"]: row for row in rows}

    fieldnames = [
        "pattern",
        "stage1_main_weighted_percent_provider_balanced",
        "stage1_rep2_weighted_percent_provider_balanced",
        "exact_replication_mean_weighted_percent_provider_balanced",
        "stage2_t03_weighted_percent_provider_balanced",
        "stage1_main_source",
        "stage1_rep2_source",
        "stage2_t03_source",
    ]

    output_rows: list[dict[str, str]] = []
    for pattern in PATTERN_ORDER:
        row: dict[str, str] = {"pattern": pattern}
        for run_label, zip_path, member_path in RUNS:
            run_row = per_run[run_label][pattern]
            value = float(run_row["weighted_percent_provider_balanced"])
            row[f"{run_label}_weighted_percent_provider_balanced"] = f"{value:.6f}"
            row[f"{run_label}_source"] = f"{zip_path.relative_to(ROOT)}::{member_path}"
        exact_replication_mean = (
            float(row["stage1_main_weighted_percent_provider_balanced"])
            + float(row["stage1_rep2_weighted_percent_provider_balanced"])
        ) / 2.0
        row["exact_replication_mean_weighted_percent_provider_balanced"] = f"{exact_replication_mean:.6f}"
        output_rows.append(row)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"saved: {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
