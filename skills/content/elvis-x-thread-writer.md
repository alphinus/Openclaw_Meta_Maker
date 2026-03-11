# Skill

## Name

/elvis-x-thread-writer

## Beschreibung

Schreibt einen vollständigen X-Thread mit 8–12 Tweets zu einem vorgegebenen Thema. Liefert einen strukturierten Thread mit Hook-Tweet, Entwicklungs-Tweets, Beweis-Tweet, Übergangs-Tweet und CTA-Tweet — fertig zum Posten oder zur weiteren Bearbeitung.

## Ziele

- Fertiger X-Thread mit min. 8 und max. 12 Tweets, jeder unter 280 Zeichen
- Hook-Tweet der Neugier weckt und zum Weiterlesen animiert (min. 60, max. 280 Zeichen)
- Klare Struktur: Einstieg → Entwicklung → Beweis → Übergang → CTA
- Zeichenanzahl für jeden Tweet explizit dokumentiert

## Strategie

Der Thread wird von der Struktur her gedacht: Hook zuerst, dann Entwicklung des Arguments in Einzelpunkten, dann Beweis durch Daten oder Story, dann Übergang, dann klarer CTA. Jeder Tweet muss eigenständig verständlich sein — kein Tweet darf nur im Kontext des vorherigen Sinne ergeben. Die Nummerierung im Tweet (z.B. "2/") erzeugt Orientierung und signalisiert dem Leser, dass er sich in einem strukturierten Thread befindet.

## Einschränkungen

- Min. 8, max. 12 Tweets pro Thread — nicht weniger, nicht mehr
- Jeder Tweet: max. 280 Zeichen (Twitter-Limit)
- Hook-Tweet: min. 60 Zeichen, max. 280 Zeichen — kein Doppelpunkt am Ende
- Entwicklungs-Tweets 2–7: je max. 280 Zeichen, je genau ein Punkt oder Argument, Nummerierung im Tweet
- Keine Hashtags außer der Operator fordert sie explizit an (max. 2 pro Tweet)
- Kein automatisches Posten — Output ist zur manuellen Freigabe bestimmt

## Ausführungsschritte

1. Lies das vorgegebene Thema und identifiziere: (a) die 1 Kernaussage des Threads in einem Satz, (b) 5–7 Unterpunkte oder Argumente die den Thread aufbauen, (c) 1 Beweis (Zahl, Beispiel oder persönliche Story). Dokumentiere diese Punkte als "Thread-Briefing" vor dem Thread.
2. Schreibe den Hook-Tweet (Tweet 1): Formuliere eine starke Frage oder eine kontra-intuitive Aussage — kein Doppelpunkt am Ende. Der Hook muss min. 60 Zeichen und max. 280 Zeichen haben. Dokumentiere die Zeichenanzahl in Klammern direkt nach dem Tweet: z.B. "(187 Zeichen)".
3. Schreibe die Entwicklungs-Tweets (Tweets 2–7, mindestens 5 Tweets): Jeder Tweet enthält genau einen Punkt oder ein Argument, beginnt mit der Nummerierung im Format "N/" (z.B. "2/") und ist max. 280 Zeichen lang. Je Tweet Zeichenanzahl dokumentieren.
4. Schreibe den Beweis-Tweet (Tweet 8 oder später): Belege die Kernaussage mit einem konkreten Datenpunkt, einem Beispiel oder einer kurzen Story (max. 280 Zeichen). Zeichenanzahl dokumentieren.
5. Schreibe den Übergangs-Tweet: Formuliere einen Satz der den Leser auf das Fazit vorbereitet, max. 100 Zeichen. Empfohlene Formulierung: "Hier ist das Wichtigste:" oder ähnlich knappe Überleitung. Zeichenanzahl dokumentieren.
6. Schreibe den CTA-Tweet (letzter Tweet): Formuliere genau 1 klare Handlungsaufforderung — Folgen, Reposten, Kommentieren oder Link-Klick. Max. 280 Zeichen. Kein zweiter CTA im gleichen Tweet. Zeichenanzahl dokumentieren.
7. Prüfe den gesamten Thread: Zähle die Tweets (min. 8, max. 12), stelle sicher dass kein Tweet > 280 Zeichen ist und der Hook-Tweet min. 60 Zeichen hat. Falls der Hook-Tweet < 60 oder > 280 Zeichen ist: neu schreiben.

## Verifikation

- Thread enthält min. 8 und max. 12 Tweets — jeder nummeriert und als eigener Block
- Zeichenanzahl für jeden Tweet dokumentiert und im Bereich ≤ 280 Zeichen
- Hook-Tweet: min. 60 Zeichen, kein Doppelpunkt am Ende
- Entwicklungs-Tweets 2–7 enthalten je Nummerierung im Format "N/"
- Failure-Indikator: Hook-Tweet > 280 Zeichen oder < 60 Zeichen → Meldung "Hook außerhalb Zeichenlimit — neu schreiben" und Thread-Erstellung stoppen
- Failure-Indikator: Thema < 5 Wörter oder kein klares Subjekt → Meldung "Thema zu vage — bitte mit min. 5 Wörtern beschreiben"
- Akzeptanzkriterium: 8–12 Tweets, alle ≤ 280 Zeichen, Hook 60–280 Zeichen, 1 CTA-Tweet am Ende

## Abhängigkeiten

- Input: Ein konkretes Thema (1–5 Sätze) und optional: Ziel-Publikum und gewünschter Tonfall
- Empfohlene Vorgänger-Skills: /elvis-x-hook-writer (liefert getestete Hook-Formulierungen als Basis), /elvis-viral-formula (liefert virales Struktur-Framework als Orientierung)

## Output

Thread-Briefing (3 Punkte) + 8–12 Tweets (je mit Zeichenanzahl in Klammern, nummeriert als Tweet 1, Tweet 2, usw.) + Gesamt-Tweet-Anzahl am Ende. Gesamtlänge: max. 800 Wörter, Markdown-Format.
