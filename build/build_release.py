#!/usr/bin/env python3
"""Builds distributable stop-slop skill packages from build/manifest.yml.

Design constraint that matters: this does NOT flatten every reference file
into one big SKILL.md. Each package gets a small SKILL.md (core method +
a pointer table) plus a references/ folder holding only the files that
package actually needs. Claude reads a reference file on demand when the
skill's own router.md tells it to -- not all of them, every time, just
because they happen to be zipped together. Concatenating everything into
SKILL.md would defeat that and force every language's rules into context
on every trigger, regardless of what language the text is actually in.
"""
from __future__ import annotations

import shutil
import sys
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references"
DIST = ROOT / "dist"

EN_FILES = ["phrases.md", "structures.md", "examples.md"]

LANG_NAMES = {"ru": "Russian", "uk": "Ukrainian", "be": "Belarusian", "bg": "Bulgarian", "de": "German"}

UPSTREAM_METADATA = {
    "upstream_author": "Hardik Pandya (https://hvpandya.com)",
    "upstream_repo": "hardikpandya/stop-slop",
    "extension": "Slavic-language locale packs",
}


class ManifestError(Exception):
    """Manifest problem a human should fix; message says exactly what and where."""


def load_targets() -> list[dict]:
    with open(ROOT / "build" / "manifest.yml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    targets = data.get("targets")
    if not targets:
        raise ManifestError("manifest.yml has no 'targets' list")
    validate_targets(targets)
    return targets


def validate_targets(targets: list[dict]) -> None:
    """Fail fast with a precise message instead of a bare KeyError mid-build.

    The likeliest real mistake this catches: writing the *package* language
    tag ('ua', 'by') where the ISO *file* code ('uk', 'be') is required --
    the two deliberately differ in this repo, so the typo is easy to make.
    """
    seen_names: set[str] = set()
    for i, target in enumerate(targets):
        where = f"manifest.yml target #{i + 1}"
        name = target.get("name")
        if not name:
            raise ManifestError(f"{where}: missing 'name'")
        if name in seen_names:
            raise ManifestError(f"{where}: duplicate name '{name}'")
        seen_names.add(name)
        if not target.get("description"):
            raise ManifestError(f"{where} ({name}): missing 'description'")

        langs = target.get("langs", [])
        include_english = target.get("include_english", False)
        if not langs and not include_english:
            raise ManifestError(f"{where} ({name}): no langs and include_english is false -- package would be empty")
        if include_english:
            for fname in EN_FILES:
                if not (REFS / fname).is_file():
                    raise ManifestError(
                        f"{where} ({name}): include_english is true but upstream file "
                        f"references/{fname} is missing from this checkout. These three files "
                        f"({', '.join(EN_FILES)}) come from hardikpandya/stop-slop (MIT) and must "
                        f"be present in references/ for any English-including package."
                    )
        for lang in langs:
            if lang not in LANG_NAMES:
                raise ManifestError(
                    f"{where} ({name}): unknown lang code '{lang}'. Known: {sorted(LANG_NAMES)}. "
                    f"Note: file codes are ISO ('uk', 'be'), not the package-name tags ('ua', 'by')."
                )
            locale_file = REFS / "locales" / f"{lang}.md"
            if not locale_file.is_file():
                raise ManifestError(f"{where} ({name}): locale file not found: {locale_file}")


def reference_table(langs: list[str], include_english: bool) -> str:
    """Pointer section for SKILL.md: which file(s) to read for which language."""
    rows = []
    if include_english:
        rows.append("| English | `references/phrases.md`, `references/structures.md`, `references/examples.md` |")
    for lang in langs:
        rows.append(f"| {LANG_NAMES[lang]} | `references/{lang}.md` |")

    total = len(rows)
    if total > 1:
        header = (
            "## Language handling\n\n"
            "This package bundles more than one language. Read "
            "[references/router.md](references/router.md) first -- it "
            "explains how to detect the text's language and which single "
            "row below to act on. Do not read every row's file "
            "\"just in case\"; that costs context for no benefit.\n\n"
        )
    else:
        header = "## Reference\n\nRead the file below for phrases, structures, and examples to check against.\n\n"

    table = "| Language | Reference file |\n|---|---|\n" + "\n".join(rows)
    return header + table


def build_target(target: dict) -> Path:
    name = target["name"]
    langs = target.get("langs", [])
    include_english = target.get("include_english", False)

    out_dir = DIST / name
    if out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / "references").mkdir(parents=True)

    if include_english:
        for fname in EN_FILES:
            shutil.copy(REFS / fname, out_dir / "references" / fname)
    for lang in langs:
        shutil.copy(REFS / "locales" / f"{lang}.md", out_dir / "references" / f"{lang}.md")

    total_lang_count = len(langs) + (1 if include_english else 0)
    if total_lang_count > 1:
        shutil.copy(REFS / "router.md", out_dir / "references" / "router.md")

    core_method = (REFS / "core-method.md").read_text(encoding="utf-8").strip()
    pointer_section = reference_table(langs, include_english)

    frontmatter = {
        "name": name,
        "description": target["description"],
        # Both upstream stop-slop and this fork's additions are MIT; stating
        # it in the shipped SKILL.md (like humanizer-ru does) means the
        # license travels with every copy, not only with the repo.
        "license": "MIT",
        "metadata": dict(UPSTREAM_METADATA),
    }
    fm_yaml = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)

    skill_md = f"---\n{fm_yaml}---\n\n{core_method}\n\n{pointer_section}\n"
    (out_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")

    zip_path = DIST / f"{name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for file in sorted(out_dir.rglob("*")):
            if file.is_file():
                z.write(file, arcname=file.relative_to(DIST))

    verify_zip(zip_path, name)
    return zip_path


def verify_zip(zip_path: Path, name: str) -> None:
    """Post-build self-check; turns the promises in research/README.md into code.

    research/ (and any other repo content outside the manifest) must never
    ship in a package. This was previously checked by hand-grepping every
    zip after every build; a manual check that has to be remembered is a
    check that will eventually be skipped.
    """
    with zipfile.ZipFile(zip_path) as z:
        names = z.namelist()

    forbidden = [n for n in names if "research" in n.lower() or "bibliography" in n.lower()]
    if forbidden:
        raise RuntimeError(f"{zip_path.name}: research content leaked into package: {forbidden}")

    stray = [n for n in names if not n.startswith(f"{name}/")]
    if stray:
        raise RuntimeError(f"{zip_path.name}: entries outside the package dir: {stray}")

    if f"{name}/SKILL.md" not in names:
        raise RuntimeError(f"{zip_path.name}: SKILL.md missing from package")


def main() -> None:
    DIST.mkdir(exist_ok=True)
    try:
        targets = load_targets()
    except ManifestError as e:
        print(f"manifest error: {e}", file=sys.stderr)
        sys.exit(1)
    for target in targets:
        zip_path = build_target(target)
        size_kb = zip_path.stat().st_size / 1024
        print(f"built {zip_path.name:30s} {size_kb:6.1f} KB")
    print(f"verified: {len(targets)} packages, research/ isolation and SKILL.md presence checked in each")


if __name__ == "__main__":
    main()
