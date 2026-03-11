# Skill

## Name

/elvis-x-hook-writer

## Beschreibung

Generiert 5 Tweet-Varianten zu einem vorgegebenen Thema, jede mit maximal 280 Zeichen und einem unterschiedlichen Hook-Typ. Liefert einen direkten Vergleich der Varianten mit Empfehlung für die stärkste — einsatzbereit für sofortiges Posting oder weiteres A/B-Testing.

## Ziele

- 5 fertige Tweet-Varianten zu einem Thema, jede unter 280 Zeichen
- Jede Variante nutzt einen anderen Hook-Typ: Frage, Aussage, Kontrast, Liste, Story
- Zeichenanzahl für jede Variante explizit angegeben (kein manuelles Zählen nötig)
- Eine begründete Empfehlung welche Variante für das Ziel-Publikum am stärksten ist

## Strategie

Der Skill arbeitet hook-first: Der Hook ist die erste Zeile und entscheidet ob jemand weiterliest. Deshalb wird zuerst der stärkste Hook-Typ für das jeweilige Thema identifiziert, dann die Varianten entwickelt. Jede Variante ist eigenständig — kein Copy-Paste von Satzteilen. Die Empfehlung basiert auf drei Kriterien: Ziel-Publikum des Operators, Thema-Typ (Bildung, Meinung, Story, Angebot), und aktuellem Kontext (Zeitdruck, Kontroverse, Neuigkeit).

## Einschränkungen

- Genau 5 Varianten pro Aufruf — nicht mehr, nicht weniger
- Jede Variante: max. 280 Zeichen (Twitter-Limit), min. 80 Zeichen
- Keine Hashtags außer der Operator fordert sie explizit an (max. 2 pro Tweet)
- Keine URLs in die Varianten einbauen — Operator fügt Links separat hinzu
- Kein automatisches Posting — Output ist immer zur manuellen Freigabe bestimmt

## Ausführungsschritte

1. Lies das vorgegebene Thema und identifiziere: (a) den Kernaussage in einem Satz, (b) das primäre Ziel-Publikum (Anfänger / Fortgeschrittene / Entscheider), (c) den Tonfall (sachlich, provokativ, inspirierend, lehrreich). Dokumentiere diese drei Punkte im Output als "Themen-Briefing" vor den Varianten.
2. Schreibe Variante 1 (Hook-Typ: Frage). Formuliere eine Frage die das Ziel-Publikum sofort mit "Ja" oder "das frage ich mich auch" beantworten würde. Die Frage steht in Zeile 1, die Antwort/Aussage in Zeile 2–3. Zähle die Zeichen manuell und dokumentiere die Anzahl direkt nach der Variante in Klammern: z.B. "(143 Zeichen)".
3. Schreibe Variante 2 (Hook-Typ: Aussage). Beginne mit einer konkreten, überraschenden oder kontra-intuitiven Behauptung. Keine Frage. Die Aussage soll eine starke Meinung oder einen überraschenden Fakt enthalten. Zeichenanzahl dokumentieren.
4. Schreibe Variante 3 (Hook-Typ: Kontrast). Nutze das Struktur-Muster "Die meisten [Gruppe] tun X. Die Besten tun Y." oder "Früher war X. Heute ist Y." — ein klarer Gegensatz in den ersten zwei Zeilen. Zeichenanzahl dokumentieren.
5. Schreibe Variante 4 (Hook-Typ: Liste). Beginne mit einer Zahl: "3 Gründe warum …", "5 Fehler die …", "7 Dinge die …". Die Liste muss vollständig im Tweet Platz finden — kein "Thread unten". Zeichenanzahl dokumentieren.
6. Schreibe Variante 5 (Hook-Typ: Story). Beginne mit einem konkreten Moment oder einer konkreten Person: "Letzte Woche hat …", "Ich habe [Jahr] einen Fehler gemacht …", "Ein Kunde fragte mich …". Die Mini-Story hat einen Anfang (1 Satz), ein Problem (1 Satz) und eine Auflösung (1–2 Sätze). Zeichenanzahl dokumentieren.
7. Schreibe die Empfehlung: Welche Variante (Nummer) ist für das identifizierte Ziel-Publikum am stärksten und warum? Begründung in max. 3 Sätzen, basierend auf Hook-Typ, Thema-Typ und Tonfall aus Schritt 1.

## Verifikation

- Alle 5 Varianten vorhanden: Frage, Aussage, Kontrast, Liste, Story — jede als eigener Block
- Zeichenanzahl für jede Variante dokumentiert und im Bereich 80–280 Zeichen
- Keine Variante ist eine leichte Umformulierung einer anderen — alle 5 sind strukturell verschieden
- Empfehlung nennt explizit die Varianten-Nummer und enthält eine inhaltliche Begründung
- Failure-Indikator: Wenn das vorgegebene Thema zu vage ist (weniger als 5 Wörter, kein klares Subjekt), gibt der Skill "Thema zu vage — bitte präzisieren: [Beispiel-Formulierung]" aus und stoppt
- Akzeptanzkriterium: 5 strukturell verschiedene Varianten, alle innerhalb des Zeichenlimits, eine begründete Empfehlung

## Abhängigkeiten

- Input: Ein konkretes Thema (1–3 Sätze Beschreibung) und optional: Ziel-Publikum und gewünschter Tonfall
- Empfohlene Vorgänger-Skills: /elvis-growth-audit (liefert Top-Themen und funktionierende Content-Formate als Input)

## Output

Themen-Briefing (3 Punkte) + 5 Tweet-Varianten (je mit Zeichenanzahl in Klammern) + 1 Empfehlung mit Begründung. Gesamtlänge: max. 600 Wörter, Markdown-Format.
