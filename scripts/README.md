# Scripts

This directory contains the stable build and verification wrappers for the
current NRR-Patterns repository surface.

Released manuscript and package artifacts still use the integrated `paper7`
stem for continuity, so the wrappers below verify that fixed release surface
without renaming any shipped artifact stems.

## Stable entrypoints

- `build_current_manuscript.sh`
  - builds the current manuscript in `manuscript/current/` to a temp output directory
- `verify_active_review_surface.sh`
  - verifies the pair-only `manuscript/current/` review surface, the figure assets under `manuscript/figures/`, and `manuscript/checksums_active_review_surface_sha256.txt`
- `verify_current_package.sh`
  - verifies the active review surface first, then checks the shipped audit and reproducibility manifests

These entrypoints define the stable reviewer-facing package interface for the
current repository surface.
