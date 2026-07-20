# Stop Slop — Core Method

Eliminate predictable AI writing patterns from prose, independent of language.

## Technical check: HTML/typographic artifacts (language-agnostic)

Source: [SEOquick](https://seoquick.com.ua/ai-content-detection-guide/) (real Ukrainian SEO agency, since 2008) — a purely technical check, independent of language. Text copy-pasted from a chatbot into a CMS or web page often carries literal HTML entities that a human typing directly never produces: `&mdash;` (em dash), `&ldquo;`/`&rdquo;` (curly quotes), `&nbsp;` (non-breaking space), stray `data-` attributes. Finding 3+ of these in a page's source is a fast, purely mechanical check — open the HTML, search for these strings, no linguistic judgment required. Related to but distinct from humanizer-ru's "copy-paste artifacts" category (which covers chatbot-UI leftovers like `oai_citation`, `citeturn...`) — this one is about typographic entities specifically.

## Fundamental principle: statistical deviation

Source: [ilyautov/humanizer-ru](https://github.com/ilyautov/humanizer-ru) (MIT). An LLM's output tends toward the statistically most probable continuation — the version that fits the largest number of contexts. Humanization is the deliberate choice of a *less probable but more characteristic* option: not the average continuation, but the one a specific author would actually choose. Keep this as the underlying test behind every rule below: not "is this construction banned" but "would the model default to the typical version here, and what would this particular author say instead."

## Core Rules

1. **Cut filler phrases.** Remove throat-clearing openers, empty intensifiers, and hedge words. See the language-specific reference file for this text's language.
2. **Break formulaic structures.** Avoid binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency. See the language-specific reference file.

   Nuance worth stating explicitly: a contrast construction ("not X, it's Y") is a genuine logical operator, not automatically a tell. Banning it outright can cost real content — concepts that are inherently defined by contrast (e.g. explaining a tradeoff) may become inexpressible without it. The actual tell is *decorative* repetition of the pattern for manufactured drama with no real distinction behind it. Cut the decorative use; keep the substantive one.
3. **Use active voice.** Every sentence needs a real subject doing something. Avoid passive constructions and inanimate objects performing human actions ("the complaint becomes a fix").
4. **Be specific.** No vague declaratives ("the reasons are structural"). Name the specific thing. No lazy extremes ("every," "always," "never") doing vague work.
5. **Put the reader in the room.** No narrator-from-a-distance voice. Specifics beat abstractions.
6. **Vary rhythm.** Mix sentence lengths. Two items beat three. End paragraphs differently.
7. **Trust readers.** State facts directly. Skip softening, justification, hand-holding.
8. **Cut quotables.** If a line sounds like a pull-quote, rewrite it.

Note: punctuation- and word-order-specific checks (such as the English "no em dash" and "sentence doesn't start with a Wh-word" checks) are intentionally left out of this shared file. They don't transfer across languages as-is — for example, the em dash is grammatically required in some Russian constructions, so an absolute "no em dash" rule would misfire on correct Russian text. Each language's own reference file defines its own punctuation- and structure-level checks.

## Scoring

Rate 1-10 on each dimension:

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds human? |
| Density | Anything cuttable? |

Below 35/50: revise.

---

Adapted from the language-agnostic portion of [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) (MIT license). See `SYNC_STATUS.md` in the repository root for the upstream commit this was last synced against.
