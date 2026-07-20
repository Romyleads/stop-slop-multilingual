# Changelog — locale packs and build system

This tracks changes to this fork's own additions (locale files, router,
build system, README/visual assets). It's deliberately a separate file
from upstream's own `CHANGELOG.md` — that file belongs to the upstream
author's own release history, and interleaving our entries into it would
turn every future `git rebase upstream/main` into a manual merge instead
of a clean fast-forward. Same reasoning as keeping `router.md` out of
`SKILL.md`: don't add lines to a file the upstream author is also
actively editing.

## 2026-07-20

### Added
- Initial locale packages: `ru`, `uk` (reviewed starter sets), `be`, `bg`
  (draft stubs, need native-speaker review)
- `de`, `en-de` German packages (starter set, medium confidence, unreviewed)
- `references/core-method.md` — language-agnostic rules extracted from
  upstream `SKILL.md`
- `references/router.md` — language detection for multi-language packages
- `build/manifest.yml` + `build/build_release.py` — generates one
  self-contained package per language combination, no cross-language
  duplication
- `.github/workflows/release.yml` — builds all packages on every GitHub
  release, plus a manual `workflow_dispatch` dry-run
- `assets/banner.svg` — original visual design (abstract pennant garland,
  light palette), deliberately distinct from upstream's own banner style
- `SYNC_STATUS.md` — tracks the upstream commit this fork is synced to

### Changed
- Renamed the "all languages bundled" package from `stop-slop-full` to
  `stop-slop-en-ru-ua-be-bg-de` — the old name implied coverage of "all
  languages," which is inaccurate; the new name spells out exactly what's
  included
- Removed all national flags and flag emoji from the banner and README
  language table — replaced with abstract color-coded labels, to avoid
  the Russian/Ukrainian and Belarusian-flag-variant sensitivities that
  literal flags would introduce for this project's actual audience

## 2026-07-20 (revision)

### Changed — not just added
- Narrowed the "не X, а Y" / binary contrast rule in `ru.md` and `uk.md`
  after checking external research (a Habr analysis showing the same
  construction is a genuine logical operator, not inherently a tell —
  banning it outright measurably degraded a test model's ability to
  express tradeoff concepts). The rule now distinguishes decorative use
  (cut) from substantive use (keep), instead of banning the pattern
  wholesale. Same nuance added to `core-method.md` since it's not
  Russian/Ukrainian-specific.

### Added, grounded in external sources rather than analogy alone
- "является"/"являється" copula-overuse pattern (machine-translation
  artifact from English-trained models, not general канцелярит)
- Overuse of participial clauses as pseudo-sophistication (source: a
  Ukrainian-language piece analyzing this exact AI-tell)
- "раскрыть потенциал" / "розкрити потенціал", "в эпоху цифровизации" /
  "в епоху цифровізації" — specific variants independently confirmed by
  multiple Russian-language sources analyzing LLM output
- Flagged (not yet added as confirmed): "являється" as a possible
  Russian-calque purism issue in Ukrainian specifically, separate from
  its stylistic status in Russian — needs native-speaker confirmation
  before treating as settled

## 2026-07-20 (research infrastructure)

### Added
- `research/` — the full source trail (academic papers, benchmarks,
  practitioner articles), explicitly excluded from every downloadable
  package. Verified by inspecting every built `.zip`, not just by the
  folder's absence from `manifest.yml`.
- `research/bibliography.md` — two-tier source list (academic/foundational
  vs. practitioner/observational), tagged `[confirmed]` where a source
  changed locale content vs. `[seed]` where it's found but unused
- `research/DEEP-RESEARCH-PROMPT.md` — reusable brief for handing to other
  AI systems (Gemini, ChatGPT, Grok, etc.) to extend the source list in a
  format that merges into `bibliography.md` without reformatting
- `README.md` "Research basis" section — curated highlights for anyone who
  wants credibility signal without reading the full trail

## 2026-07-21 (Gemini deep-research pass — Ukrainian)

