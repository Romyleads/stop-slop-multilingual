# Deutsch: Phrasen und Strukturen

Ehemals reines Starter-Set aus unaided model knowledge, jetzt mit externen
Quellen unterlegt (siehe `research/bibliography.md`, dritter Recherchedurchlauf).
Weiterhin nicht von einem muttersprachlichen Lektor gegengeprüft — vor
produktivem Einsatz idealerweise einmal von einer Person mit Deutsch als
Erstsprache durchsehen lassen.

## Einleitende Floskeln

- „Es ist wichtig zu erwähnen, dass"
- „Es sei an dieser Stelle betont, dass"
- „Zunächst einmal sollte man festhalten"
- „Man muss sagen, dass"

## Leere Verstärker

- „in der heutigen Zeit" / „im heutigen Zeitalter" — leerer Zeitmarker ohne Informationsgehalt
- „bekanntlich"
- „zweifellos" als Füllwort statt als echte Betonung einer konkreten Aussage

## Formelhafte Gegenüberstellungen (Calque des englischen KI-Musters)

| Muster | Problem |
|---|---|
| „Es geht nicht um X, sondern um Y" | direkte Übersetzung von "not X, it's Y" |
| „Das ist nicht einfach X, das ist Y" | formelhafte Zuspitzung statt direkter Aussage |
| „nicht nur X, sondern auch Y" | additive Abschwächung ohne eigenen Inhalt |

Beispiel:
- Schwächer: „Es geht nicht um die Technologie. Es geht um die Menschen."
- Direkter: „Die Technologie lässt sich steuern. Die Menschen nicht."

