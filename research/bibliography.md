# Bibliography

## Prior art — direct competing/parallel projects

- **github.com/ilyautov/humanizer-ru** — MIT license (confirmed directly in SKILL.md frontmatter and via the awesome-claude-code registry). 52 patterns, v3.10+, actively maintained, includes its own eval harness, false-positive guards, voice calibration, and a "fact-lock" principle against inventing specifics. **Decision: adopted as a source.** Read in full 2026-07-21; genuinely novel categories (pro-drop violations, nominalization ratio, punctuation calques, emotional flatness, missing particles, missing figurative language, modal hedging, information-density evenness, block-skeleton uniformity) added to `ru.md` with attribution. The universal "statistical deviation" framing principle was added to `core-method.md`.
- **github.com/Vladimir-Human/humanizer-ru** (35 patterns) and **github.com/smixs/humanizer-ru** (32 patterns) — license not independently confirmed for either. Not used as sources; lower priority given ilyautov's project is both more comprehensive and confirmed-MIT.

**Known disagreement, resolved with reasoning, not silently:** ilyautov/humanizer-ru bans "не просто X, а Y" / "не только X, но и Y" outright, with no exception — conflicting with this project's own narrowed rule (see the 2026-07-20 revision entry in `CHANGELOG-locales.md`, based on the Habr/Gemini finding that blanket bans on this construction cost real conceptual content). Kept our narrower rule rather than adopting the blanket ban, because the two projects optimize for different things: humanizer-ru explicitly targets detector evasion (cites GPTZero/DivEye bypass rates), where a mechanical ban is defensible since detectors count frequency, not meaning; this project targets writing quality, where meaning loss is the thing to avoid. Documented in `ru.md` directly, not just here.

**Convergent finding:** humanizer-ru's "модальная неопределённость" (overuse of "может/способен/призван") independently corroborates the "мочь" claim attributed to the Черкасова/Тактарова academic paper in the second Russian deep-research pass below, which had been left as `[seed]` because the paper's body text wasn't independently accessible. Two independent routes landing on the same specific claim raises confidence in it even without reading the paper directly.



Two tiers, deliberately kept separate: academic/foundational research on
machine-generated text detection (peer-reviewed or arXiv, language-agnostic
methodology usually validated across many languages including Slavic ones),
and practitioner/observational articles (blog posts, journalism — useful for
catching concrete, current phrase-level tells that academic papers don't
list at that granularity, but not peer-reviewed).

Status markers: **[confirmed]** = directly used to write or revise a locale
file. **[seed]** = found, looks relevant, not yet used — a candidate for
whoever runs the next deep-research pass.

## Tier 1 — Academic / foundational

| Source | What it covers | Informed |
|---|---|---|
| Wang, Mansurov, et al. — SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection. `arxiv.org/pdf/2404.14183` | Shared task benchmark across many languages; establishes that MGT detection is language-sensitive, not a single universal signal | [seed] — hasn't been mined per-language yet |
| Macko, Moro, et al. (2023) — MULTITuDE: Large-scale multilingual machine-generated text detection benchmark | Benchmark dataset spanning multiple languages; worth checking directly for Slavic-language coverage | [seed] |
| Okulska, Stetsenko, Kołos, et al. (2023) — StyloMetrix: An open-source multilingual tool for representing stylometric vectors. `arxiv.org/abs/2309.12810` | Open-source tool for stylometric feature extraction, built with multilingual (Polish-team-led) coverage — plausibly extensible to other Slavic languages | [seed] — worth checking if it has Russian/Ukrainian feature sets, or how hard they'd be to add |
| Authorship attribution in multilingual machine-generated texts (2025). `arxiv.org/abs/2508.01656` | Directly on-topic: authorship attribution specifically in multilingual MGT | [seed] |
| Kumarage, Garland, et al. (2023) — Stylometric detection of AI-generated text in Twitter timelines. `arxiv.org/abs/2303.03697` | Establishes stylometric (not just statistical/perplexity) detection as a valid approach — methodological backing for why a phrase/structure list is a legitimate strategy at all | [confirmed] — supports the project's core premise, not a specific phrase |
| Нора Галь — «Слово живое и мёртвое» (1972). `lib.ru/TRANSLATORS/NORA_GAL/slowo.txt` (mirror had encoding issues when fetched directly; readable text obtained via search snippets instead) | Not about AI at all — predates LLMs by 50 years. Classic Russian work on канцелярит (bureaucratic-speak disease). Names two specific patterns LLM output reproduces: "расщепление сказуемого" (verb replaced by noun+auxiliary-verb: "вести борьбу" instead of "бороться") and "гирлянды причастий и деепричастий" (chains of participial constructions, with the canonical Chekhov misattached-participle joke as illustration) | [confirmed] — strongest foundational source found so far precisely because it's not about AI; it identifies the underlying disease LLMs happen to reproduce. Added both patterns to `ru.md` |

