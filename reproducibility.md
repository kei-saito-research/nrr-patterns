# Reproducibility Guide (`NRR-Patterns`)

## Scope

This review ZIP is the bounded audit package for the `NRR-Patterns` line.
Released filenames inside the package still use the integrated `paper7` stem
for continuity. It audits the released matched-run output surface and preserved
nested source members, fixing the released audit surface rather than acting as
a live rerun handoff. It is not a full repo clone and it is not a live-rerun
handoff. The shipped root-level guides are only `README.md` and this file; the
shipped operational surface is the current manuscript package plus the bundled
claim-trace artifacts under `results/`, `repro/`, `scripts/`, and
carried-forward `nrr-boundary/` stats.

The package uses two evidence shapes:
- top-level shipped artifacts that exist directly in the extracted ZIP
- nested source members that live inside the bundled result ZIPs and should be
  cited with `zip::member` notation rather than as top-level paths

## Current review package

- Mainline integrated TeX:
  - `manuscript/current/paper7_integrated_manuscript_v0_29_2026-04-01.tex`
- Current integrated PDF snapshot:
  - `manuscript/current/paper7_integrated_manuscript_v0_29_2026-04-01.pdf`
- Current integrated manuscript figures:
  - `manuscript/current/fig_principles_weighted_3runs.png`
  - `manuscript/current/fig_r2_comparison_weighted.png`
  - `manuscript/current/paper7_stageb_sign_flip_boundaries.png`
- Integrated checksum manifest:
  - `manuscript/current/paper7_integrated_checksums_sha256.txt`
- Audit-surface anchors:
  - `repro/paper7_integrated_audit_surface_sha256_v19_2026-04-01.txt`
  - `repro/paper7_integrated_repro_checksums_sha256.txt`
  - `repro/paper7_integrated_package_map_v19_2026-04-01.md`
  - `repro/paper7_split_comparison_contract_v12_2026-04-01.md`
  - `repro/paper7_stageb_selection_rule_v1_2026-03-31.md`
  - `repro/paper7_fixed_paired_protocol_spec_v7_2026-04-01.md` (superseded provenance note only)

## Top-level shipped evidence

- Comparison headline summary:
  - `results/analysis/paper7_integrated_comparison_headline_summary_v2_2026-03-31.csv`
- Provider-separated stability summary:
  - `results/analysis/paper7_provider_separated_stability_summary_v2_2026-04-01.csv`
- r2 comparison summaries:
  - `results/analysis/paper7_comparison_summary_r2_aggregated.csv`
  - `results/analysis/paper7_comparison_summary_r2_by_provider.csv`
- No-position appendix/package-first summaries:
  - `results/analysis/paper7_no_position_summary.csv`
  - `results/analysis/paper7_no_position_paired.csv`
- Bundled result ZIPs:
  - `results/paper7_results_allproviders_clean.zip`
  - `results/paper7_results_stage1_t00_rep2.zip`
  - `results/paper7_results_stage2_t03.zip`
  - `results/paper7_compare_t00_r2_anthropic.zip`
  - `results/paper7_compare_t00_r2_openai.zip`
  - `results/paper7_compare_t00_r2_gemini.zip`
  - `results/paper7_no_position_t00.zip`

## Nested source members used by the manuscript

- Stage1 main exact-replication source members:
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t00.csv`
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_allproviders_paired_deltas_merged_t00.csv`
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_prod_anthropic_clean_t00_paired_deltas.csv`
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_prod_gemini_clean_t00_paired_deltas.csv`
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_prod_openai_clean_t00_paired_deltas.csv`
- Stage1 rep2 exact-replication source member:
  - `results/paper7_results_stage1_t00_rep2.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t00.csv`
  - `results/paper7_results_stage1_t00_rep2.zip::results/analysis/paper7_prod_anthropic_clean_t00_paired_deltas.csv`
  - `results/paper7_results_stage1_t00_rep2.zip::results/analysis/paper7_prod_gemini_clean_t00_paired_deltas.csv`
  - `results/paper7_results_stage1_t00_rep2.zip::results/analysis/paper7_prod_openai_clean_t00_paired_deltas.csv`
- Stage2 separated robustness source members:
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t03.csv`
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_allproviders_paired_deltas_merged_t03.csv`
- Stage2 provider-specific raw members used for the provider-separated table and the strongest Branch tail-risk sentence:
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_prod_anthropic_clean_t03_paired_deltas.csv`
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_prod_gemini_clean_t03_paired_deltas.csv`
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_prod_openai_clean_t03_paired_deltas.csv`

## Shipped commands

- Scripts reference:
  - `./scripts/README.md`
- Build the current manuscript to a temp output dir:
  - `./scripts/build_current_manuscript.sh`
  - default output: `/tmp/nrr-patterns_current_build/paper7_integrated_manuscript_v0_29_2026-04-01.pdf`
- Verify the active review surface:
  - `./scripts/verify_active_review_surface.sh`
- Verify the current review-package checksum manifest:
  - `./scripts/verify_current_package.sh`
- Verify the broader audit release surface:
  - `./scripts/verify_audit_surface.py repro/paper7_integrated_audit_surface_sha256_v19_2026-04-01.txt`
- Rebuild shipped summary CSVs from bundled artifacts:
  - `python3 ./scripts/aggregate_comparison_r2.py`
  - `python3 ./scripts/build_paper7_integrated_comparison_headline_summary.py`
  - `python3 ./scripts/build_paper7_provider_separated_stability_summary.py`
  - `python3 ./scripts/verify_provider_separated_summary.py`
  - `python3 ./scripts/verify_zip_member_refs.py --help`

## Verification

```bash
cd <repo-root>
./scripts/verify_active_review_surface.sh
./scripts/verify_current_package.sh
```

This checks:
- the active review surface under `manuscript/current/`
- the current manuscript checksum manifest
- the review-package checksum manifest
- the broader audit-surface checksum manifest
- reviewer-facing `repro/` references named by the current manuscript and package map
- reviewer-facing `zip::member` references named by the current manuscript and shipped guides
- reviewer-facing docs for paths that should not appear in the bounded audit ZIP

## Build

```bash
cd <repo-root>
./scripts/build_current_manuscript.sh
```

## Inspect nested members

List bundled members before opening them:

```bash
cd <repo-root>
unzip -l results/paper7_results_allproviders_clean.zip
unzip -l results/paper7_results_stage2_t03.zip
```

Read the exact nested source members used by the current manuscript:

```bash
cd <repo-root>
unzip -p results/paper7_results_allproviders_clean.zip \
  results/analysis/paper7_allproviders_pattern_summary_robust_t00.csv | head
unzip -p results/paper7_results_stage2_t03.zip \
  results/analysis/paper7_allproviders_paired_deltas_merged_t03.csv | head
```

## Package boundary

This `NRR-Patterns` authority package is intentionally narrower than a full rerun workspace. It ships
the current manuscript package, the released claim-trace artifacts, and the
verification/build scripts needed to inspect that surface. It does not attempt
to act as a full environment bootstrap or a full historical archive dump.
