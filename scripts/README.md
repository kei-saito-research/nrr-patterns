# Scripts

This directory contains the stable build and verification wrappers for the
current NRR-Patterns repository surface.

The wrappers below verify the fixed manuscript and artifact surface for the
current repository snapshot.

## Stable entrypoints

- `build_current_manuscript.sh`
  - builds the current manuscript in `manuscript/current/` to a temp output directory
- `verify_active_review_surface.sh`
  - verifies `manuscript/current/`, the figure assets under `manuscript/figures/`, and `manuscript/checksums_active_review_surface_sha256.txt`
- `verify_current_package.sh`
  - verifies the active manuscript surface first, then checks the shipped artifact and reproducibility manifests

These entrypoints define the stable package interface for the current
repository surface.
