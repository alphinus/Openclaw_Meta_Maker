# Skill

## Name

/elvis-content-calendar

## Beschreibung

Erstellt einen vollständigen 30-Tage-Content-Kalender für X/Twitter mit 30 geplanten Posts in 5 Kategorien. Liefert eine Markdown-Tabelle mit je einem Eintrag pro Tag — inklusive Datum, Kategorie, Thema, Format und empfohlener Posting-Zeit.

## Ziele

- Vollständiger 30-Tage-Kalender mit genau 30 Einträgen, kein Tag ohne Post
- 5 Kategorien in fester Verteilung: 12 Bildung (40%), 6 Unterhaltung (20%), 6 Inspiration (20%), 3 Konversion (10%), 3 Engagement (10%)
- Je Kategorie min. 5 Themen-Ideen im Themen-Pool
- Exportierbarer Markdown-Format mit 6 Spalten

## Strategie

Der Kalender arbeitet kategorie-first: Zuerst wird die Themen-Mischung nach der 40/20/20/10/10-Formel berechnet, dann ein Themen-Pool je Kategorie erstellt, dann die 30 Slots im Kalender mit konkreten Themen befüllt. Die Verteilung folgt dem Prinzip "Mehrwert vor Verkauf" — Bildung und Inspiration dominieren, Konversion ist bewusst auf 10% begrenzt um den Feed nicht zu kommerzialisieren.

## Einschränkungen

- Genau 30 Einträge — ein Eintrag pro Tag, kein Tag darf leer bleiben
- Kategorien-Verteilung ist fix: 12A + 6B + 6C + 3D + 3E = 30 Posts
- Keine Abweichung von der Verteilung ohne explizite Operator-Freigabe
- Posting-Zeiten sind Empfehlungen — kein automatisches Scheduling
- Themen-Pool je Kategorie: min. 5 Ideen bevor Kalender befüllt wird

## Ausführungsschritte

1. Berechne die Kategorie-Verteilung für 30 Tage: Kategorie A Bildung (How-To, Erklärt) = 30 × 40% = 12 Posts; Kategorie B Unterhaltung (Story, Humor) = 30 × 20% = 6 Posts; Kategorie C Inspiration (Quote, Erfolg) = 30 × 20% = 6 Posts; Kategorie D Konversion (Angebot, CTA) = 30 × 10% = 3 Posts; Kategorie E Engagement (Frage, Poll) = 30 × 10% = 3 Posts. Dokumentiere die Summe: 12 + 6 + 6 + 3 + 3 = 30 Posts.
2. Erstelle den Themen-Pool: Für jede der 5 Kategorien mindestens 5 konkrete Themen-Ideen basierend auf dem Nischen-Thema des Operators. Dokumentiere den Pool als Liste vor der Kalender-Tabelle (Format: "A1: Thema", "A2: Thema", usw.).
3. Erstelle die Kalender-Tabelle mit 6 Spalten: Tag (1–30), Datum (TT.MM.YYYY oder TT.MM.), Kategorie (A/B/C/D/E + Buchstaben-Kürzel), Thema (konkreter Titel, max. 60 Zeichen), Format (Tweet / Thread / Quote-Tweet / Poll), Empfohlene Zeit (z.B. "09:00 Uhr"). Befülle alle 30 Zeilen.
4. Prüfe die Lückenfreiheit: Zähle die Einträge je Kategorie in der Tabelle — soll ergeben: 12 A, 6 B, 6 C, 3 D, 3 E. Falls Abweichung: Einträge korrigieren bis die Summe stimmt.
5. Exportiere den Kalender als Markdown-Tabelle mit exakt 30 Daten-Zeilen und 1 Header-Zeile. Format: `| Tag | Datum | Kategorie | Thema | Format | Zeit |` mit Trennzeile nach dem Header. Kein Eintrag darf leer sein.

## Verifikation

- Tabelle enthält genau 30 Daten-Zeilen (Tag 1–30), keine Lücken
- Kategorien-Zählung: exakt 12A, 6B, 6C, 3D, 3E
- Themen-Pool dokumentiert: min. 5 Ideen je Kategorie (= min. 25 Ideen gesamt)
- Alle 6 Spalten befüllt — kein leeres Feld in der Tabelle
- Failure-Indikator: Weniger als 30 Einträge oder Kategorie-Summe ≠ 30 → Meldung "Kalender unvollständig — fehlende Einträge ergänzen"
- Akzeptanzkriterium: 30 Einträge in Markdown-Tabelle, Kategorie-Verteilung 12/6/6/3/3, alle Spalten befüllt

## Abhängigkeiten

- Input: Nischen-Thema des Operators (1–3 Sätze) und optional: Start-Datum des Kalenders
- Empfohlener Vorgänger-Skill: /elvis-content-ideas — kann aber auch eigenständig genutzt werden (elvis-content-ideas liefert einen erweiterten Themen-Pool als Input)

## Output

Themen-Pool (5 Kategorien × min. 5 Ideen = min. 25 Zeilen) + Kalender-Tabelle (Markdown, 30 Daten-Zeilen, 6 Spalten) + Kategorien-Zusammenfassung (12A/6B/6C/3D/3E). Gesamtlänge: max. 1000 Wörter, Markdown-Format.
