# Sync status

## Upstream (hardikpandya/stop-slop)

- upstream_commit: 8da1f03
- upstream_commit_date: 2026-07-18
- last_synced: 2026-07-20

## Our locale additions

- locales_version: 0.7.0-draft
- locales_updated: 2026-07-21
- status:
  - ru: grounded in external sources (Нора Галь, ilyautov/humanizer-ru MIT, 1ps.ru/awwwake) — still unreviewed by a native proofreader, but no longer pure by-analogy guesswork
  - uk: grounded in external sources (goroh.pp.ua, UkrQualBench) — still unreviewed by a native proofreader
  - de: grounded in external sources (Wikipedia DE, Stefan Weber, Korrektur.de, Homepage-Helden, Literaturcafé) — 6/6 confirmed, best verification rate of any language pass so far; still unreviewed by a native proofreader
  - be: grounded — hybrid future tense, orthographic near-misses, dash-omission grammar (triple-confirmed via law + Ministry standard + exam-prep materials), "не X, а Y" resolved as genuine operator (like Russian). Meta-commentary section honestly flags one claim as reasoned-but-unconfirmed rather than papering over the gap. Opener cliches and empty amplifiers remain unverified draft. Not yet reviewed by a native proofreader
  - bg: draft stub, zero external sources found or searched for

Update this file on every `git fetch upstream && rebase` cycle (upstream fields)
and on every locale content change (our fields), so a glance at this file
answers "are we in sync" without reading commit history.
