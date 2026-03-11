# Skill

## Name

/elvis-bio-writer

## Beschreibung

Generiert 3 Bio-Varianten für ein X/Twitter-Profil: sachlich (max. 120 Zeichen), provokativ (max. 150 Zeichen) und storytelling-basiert (max. 160 Zeichen). Liefert jede Variante mit expliziter Zeichenanzahl und der zugrundeliegenden Formel — einsatzbereit für sofortige Profiloptimierung.

## Ziele

- 3 fertige Bio-Varianten (sachlich, provokativ, storytelling) je mit eigenem Zeichenlimit
- Jede Variante folgt einer konkreten Formel und ist strukturell verschieden
- 3 Keywords der Kernkompetenz als Basis identifiziert
- Zeichenanzahl für jede Variante explizit dokumentiert

## Strategie

Die Bio ist das erste was ein neuer Besucher liest — sie entscheidet über Follow oder Weiterklick. Drei Varianten bieten Auswahl für unterschiedliche Ziel-Situationen: sachlich für B2B und Fach-Publikum, provokativ für Differenzierung in einer überfüllten Nische, storytelling für emotionale Verbindung. Die Formeln erzwingen Struktur und verhindern generische Phrasen. Zeichenlimits sind je Variante unterschiedlich weil der Stil das nötige Volumen bestimmt.

## Einschränkungen

- Variante A sachlich: max. 120 Zeichen
- Variante B provokativ: max. 150 Zeichen
- Variante C storytelling: max. 160 Zeichen
- Genau 3 Varianten pro Aufruf — nicht mehr, nicht weniger
- Keine Emojis außer explizit angefordert
- Keine URLs in der Bio — Operator fügt Links separat hinzu

## Ausführungsschritte

1. Identifiziere die Kernkompetenz des Operators in genau 3 Keywords: Was tut der Operator? Für wen? Mit welchem Ergebnis? Dokumentiere die 3 Keywords als "Kompetenz-Basis" vor den Varianten.
2. Schreibe Variante A — sachlich (max. 120 Zeichen): Formel: "[Rolle] der [Tätigkeit] für [Zielgruppe]". Beispiel: "Marketing-Berater der Coaches 10k-Reichweite in 90 Tagen aufbauen". Zeichenanzahl in Klammern dokumentieren. Falls Variante A > 120 Zeichen → kürzen bis Limit eingehalten.
3. Schreibe Variante B — provokativ (max. 150 Zeichen): Formel: "Nicht [Klischee]. [Differenzierung]. [CTA]." Beginne mit einem gebrochenen Klischee der Branche oder Berufsgruppe des Operators, dann die echte Differenzierung, dann ein kurzer CTA. Zeichenanzahl dokumentieren.
4. Schreibe Variante C — storytelling (max. 160 Zeichen): Formel: "Von [Ausgangssituation X] zu [Ergebnis Y]. Jetzt [aktuelle Tätigkeit/Einladung]." Die Transformation muss konkret und messbar sein (z.B. "Von 0 auf 12k Followern in 6 Monaten"). Zeichenanzahl dokumentieren.
5. Dokumentiere für alle 3 Varianten die Zeichenanzahl in einer Zusammenfassungs-Tabelle: Variante | Zeichen | Limit | Status (✓/✗). Falls eine Variante das Limit überschreitet: Kürzungs-Vorschlag direkt nach der Variante angeben.

## Verifikation

- Alle 3 Varianten vorhanden: sachlich, provokativ, storytelling — je als eigener Block mit Formel-Label
- Zeichenanzahl für jede Variante dokumentiert: A ≤ 120, B ≤ 150, C ≤ 160 Zeichen
- 3 Keywords der Kernkompetenz als "Kompetenz-Basis" dokumentiert
- Zusammenfassungs-Tabelle mit Status je Variante vorhanden
- Failure-Indikator: Variante A > 120 Zeichen → Meldung "Variante A überschreitet 120 Zeichen — kürzen" mit Kürzungs-Vorschlag
- Failure-Indikator: Kernkompetenz nicht identifizierbar (Input < 3 Wörter oder ohne Rolle) → Meldung "Profil-Input zu vage — bitte Rolle, Tätigkeit und Zielgruppe angeben"
- Akzeptanzkriterium: 3 Varianten mit erkennbaren Formeln, alle innerhalb Zeichenlimits, Zusammenfassungs-Tabelle vollständig

## Abhängigkeiten

- Input: Kurze Profil-Beschreibung (1–3 Sätze: Rolle, Tätigkeit, Zielgruppe, optionale Erfolgs-Zahl)
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill)

## Output

Kompetenz-Basis (3 Keywords) + 3 Bio-Varianten (je mit Formel-Label, Text und Zeichenanzahl) + Zusammenfassungs-Tabelle (Variante / Zeichen / Limit / Status). Gesamtlänge: max. 350 Wörter, Markdown-Format.
