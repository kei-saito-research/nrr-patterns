# Reproducibility Guide (`NRR-Patterns`)

## Scope

This repository provides the manuscript snapshot and bundled reproducibility artifacts for the `NRR-Patterns` line. Current filenames inside the package use `NRR-Patterns` artifact stems. The bundled surface includes the manuscript package plus claim-trace artifacts under `results/`, `repro/`, `scripts/`, and carried-forward `nrr-boundary/` stats. It is narrower than a full rerun workspace or full repo clone.

The package uses two evidence shapes:
- top-level shipped artifacts that exist directly in the extracted ZIP
- nested source members that live inside the bundled result ZIPs and should be
  cited with `zip::member` notation rather than as top-level paths

## Current snapshot

- Manuscript TeX:
  - `manuscript/current/nrr_patterns_manuscript_v0_36_2026-04-13.tex`
- Manuscript PDF snapshot:
  - `manuscript/current/nrr_patterns_manuscript_v0_36_2026-04-13.pdf`
- Manuscript figures:
  - `manuscript/figures/fig_patterns_weighted_3runs.png`
  - `manuscript/figures/fig_r2_comparison_weighted.png`
  - `manuscript/figures/nrr_patterns_stageb_sign_flip_boundaries.png`
- Checksum manifest:
  - `manuscript/checksums_active_review_surface_sha256.txt`
- Reproducibility anchors:
  - `repro/nrr_patterns_audit_surface_sha256_v20_2026-04-12.txt`
  - `repro/nrr_patterns_repro_checksums_sha256.txt`
  - `repro/nrr_patterns_package_map_v20_2026-04-12.md`
  - `repro/nrr_patterns_split_comparison_contract_v13_2026-04-12.md`
  - `repro/nrr_patterns_stageb_selection_rule_v2_2026-04-12.md`
  - `repro/nrr_patterns_fixed_paired_protocol_spec_v8_2026-04-12.md` (provenance note)

## Top-level shipped evidence

- Comparison headline summary:
  - `results/analysis/nrr_patterns_comparison_headline_summary_v3_2026-04-12.csv`
- Provider-separated stability summary:
  - `results/analysis/nrr_patterns_provider_separated_stability_summary_v3_2026-04-12.csv`
- r2 comparison summaries:
  - `results/analysis/nrr_patterns_comparison_summary_r2_aggregated.csv`
  - `results/analysis/nrr_patterns_comparison_summary_r2_by_provider.csv`
- No-position appendix/package-first summaries:
  - `results/analysis/nrr_patterns_no_position_summary.csv`
  - `results/analysis/nrr_patterns_no_position_paired.csv`
- Bundled result ZIPs:
  - `results/nrr_patterns_results_allproviders_clean.zip`
  - `results/nrr_patterns_results_stage1_t00_rep2.zip`
  - `results/nrr_patterns_results_stage2_t03.zip`
  - `results/nrr_patterns_compare_t00_r2_anthropic.zip`
  - `results/nrr_patterns_compare_t00_r2_openai.zip`
  - `results/nrr_patterns_compare_t00_r2_gemini.zip`
  - `results/nrr_patterns_no_position_t00.zip`

## Nested source members used by the manuscript

- Stage1 main exact-replication source members:
  - `results/nrr_patterns_results_allproviders_clean.zip::results/analysis/nrr_patterns_allproviders_pattern_summary_robust_t00.csv`
  - `results/nrr_patterns_results_allproviders_clean.zip::results/analysis/nrr_patterns_allproviders_paired_deltas_merged_t00.csv`
  - `results/nrr_patterns_results_allproviders_clean.zip::results/analysis/nrr_patterns_prod_anthropic_clean_t00_paired_deltas.csv`
  - `results/nrr_patterns_results_allproviders_clean.zip::results/analysis/nrr_patterns_prod_gemini_clean_t00_paired_deltas.csv`
  - `results/nrr_patterns_results_allproviders_clean.zip::results/analysis/nrr_patterns_prod_openai_clean_t00_paired_deltas.csv`
