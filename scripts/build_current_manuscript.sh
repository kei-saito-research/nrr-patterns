#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CURRENT_DIR="$ROOT/manuscript/current"
INTEGRATED_TEX="$(find "$CURRENT_DIR" -maxdepth 1 -type f -name 'paper7_integrated_manuscript_v*.tex' | sort -V | tail -n 1)"
MAIN_TEX=""

if [ -f "$INTEGRATED_TEX" ]; then
  MAIN_TEX="$INTEGRATED_TEX"
else
  MAIN_TEX="$(find "$CURRENT_DIR" -maxdepth 1 -type f -name 'nrr-principles_manuscript_v*.tex' | sort -V | tail -n 1)"
fi
OUT_DIR="${1:-/tmp/nrr-patterns_current_build}"

if [ -z "$MAIN_TEX" ]; then
  echo "No current manuscript TeX found in $CURRENT_DIR" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"
cd "$CURRENT_DIR"
tectonic -X compile --outdir "$OUT_DIR" "$(basename "$MAIN_TEX")"
