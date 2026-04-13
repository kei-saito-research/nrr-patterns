#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CURRENT_DIR="$ROOT/manuscript/current"
FIGURES_DIR="$ROOT/manuscript/figures"
MANIFEST="$ROOT/manuscript/checksums_active_review_surface_sha256.txt"

current_files=()
while IFS= read -r file; do
  current_files+=("$file")
done < <(find "$CURRENT_DIR" -maxdepth 1 -type f | LC_ALL=C sort)

tex_files=()
while IFS= read -r file; do
  tex_files+=("$file")
done < <(find "$CURRENT_DIR" -maxdepth 1 -type f -name 'nrr_patterns_manuscript_v*.tex' | LC_ALL=C sort)

pdf_files=()
while IFS= read -r file; do
  pdf_files+=("$file")
done < <(find "$CURRENT_DIR" -maxdepth 1 -type f -name 'nrr_patterns_manuscript_v*.pdf' | LC_ALL=C sort)

png_files=()
while IFS= read -r file; do
  png_files+=("$file")
done < <(find "$FIGURES_DIR" -maxdepth 1 -type f -name '*.png' | LC_ALL=C sort)

if [ ! -f "$MANIFEST" ]; then
  echo "Missing active review surface manifest: $MANIFEST" >&2
  exit 1
fi

if [ "${#current_files[@]}" -ne 2 ]; then
  echo "Active review surface must contain exactly 2 files in $CURRENT_DIR" >&2
  exit 1
fi

if [ "${#tex_files[@]}" -ne 1 ] || [ "${#pdf_files[@]}" -ne 1 ] || [ "${#png_files[@]}" -ne 3 ]; then
  echo "Active review surface must contain exactly one manuscript .tex and .pdf in $CURRENT_DIR, plus three figure .png files in $FIGURES_DIR" >&2
  exit 1
fi

tex_base="$(basename "${tex_files[0]}" .tex)"
pdf_base="$(basename "${pdf_files[0]}" .pdf)"
if [ "$tex_base" != "$pdf_base" ]; then
  echo "Current manuscript .tex and .pdf basenames do not match: $tex_base vs $pdf_base" >&2
  exit 1
fi

cd "$ROOT"
shasum -a 256 -c "manuscript/$(basename "$MANIFEST")"