## Second deep-research pass (Russian) — mixed reliability, verified individually

The task brief for this pass was written in language-model-generated style itself (vague grandiose framing: "ряд глубоких лингвистических аномалий," "дидактического сглаживания") — a signal to verify claims individually rather than trust the report's confident tone.

| Source | Claim | Status |
|---|---|---|
| Wikipedia:Признаки сгенерированности текста (ru.wikipedia.org) | Cites false-agency examples, "не только...но и" parallelism, "rule of three" | [seed] — essay's existence confirmed (real Wikipedia essay, referenced by actual deletion-criteria policy), but the specific quoted examples were not found verbatim in available snippets |
| Черкасова М. Н., Тактарова А. В. — "Признаки сгенерированного текста в академическом дискурсе," 2024. DOI 10.30853/phil20240307 | Cites modal-verb overuse ("мочь"), "noun — это" predicate structure, lexical incompatibility ("иметь большую роль") | [seed] — paper's existence and legitimacy fully confirmed (peer-reviewed ВАК journal, ORCID authors, CC BY 4.0), but only the abstract was accessible, not the body, so the specific claims are unverified |
| **humanizer-ru** (Vladimir-Human/humanizer-ru, ilyautov/humanizer-ru, smixs/humanizer-ru on GitHub) | "Рваная медитативность," pseudo-Socratic questions, pseudo-therapeutic register | [confirmed] — exact phrases independently found verbatim across multiple real, published, iterated (ilyautov's is at v2.1) Claude-skill projects doing this exact task for Russian. **Bigger finding: this is direct prior art** -- 32-52 cataloged patterns already exist in production, more than this project currently has |
| "Блог М.Видео / Text.ru" — "Когда роботы сочиняют симфонии" | Verbal-noun list-item openers, gerund-clause openers ("учитывая вышесказанное") | [seed, unverified] — did not search for this source; the M.Video/Text.ru combination is an odd pairing worth scrutiny before trusting |
| Text.ru blog — "Как определить, что текст написала нейросеть" | Hypothetical "empty examples," triple-negation chains | [seed, unverified] — not checked |

## Tier 2 — Practitioner / observational (Russian)

| Source | Key finding | Informed |
|---|---|---|
| Камиль Гадеев — «Штампы LLM. Разбираю с новой точки зрения», Habr, 2026. `habr.com/ru/articles/1032294/` | Argues "не X, а Y" and similar contrast/causal constructions are logical operators, not inherent tells — banning them outright measurably degraded a test model's ability to express tradeoff concepts (tested on Gemini) | [confirmed] — narrowed the binary-contrast rule in `ru.md`, `uk.md`, and `core-method.md` |
| 1ps.ru — «Как проверить текст на нейросети», 2024. `1ps.ru/blog/ai/2024/...` | Models trained mostly on English data produce Russian text with unnaturally explicit "быть"/"является" where natural Russian drops the copula | [confirmed] — added "является" copula-overuse section to `ru.md` |
| awwwake.ru — «Как понять, что автор текста — нейросеть», 2024 | Independently names "является"-style канцеляризм as a marker | [confirmed] — corroborates the above |

## Tier 2 — Practitioner / observational (Ukrainian)

| Source | Key finding | Informed |
|---|---|---|
| rbc.ua — «5 ознак, що текст написав ШІ, а не людина», 2025. `rbc.ua/rus/styler/...` | Overuse of participial clauses ("що ілюструють...") where coordination with "і" would be more direct — named as a specific AI-tell | [confirmed] — added participial-clause section to `uk.md`, mirrored into `ru.md` since the underlying grammar applies to both |
| NV.ua — «Поширена калька з російської, якої варто уникати», 2024, and «5 популярних кальок з російської», 2024 | General confirmation that Russian-calque avoidance is an active, named concern among Ukrainian editors | [seed] — supports but doesn't confirm the specific "являється" hypothesis in `uk.md`; general search did not surface that exact word, still needs native-speaker check |
| Горох (goroh.pp.ua) — «ЯВЛЯЄТЬСЯ/ЯВЛЯЄМОСЬ — слововживання». Found via Gemini deep research, re-verified directly | "являється" as copula in a compound predicate is explicitly non-normative, attributed to Russian influence. Confirmed exact wording: "Він являється майстром високого класу" flagged incorrect; "він — майстер" / "він є майстром" correct | [confirmed] — strongest single finding of this pass; upgrades the earlier hypothesis in `uk.md` from unconfirmed to settled |
| Горох (goroh.pp.ua) — «ДАНИЙ — слововживання». Found via Gemini, re-verified directly | "Даний" as demonstrative is calqued from Russian "данный"; replace with "цей" / context-appropriate word. Names bureaucratic formulas "у даний час," "на даний час," "у даному разі" | [confirmed] — source independently re-verified as a real, legitimate Ukrainian usage dictionary; new item added to `uk.md` |
| UkrQualBench (github.com/grayodesa/ukrqualbench, 2026). Found via Gemini, existence re-verified | AI-specific Ukrainian LLM-quality benchmark; reported "Critical Russisms to Detect" list: "прийняти участь"→"взяти участь", "на протязі"→"протягом", "слідуючий"→"наступний", "отримати досвід"→"здобути досвід" | [confirmed, partial] — benchmark itself is real, not hallucinated; the exact phrase list was not independently re-checked against the repo, only taken from Gemini's summary — added to `uk.md` with that caveat noted |
| Ніна Станкевич — Вісник Львівського університету, 2020. Not independently re-verified | Academic article listing calques found even in student academic writing: "приналежність," "співпадати," "у даний час," "область науки," "точка зору," "у відповідності з," "у залежності від" | [seed] — plausible, consistent with known Ukrainian purism debates, article itself unverified |
| С. В. Шевчук — "Моделі перекладу активних дієприкметників...", 2013. Not independently re-verified | Active participles (-учий/-ючий/-ачий) argued not native to Ukrainian; gives replacement pairs like "контактуючі мови"→"мови в контакті" | [confirmed, partial] — underlying claim matches a known long-standing prescriptive-grammar debate; specific article unverified, added to `uk.md` with medium confidence |
| Горох (goroh.pp.ua) — «МІРОПРИЄМСТВО — слововживання», aggregates «Мова – не калька», «Уроки державної мови», «Словник-антисуржик» (three independent dictionaries agree). Found by browsing the site directly, not from Gemini's table | "Міроприємство" is a calque of "мероприятие," doesn't exist in Ukrainian; correct form "захід/заходи." Source names the exact register: business correspondence, reports, meetings. Bonus finding: "заходи по [X]" is a calqued preposition, should be "заходи щодо [X]" | [confirmed] — strongest-attested finding of this whole pass: three independent dictionary sources agree, includes citations from classic Ukrainian writers and a live bureaucratic example |

## Third Ukrainian deep-research pass — 2 of 5 confirmed verbatim, 2 not found at all

Same red flag as the second Russian pass: the report's own framing prose was AI-slop-heavy ("Швидка експансія великих мовних моделей призвела до виникнення специфічного типу контенту"). Verified each source individually rather than trusting the confident tone.

| Source | Claim | Status |
|---|---|---|
| SEOquick / Unmiss AI Detector. `seoquick.com.ua/ai-content-detection-guide/` | HTML entities (&mdash;, &ldquo;/&rdquo;, &nbsp;, stray data- attributes) left in copy-pasted AI text as literal code artifacts | [confirmed] — real Ukrainian SEO agency (since 2008), found the exact article, claim verified closely. Added as a language-agnostic technical check to `core-method.md` |
| РБК-Україна. `rbc.ua/rus/news/k-shvidko-zrozumiti-shcho-tekst-napisaniy-1775649654.html` | Calqued English AI-clichés: "мереживо" (tapestry), "занурюватися" (delve), "багатогранний" (multifaceted), "лідерство думок" (thought leadership) | [confirmed] — found the exact article, claim matches verbatim. Added to `uk.md` |
| "Acer Blog Ukraine" — dash-frequency stylometric analysis | Statistical claims about em-dash frequency tied to token-weight training patterns | [not found] — no evidence this article exists. Same red-flag pattern as the earlier "М.Видео/Text.ru" pairing: an electronics manufacturer's blog publishing deep linguistic analysis is an implausible combination. Not used. |
| OnlineCorrector / ZNO Osvita.ua | "являється" copula (already independently confirmed elsewhere) plus specific participle-calque pair "відмінений рейс" → should be "скасований рейс," "прибулий" used as a noun | [seed, inconclusive] — OnlineCorrector itself is real (independently seen referenced on goroh.pp.ua). The specific "відмінений/скасований" claim was checked directly and found genuinely mixed usage in real Ukrainian text, not a clear-cut calque — left unconfirmed rather than forced into `uk.md` |
| Cityhost.ua — modal-verb overuse ("може") and long-sentence agreement errors | Overuse of "може" to avoid direct responsibility | [not found] — no evidence this article exists. Same red-flag pattern as Acer: a web-hosting company's blog on deep grammatical analysis is an implausible pairing. Not used. |

## Not yet searched (open for the next pass)

- Bulgarian-language sources — none found in this session (see separate Bulgarian pass note if one exists)

## Belarusian deep-research pass — 2 reports, mixed depth of verification

Two independent reports arrived for the same language. Verified each source individually; one report (academic-citation style, with inline citation markers) turned out to be unusually strong — both of its checkable claims confirmed *verbatim*, including one full-text fetch of a real conference paper. The other report's sources exist but weren't verified to the same depth of specific content.

| Source | Claim | Status |
|---|---|---|
| Nazaranka, T. (2025). *Navigating Language Contact in the Digital Age: An AI Experiment with Belarusian.* DiSlaw, 2, 17–32. `dislaw.at/ds/en/article/view/154` | Hybrid future tense ("будзе акружала" instead of "будзе акружаць"), comma after a pronoun in direct address, hypercorrective comma before "і" when GPT edits Belarusian text | [confirmed] — fetched the full paper text, all three findings verified verbatim, including full prompt logs. **Attribution correction**: one report attributed this paper to "Anna Berenika Siwirska" — wrong. Siwirska is a real Belarusian-studies scholar (confirmed via a different, real citation in the Poritski et al. paper below), but she did not write this paper; the actual author is Tatsiana Nazaranka, University of Salzburg |
| Poritski, V., Volchek, O., Aparovich, M., Harytskaya, V., Smrz, P. (2026). *Tracking the evolution of LLM capabilities for Belarusian with OpenAI Evals.* LoResLM 2026 (ACL Anthology), 378–387 | Pseudo-word/orthographic-near-miss acceptance ("масштабны" vs "маштабны", "злучанне" vs "злучэнне", "звычаёў" vs "звычаяў"); case-government errors in grammar-acceptability judgments ("спрыяюць росквіце" instead of dative "росквіту") | [confirmed] — fetched the full paper (ACL Anthology PDF), both findings quoted verbatim in the source. High-quality benchmark paper, real research group (Brno University of Technology + independent researchers) |
| Пунько, К., Албут, А. А. «Асаблівасці беларускай мовы ChatGPT.» БДУІР conference proceedings, p. 58 | Orthographic hybridism (Taraškievica soft signs intruding into Narkamaŭka text), Ukrainianisms, "веды"/"вядомасць" paronym confusion | [confirmed, source exists] — found the exact title in the actual BSUIR conference PDF at the claimed page. Did not fetch and verify the specific linguistic claims line-by-line; treat content claims as plausible-but-unconfirmed until checked directly |
| Kaleta, R. (2019 per Belarusian Wikipedia; report says 2018). *Błędologia w glottodydaktyce białorutenistycznej* ["Памылкалогія ў беларусістычнай глотадыдактыцы"]. University of Warsaw doctoral dissertation | Overuse of "дадзены" as a demonstrative calque of Russian "данный"; calqued bureaucratic verbs | [confirmed, source exists] — real scholar (has a Belarusian Wikipedia page), real dissertation title matches closely, minor year discrepancy (2018 vs 2019) not resolved. Content claims not independently verified line-by-line |
| Т. Я. Старасценка, *Стылістыка беларускай мовы*; Т. А. Кісель / Н. Р. Якубук, *Беларуская мова (прафесійная лексіка)*, Baranavichy State University (2025); «Слоўнік Свабоды» (В. Цыганкоў) | Bureaucratic periphrases ("ажыццяўляць кіраўніцтва" instead of "кіраваць"), "-ства" calques of Russian process-nouns instead of native "-нне" | [seed, not verified this pass] — plausible academic/practitioner sources given the topic and institutions named, but not individually searched for in this pass. Time budget went to the two most-citable sources above instead |

**What changed the working assumption**: the earlier draft `be.md` guessed that Russian is the dominant interference source for Belarusian, by analogy with Ukrainian. The confirmed Nazaranka paper complicates this directly — the specific hybrid-future-tense error is explained as *Polish* interference, and GPT itself kept wrongly attributing it to Russian. Worth remembering when reviewing Belarusian text: don't assume every interference pattern traces back to Russian.

## Belarusian deep-research pass #3 — targeted, 2 reports on the 3 named gaps

Narrow follow-up request (dash, formulaic contrasts, meta-commentary only) per the earlier gap analysis. One report (doc A) presented findings confidently including a podcast citation; the other (doc B) was notably more epistemically careful — it explicitly stated when three parallel searches timed out and found nothing, and explicitly said no source ties "Падводзячы вынік" to AI specifically. Verified independently rather than trusting either report's confidence level.

| Source | Claim | Status |
|---|---|---|
| Law № 420-З (23 July 2008) "Аб Правілах беларускай арфаграфіі і пунктуацыі" — full text on be.wikisource.org, `daviedka.bnkorpus.info/pravapis2008/` | Codifies dash usage including omission rules; also codifies "не X, а Y" as a genuine contrast construction | [confirmed] — real law, full text fetched. Both reports cited this independently, correctly |
| Ministry of Education testing standard (ЗАЦВЕРДЖАНА Загад Міністэрства адукацыі), via `s3-minsk.cloud.mts.by` archive | Exact rule, quoted verbatim: dash omitted when subject is a personal pronoun ("Я _ чалавек") or when negation "не" stands between subject and nominative predicate ("Кажан _ не птушка") | [confirmed] — found the exact rule text verbatim in an official exam-prep standard document, independent of the law text itself. Strongest single confirmation of a grammar rule in this project so far |
| adukar.com DRT exam consultation materials | Same dash-omission rule, independently phrased | [confirmed] — corroborates the above from a third independent document |
| "Кіло слова" podcast (Марыя Пархімчык), episode 5, "Доўгі працяжнік — прымета штучнага інтэлекта?" | Long dash + typographic quotes as AI markers, specific keyboard-friction argument | [not found] — searched directly, no trace of this podcast or episode. Same red-flag shape as "Acer Blog Ukraine" and "Cityhost.ua" before: a confident, specific citation that doesn't check out. Not used |
| "Prompt Enhance AI" program / blog translation examples | Practical examples of machine translation defects | [not found / not checked] — vague, unverifiable citation, not pursued given time budget and the red flag above |
| §2-1 textbook reference on scientific-style functional connectors | "Такім чынам" and gerund constructions like "абагульняючы, аналізуючы, падсумоўваючы" are normal, codified features of scientific style | [confirmed, source exists] — generic textbook citation, plausible, not individually hunted down to a specific verified document |

### Honest gap, preserved rather than papered over
Neither report found a source specifically calling "Падводзячы вынік" an AI-calque or unnatural construction — one report's own words: "для дакладнай формулы... не знойдзена прымальнай крыніцы... таму так сцвярджаць нельга." The grammatical argument against it (gerund/dzeepryslouny clauses require same-subject agreement with the main clause, and typical AI usage violates this) is a real, plausible linguistic argument — and Russian has an analogous, sourced rule (Nora Gal, already in `ru.md`) — but for Belarusian specifically it remains an inference, not a confirmed finding. Written into `be.md` with that distinction stated explicitly rather than silently upgraded to "confirmed."

## German deep-research pass — 6 of 6 confirmed (best verification rate so far)

Same red-flag style as the Russian and Ukrainian passes (dense academic-sounding framing: "Forensische Textanalyse im Zeitalter generativer Sprachmodelle"), but this time every single source checked out, including a specific finding that reversed one of our own prior assumptions rather than just adding new phrases.

| Source | Claim | Status |
|---|---|---|
| Wikipedia:Anzeichen für KI-generierte Inhalte (de.wikipedia.org) | Calqued metaphors/superlatives: "reicher kultureller Teppich," "eingebettet," "im Herzen von," "atemberaubend," "bleibendes Vermächtnis" | [confirmed] — exact wording found verbatim on the actual page. German-language sibling of the Russian Wikipedia essay found earlier |
| Homepage-Helden. `homepage-helden.de/journal/ki-textmuster/` | Decorative "Nicht A, sondern B," over-symmetric bullet structures, missing concrete cases/personal experience | [confirmed] — exact article found, claims verified closely |
| eology (AI-Roundtable series). `eology.de` | "Menschen" as generic subject inflation, "kann" modal hedging, H2-title repetition in first sentence | [confirmed, partial] — eology itself and its AI-Roundtable series are real; the general "kann"-hedging claim is independently corroborated by multiple other German sources (ahead-ai.de, korrektur.de), but this exact framing wasn't pinned to one specific eology article |
| Plagiatsgutachten (Stefan Weber). `plagiatsgutachten.com/blog/chatgpt-texte-erkennen/` | Systematic absence of Austrian/Swiss regionalisms in DACH-targeted text: "weiters"→"des Weiteren," "allfällig"→"eventuell," "heuer"→"in diesem Jahr" | [confirmed] — exact wording matches verbatim. Stefan Weber is a real, well-documented Austrian "Plagiatsjäger" (Wikipedia page, high-profile cases incl. a government minister's resignation) |
| Korrektur.de. `korrektur.de/ki-texte-erkennen-merkmale-checkliste` | "Drei-Drei-Drei" structural symmetry, sentence-length variance below a 0.4 coefficient, American straight quotes `" "` instead of German `„ "` | [confirmed] — exact article found, claims match closely |
| Literaturcafé (bonus row). `literaturcafe.de/rettet-den-gedankenstrich-vor-der-ki/` | **Reverses our own prior assumption**: the German dash itself is a legitimate, historically established device; the actual tell is the unspaced American em-dash import, partly explained by tokenizer economics (`" —"` as a single token) | [confirmed] — exact article found. Independently corroborated by four more German sources found in the same search (t3n.de ×2, all-ai.de, contentconsultants.de, blog'n'relations, ki-news-daily.de) — the strongest convergence of independent sources on one claim across all three language passes so far |

### What this pass changed, not just added
The prior `de.md` dash section stated an unverified guess (no dash-exception like Russian/Ukrainian, since German has no copula-drop) as if it were settled. It was wrong in its practical conclusion, even though the reasoning sounded plausible: German does lack copula-drop, but that turned out to be the wrong reason to look for — the actual exception is historical/typographic (an established Halbgeviertstrich tradition) plus a tokenizer-economics explanation neither we nor the reasoning anticipated. Rewritten in `de.md` with the correction stated explicitly, not silently.


