# Language router

This file only matters for packages that bundle more than one language. Use it to decide which reference file to read before applying the Core Rules.

1. Determine the language primarily from an explicit request ("check this in Ukrainian"); otherwise from the dominant language of the text being edited.
2. Read exactly one reference file for that language. Do not read reference files for other languages "just in case" — that wastes context for no benefit.
3. If the text mixes languages in clearly separate segments (e.g. an English paragraph followed by a Russian one), process each segment against its own reference file.
4. If the text is too short or ambiguous to identify a language confidently, apply only the Core Rules above and skip language-specific reference files entirely.
5. If the language is identified confidently but its row's file is **not** in this package (the table below lists every language this project knows, not every language this particular package bundles — the package's own `SKILL.md` table is authoritative for what's included), do not attempt to read the missing file. Apply only the Core Rules, and tell the user this package doesn't cover that language — other stop-slop packages might.

| Detected language | Reference file(s) to read |
|---|---|
| English | `references/phrases.md`, `references/structures.md`, `references/examples.md` |
| Russian | `references/ru.md` |
| Ukrainian | `references/uk.md` |
| Belarusian | `references/be.md` |
| Bulgarian | `references/bg.md` |
| German | `references/de.md` |
