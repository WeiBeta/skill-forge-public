"""Build or check a public source bundle offline with Python's standard library."""
# SPDX-License-Identifier: AGPL-3.0-only

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import stat
import sys
import unicodedata
import zipfile

MANIFEST = "PUBLIC-MANIFEST.json"
STAMP = (1980, 1, 1, 0, 0, 0)
MAX_FILE = 32 * 1024**2
MAX_TOTAL = 128 * 1024**2
MAX_MEMBERS = 512
MAX_ARCHIVE = MAX_TOTAL + 1024**2
LICENSE = "AGPL-3.0-only"
CORE_SKILLS = (
    "code-review", "diagnosing-bugs", "domain-modeling", "writing-for-agents", "work-dispatch",
    "agent-recovery", "ledger-reconcile", "feedback",
)
LEGACY_FIVE_CORE_VERSIONS = {"0.2.1", "0.3.0"}
LEGACY_SEVEN_CORE_VERSIONS = {"0.3.1", "0.3.2"}
REQUIRED = {
    "README.md", "README.zh-CN.md", "assets/hero.png", "release.json", "LICENSE",
    "third_party/mattpocock/LICENSE.txt", "scripts/public_package.py",
} | {f"skills/forge-{name}/SKILL.md" for name in CORE_SKILLS}
VERSION = re.compile(r"(?:0|[1-9][0-9]{0,8})(?:\.(?:0|[1-9][0-9]{0,8})){2}")
SHA256 = re.compile(r"[0-9a-f]{64}")
DEVICE = re.compile(r"(?:con|prn|aux|nul|com[0-9]|lpt[0-9]|conin\$|conout\$)(?:\..*)?")


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_object(data, label):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result

    try:
        value = json.loads(data.decode("utf-8"), object_pairs_hook=unique)
    except (UnicodeError, ValueError, RecursionError):
        raise ValueError(f"{label}: invalid JSON") from None
    if not isinstance(value, dict):
        raise ValueError(f"{label}: expected an object")
    return value


def safe_name(name):
    if not isinstance(name, str) or len(name) > 240:
        raise ValueError("Invalid portable path")
    for part in name.split("/"):
        key = unicodedata.normalize("NFKC", part).casefold()
        if (
            not key or key in {".", "..", ".git", "git~1"} or key.endswith((" ", "."))
            or any(c in key for c in '\\/:<>"|?*')
            or any(unicodedata.category(c).startswith("C") for c in part)
            or DEVICE.fullmatch(key)
            or part != unicodedata.normalize("NFC", part)
        ):
            raise ValueError("Invalid portable path")


def validate_names(names):
    # Check each prefix as well as the leaf: Docs/a and docs/b conflict on Windows.
    prefixes = {}
    leaves = set()
    for name in names:
        safe_name(name)
        if name in leaves:
            raise ValueError("Duplicate member path")
        leaves.add(name)
        parts = name.split("/")
        for end in range(1, len(parts) + 1):
            prefix = "/".join(parts[:end])
            key = unicodedata.normalize("NFKC", prefix).casefold()
            if prefixes.setdefault(key, prefix) != prefix:
                raise ValueError("Case or Unicode collision in member paths")
    for name in leaves:
        parts = name.split("/")
        if any("/".join(parts[:end]) in leaves for end in range(1, len(parts))):
            raise ValueError("File and directory paths collide")


def plain_stat(path):
    info = path.lstat()
    if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
        raise ValueError("Symbolic link or reparse point rejected")
    return info


def local_path(path):
    path = Path(path).absolute()
    if ".." in path.parts or str(path).startswith(("\\\\", "//")):
        raise ValueError("Use a normalized local filesystem path")
    for entry in reversed((path, *path.parents)):
        if os.path.lexists(entry):
            plain_stat(entry)
    return path


def read_file(path, limit=MAX_FILE):
    info = plain_stat(path)
    if not stat.S_ISREG(info.st_mode) or info.st_size > limit:
        raise ValueError("Expected a bounded regular file")
    with path.open("rb") as stream:
        data = stream.read(info.st_size + 1)
    if len(data) != info.st_size:
        raise ValueError("File changed while reading")
    return data


def directories_for(names):
    return {name.rsplit("/", i)[0] for name in names for i in range(1, name.count("/") + 1)}


def read_tree(path, *, ignore_git=False):
    root = local_path(path)
    if not root.is_dir():
        raise ValueError("Expected a source directory")
    files, directories = {}, set()
    total = 0

    def visit(directory):
        nonlocal total
        for entry in directory.iterdir():
            info = plain_stat(entry)
            relative = entry.relative_to(root).as_posix()
            if ignore_git and relative == ".git":
                if not (stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode)):
                    raise ValueError("Invalid repository metadata path")
                continue
            safe_name(relative)
            if len(directories) + len(files) >= 2 * MAX_MEMBERS:
                raise ValueError("Too many source entries")
            if stat.S_ISDIR(info.st_mode):
                directories.add(relative)
                visit(entry)
            else:
                data = read_file(entry)
                total += len(data)
                if len(files) >= MAX_MEMBERS or total > MAX_TOTAL:
                    raise ValueError("Public source exceeds size limits")
                files[relative] = data

    visit(root)
    validate_names(files)
    if directories != directories_for(files):
        raise ValueError("Unexpected empty directory in public source")
    return files


