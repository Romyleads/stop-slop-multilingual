# research/

Raw research trail behind `references/locales/*.md`: every article, paper,
and benchmark found while grounding the locale content in actual
linguistic/detection research instead of pure by-analogy translation from
English.

## Why this isn't "hidden," just excluded from downloads

Nothing here is secret — it's a normal part of the git repository, visible
to anyone who browses the repo on GitHub. What it deliberately is *not*:
referenced by any `SKILL.md`, or listed in `build/manifest.yml`. That
means `build/build_release.py` never copies it into any package, so it
costs zero context tokens for anyone who installs a skill from Releases,
and it doesn't inflate download size. If a future contributor changes the
build script to scan the whole repo instead of following the manifest
explicitly, that would be a bug — this folder existing and growing large
should never change what ships in `dist/`.

The curated, short version of what's in here lives in the main
[README.md](../README.md#research-basis) `Research basis` section, for
anyone who wants credibility signal without reading the whole trail.

## Files

- `bibliography.md` — sources found so far, split into academic/foundational
  and practitioner/observational tiers, tagged by which language they informed
- `RECHECK.md` — schedule for re-verifying sources that go stale (fast-moving
  GitHub projects especially), so a one-time check doesn't quietly become
  a permanent assumption
- `DEEP-RESEARCH-PROMPT.md` — a reusable task brief for asking other AI
  systems (Gemini, ChatGPT, Grok, another Claude model, etc.) to find more
  sources in a format that merges cleanly into `bibliography.md`, and now
  also produces a ready-to-paste locale-file draft for each applicable finding

## How to add findings from another model's deep research

1. Run `DEEP-RESEARCH-PROMPT.md` in whichever system.
2. Paste its output into `bibliography.md` under the right language section,
   keeping the same row format so the table stays mergeable.
3. If a finding changes what a locale file says (not just adds a citation),
   log that as a "Changed" entry in `../CHANGELOG-locales.md`, the same way
   the "не X, а Y" correction was logged — a source that only adds
   confidence isn't the same as one that overturns a prior claim.
