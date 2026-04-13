# NRR-Patterns: Delayed-Commitment Patterns in Stateful LLM Systems

This repository hosts the manuscript snapshot and reproducibility assets for the `NRR-Patterns` line. The manuscript compares delayed-commitment patterns under a split comparison contract with a fixed matched-run comparison headline on two fixed matched `t=0.0` runs and a separated robustness member, then reports provider-sensitive boundary behavior under explicit conditions.

NRR is not an anti-LLM framework.
NRR does not replace standard LLM use.
NRR optimizes when to commit and when to defer, under explicit conditions.

Part of the Non-Resolution Reasoning (NRR) research program.

## NRR Series Hub (Start here)

For the cross-paper map and current series links, start here:
- [NRR Series Hub](https://github.com/kei-saito-research/nrr-series-hub)

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18819444.svg)](https://doi.org/10.5281/zenodo.18819444)

## Current manuscript snapshot

- Manuscript source:
  - `manuscript/current/nrr_patterns_manuscript_v0_36_2026-04-13.tex`
- Manuscript PDF:
  - `manuscript/current/nrr_patterns_manuscript_v0_36_2026-04-13.pdf`
- Checksum manifest:
  - `manuscript/checksums_active_review_surface_sha256.txt`
- Reproducibility anchors:
  - `repro/nrr_patterns_audit_surface_sha256_v20_2026-04-12.txt`
  - `repro/nrr_patterns_package_map_v20_2026-04-12.md`
  - `repro/nrr_patterns_split_comparison_contract_v13_2026-04-12.md`
  - `repro/nrr_patterns_stageb_selection_rule_v2_2026-04-12.md`
- Figures used by the manuscript:
  - `manuscript/figures/fig_patterns_weighted_3runs.png`
  - `manuscript/figures/fig_r2_comparison_weighted.png`
  - `manuscript/figures/nrr_patterns_stageb_sign_flip_boundaries.png`
- The bundled ZIP inspects the released matched-run output surface and nested source members rather than acting as a full rerun workspace.
- The bundled root-level guides are `README.md` and `reproducibility.md`.

## Snapshot entry points

The bundled ZIP uses `repro/nrr_patterns_split_comparison_contract_v13_2026-04-12.md` as its comparison contract. The file `repro/nrr_patterns_fixed_paired_protocol_spec_v8_2026-04-12.md` is retained as provenance for the bundled artifact set.

- Reproducibility guide:
  - `reproducibility.md`
- Top-level shipped summaries:
  - `results/analysis/nrr_patterns_comparison_headline_summary_v3_2026-04-12.csv`
  - `results/analysis/nrr_patterns_provider_separated_stability_summary_v3_2026-04-12.csv`
  - `results/analysis/nrr_patterns_comparison_summary_r2_aggregated.csv`
  - `results/analysis/nrr_patterns_comparison_summary_r2_by_provider.csv`
  - `results/analysis/nrr_patterns_no_position_summary.csv`
  - `results/analysis/nrr_patterns_no_position_paired.csv`
- Nested source members used for claim trace:
  - `results/nrr_patterns_results_allproviders_clean.zip::results/analysis/nrr_patterns_allproviders_pattern_summary_robust_t00.csv`
  - `results/nrr_patterns_results_allproviders_clean.zip::results/analysis/nrr_patterns_allproviders_paired_deltas_merged_t00.csv`
  - `results/nrr_patterns_results_allproviders_clean.zip::results/analysis/nrr_patterns_prod_anthropic_clean_t00_paired_deltas.csv`
  - `results/nrr_patterns_results_allproviders_clean.zip::results/analysis/nrr_patterns_prod_gemini_clean_t00_paired_deltas.csv`
  - `results/nrr_patterns_results_allproviders_clean.zip::results/analysis/nrr_patterns_prod_openai_clean_t00_paired_deltas.csv`
  - `results/nrr_patterns_results_stage1_t00_rep2.zip::results/analysis/nrr_patterns_allproviders_pattern_summary_robust_t00.csv`
  - `results/nrr_patterns_results_stage1_t00_rep2.zip::results/analysis/nrr_patterns_prod_anthropic_clean_t00_paired_deltas.csv`
  - `results/nrr_patterns_results_stage1_t00_rep2.zip::results/analysis/nrr_patterns_prod_gemini_clean_t00_paired_deltas.csv`
  - `results/nrr_patterns_results_stage1_t00_rep2.zip::results/analysis/nrr_patterns_prod_openai_clean_t00_paired_deltas.csv`
  - `results/nrr_patterns_results_stage2_t03.zip::results/analysis/nrr_patterns_allproviders_pattern_summary_robust_t03.csv`
  - `results/nrr_patterns_results_stage2_t03.zip::results/analysis/nrr_patterns_allproviders_paired_deltas_merged_t03.csv`
  - `results/nrr_patterns_results_stage2_t03.zip::results/analysis/nrr_patterns_prod_anthropic_clean_t03_paired_deltas.csv`
  - `results/nrr_patterns_results_stage2_t03.zip::results/analysis/nrr_patterns_prod_gemini_clean_t03_paired_deltas.csv`
  - `results/nrr_patterns_results_stage2_t03.zip::results/analysis/nrr_patterns_prod_openai_clean_t03_paired_deltas.csv`
- Included scripts:
  - `./scripts/aggregate_comparison_r2.py`
  - `./scripts/build_nrr_patterns_comparison_headline_summary.py`
  - `./scripts/build_nrr_patterns_provider_separated_stability_summary.py`
  - `./scripts/README.md`
  - `./scripts/build_current_manuscript.sh`
  - `./scripts/verify_active_review_surface.sh`
  - `./scripts/verify_current_package.sh`
  - `./scripts/verify_provider_separated_summary.py`
  - `./scripts/verify_audit_surface.py repro/nrr_patterns_audit_surface_sha256_v20_2026-04-12.txt`
- Reproducibility manifests:
  - `repro/nrr_patterns_comparison_claims_manifest_v7_2026-04-12.csv`
  - `repro/nrr_patterns_boundary_claims_manifest_v2_2026-04-12.csv`
  - `repro/nrr_patterns_package_map_v20_2026-04-12.md`
  - `repro/nrr_patterns_split_comparison_contract_v13_2026-04-12.md`
  - `repro/nrr_patterns_fixed_paired_protocol_spec_v8_2026-04-12.md` (provenance note)
  - `repro/nrr_patterns_repro_checksums_sha256.txt`
  - `repro/nrr_patterns_audit_surface_sha256_v20_2026-04-12.txt`

## Bundled ZIP structure

```text
nrr-patterns-review-zip/
|-- README.md
|-- reproducibility.md
|-- manuscript/
|   |-- current/
|   `-- figures/
|-- nrr-boundary/
|   `-- stats/stageb_all/
|-- results/
|   |-- analysis/
|   |-- nrr_patterns_results_allproviders_clean.zip
|   |-- nrr_patterns_results_stage1_t00_rep2.zip
|   |-- nrr_patterns_results_stage2_t03.zip
|   |-- nrr_patterns_compare_t00_r2_*.zip
|   `-- nrr_patterns_no_position_t00.zip
|-- repro/
|   |-- nrr_patterns_package_map_v20_2026-04-12.md
|   |-- nrr_patterns_split_comparison_contract_v13_2026-04-12.md
|   |-- nrr_patterns_stageb_selection_rule_v2_2026-04-12.md
|   |-- nrr_patterns_fixed_paired_protocol_spec_v8_2026-04-12.md
|   |-- nrr_patterns_comparison_claims_manifest_v7_2026-04-12.csv
|   |-- nrr_patterns_boundary_claims_manifest_v2_2026-04-12.csv
|   |-- nrr_patterns_repro_checksums_sha256.txt
|   `-- nrr_patterns_audit_surface_sha256_v20_2026-04-12.txt
`-- scripts/
    |-- aggregate_comparison_r2.py
    |-- build_nrr_patterns_comparison_headline_summary.py
    |-- build_nrr_patterns_provider_separated_stability_summary.py
    |-- README.md
    |-- build_current_manuscript.sh
    |-- verify_audit_surface.py
    |-- verify_active_review_surface.sh
    |-- verify_current_package.sh
    |-- verify_provider_separated_summary.py
    `-- verify_zip_member_refs.py
```
