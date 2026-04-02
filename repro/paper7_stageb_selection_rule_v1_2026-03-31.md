# Integrated paper7 Stage B selection rule v1

## Purpose

This file freezes the paper-local rule for what enters the integrated `paper7`
boundary-honesty layer from Stage B. It is an integration rule for this
comparison-led manuscript, not a claim that the full Stage B program was
originally preregistered for paper7 itself.

## Boundary-layer objective

- The role of Stage B inside integrated `paper7` is narrow:
  - make the comparison-side pattern map honest about provider-sensitive
    weakening, reversal, and non-effective regions
- The role of Stage B inside integrated `paper7` is not:
  - replace the main comparison spine
  - reopen the full operator-boundary paper
  - promote every Stage B diagnostic into the main text

## Selection rule

Keep a Stage B artifact in the integrated manuscript only if it serves at least
one of the following paper-local honesty roles:

1. It gives the minimal manuscript-facing provider-balanced carry-forward read on
   the retained key quality/cost metrics.
2. It exposes provider-separated reversal or zero-mass that a pooled summary
   would hide.
3. It supplies a compact sign-flip surface for direct honesty reporting.
4. It supplies a multiplicity-controlled confirmatory summary that prevents
   over-reading noisy carry-forward cells.

Artifacts that mainly elaborate the broader operator-boundary story without
changing the comparison-led read stay package-first rather than main-text
central.

## Retained manuscript-facing key metrics

- `misinterpretation_rate`
- `rework_cost_tokens`

These are retained because they are the smallest downstream quality/cost pair
that can make the five-pattern comparison map honest without turning integrated
`paper7` into a second boundary-led manuscript.

## Retained Stage B artifacts

- `nrr-boundary/stats/stageb_all/mst_provider_balanced.csv`
  - manuscript-facing balanced carry-forward summary for the retained key metrics
- `nrr-boundary/stats/stageb_all/mst_provider_separated.csv`
  - provider-separated honesty surface used to expose reversal, zero, and sparse
    carry-forward behavior
- `nrr-boundary/stats/stageb_all/mst_sign_flip_boundaries.csv`
  - compact sign-flip map for direct honesty reporting
- `nrr-boundary/stats/stageb_all/stageb_confirmatory_tests_holm30.csv`
  - confirmatory summary used to anchor sparse/nonzero counts and Holm-filtered
    carry-forward claims

## Main-text reporting rule

- The manuscript may summarize the retained key metrics in provider-balanced
  form.
- Any strong carry-forward reading must be checked against:
  - provider-separated reversal/zero structure
  - `n_nonzero` mass in the confirmatory summary
- Main-text non-effective reporting is limited to a compact all-provider-zero
  slice so the honesty layer stays readable.
- Fuller zero/negative mass remains available in the shipped provider-separated
  artifact.

## Demotion rule

- Diagnostics that would mainly expand a separate Stage B story remain
  appendix/package-first unless they materially alter the comparison-led
  interpretation.
- This includes broader operator-boundary elaboration that is useful for repo
  completeness but not necessary for the paper-local honesty contract.
