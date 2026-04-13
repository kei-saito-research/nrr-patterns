# NRR-Patterns package map v20

## Purpose

This file freezes the reviewer-facing source-of-truth names for NRR-Patterns
after the current provider-separated comparison refresh. The current release
surface keeps one comparison headline summary in-package while also
shipping a compact provider-separated stability summary plus the canonical
upstream source members for drill-down inside the same audit surface.

## Canonical evidence roles

- Main comparison spine
  - manifest: `repro/nrr_patterns_comparison_claims_manifest_v7_2026-04-12.csv`
  - status: active
  - role: fixed paired comparison over the five delayed-commitment patterns, with explicit unequal support volume across patterns
  - reviewer-facing summary: `results/analysis/nrr_patterns_comparison_headline_summary_v3_2026-04-12.csv`
  - reviewer-facing provider-separated summary: `results/analysis/nrr_patterns_provider_separated_stability_summary_v3_2026-04-12.csv`
- Paper-local comparison contract
  - spec: `repro/nrr_patterns_split_comparison_contract_v13_2026-04-12.md`
  - status: active
  - role: freezes the NRR-Patterns's exact-replication headline, provider-separated stability read, separated robustness member, fairness constraints, run members, and support-volume interpretation
- Historical comparison contract
  - spec: `repro/nrr_patterns_fixed_paired_protocol_spec_v8_2026-04-12.md`
  - status: shipped as a superseded provenance note only
  - role: preserves the pre-split contract transition story in a non-active form, but it is not part of the active reviewer-facing source-of-truth path
- Compression control
  - manifest: `repro/nrr_patterns_comparison_claims_manifest_v7_2026-04-12.csv`
  - status: active
  - role: compact main-text control against a generic prompt-shortening explanation for the retained three-pattern subset
- Boundary honesty layer
  - manifest: `repro/nrr_patterns_boundary_claims_manifest_v2_2026-04-12.csv`
  - status: active
  - role: selected Stage B carry-forward for provider-sensitive weakening, sign-flip, and non-effective reporting
- Paper-local Stage B selection rule
  - spec: `repro/nrr_patterns_stageb_selection_rule_v2_2026-04-12.md`
  - status: active
  - role: freezes why the retained Stage B artifacts enter the current NRR-Patterns manuscript while broader boundary elaboration stays package-first
- Appendix/package-first surfaces
  - manifest: `repro/nrr_patterns_comparison_claims_manifest_v7_2026-04-12.csv`
  - status: demoted by default
  - role: no-position robustness and other non-mainline surfaces

## Reading order

1. Read the current NRR-Patterns manuscript.
2. Read the comparison headline summary, then the provider-separated stability summary, then the split comparison contract and the comparison claims manifest for source-level drill-down and the retained three-pattern compression control.
3. Read the Stage B selection rule, then the boundary claims manifest for selected Stage B honesty carry-forward.
4. Use `repro/nrr_patterns_audit_surface_sha256_v20_2026-04-12.txt` together with `scripts/verify_audit_surface.py` to verify the shipped audit surface.

## Scope rule

- `ordered-combination` remains outside the default NRR-Patterns mainline.
- `no-position` remains appendix/package-first unless later manuscript pressure makes promotion necessary.
- NRR-Patterns uses `Stage B` to make the comparison map honest, not to replace the comparison spine.
- The current audit surface ships `no-position` as an appendix/package-first artifact but keeps `ordered-combination` demoted out of the default release surface.
- The current release surface is auditable claim-trace packaging, not a full end-to-end rerun bundle.

## Release-surface note

This v20 package map keeps the reviewer-facing comparison headline on one explicit
matched-run summary artifact while also exposing a compact
provider-separated stability summary for the same surface. It also makes the
split comparison contract, its shipped historical predecessor, and the Stage B
selection rule explicit, so the shipped comparison, appendix, and selected
honesty artifacts can be verified as a release surface rather than merely named
in prose. In addition, the manuscript's IME / Transfer / Coupled context-only
series-path citations are now frozen to fixed repository tree snapshots rather
than moving repo-root URLs. The shipped predecessor note is now explicitly
non-active, so the reviewer-facing audit surface presents only one active
comparison contract. The shipped root-level review guides are also narrowed to
the bounded audit ZIP itself and distinguish top-level shipped artifacts from
nested ZIP members. The canonical comparison claims manifest now also pins the
provider-specific paired-delta members used to build the provider-separated
summary, alongside the merged paired-delta drill-down members and the raw
Stage2 Gemini paired-delta member used for the strongest Branch tail-risk
sentence. The shipped verify path now also checks provider-separated summary
invariants directly, so `none` negative-provider rows cannot silently ship with
populated most-negative context fields. In addition, the current
NRR-Patterns manuscript now re-anchors the context-only Transfer citation to the
actual `v123` manuscript title and cited-tree wording, so the fixed series-path
reference description matches the frozen snapshot it names. The same fixed-tree
snapshot wording contract is now also applied consistently to the Coupled
series-path citation. The current NRR-Patterns manuscript front matter now states
the fixed matched-run comparison spine separately from the selected Stage B
honesty carry-forward, so sign-flip and non-effective regions are not presented
as if they came from the same headline evidence role. Here, exact replication
names the fixed matched-run output surface summarized and traced in-package;
the current release surface audits that output surface rather than providing an
independent rerun handoff.