- Stage1 rep2 exact-replication source member:
  - `results/nrr_patterns_results_stage1_t00_rep2.zip::results/analysis/nrr_patterns_allproviders_pattern_summary_robust_t00.csv`
  - `results/nrr_patterns_results_stage1_t00_rep2.zip::results/analysis/nrr_patterns_prod_anthropic_clean_t00_paired_deltas.csv`
  - `results/nrr_patterns_results_stage1_t00_rep2.zip::results/analysis/nrr_patterns_prod_gemini_clean_t00_paired_deltas.csv`
  - `results/nrr_patterns_results_stage1_t00_rep2.zip::results/analysis/nrr_patterns_prod_openai_clean_t00_paired_deltas.csv`
- Stage2 separated robustness source members:
  - `results/nrr_patterns_results_stage2_t03.zip::results/analysis/nrr_patterns_allproviders_pattern_summary_robust_t03.csv`
  - `results/nrr_patterns_results_stage2_t03.zip::results/analysis/nrr_patterns_allproviders_paired_deltas_merged_t03.csv`
- Stage2 provider-specific raw members used for the provider-separated table and the strongest Branch tail-risk sentence:
  - `results/nrr_patterns_results_stage2_t03.zip::results/analysis/nrr_patterns_prod_anthropic_clean_t03_paired_deltas.csv`
  - `results/nrr_patterns_results_stage2_t03.zip::results/analysis/nrr_patterns_prod_gemini_clean_t03_paired_deltas.csv`
  - `results/nrr_patterns_results_stage2_t03.zip::results/analysis/nrr_patterns_prod_openai_clean_t03_paired_deltas.csv`

## Commands

- Scripts reference:
  - `./scripts/README.md`
- Build the current manuscript to a temp output dir:
  - `./scripts/build_current_manuscript.sh`
  - default output: `/tmp/nrr-patterns_current_build/nrr_patterns_manuscript_v0_36_2026-04-13.pdf`
- Verify the active manuscript surface:
  - `./scripts/verify_active_review_surface.sh`
- Verify the current package checksums:
  - `./scripts/verify_current_package.sh`
- Verify the broader artifact surface:
  - `./scripts/verify_audit_surface.py repro/nrr_patterns_audit_surface_sha256_v20_2026-04-12.txt`
- Rebuild shipped summary CSVs from bundled artifacts:
  - `python3 ./scripts/aggregate_comparison_r2.py`
  - `python3 ./scripts/build_nrr_patterns_comparison_headline_summary.py`
  - `python3 ./scripts/build_nrr_patterns_provider_separated_stability_summary.py`
  - `python3 ./scripts/verify_provider_separated_summary.py`
  - `python3 ./scripts/verify_zip_member_refs.py --help`

## Verification

```bash
cd <repo-root>
./scripts/verify_active_review_surface.sh
./scripts/verify_current_package.sh
```

This checks:
- the active manuscript surface under `manuscript/current/`
- the manuscript-facing figure assets under `manuscript/figures/`
- the current manuscript checksum manifest
- the package checksum manifest
- the broader artifact-surface checksum manifest
- `repro/` references named by the current manuscript and package map
- `zip::member` references named by the current manuscript and shipped guides
- docs for paths that should not appear in the bundled ZIP

## Build

```bash
cd <repo-root>
./scripts/build_current_manuscript.sh
```

## Inspect nested members

List bundled members before opening them:

```bash
cd <repo-root>
unzip -l results/nrr_patterns_results_allproviders_clean.zip
unzip -l results/nrr_patterns_results_stage2_t03.zip
```

Read the exact nested source members used by the current manuscript:

```bash
cd <repo-root>
unzip -p results/nrr_patterns_results_allproviders_clean.zip \
  results/analysis/nrr_patterns_allproviders_pattern_summary_robust_t00.csv | head
unzip -p results/nrr_patterns_results_stage2_t03.zip \
  results/analysis/nrr_patterns_allproviders_paired_deltas_merged_t03.csv | head
```

## Package boundary

This package is intentionally narrower than a full rerun workspace. It ships
the current manuscript package, the bundled claim-trace artifacts, and the
verification/build scripts needed to inspect that surface. It does not attempt
to act as a full environment bootstrap or a full historical archive dump.
