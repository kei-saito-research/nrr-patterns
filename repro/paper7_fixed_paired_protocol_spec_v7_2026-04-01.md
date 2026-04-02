# Integrated paper7 fixed paired protocol spec v7

## Status

- This file is a provenance-only historical predecessor note.
- It is not the active comparison contract for the current integrated `paper7`
  release surface.
- The active comparison contract is:
  - `repro/paper7_split_comparison_contract_v12_2026-04-01.md`
- The current reviewer-facing package freeze is:
  - `repro/paper7_integrated_package_map_v19_2026-04-01.md`

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
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t00.csv`
- `stage1_rep2`
  - `results/paper7_results_stage1_t00_rep2.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t00.csv`
- `stage2_t03`
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t03.csv`

These members are kept here only to document the predecessor read. They must
not be used as the current headline-contract definition for the reviewer-facing
package.

## Supersession map

- Superseded predecessor claim:
  - `three-run spine / three-run mean`
- Replacement current claim:
  - `two-run exact-replication headline + separated Stage2 robustness member`
- Active source-of-truth files:
  - `repro/paper7_split_comparison_contract_v12_2026-04-01.md`
  - `repro/paper7_integrated_comparison_claims_manifest_v6_2026-04-01.csv`
  - `repro/paper7_integrated_package_map_v19_2026-04-01.md`
  - `results/analysis/paper7_integrated_comparison_headline_summary_v2_2026-03-31.csv`
  - `results/analysis/paper7_provider_separated_stability_summary_v2_2026-04-01.csv`

## Boundary on use

- This note is shipped only to preserve transition traceability.
- If any wording here conflicts with the active split contract or the package
  map, the active split contract and package map control.
- This note does not supersede broader repo-level experiment history or
  archived preregistration notes.
