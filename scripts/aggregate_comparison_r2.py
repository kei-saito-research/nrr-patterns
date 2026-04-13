#!/usr/bin/env python3
from __future__ import annotations

import csv
import io
import math
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

RESULTS_DIR = ROOT / "results"
ANALYSIS_DIR = RESULTS_DIR / "analysis"

ZIP_PATHS = {
    "anthropic": RESULTS_DIR / "nrr_patterns_compare_t00_r2_anthropic.zip",
    "openai": RESULTS_DIR / "nrr_patterns_compare_t00_r2_openai.zip",
    "gemini": RESULTS_DIR / "nrr_patterns_compare_t00_r2_gemini.zip",
}
PAIRED_MEMBER = "results_compare_t00_r2/analysis/nrr_patterns_comparison_paired.csv"


def weighted_percent(rows: list[dict[str, str]]) -> float:
    base = sum(float(r["baseline_tokens"]) for r in rows)
    red = sum(float(r["reduction_tokens"]) for r in rows)
    return (red / base * 100.0) if base else math.nan


def summarize_pairs(pair_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in pair_rows:
        grouped[(row["pattern"], row["comparison"])].append(row)

    out: list[dict[str, object]] = []
    for (pattern, comparison), rows in sorted(grouped.items()):
        vals = [float(r["reduction_percent"]) for r in rows]
        vals_sorted = sorted(vals)
        n_all = len(vals_sorted)
        if n_all == 0:
            continue
        median = vals_sorted[n_all // 2] if n_all % 2 == 1 else (vals_sorted[n_all // 2 - 1] + vals_sorted[n_all // 2]) / 2.0
        trim_k = int(n_all * 0.1)
        trimmed = vals_sorted[trim_k : n_all - trim_k] if n_all - trim_k > trim_k else vals_sorted
        finite_cps = [float(r["cost_per_success_delta_tokens"]) for r in rows if str(r["cost_per_success_delta_tokens"]) != "nan"]
        out.append(
            {
                "pattern": pattern,
                "comparison": comparison,
                "n_all": n_all,
                "mean_percent": sum(vals) / n_all,
                "median_percent": median,
                "trimmed10_mean_percent": sum(trimmed) / len(trimmed),
                "weighted_percent_sum_red_over_sum_base": weighted_percent(rows),
                "min_percent": min(vals),
                "max_percent": max(vals),
                "mean_cost_per_success_delta_tokens": sum(finite_cps) / len(finite_cps) if finite_cps else math.nan,
            }
        )
    return out


def read_csv_from_zip(zip_path: Path, member: str) -> list[dict[str, str]]:
    with zipfile.ZipFile(zip_path) as zf:
        with zf.open(member) as f:
            return list(csv.DictReader(io.TextIOWrapper(f, encoding="utf-8")))


def load_pair_rows() -> list[dict[str, str]]:
    all_rows: list[dict[str, str]] = []
    for provider, zip_path in ZIP_PATHS.items():
        if not zip_path.exists():
            raise FileNotFoundError(f"Missing comparison ZIP for {provider}: {zip_path}")
        rows = read_csv_from_zip(zip_path, PAIRED_MEMBER)
        if not rows:
            raise ValueError(f"No paired rows found in {zip_path}")
        for row in rows:
            row["provider"] = row.get("provider") or provider
        all_rows.extend(rows)
    return all_rows


def aggregate_provider_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    by_provider: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_provider[row["provider"]].append(row)
    for provider in sorted(by_provider):
        for summary in summarize_pairs(by_provider[provider]):
            out.append({"provider": provider, **summary})
    return out


def aggregate_allproviders(provider_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in provider_rows:
        grouped[(str(row["pattern"]), str(row["comparison"]))].append(row)

    out: list[dict[str, object]] = []
    for (pattern, comparison), rows in sorted(grouped.items()):
        n_all_total = sum(int(row["n_all"]) for row in rows)
        if n_all_total <= 0:
            continue

        def weighted(key: str) -> float:
            return sum(float(row[key]) * int(row["n_all"]) for row in rows) / n_all_total

        provider_balanced = sum(float(row["weighted_percent_sum_red_over_sum_base"]) for row in rows) / len(rows)
        out.append(
            {
                "pattern": pattern,
                "comparison": comparison,
                "providers": ",".join(sorted(str(row["provider"]) for row in rows)),
                "n_all_total": n_all_total,
                "mean_percent_n_weighted": weighted("mean_percent"),
                "median_percent_n_weighted": weighted("median_percent"),
                "trimmed10_mean_percent_n_weighted": weighted("trimmed10_mean_percent"),
                "weighted_percent_provider_balanced_n_weighted": provider_balanced,
                "mean_cost_per_success_delta_tokens_n_weighted": weighted("mean_cost_per_success_delta_tokens"),
            }
        )
    return out


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    pair_rows = load_pair_rows()
    by_provider_rows = aggregate_provider_rows(pair_rows)
    aggregated_rows = aggregate_allproviders(by_provider_rows)

    by_provider_path = ANALYSIS_DIR / "nrr_patterns_comparison_summary_r2_by_provider.csv"
    aggregated_path = ANALYSIS_DIR / "nrr_patterns_comparison_summary_r2_aggregated.csv"

    write_csv(
        by_provider_path,
        [
            "provider",
            "pattern",
            "comparison",
            "n_all",
            "mean_percent",
            "median_percent",
            "trimmed10_mean_percent",
            "weighted_percent_sum_red_over_sum_base",
            "min_percent",
            "max_percent",
            "mean_cost_per_success_delta_tokens",
        ],
        by_provider_rows,
    )
    write_csv(
        aggregated_path,
        [
            "pattern",
            "comparison",
            "providers",
            "n_all_total",
            "mean_percent_n_weighted",
            "median_percent_n_weighted",
            "trimmed10_mean_percent_n_weighted",
            "weighted_percent_provider_balanced_n_weighted",
            "mean_cost_per_success_delta_tokens_n_weighted",
        ],
        aggregated_rows,
    )

    print(f"saved: {by_provider_path}")
    print(f"saved: {aggregated_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
