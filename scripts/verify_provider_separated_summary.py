#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = max(
    (ROOT / "results" / "analysis").glob("paper7_provider_separated_stability_summary_v*.csv"),
    key=lambda p: p.name,
)

STAGE2_PROVIDER_FIELDS = {
    "anthropic": "stage2_t03_anthropic_weighted_percent_provider_separated",
    "gemini": "stage2_t03_gemini_weighted_percent_provider_separated",
    "openai": "stage2_t03_openai_weighted_percent_provider_separated",
}

NEGATIVE_CONTEXT_FIELDS = [
    "stage2_most_negative_provider",
    "stage2_most_negative_provider_weighted_percent",
    "stage2_most_negative_provider_worst_row_percent",
    "stage2_most_negative_provider_worst_row_scenario",
    "stage2_most_negative_provider_worst_row_repetition",
    "stage2_most_negative_provider_weighted_percent_without_worst_row",
]


def parse_negative_providers(raw: str) -> list[str]:
    if not raw or raw == "none":
        return []
    return raw.split(";")


def main() -> int:
    rows = list(csv.DictReader(SUMMARY_PATH.open(encoding="utf-8", newline="")))
    errors: list[str] = []

    for row in rows:
        pattern = row["pattern"]
        negatives = parse_negative_providers(row["stage2_negative_providers"])
        most_negative_provider = row["stage2_most_negative_provider"]

        if not negatives:
            populated = [field for field in NEGATIVE_CONTEXT_FIELDS if row[field] != ""]
            if populated:
                errors.append(
                    f"{pattern}: stage2_negative_providers=none but negative-context fields are populated: {', '.join(populated)}"
                )
            continue

        if most_negative_provider not in negatives:
            errors.append(
                f"{pattern}: stage2_most_negative_provider={most_negative_provider!r} is not listed in stage2_negative_providers={row['stage2_negative_providers']!r}"
            )
            continue

        provider_field = STAGE2_PROVIDER_FIELDS[most_negative_provider]
        provider_value = float(row[provider_field])
        reported_value = float(row["stage2_most_negative_provider_weighted_percent"])

        if provider_value >= 0:
            errors.append(
                f"{pattern}: most-negative provider {most_negative_provider} is non-negative at {provider_value:.6f}"
            )
        if abs(provider_value - reported_value) > 1e-9:
            errors.append(
                f"{pattern}: reported most-negative value {reported_value:.6f} does not match provider field {provider_value:.6f}"
            )

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"OK_PROVIDER_SEPARATED_SUMMARY  {SUMMARY_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
