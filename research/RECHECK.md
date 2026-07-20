# Recheck schedule

Sources go stale at different rates. This file tracks when each was last
checked and when it's due again, so "we researched this once" doesn't
quietly turn into "we researched this in 2026 and never looked again."

## Why this matters, concretely

ilyautov/humanizer-ru's own HARD BANS table says outright: patterns that
get widely publicized start disappearing from LLM output ("delve" fell
off after 2024, per their own note), so their list needs regular
refreshing. If the source itself has a stated shelf life, our derived
content inherits that shelf life too.

## Cadence by source type

| Source type | Recheck interval | Why |
|---|---|---|
| Actively maintained GitHub projects (humanizer-ru) | Every ~2 months | Fast-moving; ilyautov's is on v3.14 already, multiple releases in weeks |
| Academic papers / benchmarks (SemEval, MULTITuDE, StyloMetrix, Черкасова/Тактарова) | Every ~6 months | Search for newer citing papers or follow-up work, not just re-reading the same one |
| Practitioner blogs (Habr, 1ps.ru, rbc.ua, NV.ua) | Every ~6 months, or opportunistically | Individual posts don't update, but new posts on the same topic appear; worth a fresh search, not re-fetching the same URL |
| Dictionaries (Горох) | Every ~12 months | Slow-moving reference content, low priority |

## Log

| Source | Last checked | Next due | Notes |
|---|---|---|---|
| ilyautov/humanizer-ru | 2026-07-21 | 2026-09 | Was v3.10 at last check; confirm still MIT, check changelog for new pattern categories before re-diffing against `ru.md` |
| Черкасова М. Н., Тактарова А. В. (2024) | 2026-07-21 | 2027-01 | Only abstract read; next check should attempt the actual PDF, not just re-confirm the abstract exists |
| Wikipedia:Признаки сгенерированности текста | 2026-07-21 | 2027-01 | Wikipedia essays get edited continuously; re-check means re-reading current text, not assuming 2026-07-21's version persists |
| goroh.pp.ua | 2026-07-21 | 2027-07 | Dictionary content, slow-moving |
| UkrQualBench | 2026-07-21 | 2027-01 | Young project (2026), check for version bumps to its russism list specifically |
| Belarusian / Bulgarian sources | never searched | — | Not on a recheck cadence yet because nothing has been found to go stale. First pass takes priority over rechecking what doesn't exist. |
| German sources (Wikipedia DE, Homepage-Helden, Stefan Weber, Korrektur.de, Literaturcafé) | 2026-07-21 | 2027-01 | First pass, 6/6 confirmed — best rate of all three language passes so far. Stefan Weber specifically is an active commentator; check for new posts, not just re-reading the same one |

## How to recheck (not just "look at it again")

1. For GitHub projects: check the release tag / changelog, not just the README — a version bump might only add categories, not change existing ones.
2. For academic sources: search for papers citing the original, not only re-reading it — citation chains surface follow-up corrections.
3. For anything already `[confirmed]` in `bibliography.md`: a recheck that finds no change is still worth a one-line log entry here ("still current as of [date]"), so the next person doesn't redo the same check.
4. Update this file's Log table after every recheck, whether or not anything changed.
