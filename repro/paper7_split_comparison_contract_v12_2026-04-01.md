# Integrated paper7 split comparison contract v12

## Purpose

This file freezes the paper-local comparison contract for the derived
integrated `paper7` split-comparison line. It replaces the earlier
`fixed paired protocol` wording with an explicit separation between:

- the headline exact-replication spine
- the carried-forward temperature-robustness member

It is not a full rerun bundle and does not attempt to restate every prompt
template.

## Canonical paired unit

- The basic unit is a baseline-vs-pattern pair executed under the same:
  - scenario
  - repetition
  - provider
  - model
  - temperature
- The comparison uses the paired token outcome for that matched row rather than
  an unmatched aggregate across different prompts or providers.

## Headline exact-replication spine

- `stage1_main`
  - `results/paper7_results_allproviders_clean.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t00.csv`
- `stage1_rep2`
  - `results/paper7_results_stage1_t00_rep2.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t00.csv`

These two source members define the headline exact-replication spine for the
integrated manuscript because they keep the paired unit and operative
temperature fixed at `t=0.0`.

## Separated temperature-robustness member

- `stage2_t03`
  - `results/paper7_results_stage2_t03.zip::results/analysis/paper7_allproviders_pattern_summary_robust_t03.csv`

This member is retained to test whether the same paired comparison object
survives a controlled condition shift. It is part of the manuscript's
robustness read, but it is not folded into the headline exact-replication mean.

## Provider/model scope

- Providers/models carried by the split comparison surface:
  - `gemini-2.0-flash`
  - `claude-sonnet-4-20250514`
  - `gpt-4o-mini-2024-07-18`
- Patterns:
  - `hierarchical`
  - `lazy`
  - `branch`
  - `delta`
  - `conditional`
- Temperature on the split surface:
  - `t=0.0` for `stage1_main`
  - `t=0.0` for `stage1_rep2`
  - `t=0.3` for `stage2_t03` as the separated robustness member

## Fairness constraints carried into integrated paper7

- No outcome-based rerun is allowed.
- Transport/API retry is allowed only for failure recovery, not for
  result-dependent replacement.
- Pattern-vs-baseline contrasts keep the intended turn structure aligned within
  each pattern family rather than comparing unrelated interaction lengths.
- The manuscript reads these members as one comparison program only because the
  paired unit, provider set, pattern set, and fairness constraints are held
  fixed across the headline spine and the separated robustness member.

## Headline metric contract

- For each provider within a given run member and pattern, compute the
  provider-level weighted reduction percentage as:
  - `100 * sum(reduction_tokens) / sum(baseline_tokens)`
- In the shipped robust source members, that provider-level weighted reduction
  is the quantity that feeds `weighted_percent_provider_balanced`.
- The run-level provider-balanced quantity is the simple arithmetic mean of
  those provider-level weighted percentages across the shipped providers for
  that run member.
- The integrated headline summary
  `results/analysis/paper7_integrated_comparison_headline_summary_v2_2026-03-31.csv`
  records those run-level values.
- The manuscript-facing provider-separated stability summary
  `results/analysis/paper7_provider_separated_stability_summary_v2_2026-04-01.csv`
  records the provider-level weighted percentages for the two exact-replication
  runs and the separated Stage2 member, together with negative-provider flags
  and, only when a Stage2 negative provider exists, worst-row outlier context
  for the most-negative Stage2 provider.
- The manuscript headline mean is the exact-replication mean:
  - `(stage1_main + stage1_rep2) / 2`
- The `stage2_t03` value is reported separately as the temperature-robustness
  member and is not averaged into the headline mean.

## Support-volume contract

- `Paired rows/run` in the manuscript is the paired-row count per run member
  for the shipped robust comparison source behind that pattern.
- On the current split surface:
  - `hierarchical`, `lazy`, and `branch` carry `n_all=45` per run
  - `delta` and `conditional` carry `n_all=18` per run

## Relationship to the larger repo

- This split comparison contract freezes the comparison read for the derived
  integrated `paper7` line only.
- It should be read together with:
  - `repro/paper7_integrated_comparison_claims_manifest_v6_2026-04-01.csv`
  - `repro/paper7_integrated_package_map_v19_2026-04-01.md`
- The historical predecessor spec
  `repro/paper7_fixed_paired_protocol_spec_v7_2026-04-01.md` is shipped only as
  a superseded provenance note for the contract transition and must not be used
  as the active headline-comparison contract for the integrated manuscript.
- It does not supersede broader repo-level experiment history or archived
  preregistration notes.