### Changed — hypothesis upgraded to confirmed
- "являється" as copula overuse in Ukrainian: was logged 2026-07-20 as an
  unconfirmed hypothesis needing native-speaker check. Found via Gemini
  deep research, then independently re-verified directly against
  goroh.pp.ua (a real, legitimate Ukrainian usage dictionary, not taken
  on Gemini's word alone). Confirmed non-normative, attributed to
  Russian influence. `uk.md` updated accordingly.

### Added, with per-source verification noted
- "даний" as a calqued demonstrative — source independently re-verified
- Concrete replacement pairs for participial-clause overuse
  ("контактуючі мови"→"мови в контакті" etc.) — underlying claim matches
  known Ukrainian prescriptive-grammar debate, specific academic source
  not independently re-verified
- AI-specific russism list from UkrQualBench benchmark — benchmark's
  existence independently re-verified as real; the specific phrase list
  taken from Gemini's summary only, not re-checked against the repo
  itself

### Process note
Two of five sources from this pass were re-verified by direct search
before being written into `uk.md` at all (являється, даний). Two were
added with an explicit lower-confidence caveat rather than either
rejected outright or trusted fully (UkrQualBench's exact list,
participle-pairs article). One was logged as `[seed]` only, not used in
any locale file. This is the intended process going forward: an AI
system's deep-research output gets spot-checked before it changes what
ships, not merged wholesale on the strength of citation-looking output.

## 2026-07-21 (self-directed follow-up, not from the Gemini table)

### Added
- "міроприємство" → "захід/заходи", and the calqued preposition pattern
  "заходи по [X]" → "заходи щодо [X]" — found by browsing goroh.pp.ua's
  full "Слововживання" index directly (a much larger resource than the
  single pages Gemini's table had surfaced), not from the deep-research
  table itself. Three independent sub-dictionaries on that one site
  agree, making this the single most-attested finding so far.

### Correction (self-caught, not user-caught)
- Editing this entry into `bibliography.md`, a `str_replace` accidentally
  deleted the Шевчук row instead of appending after it. Caught before
  rebuilding by re-grepping the file rather than assuming the edit did
  what it was supposed to. Restored.

### Explicitly not done
- Did not import the rest of goroh.pp.ua's "Суржик чи калька" list
  (утюг, чемодан, капля, сільодка, etc.) — those are everyday spoken-
  register object-vocabulary errors, not patterns plausible in LLM-
  generated prose, which is this project's actual scope. Cataloguing
  general Ukrainian surzhyk is a different, broader problem than
  catching AI writing tells.

## 2026-07-21 (Russian: finding a foundational source, not another blog)

### Added
- `ru.md`: strengthened the participial-clause section with a canonical
  source (Нора Галь, "Слово живое и мёртвое," 1972) instead of only the
  general reasoning it had before -- includes the classic Chekhov
  misattached-participle example
- `ru.md`: new section, "расщепление сказуемого" (verb-into-noun-phrase
  splitting: "вести борьбу" instead of "бороться") -- a distinct pattern
  from participial overuse, both documented in the same source

### Process note
Two attempts to fetch the primary source directly (lib.ru and vavilon.ru
mirrors) both returned koi8-r-encoded text that rendered as mojibake --
not usable, and not guessed at or reconstructed. Usable, correctly
-encoded excerpts were instead obtained via web search snippets, which
extracted the text cleanly through a different pipeline. Documenting this
because it's a real failure mode worth knowing about for future research
passes on older Russian-language web sources: verify the fetched text is
actually legible before treating it as read, don't assume a 200 response
means readable content.

Current locale content version: `0.4.0-draft` (see `SYNC_STATUS.md`).
`-draft` stays in the version string as long as `be.md`/`bg.md` are
unreviewed stubs and `de.md` is unreviewed — drop it only when every
bundled language has had a native-speaker pass, not before.

## 2026-07-21 (second Russian deep-research pass — mixed reliability)

### Added
- `ru.md`: new section on 2025-2026-era patterns (рваная медитативность,
  pseudo-Socratic questions, pseudo-therapeutic register) — verified
  verbatim against real, published, iterated humanizer-ru projects on
  GitHub, not just taken from the deep-research report's word

### Explicitly not added
- Four of five claims in this pass's report (Wikipedia false-agency
  examples, the academic paper's specific findings, and both Text.ru-
  adjacent blog sources) were not independently verified at the level
  of specific quoted phrases -- the underlying sources are confirmed
  real (or in two cases, not even checked), but their exact claims stay
  `[seed]` in bibliography.md, not written into `ru.md`, until verified
  the same way являється and міроприємство were.

### Bigger finding than any individual phrase
Discovered three independent, published, actively-maintained competing
projects (humanizer-ru by three different GitHub authors) doing this
exact task for Russian, with 32-52 cataloged patterns each -- more than
this project currently has. Logged in `research/bibliography.md` under
"Prior art" as a decision point, not silently incorporated. Worth a
conversation about whether to keep deriving patterns one deep-research
pass at a time, or review those catalogs directly with proper
attribution.

### Process note
The task brief that produced this pass's report was itself written in
noticeably AI-slop-heavy style (vague grandiose framing like "ряд
глубоких лингвистических аномалий"). Treated as a signal to verify
harder, not as disqualifying -- three of five underlying sources turned
out to be completely real, one of them (humanizer-ru) more valuable
than expected.

## 2026-07-21 (adopting ilyautov/humanizer-ru as a source)

### Verified before adopting
- Fetched the full SKILL.md (524 lines) directly, not just README
  snippets. Confirmed MIT license twice: in the file's own frontmatter
  and in the awesome-claude-code registry listing (issue #2036).
- Did not verify licenses for the other two prior-art projects
  (Vladimir-Human, smixs) -- not used as sources for that reason.

### Added, with attribution
- `core-method.md`: universal "statistical deviation" principle
- `ru.md`: pro-drop violations, synonym-carousel avoidance,
  nominalization ratio, punctuation calques, emotional flatness,
  missing particles (же/ведь/вот), missing figurative language, modal
  hedging ("может"), information-density evenness, block-skeleton
  uniformity
- `ru.md`: new "Ложные срабатывания" (false-positive guard) section,
  mirroring humanizer-ru's own discipline about when NOT to apply a
  pattern

### Explicit disagreement kept, not resolved by silent adoption
humanizer-ru bans "не просто X, а Y" / "не только X, но и Y" outright.
This project's narrower rule (decorative use only) stays as-is. Reason:
humanizer-ru's own stated goal includes detector evasion (cites
GPTZero/DivEye bypass metrics); this project's goal is writing quality.
A mechanical ban serves the former better than the latter. Documented
directly in `ru.md`, not only here, so a reader of the locale file sees
the disagreement without needing to open the bibliography.

### Not done in this pass
Only ~10 of humanizer-ru's 52 patterns were selected for import --
the ones with no existing equivalent in `ru.md`. Categories with partial
overlap (канцелярит, "является", causal connectors, dash usage) were
left as this project's own existing versions rather than replaced
wholesale, to avoid discarding the Nora Gal / Habr-sourced reasoning
already in place. A fuller pass modeled more closely on humanizer-ru's
full structure (quad-pass audit process, voice calibration, fact-lock
principle) is a reasonable follow-up, not done here.

## 2026-07-21 (third Ukrainian pass — 2 of 5 confirmed, 2 not found)

### Added
- `core-method.md`: language-agnostic HTML/typographic-artifact
  technical check (&mdash;, curly quotes, &nbsp;) -- source SEOquick,
  verified real
- `uk.md`: calqued English AI-clichés section ("мереживо," "занурюватися,"
  "багатогранний," "лідерство думок") -- source РБК-Україна, verified
  verbatim
- `uk.md`: strengthened the dash section with the keyboard-input-friction
  reasoning (Alt+0151 barrier) and a pointer to the new technical check

### Not added, with reasons
- "Acer Blog Ukraine" and "Cityhost.ua" claims -- searched for both,
  found no evidence either article exists. Same red-flag shape as the
  earlier "М.Видео/Text.ru" non-source: an electronics manufacturer and
  a hosting company publishing deep linguistic analysis is an
  implausible pairing, and this time it didn't check out at all, not
  even partially.
- The "відмінений рейс" / "прибулий" participle-calque claim -- checked
  directly, found genuinely mixed real-world usage rather than a clear
  calque. Left as `[seed, inconclusive]` rather than added on the
  strength of a plausible-sounding but unconfirmed claim.

### Process note
This is the second deep-research report (after the Russian one) whose
own prose was written in noticeably AI-slop-heavy style, and the second
time exactly 2 of 5 sources turned out to be unfindable. Worth noting as
a pattern for whoever runs future passes: roughly 40% unfindable-source
rate across two independent reports so far is not a fluke to shrug off.

## 2026-07-21 (code review: 5 defects found and fixed, verified by runs)

### Fixed, by severity
1. `.github/workflows/release.yml`: missing `permissions: contents:
   write` -- the release-asset upload would have failed with 403 on the
   very first real release, since new repos default to a read-only
   GITHUB_TOKEN. Found by reading, would only have surfaced at publish
   time. Also loosely pinned pyyaml (>=6,<7).
2. `uk.md`: relative link `../core-method.md` resolved in the repo but
   was broken inside every built package (core-method is embedded into
   SKILL.md there; no path works in both contexts). Replaced with a
   context-independent textual pointer. Verified by resolving every
   internal link inside all 9 built zips programmatically.
3. `build_release.py`: no manifest validation -- a likely `ua`/`uk` typo
   (package tags and ISO file codes deliberately differ in this repo)
   would crash with a bare KeyError. Added `ManifestError` with precise
   messages naming the target and the fix; negative-tested by building
   with an intentional `ua` typo. Also: `license: MIT` now ships in every
   package's SKILL.md frontmatter, and `verify_zip()` turns the
   previously manual research/-isolation grep into a hard post-build
   check (a manual check that must be remembered is a check that will
   eventually be skipped).
4. Mixed Latin/Cyrillic inside single words: "physически" in `ru.md`
   and three "canцелярит"-family instances in research/changelog files.
   Ironic, since mixed-script characters are literally one of the AI
   tells in the catalog this project maintains. Swept the whole repo
   afterwards: zero remaining.
5. `router.md`: no explicit rule for a confidently-detected language
   whose file isn't bundled in the narrower packages (e.g. German text
   given to stop-slop-ru-ua) -- the router would point at a missing
   file. Added rule 5: apply Core Rules only and say so; also fixed a
   wrong "listing above" self-reference.

### Verification record
Normal build (9 packages, all self-checks green), negative manifest
test (clean exit 1 with the intended message), workflow YAML parse,
frontmatter parse of a built package (license present), link resolution
across all zips, full-repo mixed-script scan. No behavior of the
packages changed beyond the fixes listed; sizes and file sets diffed
clean against the pre-review build.

## 2026-07-21 (German pass: 6/6 confirmed, one prior assumption reversed)

### Verified before writing anything
All 6 sources (5 required + 1 bonus) checked individually despite the
report's own AI-slop-heavy framing prose. Best verification rate across
all three language passes run so far (Russian: 3/5 usable, Ukrainian:
3/5 usable, German: 6/6).

### Corrected, not just added
`de.md`'s dash section previously stated an unverified guess as settled
fact: that German has no dash-exception like Russian/Ukrainian because
it lacks copula-drop. This research reversed that conclusion -- German
dash usage is legitimate and historically established for unrelated
reasons (typographic tradition, not grammar), and the actual marker is
the unspaced American em-dash import, corroborated by five independent
German sources including a tokenizer-economics explanation
(literaturcafe.de). Rewritten with the correction stated explicitly.

Also flipped from "unconfirmed" to "confirmed": the decorative "Nicht A,
sondern B" construction is, unlike in Russian, essentially always
decorative in German -- no known exception for genuine logical contrast.

### Added, all with attribution
- Wikipedia DE calqued-metaphor list (kultureller Teppich, im Herzen von,
  atemberaubend, bleibendes Vermächtnis)
- DACH-regionalism absence (Stefan Weber): weiters/allfällig/heuer
  systematically smoothed to standard-German equivalents
- Drei-Drei-Drei structural symmetry, sentence-length variance, wrong
  American quotes (Korrektur.de)
- Missing concrete cases/personal experience as the hardest marker to
  fake (Homepage-Helden)

### Version bump
`de.md` moved from unaided-knowledge draft to externally-grounded,
matching what happened to `ru.md`/`uk.md` in an earlier pass. Bumped
locale content version to 0.4.0-draft in `SYNC_STATUS.md`. Still
`-draft` overall: be/bg remain untouched stubs and no locale has had a
native-speaker pass yet -- one well-sourced language doesn't change
that for the other four.

## 2026-07-21 (first real CI run failed; root cause was the project archive, not CI)

### What happened
The very first workflow run on the published standalone repo failed with
exit 1. Reproduced locally on an exact copy of the pushed tree: 5
packages built, then FileNotFoundError on references/phrases.md.

### Root cause
The project transfer archive deliberately packed only this fork's own
files and never included upstream's three English reference files
(phrases.md, structures.md, examples.md) -- fine under the original
fork-based publishing plan where upstream files come with the clone,
wrong for the standalone-repo path actually taken. The publishing
instructions weren't re-checked against the archive's contents. A
second, own defect compounded it: validate_targets() checked locale
files but not the English ones, so the failure surfaced as a raw
traceback mid-build instead of a clear pre-build error.

### Fixed
- The three upstream files now ship in the project archive (MIT,
  attribution already in LICENSE and README).
- validate_targets() now checks EN_FILES for any include_english
  target, failing before any package is built, with a message naming
  the target, the file, and where the files come from.
- actions/checkout v4 -> v5, actions/setup-python v5 -> v6 (Node 24),
  which also clears the deprecation warning from the failed run.
  Versions confirmed to exist via release pages, not guessed.
- README's "unchanged from upstream" list no longer names root
  SKILL.md, which doesn't exist in the standalone repo.

### Verified
Normal build (9 packages), negative test (phrases.md removed ->
clean ManifestError, exit 1, nothing built), and a full simulation of
the user's pushed tree plus these fixes (exit 0, all 9 built, workflow
YAML parses).

