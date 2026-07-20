# Deep-research task brief

Ready-to-paste prompt for Gemini Pro (Deep Research mode), ChatGPT, Grok,
or another Claude conversation. Run once per language — swap in the
matching "already covered" block before running. Exactly 5 sources per
run, ranked by how directly applicable they are, not a general survey.

---

## Master prompt (fill in `[LANGUAGE]` and the covered-block placeholder)

```
You are doing focused deep research, not a general survey.

TASK: find EXACTLY 5 sources for [LANGUAGE] that identify concrete,
directly-applicable markers of AI/LLM-generated text -- phrases,
grammatical constructions, punctuation habits -- that a human editor
could check by hand right now, not general claims like "AI text sounds
robotic."

HARD CONSTRAINT: exactly 5 sources, ranked 1 (most applicable) to 5
(least). Do not pad the count with weak sources -- if fewer than 5
genuinely applicable ones exist, say "found N, short of the target 5"
and explain what was searched and why nothing else qualified.

ACCEPT:
- academic papers/benchmarks that test [LANGUAGE] specifically in their
  evaluation set (not just "multilingual" in the abstract -- verify
  [LANGUAGE] was actually tested)
- practitioner articles naming specific constructions, not generic
  "sounds unnatural" claims
- native-speaker style/usage resources that independently flag a
  construction as unnatural or calqued, even without mentioning AI, if
  that construction plausibly shows up in LLM output

REJECT:
- generic "N signs of AI text" listicles that just translate well-known
  English tells into [LANGUAGE] without evidence they occur in actual
  [LANGUAGE] text
- AI-detector marketing pages with no disclosed methodology
- anything whose only advice is "run it through a detector"

ALREADY COVERED -- don't just re-find these, look for gaps or corrections:
[PASTE LANGUAGE BLOCK]

OUTPUT FORMAT -- one row per source, exactly this table, so it merges
directly into an existing file:

| # | Source | Concrete finding (name the actual phrase/construction) | Directly applicable? (yes/partial/no + why) | Contradicts or changes anything in "already covered"? |
|---|---|---|---|---|

Rank by applicability, most applicable first. An interesting-but-not-
directly-applicable source can go as a 6th+ bonus row below the 5, but
the 5 required rows must all be "yes" or "partial."

For every row marked "yes" or "partial," ALSO produce a ready-to-paste
draft block in this exact format (this is what actually goes into the
locale file, not just the bibliography row above):

**[Category name in bold]** — [one-sentence explanation of what the
pattern is and why it's a tell]

- Плохо: «[a concrete bad example in [LANGUAGE]]»
- Хорошо: «[the corrected version]»

Do not skip this even if it feels redundant with the table row above --
the table row is for the bibliography, this block is what gets copy-
pasted into the actual rules file. If a finding doesn't have a concrete
example you can construct confidently, say so instead of inventing one:
"no confident example available" is better than a fabricated one.
```

## "Already covered" blocks, per language

### Russian
```
- Opener cliches: "Важно отметить", "Стоит отметить" and similar
- Empty intensifiers: "в современном мире", "как известно", "безусловно"
- "Раскрыть потенциал"
- "не X, а Y" contrast -- IMPORTANT: already established (Habr, tested
  on Gemini) that a blanket ban is wrong; it's a working logical
  operator. The tell is decorative use with no real semantic contrast.
- "является" copula overuse where natural Russian drops it (English-
  trained-model artifact)
- Participial-clause overuse as pseudo-sophistication
- Unsolicited summary meta-commentary ("Резюмируя", "Подводя итог")
- Em dash -- already established that the English "no dash" rule
  doesn't transfer: Russian dash is grammatically required in some
  constructions (dropped copula)
```

### Ukrainian
```
- Same set as Russian (see above), plus:
- Unconfirmed hypothesis: "являється" may be a Russian calque perceived
  by editors as an error, not just style -- needs confirmation or
  refutation
- Participial-clause overuse -- confirmed by one source (Excel-
  terminology example) but only one
```

### Belarusian
```
- Almost nothing externally confirmed. Only a 3-item draft (opener
  cliches, "у сучасным свеце" filler, a dash caveat borrowed by
  analogy from Russian/Ukrainian -- NOT verified for Belarusian
  specifically). This is effectively a first pass.
```

### Bulgarian
```
- Same situation as Belarusian: 3-item draft, nothing confirmed. First
  pass.
```

### German
```
- Current list is unaided model knowledge, not externally sourced:
  opener cliches ("Es ist wichtig zu erwähnen"), "in der heutigen
  Zeit", formulaic contrasts, meta-commentary. Also an unconfirmed
  claim that the English "no dash" rule probably transfers to German
  without the Russian/Ukrainian-style exception, since German doesn't
  drop the copula the way Slavic languages do -- worth checking.
```

## After running

Paste new rows into `research/bibliography.md` under the matching
language section. If a result contradicts existing locale content (the
"Directly applicable" or last column says so), log it in
`../CHANGELOG-locales.md` as a **Changed**, not just an **Added** -- see
the 2026-07-20 (revision) entry for the format.
