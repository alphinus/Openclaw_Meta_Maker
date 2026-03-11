# Skill

## Name

/elvis-content-ideas

## Beschreibung

Generiert 20 Content-Ideen zu einem Thema, aufgeteilt in 4 Kategorien: Bildung (8), Unterhaltung (5), Inspiration (4), Konversion (3). Je Idee: Kategorie, Ideen-Titel, Format (Single/Thread/Poll) und Dringlichkeit (Evergreen/Trend). Nutzt Trend-Themen aus elvis-x-trend-scanner als Input.

## Ziele

- 20 fertige Content-Ideen: 8 Bildung + 5 Unterhaltung + 4 Inspiration + 3 Konversion
- Je Idee: Kategorie-Label, Titel, Format-Empfehlung, Dringlichkeits-Tag
- Mindestens 3 Ideen in jeder Kategorie (Warnung wenn Kategorie unterversorgt)
- Thema in 3 Unter-Themen aufgeteilt als Brainstorming-Basis

## Strategie

20 Ideen decken typischerweise 3–4 Wochen Content ab und vermeiden den "leeren Kalender"-Effekt. Die 8/5/4/3-Aufteilung folgt dem Pareto-Prinzip für X/Twitter: Bildungs-Content erzeugt Reichweite, Unterhaltung schafft Bindung, Inspiration baut Vertrauen, Konversions-Content konvertiert. Das Evergreen/Trend-Tag priorisiert die Reihenfolge: Trend-Content zuerst, Evergreen-Content als Puffer.

## Einschränkungen

- Exakt 20 Ideen — nicht mehr, nicht weniger
- Kategorie-Aufteilung fix: (A) Bildung = 8 Ideen, (B) Unterhaltung = 5 Ideen, (C) Inspiration = 4 Ideen, (D) Konversion = 3 Ideen
- Wenn eine Kategorie weniger als die Soll-Anzahl erreicht → sofort auffüllen, nicht übergehen
- Je Idee ein Format (Single-Post, Thread oder Poll) und ein Dringlichkeits-Tag (Evergreen oder Trend)
- Kein automatisches Posten — Output ist zur Kalender-Planung bestimmt

## Ausführungsschritte

1. Teile das Thema in genau 3 Unter-Themen auf: Benenne 3 Aspekte, Zielgruppen-Probleme oder Anwendungsfälle des Haupt-Themas. Dokumentiere diese 3 Unter-Themen als "Brainstorming-Basis" vor der Ideen-Liste. Wenn elvis-x-trend-scanner verfügbar ist: Prüfe ob Trend-Themen als 1 oder mehr der 3 Unter-Themen nutzbar sind.
2. Brainstorme je Unter-Thema mindestens 7 Roh-Ideen (= mindestens 21 Roh-Ideen gesamt). Schreibe alle auf — keine Selbstzensur in dieser Phase. Format: kurze Beschreibung, noch kein Kategorie-Label.
3. Wähle die 20 stärksten Ideen aus den ≥21 Roh-Ideen. Auswahlkriterium: Relevanz für die Zielgruppe (nicht persönliches Interesse des Autors). Sortiere die 20 ausgewählten Ideen nach Kategorie: A, B, C, D.
4. Weise jeder Idee ein Format zu: Single-Post wenn 1 klarer Gedanke (≤280 Zeichen möglich), Thread wenn ≥3 Entwicklungsschritte nötig, Poll wenn Meinungsabfrage natürlich wirkt. Weise Dringlichkeits-Tag zu: "Trend" wenn Bezug zu aktuellem Ereignis oder Trend-Thema, "Evergreen" für zeitlose Inhalte.
5. Prüfe Kategorie-Vollständigkeit: A = genau 8, B = genau 5, C = genau 4, D = genau 3. Wenn eine Kategorie unterversorgt ist → fehlende Ideen sofort ergänzen aus den Roh-Ideen oder neu generieren. Dokumentiere den finalen Output als nummerierte Liste mit Kategorie-Label, Titel, Format und Dringlichkeit.

## Verifikation

- Thema in genau 3 Unter-Themen aufgeteilt und dokumentiert
- Mindestens 21 Roh-Ideen generiert (oder Zahl dokumentiert)
- Exakt 20 finale Ideen: 8×A + 5×B + 4×C + 3×D
- Jede Idee mit Kategorie-Label (A/B/C/D), Titel, Format (Single/Thread/Poll) und Dringlichkeit (Evergreen/Trend)
- Failure-Indikator: Weniger als 3 Ideen in einer Kategorie → Meldung "Kategorie [X] unterversorgt — [Soll-Anzahl - Ist-Anzahl] Ideen fehlen. Ergänze aus Roh-Ideen oder generiere neu."
- Akzeptanzkriterium: Exakt 20 Ideen in der 8/5/4/3-Verteilung, alle 4 Felder je Idee ausgefüllt

## Abhängigkeiten

- Input: Haupt-Thema für das Content-Ideen generiert werden sollen
- Empfohlene Vorgänger-Skills: elvis-x-trend-scanner (empfohlen — Trend-Themen als Unter-Themen-Input für Dringlichkeits-Tag "Trend")

## Output

Brainstorming-Basis (3 Unter-Themen) + 20 Content-Ideen als nummerierte Liste mit Kategorie (A/B/C/D), Titel, Format (Single/Thread/Poll) und Dringlichkeit (Evergreen/Trend). Gesamtlänge: max. 500 Wörter, Markdown-Format.
