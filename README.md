# NRR-Patterns: Delayed-Commitment Patterns in Stateful LLM Systems

This repository is the current public authority for the `NRR-Patterns` line.
The released manuscript and package artifacts in this bounded audit surface
still retain the integrated `paper7` stem for continuity. The current
NRR-Patterns manuscript compares delayed-commitment patterns under a split
comparison contract with a fixed matched-run comparison headline on two fixed
matched `t=0.0` runs and a separated robustness member, then carries forward
selected provider-sensitive boundary reporting to keep the resulting pattern
map honest under explicit conditions. The shipped review ZIP audits that
released output surface rather than serving as an independent rerun workspace.

Historical note:
- the older `nrr-principles` repository remains as historical/source continuity for the pre-integration and local integration history
- the standalone `nrr-boundary` repository remains as a historical/source support surface
- neither old repository should be read as a competing live mainline now that this `NRR-Patterns` authority surface exists

NRR is not an anti-LLM framework.
NRR does not replace standard LLM use.
NRR optimizes when to commit and when to defer, under explicit conditions.
Series numbering policy: `paper3` is permanently skipped and never reused.

Part of the Non-Resolution Reasoning (NRR) research program.

## NRR Series Hub (Start here)

For the cross-paper map and current series links, start here:
- [NRR Series Hub](https://github.com/kei-saito-research/nrr-series-hub)

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18819444.svg)](https://doi.org/10.5281/zenodo.18819444)

## Current manuscript snapshot

- Mainline integrated manuscript source:
  - `manuscript/current/paper7_integrated_manuscript_v0_31_2026-04-03.tex`
- Mainline integrated manuscript PDF:
  - `manuscript/current/paper7_integrated_manuscript_v0_31_2026-04-03.pdf`
- Mainline integrated checksum manifest:
  - `manuscript/current/paper7_integrated_checksums_sha256.txt`
- Mainline integrated audit-surface anchors:
  - `repro/paper7_integrated_audit_surface_sha256_v19_2026-04-01.txt`
  - `repro/paper7_integrated_package_map_v19_2026-04-01.md`
  - `repro/paper7_split_comparison_contract_v12_2026-04-01.md`
  - `repro/paper7_stageb_selection_rule_v1_2026-03-31.md`
- Mainline integrated figures used by manuscript:
  - `manuscript/current/fig_patterns_weighted_3runs.png`
  - `manuscript/current/fig_r2_comparison_weighted.png`
  - `manuscript/current/paper7_stageb_sign_flip_boundaries.png`
- Current review ZIP audits the released matched-run output surface and nested source members rather than providing an independent rerun workspace.
- Shipped root-level docs inside that ZIP are only `README.md` and `reproducibility.md`.

## Review-package entry points

The current review ZIP has one active comparison contract: `repro/paper7_split_comparison_contract_v12_2026-04-01.md`. The shipped `repro/paper7_fixed_paired_protocol_spec_v7_2026-04-01.md` file is a historical provenance note only, while `repro/paper7_integrated_boundary_claims_manifest_v1_2026-03-29.csv` and `repro/paper7_integrated_repro_checksums_sha256.txt` are part of the current audit surface.

- Integrated review-package guide:
  - `reproducibility.md`
- Top-level shipped summaries:
  - `results/analysis/paper7_integrated_comparison_headline_summary_v2_2026-03-31.csv`
  - `results/analysis/paper7_provider_separated_stability_summary_v2_2026-04-01.csv`
  - `results/analysis/paper7_comparison_summary_r2_aggregated.csv`
  - `results/analysis/paper7_comparison_summary_r2_by_provider.csv`
  - `results/analysis/paper7_no_position_summary.csv`
  - `results/analysis/paper7_no_position_paired.csv`
- Nested source members used for claim trace:
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t00.csv`
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_allproviders_paired_deltas_merged_t00.csv`
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_prod_anthropic_clean_t00_paired_deltas.csv`
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_prod_gemini_clean_t00_paired_deltas.csv`
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_prod_openai_clean_t00_paired_deltas.csv`
  - `results/paper7_results_stage1_t00_rep2.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t00.csv`
  - `results/paper7_results_stage1_t00_rep2.zip::results/analysis/paper7_prod_anthropic_clean_t00_paired_deltas.csv`
  - `results/paper7_results_stage1_t00_rep2.zip::results/analysis/paper7_prod_gemini_clean_t00_paired_deltas.csv`
  - `results/paper7_results_stage1_t00_rep2.zip::results/analysis/paper7_prod_openai_clean_t00_paired_deltas.csv`
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t03.csv`
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_allproviders_paired_deltas_merged_t03.csv`
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_prod_anthropic_clean_t03_paired_deltas.csv`
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_prod_gemini_clean_t03_paired_deltas.csv`
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_prod_openai_clean_t03_paired_deltas.csv`
- Shipped audit-package scripts:
  - `./scripts/aggregate_comparison_r2.py`
  - `./scripts/build_paper7_integrated_comparison_headline_summary.py`
  - `./scripts/build_paper7_provider_separated_stability_summary.py`
  - `./scripts/README.md`
  - `./scripts/build_current_manuscript.sh`
  - `./scripts/verify_active_review_surface.sh`
  - `./scripts/verify_current_package.sh`
  - `./scripts/verify_provider_separated_summary.py`
  - `./scripts/verify_audit_surface.py repro/paper7_integrated_audit_surface_sha256_v19_2026-04-01.txt`
- Integrated package manifests:
  - `repro/paper7_integrated_comparison_claims_manifest_v6_2026-04-01.csv`
  - `repro/paper7_integrated_boundary_claims_manifest_v1_2026-03-29.csv`
  - `repro/paper7_integrated_package_map_v19_2026-04-01.md`
  - `repro/paper7_split_comparison_contract_v12_2026-04-01.md` (active comparison contract)
  - `repro/paper7_fixed_paired_protocol_spec_v7_2026-04-01.md` (historical / superseded provenance note only)
  - `repro/paper7_integrated_repro_checksums_sha256.txt`
  - `repro/paper7_integrated_audit_surface_sha256_v19_2026-04-01.txt`

## Mainline Read

- Current cross-series mainline for this repository:
  - `NRR-Patterns` (released artifact stem: integrated `paper7`)
- Historical/source surfaces kept here but not current mainline:
  - standalone `NRR-Principles`
  - carried-forward `Boundary` source references consumed by the current `NRR-Patterns` line
- Standalone sibling repository status:
  - `nrr-boundary` remains a historical/source support surface and should not be read as a separate live mainline while `NRR-Patterns` is the active line

## Shipped review-zip structure

```text
nrr-patterns-review-zip/
|-- README.md
|-- reproducibility.md
|-- manuscript/
|   `-- current/
|-- nrr-boundary/
|   `-- stats/stageb_all/
|-- results/
|   |-- analysis/
|   |-- paper7_results_allproviders_clean.zip
|   |-- paper7_results_stage1_t00_rep2.zip
|   |-- paper7_results_stage2_t03.zip
|   |-- paper7_compare_t00_r2_*.zip
|   `-- paper7_no_position_t00.zip
|-- repro/
|   |-- paper7_integrated_package_map_v19_2026-04-01.md
|   |-- paper7_split_comparison_contract_v12_2026-04-01.md
|   |-- paper7_stageb_selection_rule_v1_2026-03-31.md
|   |-- paper7_fixed_paired_protocol_spec_v7_2026-04-01.md
|   |-- paper7_integrated_comparison_claims_manifest_v6_2026-04-01.csv
|   |-- paper7_integrated_boundary_claims_manifest_v1_2026-03-29.csv
|   |-- paper7_integrated_repro_checksums_sha256.txt
|   `-- paper7_integrated_audit_surface_sha256_v19_2026-04-01.txt
`-- scripts/
    |-- aggregate_comparison_r2.py
    |-- build_paper7_integrated_comparison_headline_summary.py
    |-- build_paper7_provider_separated_stability_summary.py
    |-- README.md
    |-- build_current_manuscript.sh
    |-- verify_audit_surface.py
    |-- verify_active_review_surface.sh
    |-- verify_current_package.sh
    |-- verify_provider_separated_summary.py
    `-- verify_zip_member_refs.py
```
