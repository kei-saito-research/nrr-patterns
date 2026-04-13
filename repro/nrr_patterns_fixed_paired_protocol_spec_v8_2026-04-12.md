# NRR-Patterns fixed paired protocol spec v8

## Status

- This file is a provenance-only historical predecessor note.
- It is not the active comparison contract for the current NRR-Patterns
  release surface.
- The active comparison contract is:
  - `repro/nrr_patterns_split_comparison_contract_v13_2026-04-12.md`
- The current reviewer-facing package freeze is:
  - `repro/nrr_patterns_package_map_v20_2026-04-12.md`

## Purpose

This note preserves the earlier `fixed paired protocol` read so the contract
transition remains inspectable without presenting that earlier read as current
source-of-truth. It records what the older package line meant before the split
comparison contract was introduced.

## Historical predecessor summary

- Earlier predecessor read:
  - treated `stage1_main`, `stage1_rep2`, and `stage2_t03` as one carried
    comparison spine
  - summarized that surface through a three-run mean
- Current active read:
  - uses `stage1_main` and `stage1_rep2` as the headline exact-replication
    spine
  - keeps `stage2_t03` as a separated robustness member
  - does not average `stage2_t03` into the headline mean

## Canonical paired unit that remains shared

- The basic unit remains a baseline-vs-pattern pair executed under the same:
  - scenario
  - repetition
  - provider
  - model
  - temperature
- The comparison still uses the paired token outcome for that matched row
  rather than an unmatched aggregate across different prompts or providers.

## Historical predecessor members

- `stage1_main`
  - `results/nrr_patterns_results_allproviders_clean.zip::results/analysis/nrr_patterns_allproviders_pattern_summary_robust_t00.csv`
- `stage1_rep2`
  - `results/nrr_patterns_results_stage1_t00_rep2.zip::results/analysis/nrr_patterns_allproviders_pattern_summary_robust_t00.csv`
- `stage2_t03`
  - `results/nrr_patterns_results_stage2_t03.zip::results/analysis/nrr_patterns_allproviders_pattern_summary_robust_t03.csv`

These members are kept here only to document the predecessor read. They must
not be used as the current headline-contract definition for the reviewer-facing
package.

## Supersession map

- Superseded predecessor claim:
  - `three-run spine / three-run mean`
- Replacement current claim:
  - `two-run exact-replication headline + separated Stage2 robustness member`
- Active source-of-truth files:
  - `repro/nrr_patterns_split_comparison_contract_v13_2026-04-12.md`
  - `repro/nrr_patterns_comparison_claims_manifest_v7_2026-04-12.csv`
  - `repro/nrr_patterns_package_map_v20_2026-04-12.md`
  - `results/analysis/nrr_patterns_comparison_headline_summary_v3_2026-04-12.csv`
  - `results/analysis/nrr_patterns_provider_separated_stability_summary_v3_2026-04-12.csv`

## Boundary on use

- This note is shipped only to preserve transition traceability.
- If any wording here conflicts with the active split contract or the package
  map, the active split contract and package map control.
- This note does not supersede broader repo-level experiment history or
  archived preregistration notes.
