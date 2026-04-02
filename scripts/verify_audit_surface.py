#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import sys
from pathlib import Path


def resolve_candidate(root: Path, rel_path: str) -> Path:
    direct = root / rel_path
    if direct.exists():
        return direct
    if rel_path.startswith("nrr-boundary/"):
        sibling = root / ".." / rel_path
        sibling = sibling.resolve()
        if sibling.exists():
            return sibling
    return direct


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_audit_surface.py <manifest>", file=sys.stderr)
        return 2

    manifest_path = Path(sys.argv[1]).resolve()
    root = manifest_path.parents[1]
    ok = True

    with manifest_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            expected, rel_path = line.split("  ", 1)
            target = resolve_candidate(root, rel_path)
            if not target.exists():
                print(f"MISSING  {rel_path}")
                ok = False
                continue
            observed = sha256_file(target)
            if observed != expected:
                print(f"FAIL  {rel_path}")
                ok = False
            else:
                print(f"OK  {rel_path}")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