def release_identity(files, *, allow_legacy=False):
    if "release.json" not in files:
        raise ValueError("Required public source files are missing")
    data = json_object(files["release.json"], "public release.json")
    core = CORE_SKILLS
    if allow_legacy and data.get("product_version") in LEGACY_FIVE_CORE_VERSIONS:
        core = CORE_SKILLS[:5]
    elif allow_legacy and data.get("product_version") in LEGACY_SEVEN_CORE_VERSIONS:
        core = CORE_SKILLS[:7]
    required = (REQUIRED - {f"skills/forge-{name}/SKILL.md" for name in CORE_SKILLS}) | {
        f"skills/forge-{name}/SKILL.md" for name in core
    }
    if not required <= files.keys():
        raise ValueError("Required public source files are missing")
    if (
        set(data) != {"schema_version", "product_version", "public_revision", "license", "core_skills"}
        or type(data["schema_version"]) is not int or data["schema_version"] != 1
        or not isinstance(data["product_version"], str) or not VERSION.fullmatch(data["product_version"])
        or type(data["public_revision"]) is not int or not 1 <= data["public_revision"] <= 999_999
        or data["license"] != LICENSE or data["core_skills"] != list(core)
    ):
        raise ValueError("Invalid public release identity")
    return {key: data[key] for key in ("product_version", "public_revision")}


def make_manifest(files, *, allow_legacy=False):
    validate_names([*files, MANIFEST])
    identity = release_identity(files, allow_legacy=allow_legacy)
    items = [
        {"path": name, "bytes": len(data), "sha256": digest(data)}
        for name, data in sorted(files.items())
    ]
    return {
        "schema_version": 1, "kind": "public-source", **identity,
        "tree_sha256": digest(canonical(items)), "files": items,
    }


def verify_files(files, *, allow_legacy=False):
    if MANIFEST not in files:
        raise ValueError("Missing public source manifest")
    expected = make_manifest(
        {name: data for name, data in files.items() if name != MANIFEST}, allow_legacy=allow_legacy,
    )
    if files[MANIFEST] != canonical(expected):
        raise ValueError("Public manifest does not match the exact file set and bytes")
    return expected


def pack(files):
    validate_names(files)
    if (
        len(files) > MAX_MEMBERS or sum(map(len, files.values())) > MAX_TOTAL
        or any(len(data) > MAX_FILE for data in files.values())
    ):
        raise ValueError("Public source exceeds size limits")
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=STAMP)
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, data)
    return stream.getvalue()


def read_archive(data, *, allow_legacy=False):
    if len(data) > MAX_ARCHIVE:
        raise ValueError("Public archive exceeds size limit")
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            members = archive.infolist()
            if len(members) > MAX_MEMBERS:
                raise ValueError("Too many archive members")
            validate_names(info.orig_filename for info in members)
            if sum(info.file_size for info in members) > MAX_TOTAL:
                raise ValueError("Public archive exceeds size limit")
            for info in members:
                if (
                    not stat.S_ISREG(info.external_attr >> 16) or info.is_dir()
                    or info.compress_type != zipfile.ZIP_STORED or info.flag_bits & 1
                    or info.file_size > MAX_FILE or info.compress_size != info.file_size
                ):
                    raise ValueError("Unexpected archive member format")
            files = {info.filename: archive.read(info) for info in members}
    except (zipfile.BadZipFile, UnicodeError, NotImplementedError, RuntimeError, EOFError):
        raise ValueError("Malformed public archive or CRC mismatch") from None
    manifest = verify_files(files, allow_legacy=allow_legacy)
    if data != pack(files):
        raise ValueError("Archive bytes are not the canonical public ZIP")
    return manifest


def archive_name(identity):
    return f"skill-forge-public-{identity['product_version']}-r{identity['public_revision']}.zip"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    build = commands.add_parser("build", help="Create a new ZIP from a verified public source tree")
    build.add_argument("tree", type=Path)
    build.add_argument("output", type=Path)
    verify = commands.add_parser("verify", help="Verify a public directory or source ZIP")
    verify.add_argument("candidate", type=Path)
    verify.add_argument("--tree-sha256", help="Expected tree digest from a trusted release")
    verify.add_argument("--zip-sha256", help="Expected ZIP digest from a trusted release")
    args = parser.parse_args()
    try:
        if args.command == "build":
            tree, output = local_path(args.tree), local_path(args.output)
            if output.is_relative_to(tree):
                raise ValueError("Write the archive outside the source tree")
            files = read_tree(tree, ignore_git=True)
            manifest = verify_files(files)
            data = pack(files)
            with output.open("xb") as stream:
                stream.write(data)
            zip_hash = digest(data)
        else:
            candidate = local_path(args.candidate)
            if candidate.is_dir():
                manifest = verify_files(read_tree(candidate, ignore_git=True))
                zip_hash = None
            else:
                data = read_file(candidate, MAX_ARCHIVE)
                manifest, zip_hash = read_archive(data), digest(data)
            if args.tree_sha256 is not None and args.tree_sha256 != manifest["tree_sha256"]:
                raise ValueError("Public tree SHA-256 does not match the expected digest")
            if args.zip_sha256 is not None and args.zip_sha256 != zip_hash:
                raise ValueError("Public ZIP SHA-256 does not match the expected digest")
        print(json.dumps({
            "status": "PublicIntegrityVerified", "tree_sha256": manifest["tree_sha256"],
            "zip_sha256": zip_hash, "files": len(manifest["files"]),
        }))
        return 0
    except (ValueError, OSError) as error:
        message = str(error) if isinstance(error, ValueError) else "Filesystem operation failed"
        print(f"public_package: {message}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
