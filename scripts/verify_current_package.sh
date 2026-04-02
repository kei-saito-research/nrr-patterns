#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CURRENT_DIR="$ROOT/manuscript/current"
REPRO_DIR="$ROOT/repro"
REPRO_MANIFEST="$REPRO_DIR/paper7_integrated_repro_checksums_sha256.txt"
AUDIT_MANIFEST="$(find "$REPRO_DIR" -maxdepth 1 -type f -name 'paper7_integrated_audit_surface_sha256_v*.txt' | sort -V | tail -n 1)"

"$ROOT/scripts/verify_active_review_surface.sh"

cd "$REPRO_DIR"
if [ -f "$REPRO_MANIFEST" ]; then
  shasum -a 256 -c "$(basename "$REPRO_MANIFEST")"
fi

cd "$ROOT"
if [ -z "$AUDIT_MANIFEST" ]; then
  echo "No paper7 integrated audit manifest found in $REPRO_DIR" >&2
  exit 1
fi
python3 scripts/verify_audit_surface.py "$AUDIT_MANIFEST"

LATEST_TEX="$(find "$CURRENT_DIR" -maxdepth 1 -type f -name 'paper7_integrated_manuscript_v*.tex' | sort -V | tail -n 1)"
LATEST_COMPARISON_MANIFEST="$(find "$REPRO_DIR" -maxdepth 1 -type f -name 'paper7_integrated_comparison_claims_manifest_v*.csv' | sort -V | tail -n 1)"
LATEST_PACKAGE_MAP="$(find "$REPRO_DIR" -maxdepth 1 -type f -name 'paper7_integrated_package_map_v*.md' | sort -V | tail -n 1)"
LATEST_SPLIT_CONTRACT="$(find "$REPRO_DIR" -maxdepth 1 -type f -name 'paper7_split_comparison_contract_v*.md' | sort -V | tail -n 1)"
LATEST_FIXED_PROTOCOL_NOTE="$(find "$REPRO_DIR" -maxdepth 1 -type f -name 'paper7_fixed_paired_protocol_spec_v*.md' | sort -V | tail -n 1)"

check_repro_refs_in_audit_manifest() {
  local source_file="$1"
  local refs_pattern="$2"
  local ref
  local audit_rel="repro/$(basename "$AUDIT_MANIFEST")"
  local repro_rel="repro/$(basename "$REPRO_MANIFEST")"

  while IFS= read -r ref; do
    [ -z "$ref" ] && continue
    if [ ! -f "$ROOT/$ref" ]; then
      echo "Missing reviewer-facing reference: $ref (from $source_file)" >&2
      exit 1
    fi
    if [ "$ref" = "$audit_rel" ] || [ "$ref" = "$repro_rel" ]; then
      continue
    fi
    if ! grep -Fq "  $ref" "$AUDIT_MANIFEST"; then
      echo "Audit manifest is missing reviewer-facing reference: $ref (from $source_file)" >&2
      exit 1
    fi
  done < <(grep -oE "$refs_pattern" "$source_file" | sort -u || true)
}

check_repro_refs_in_audit_manifest "$LATEST_TEX" 'repro/[^}]+' 
check_repro_refs_in_audit_manifest "$LATEST_PACKAGE_MAP" 'repro/[^` ]+'
check_repro_refs_in_audit_manifest "$LATEST_SPLIT_CONTRACT" 'repro/[^` ]+'
check_repro_refs_in_audit_manifest "$LATEST_FIXED_PROTOCOL_NOTE" 'repro/[^` ]+'

python3 scripts/verify_zip_member_refs.py \
  --root "$ROOT" \
  --claims-manifest "$LATEST_COMPARISON_MANIFEST" \
  "$LATEST_TEX" \
  "$ROOT/README.md" \
  "$ROOT/reproducibility.md" \
  "$LATEST_SPLIT_CONTRACT" \
  "$LATEST_FIXED_PROTOCOL_NOTE"

python3 scripts/verify_provider_separated_summary.py

check_review_docs_for_omitted_refs() {
  local doc
  local ref
  local -a docs=("$ROOT/README.md" "$ROOT/reproducibility.md")
  local -a forbidden_refs=(
    "./scripts/run_all.sh"
    "./scripts/generate_manuscript_figures.sh"
    "./scripts/run_no_position_ablation.sh"
    "requirements.txt"
    "configs/"
    "results/figures/"
    "manuscript/archive/"
    "LICENSE"
    "results/analysis/paper7_allproviders_pattern_summary_robust.csv"
    "results/analysis/paper7_allproviders_paired_deltas_merged.csv"
  )

  for doc in "${docs[@]}"; do
    for ref in "${forbidden_refs[@]}"; do
      if grep -Fq "$ref" "$doc"; then
        echo "Review-package doc still references omitted surface: $ref (in $doc)" >&2
        exit 1
      fi
    done
  done
}

check_review_docs_for_omitted_refs
