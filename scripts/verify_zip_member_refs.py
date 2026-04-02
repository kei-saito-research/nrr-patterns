#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path
from zipfile import ZipFile


ZIP_MEMBER_RE = re.compile(r"(results/[^\s`}\\]+\.zip::[^\s`}\\]+)")


def sha256_bytes(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_claims_manifest(path: Path) -> dict[tuple[str, str], tuple[str, str]]:
    entries: dict[tuple[str, str], tuple[str, str]] = {}
    with path.open("r", encoding="utf-8") as f:
        next(f, None)
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split(",", 8)
            if len(parts) < 9:
                continue
            archive_path = parts[3]
            member_path = parts[4]
            archive_sha = parts[5]
            member_sha = parts[6]
            if member_path:
                entries[(archive_path, member_path)] = (archive_sha, member_sha)
    return entries


def collect_refs(source_files: list[Path]) -> dict[str, list[str]]:
    refs: dict[str, list[str]] = {}
    for source in source_files:
        text = source.read_text(encoding="utf-8")
        for ref in ZIP_MEMBER_RE.findall(text):
            refs.setdefault(ref, []).append(str(source))
    return refs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--claims-manifest", required=True)
    parser.add_argument("sources", nargs="+")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    claims_manifest = Path(args.claims_manifest).resolve()
    source_files = [Path(p).resolve() for p in args.sources]

    pinned = load_claims_manifest(claims_manifest)
    refs = collect_refs(source_files)

    ok = True
    for ref, origins in sorted(refs.items()):
        archive_rel, member_path = ref.split("::", 1)
        archive_path = root / archive_rel
        if not archive_path.exists():
            print(f"MISSING_ARCHIVE  {ref}  from {origins[0]}")
            ok = False
            continue

        with ZipFile(archive_path) as zf:
            names = set(zf.namelist())
            if member_path not in names:
                print(f"MISSING_MEMBER  {ref}  from {origins[0]}")
                ok = False
                continue
            member_bytes = zf.read(member_path)

        observed_archive_sha = sha256_file(archive_path)
        observed_member_sha = sha256_bytes(member_bytes)
        pinned_hashes = pinned.get((archive_rel, member_path))
        if pinned_hashes is None:
            print(f"UNPINNED_MEMBER  {ref}  from {origins[0]}")
            ok = False
            continue

        expected_archive_sha, expected_member_sha = pinned_hashes
        if expected_archive_sha and expected_archive_sha != observed_archive_sha:
            print(f"FAIL_ARCHIVE_SHA  {ref}  from {origins[0]}")
            ok = False
            continue
        if expected_member_sha and expected_member_sha != observed_member_sha:
            print(f"FAIL_MEMBER_SHA  {ref}  from {origins[0]}")
            ok = False
            continue

        print(f"OK_ZIP_MEMBER  {ref}")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
