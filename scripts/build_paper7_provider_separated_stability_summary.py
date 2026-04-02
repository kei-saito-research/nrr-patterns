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
        "results/analysis/paper7_prod_{provider}_clean_t00_paired_deltas.csv",
    ),
    (
        "stage1_rep2",
        RESULTS_DIR / "paper7_results_stage1_t00_rep2.zip",
        "results/analysis/paper7_prod_{provider}_clean_t00_paired_deltas.csv",
    ),
    (
        "stage2_t03",
        RESULTS_DIR / "paper7_results_stage2_t03.zip",
        "results/analysis/paper7_prod_{provider}_clean_t03_paired_deltas.csv",
    ),
]

PATTERN_ORDER = [
    "hierarchical",
    "delta",
    "lazy",
    "conditional",
    "branch",
]

PROVIDERS = ["anthropic", "gemini", "openai"]

OUTPUT_PATH = ANALYSIS_DIR / "paper7_provider_separated_stability_summary_v2_2026-04-01.csv"


def read_csv_from_zip(zip_path: Path, member_path: str) -> list[dict[str, str]]:
    with zipfile.ZipFile(zip_path) as zf:
        with zf.open(member_path) as f:
            return list(csv.DictReader(io.TextIOWrapper(f, encoding="utf-8")))


def weighted_percent(rows: list[dict[str, str]], pattern: str) -> tuple[float, list[dict[str, str]]]:
    filtered = [row for row in rows if row["pattern"] == pattern]
    numerator = 0.0
    denominator = 0.0
    for row in filtered:
        baseline = float(row["baseline_tokens"])
        pattern_tokens = float(row["pattern_tokens"])
        numerator += baseline - pattern_tokens
        denominator += baseline
    return (100.0 * numerator / denominator if denominator else 0.0), filtered


def format_provider_list(values: list[str]) -> str:
    return ";".join(values) if values else "none"


def main() -> int:
    fieldnames = [
        "pattern",
        "stage1_main_anthropic_weighted_percent_provider_separated",
        "stage1_main_gemini_weighted_percent_provider_separated",
        "stage1_main_openai_weighted_percent_provider_separated",
        "stage1_rep2_anthropic_weighted_percent_provider_separated",
        "stage1_rep2_gemini_weighted_percent_provider_separated",
        "stage1_rep2_openai_weighted_percent_provider_separated",
        "stage2_t03_anthropic_weighted_percent_provider_separated",
        "stage2_t03_gemini_weighted_percent_provider_separated",
        "stage2_t03_openai_weighted_percent_provider_separated",
        "exact_replication_negative_providers",
        "stage2_negative_providers",
        "stage2_most_negative_provider",
        "stage2_most_negative_provider_weighted_percent",
        "stage2_most_negative_provider_worst_row_percent",
        "stage2_most_negative_provider_worst_row_scenario",
        "stage2_most_negative_provider_worst_row_repetition",
        "stage2_most_negative_provider_weighted_percent_without_worst_row",
    ]

    run_provider_rows: dict[str, dict[str, list[dict[str, str]]]] = {}
    for run_label, zip_path, member_template in RUNS:
        per_provider: dict[str, list[dict[str, str]]] = {}
        for provider in PROVIDERS:
            per_provider[provider] = read_csv_from_zip(
                zip_path,
                member_template.format(provider=provider),
            )
        run_provider_rows[run_label] = per_provider

    output_rows: list[dict[str, str]] = []
    for pattern in PATTERN_ORDER:
        row: dict[str, str] = {"pattern": pattern}
        exact_replication_negative_providers: set[str] = set()
        stage2_negative_providers: set[str] = set()
        stage2_provider_values: dict[str, float] = {}
        stage2_provider_rows: dict[str, list[dict[str, str]]] = {}

        for run_label, _, _ in RUNS:
            for provider in PROVIDERS:
                value, filtered_rows = weighted_percent(run_provider_rows[run_label][provider], pattern)
                row[f"{run_label}_{provider}_weighted_percent_provider_separated"] = f"{value:.6f}"
                if run_label != "stage2_t03" and value < 0:
                    exact_replication_negative_providers.add(provider)
                if run_label == "stage2_t03":
                    stage2_provider_values[provider] = value
                    stage2_provider_rows[provider] = filtered_rows
                    if value < 0:
                        stage2_negative_providers.add(provider)

        row["exact_replication_negative_providers"] = format_provider_list(sorted(exact_replication_negative_providers))
        row["stage2_negative_providers"] = format_provider_list(sorted(stage2_negative_providers))
        if stage2_negative_providers:
            worst_provider = min(stage2_negative_providers, key=stage2_provider_values.get)
            worst_provider_value = stage2_provider_values[worst_provider]
            worst_rows = stage2_provider_rows[worst_provider]
            worst_row = min(
                worst_rows,
                key=lambda row_: (float(row_["baseline_tokens"]) - float(row_["pattern_tokens"])) / float(row_["baseline_tokens"]),
            )
            worst_baseline = float(worst_row["baseline_tokens"])
            worst_pattern_tokens = float(worst_row["pattern_tokens"])
            worst_row_percent = 100.0 * (worst_baseline - worst_pattern_tokens) / worst_baseline
            trimmed_rows = [row_ for row_ in worst_rows if row_ is not worst_row]
            trimmed_numerator = 0.0
            trimmed_denominator = 0.0
            for trimmed_row in trimmed_rows:
                baseline = float(trimmed_row["baseline_tokens"])
                pattern_tokens = float(trimmed_row["pattern_tokens"])
                trimmed_numerator += baseline - pattern_tokens
                trimmed_denominator += baseline
            trimmed_percent = 100.0 * trimmed_numerator / trimmed_denominator if trimmed_denominator else 0.0

            row["stage2_most_negative_provider"] = worst_provider
            row["stage2_most_negative_provider_weighted_percent"] = f"{worst_provider_value:.6f}"
            row["stage2_most_negative_provider_worst_row_percent"] = f"{worst_row_percent:.6f}"
            row["stage2_most_negative_provider_worst_row_scenario"] = (
                worst_row.get("scenario_id") or worst_row.get("scenario") or ""
            )
            row["stage2_most_negative_provider_worst_row_repetition"] = (
                worst_row.get("repetition") or worst_row.get("rep") or ""
            )
            row["stage2_most_negative_provider_weighted_percent_without_worst_row"] = f"{trimmed_percent:.6f}"
        else:
            row["stage2_most_negative_provider"] = ""
            row["stage2_most_negative_provider_weighted_percent"] = ""
            row["stage2_most_negative_provider_worst_row_percent"] = ""
            row["stage2_most_negative_provider_worst_row_scenario"] = ""
            row["stage2_most_negative_provider_worst_row_repetition"] = ""
            row["stage2_most_negative_provider_weighted_percent_without_worst_row"] = ""
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