## 2026-07-21 (first live field test of a built package)

### Setup
stop-slop-ru v0.4.0 installed into Claude Code from the published
release. A/B generation test: same prompt (CRM-implementation company
"about us" text, ~250 words, Russian), one run without the skill, one
with it.

### Results
Both texts came out clean on every classic ru.md marker: zero
"является," zero "данный," zero throat-clearing openers, zero split
predicates, zero meta-summaries, zero clone bullets, concrete details
throughout. Honest conclusion: modern Claude barely produces classic
Russian slop in this genre even unaided, so a generation test on this
model cannot demonstrate the skill's value -- its real use case is
cleaning other models' and older texts, plus editing, not restraining a
model that is already restrained.

### One real finding -> one rule change
Both texts (with AND without the skill) contained 7-8 "не X, а Y"
constructions per ~250 words. Each instance individually passes our
decorative-vs-contentful test; the density is the problem -- the text
reads as continuous polemic against an invisible opponent. The rule as
written policed single-instance decorativeness but said nothing about
density, so the skill correctly let every instance through. Added a
density guideline to ru.md (more than 2-3 per ~300 words = rhythmic
tic even when each is justified, with rewrite strategies that vary the
form instead of deleting the contrast). Likely applies to uk/de as
well but observed only in Russian so far -- not propagated by analogy,
per project discipline.

## 2026-07-21 (field test 2: known-answer target text, 12/12)

Fed a synthetic target text with 12 planted marker groups and 2
false-positive traps to the installed stop-slop-ru-ua (v0.4.0 release
build) via Claude Code. All 12 groups neutralized, including the
strongest rewrite of the test: vague "целый ряд факторов" replaced
with three concrete named obstacles. Both traps survived without
grammatical damage (rephrased rather than preserved verbatim, which is
legitimate under a full-rewrite instruction). The skill also produced
its own grammatically correct dash, confirming the dash-exception rule
does not over-purge.

Residuals, both expected: contrast density hit 3 per ~150 words --
third consecutive text confirming the density rule added after v0.4.0
shipped (the installed package predates it; goes out with the next
release), and one soft unverifiable claim ("всё больше компаний") that
no current rule covers -- noted, not yet acted on, one occurrence is
not a pattern.