**Jetzt bestätigt, nicht mehr unbestätigt** (Quellen: [homepage-helden.de](https://www.homepage-helden.de/journal/ki-textmuster/), ahead-ai.de, wörtlich verifiziert): im Gegensatz zum Russischen (wo "не X, а Y" manchmal ein echtes logisches Kontrastmittel ohne Alternative ist) ist diese Konstruktion im Deutschen praktisch immer dekoratives Beiwerk. Teil A trägt keine eigene Information, die gesamte Aussage steckt in Teil B — anders als im Russischen gibt es hier keine bekannte Ausnahme für echten logischen Kontrast, die diese Regel einschränken würde.

## Metakommentare

- „Zusammenfassend lässt sich sagen"
- „Abschließend möchte ich betonen"

## Zum Gedankenstrich — Korrektur einer eigenen falschen Annahme

**Diese Recherche hat unsere vorherige Hypothese widerlegt, nicht bestätigt.** Wir waren davon ausgegangen, dass die englische „kein Gedankenstrich"-Regel im Deutschen weitgehend unverändert gilt, weil Deutsch keine Kopula-Auslassung kennt. Fünf unabhängige deutsche Quellen ([literaturcafe.de](https://www.literaturcafe.de/rettet-den-gedankenstrich-vor-der-ki/), [korrektur.de](https://korrektur.de/ki-texte-erkennen-merkmale-checkliste), [homepage-helden.de](https://www.homepage-helden.de/journal/ki-textmuster/), t3n.de, all-ai.de) widersprechen dem übereinstimmend: der Gedankenstrich (Halbgeviertstrich „–" mit Leerzeichen) ist ein historisch etabliertes, legitimes deutsches Stilmittel — keine Kopula-Auslassung nötig, um ihn zu rechtfertigen.

Der tatsächliche KI-Marker liegt woanders: Sprachmodelle importieren den amerikanischen Geviertstrich („—", Em-Dash) **ohne Leerzeichen**, oft aus tokenizer-technischen Gründen (»—« ist in vielen Tokenizern ein einzelnes Token, Komma/Semikolon-Konstruktionen brauchen mehr Tokens — literaturcafe.de nennt das explizit als Erklärung). Der Marker ist also nicht „Gedankenstrich vorhanden", sondern:
1. Em-Dash statt Halbgeviertstrich (Breite/Typografie prüfen)
2. Fehlendes Leerzeichen um den Strich
3. Häufigkeit — mehrfach pro Absatz ist auffällig, einmal im ganzen Text ist Stilmittel, nicht Marker

- Schlecht: „Das Update behebt nicht nur Fehler—es transformiert den gesamten Workflow.“ (Em-Dash, kein Leerzeichen)
- Gut: „Das Update behebt nicht nur Fehler – es beschleunigt auch die Arbeitsabläufe.“ (Halbgeviertstrich mit Leerzeichen, sparsam verwendet)

## Wikipedia-Kalkierungen (bestätigt, wörtliches Zitat)

Quelle: [Wikipedia:Anzeichen für KI-generierte Inhalte](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte), wörtlich verifiziert. Direkt aus dem Englischen kalkierte Metaphern und Superlative, die im sachlichen deutschen Stil auffallen:

- „reicher kultureller Teppich" / „reiche Geschichte"
- „eingebettet" / „im Herzen von [Ort]"
- „atemberaubend" / „beeindruckende natürliche Schönheit"
- „bleibendes Vermächtnis"

Prüfung: diese Phrasen per Strg+F suchen — sie sind selten organisch im nüchternen deutschen Sachtext-Stil.

## Fehlende DACH-Regionalismen (Stefan Weber, bestätigt)

Quelle: [plagiatsgutachten.com](https://plagiatsgutachten.com/blog/chatgpt-texte-erkennen/), Blog des bekannten österreichischen Plagiatsjägers Stefan Weber, wörtlich verifiziert. Auf Standarddeutsch trainierte Modelle glätten österreichische/schweizerische Regionalismen systematisch weg, auch wenn der Kontext (Zielmarkt, Thema) sie verlangen würde:

- „weiters" → Modell schreibt „des Weiteren" / „zudem"
- „allfällig" → Modell schreibt „eventuell"
- „heuer" → Modell schreibt „in diesem Jahr"

Der Marker ist nicht das Fehlen einzelner Wörter, sondern das systematische Ausbleiben *jeder* regionalen Färbung in einem sonst fehlerfreien Text für ein österreichisches/schweizerisches Publikum.

## Strukturelle Symmetrie: Drei-Drei-Drei und Bullet-Uniformität (bestätigt)

Quellen: [korrektur.de](https://korrektur.de/ki-texte-erkennen-merkmale-checkliste) und [homepage-helden.de](https://www.homepage-helden.de/journal/ki-textmuster/), beide wörtlich verifiziert, unabhängig voneinander auf dieselbe Beobachtung gestoßen.

**Drei-Drei-Drei-Architektur**: Einleitung mit drei Sätzen, drei Hauptpunkte, dreigliedriges Fazit — bei organisch gewachsenem Text fast nie so sauber.

**Bullet-Uniformität**: jeder Punkt einer Liste mit exakt derselben Struktur (fett gesetztes Schlagwort, Doppelpunkt, zwei Sätze). Menschliche Listen sind unregelmäßig — ein Punkt drei Wörter, der nächste vier Sätze.

**Geringe Satzlängen-Streuung**: Modelle pendeln zuverlässig zwischen 15 und 25 Wörtern pro Satz; Menschen variieren zwischen 6 und 40. Korrektur.de nennt einen Variationskoeffizienten unter 0,4 als Warnsignal — praktisch verwertbar ohne Software: mehrere Sätze im Text zählen, wenn alle ungefähr gleich lang sind, ist das auffällig.

**Falsche Anführungszeichen**: amerikanische gerade Anführungszeichen `" "` statt deutscher `„ "` — einfach zu prüfen, oft ein Copy-Paste-Artefakt aus einem Chat-Interface.

## Fehlende Konkretisierung (bestätigt)

Quelle: [homepage-helden.de](https://www.homepage-helden.de/journal/ki-textmuster/), wörtlich verifiziert. Ein Text ohne einen einzigen konkreten Fall, Kunden, Zahl oder Anekdote zu einem Thema, das solche Konkretisierung nahelegen würde (z. B. „Conversion-Optimierung"), ist laut Quelle „das Merkmal, das am schwersten zu fälschen ist" — schwerer zu verstecken als Floskeln, weil es Erfindung statt Auslassung erfordern würde.

## Vage Aussagen

- „eine Reihe von Faktoren" ohne Nennung, welche
- „gewisse Herausforderungen" ohne Konkretisierung
- „im Großen und Ganzen" als Ersatz für eine echte Einschätzung
