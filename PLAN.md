# Pipeline: Stop Slop RU/UA/BE/BG — implementation plan for Claude Code

Read this whole file before starting. Each phase has a "Done when" check —
do not move to the next phase until that check passes. If a check fails,
fix the cause before continuing; do not skip ahead.

Context: this is a fork of `hardikpandya/stop-slop` (MIT, upstream, English
skill for removing AI writing tells). This project adds self-contained
Russian/Ukrainian/Belarusian/Bulgarian locale packs without modifying the
upstream English files, and builds them into separate downloadable
packages via GitHub Actions on release. Belarusian and Bulgarian content
is a draft and is explicitly allowed to stay a draft through this pipeline
— do not invent confident-sounding native phrasing to make Phase 3 look
more complete than it is.

## Phase 0 — Preconditions

1. Confirm you're inside the `Romyleads/stop-slop` fork (`git remote -v`
   should show `origin` pointing at it).
2. If `upstream` remote is missing, add it:
   ```
   git remote add upstream https://github.com/hardikpandya/stop-slop.git
   ```
3. Confirm branch state: `main` should be at the same commit as
   `upstream/main`. If not, do a fast-forward sync first (see Phase 5)
   before adding anything — don't build on a stale base.

**Done when:** `git remote -v` shows both remotes, and
`git rev-parse main upstream/main` prints the same commit hash for both,
or you've just fast-forwarded it to match.

## Phase 1 — Apply the build-system files

These already exist as a delivered bundle; place them at these exact
paths, don't rename anything:

```
references/core-method.md
references/router.md
references/locales/ru.md
references/locales/uk.md
references/locales/be.md
references/locales/bg.md
build/manifest.yml
build/build_release.py
.github/workflows/release.yml
SYNC_STATUS.md
```

Do not touch `SKILL.md`, `references/phrases.md`, `references/structures.md`,
or `references/examples.md` at the repo root — those are upstream's and
stay as-is.

**Done when:** `git status` shows only new files added, zero modified
files outside what's listed above.

## Phase 2 — Apply README and banner

Add:
```
README.md
assets/banner-stop-slop-multilingual.png
```

Open `assets/banner-stop-slop-multilingual.png` directly to confirm it displays
correctly before committing — a broken image in a README is worse than no
image. Since this is already a PNG (not the original SVG this project
started with), it can be used as-is for GitHub's Social Preview setting
too (Settings → Social preview) — resize to 1280×640 first if the current
dimensions don't match; GitHub crops/pads otherwise rather than erroring.

Constraint that must survive future edits: no real national flags and no
flag emoji anywhere in the banner or README (not even for languages that
feel politically uncontroversial to you) — the Russian/Ukrainian pairing
and the two competing Belarusian flags are both live sensitivities for
this project's actual audience. Use the existing colored-square /
abstract-pennant convention instead, consistently, in both the banner and
the language table.

**Done when:** the banner PNG displays correctly (no garbled text or
overflow outside the frame), and every internal README link (the ones
starting with `../../releases/` or pointing at `references/...`) matches a
file that actually exists in the repo at that path.

## Phase 3 — Expand be.md / bg.md (optional, don't fake confidence)

`references/locales/be.md` and `bg.md` are intentionally short drafts. If
you have a native speaker to consult, expand them following the structure
already used in `ru.md` and `uk.md` (throat-clearing openers, empty
intensifiers, formulaic contrasts, meta-summaries, a note on dash usage,
vague quantifiers). If you don't have a native speaker to check against,
leave them as drafts and leave the "draft quality" labels in
`build/manifest.yml` and `README.md` as they are — do not remove the draft
label just because the list got longer.

**Done when:** either the files are genuinely reviewed by a Belarusian or
Bulgarian speaker and the draft label is removed in both `manifest.yml`
and `README.md` together, or nothing in this phase changed and the draft
label stays.

## Phase 4 — Local build verification

```
pip install pyyaml --break-system-packages
python3 build/build_release.py
```

Then inspect the output, don't just check the exit code:

```
for z in dist/*.zip; do echo "--- $z ---"; unzip -l "$z"; done
```

Check specifically:
- `stop-slop-ru.zip` and `stop-slop-ua.zip` contain no `phrases.md`,
  `structures.md`, or `examples.md` (that would mean English leaked into
  a single-language package).
- Every zip's top-level entry is `<package-name>/`, not a nested or
  double-wrapped folder.
- `stop-slop-en-ru-ua-be-bg-de.zip` contains all eleven reference files
  (5 locale + 3 English + core-method + router). Note this package is
  deliberately not called "full" anywhere — the name always spells out
  every language it bundles, since this repo doesn't cover all languages
  and a name implying totality would mislead people browsing Releases.

**Done when:** all packages defined in `build/manifest.yml` build without
error and the checks above pass for at least `stop-slop-ru` and
`stop-slop-en-ru-ua-be-bg-de`.

## Phase 5 — Git: sync main, rebase the feature branch

```
git fetch upstream
git checkout main
git merge --ff-only upstream/main
git push origin main

git checkout codex/locales-slavic   # create it if it doesn't exist yet
git rebase main
```

If the rebase conflicts, resolve it, then:
```
git rebase --continue
```
Enable `git config rerere.enabled true` once, so a conflict you've
resolved before doesn't have to be resolved by hand again next sync.

```
git push --force-with-lease origin codex/locales-slavic
```

Set `codex/locales-slavic` as the repository's default branch in GitHub
repo settings, so `Code → Download ZIP` and the repo landing page show
this branch, not `main`.

**Done when:** `git diff main codex/locales-slavic --stat` shows only the
files from Phases 1–3 (plus `README.md`, `assets/banner-stop-slop-multilingual.png`) — nothing
from upstream's own files appears as changed.

## Phase 6 — Dry-run the workflow before a real release

In the GitHub UI: Actions → "Build language packs" → Run workflow
(this uses the `workflow_dispatch` trigger already in
`.github/workflows/release.yml`, so it runs without publishing anything).

Download the resulting `stop-slop-packages` artifact from the finished
run and spot-check one zip the same way as Phase 4.

**Done when:** the manual run finishes green and the downloaded artifact
matches what you built locally in Phase 4.

## Phase 7 — Cut the first real release

Publish a GitHub release (any tag, e.g. `v0.1.0`) on
`codex/locales-slavic`. The workflow's `release: types: [published]`
trigger fires automatically and attaches all 9 zips to it.

Update `SYNC_STATUS.md`'s `locales_version` and `locales_updated` fields
to match this release.

**Done when:** the release page shows all 9 `.zip` files as assets, and
each README download link
(`../../releases/latest/download/stop-slop-<name>.zip`) resolves to one
of them without a 404.

## Phase 8 — Manual smoke test

Download `stop-slop-ru.zip` from the actual release (not from local
`dist/`) and drag it into Claude Desktop, or upload it on claude.ai.
Start a conversation, paste a paragraph of Russian text containing at
least one phrase from `references/locales/ru.md`, and confirm the skill
triggers and flags it. Repeat once more with `stop-slop-en-ru-ua.zip`
using a mixed English/Russian paragraph.

**Done when:** both smoke tests show the skill actually triggering and
correctly identifying the language-specific issue, not just installing
without errors.
