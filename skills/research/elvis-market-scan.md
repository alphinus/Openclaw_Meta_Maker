# Skill

## Name

/elvis-market-scan

## Beschreibung

Führt eine strukturierte Marktrecherche zu einem vorgegebenen Thema durch. Identifiziert 10 relevante Quellen (Blogs, Paper, Competitor-Seiten), extrahiert pro Quelle Kernaussage, Datum und Relevanz-Score, und verdichtet die Ergebnisse zu einer strukturierten Zusammenfassung mit 3 Schlüssel-Erkenntnissen und einer Markt-Einschätzung.

## Ziele

- Liste von 10 relevanten Quellen mit Kernaussage, Datum (oder "undatiert") und Relevanz-Score 1–5
- 3 Schlüssel-Erkenntnisse die aus mindestens 3 verschiedenen Quellen gestützt werden
- Identifizierte Wissenslücken: Fragen die keine der 10 Quellen beantwortet
- Einschätzung des Markt-Reifegrads: Frühmarkt / Wachstumsmarkt / gesättigter Markt

## Strategie

Der Skill priorisiert Breite vor Tiefe im ersten Schritt (10 Quellen grob sichten) und geht dann in die Tiefe für die Top-5 Quellen. Quellen werden nach Relevanz-Score gefiltert, nicht nach Bekanntheit des Publishers — ein Nischen-Blog mit direktem Datenpunkt schlägt einen generischen Forbes-Artikel. Schlüssel-Erkenntnisse sind nur gültig wenn sie von mindestens 3 unabhängigen Quellen bestätigt werden. Einzelquellen-Befunde landen in der Wissenslücken-Sektion als "unbestätigt".

## Einschränkungen

- Genau 10 Quellen pro Durchlauf — nicht weniger (dann neu suchen), nicht mehr (dann priorisieren)
- Keine Quellen älter als 24 Monate außer der Operator markiert eine Quelle explizit als "Pflichtquelle"
- Keine bezahlpflichtigen Quellen aufnehmen wenn der Volltext nicht zugänglich ist — nur öffentlich lesbare Inhalte
- Schlüssel-Erkenntnisse müssen mit mindestens 3 Quellen-Verweisen belegt sein
- Keine eigenen Meinungen oder Spekulationen in den Erkenntnissen — nur belegbare Fakten

## Ausführungsschritte

1. Nimm das vorgegebene Thema und identifiziere 3 Suchwinkel: (a) Problem-Perspektive ("Welches Problem löst das?"), (b) Lösung-Perspektive ("Welche Lösungen existieren?"), (c) Markt-Perspektive ("Wer sind die Player und was sagen Zahlen?"). Dokumentiere die 3 Suchwinkel im Output als "Recherche-Rahmen" vor den Quellen.
2. Suche zu jedem Suchwinkel 3–4 relevante Quellen (Ziel: 10 Quellen gesamt, mindestens 2 pro Winkel). Priorisiere: Original-Studien/Paper (höchste Priorität), Hersteller-/Competitor-Seiten mit Zahlen (mittlere Priorität), redaktionelle Artikel und Blogs (niedrigste Priorität, max. 3 davon).
3. Erstelle für jede der 10 Quellen einen strukturierten Eintrag mit: (a) Quelle-Name und URL, (b) Publikationsdatum oder "undatiert", (c) Kernaussage in 1 Satz (max. 30 Wörter), (d) Relevanz-Score 1–5 (1 = kaum relevant, 3 = nützlich, 5 = direkt anwendbar), (e) Suchwinkel-Zuordnung (Problem / Lösung / Markt).
4. Filtere die Quellen nach Relevanz-Score: Identifiziere die Top-5 (Score ≥ 3). Lies diese 5 Quellen vollständig durch und extrahiere pro Quelle: 2–3 konkrete Datenpunkte (Zahlen, Aussagen, Studien-Ergebnisse) die direkt das Thema belegen.
5. Identifiziere 3 Schlüssel-Erkenntnisse die von mindestens 3 der 10 Quellen gestützt werden. Format pro Erkenntnis: "Erkenntnis: [Aussage]. Belege: [Quelle 1], [Quelle 2], [Quelle 3]." Füge für jede Erkenntnis einen konkreten Datenpunkt aus den Quellen hinzu.
6. Identifiziere 3–5 Wissenslücken: Fragen zum Thema die keine der 10 Quellen beantwortet oder die nur durch eine einzelne, unbestätigte Quelle abgedeckt werden. Format: "Offene Frage: [Frage] — [Quelle falls vorhanden, sonst 'unbelegt']."
7. Schreibe die Markt-Einschätzung in 3 Sätzen: Aktueller Reifegrad (Frühmarkt / Wachstumsmarkt / gesättigter Markt) mit Begründung, wichtigste Entwicklung der letzten 12 Monate, größte Unsicherheit/Risiko basierend auf den Wissenslücken.

## Verifikation

- Vollständigkeit: Genau 10 Quellen mit allen 5 Feldern (Name/URL, Datum, Kernaussage, Score, Winkel)
- Belegbarkeit: Jede der 3 Schlüssel-Erkenntnisse enthält mindestens 3 Quellen-Verweise mit Quellenname
- Keine Eigenspekulation: Erkenntnisse enthalten keine Formulierungen wie "wahrscheinlich", "könnte sein", "vermutlich" ohne Quellenbeleg
- Failure-Indikator: Weniger als 5 öffentlich zugängliche Quellen gefunden → Skill bricht ab mit "Zu wenige öffentliche Quellen (< 5) — Thema zu nischig oder zu neu für verlässliche Markt-Analyse"
- Akzeptanzkriterium: 10 bewertete Quellen, 3 belegte Schlüssel-Erkenntnisse, Wissenslücken-Liste, Markt-Einschätzung — alles in einem strukturierten Markdown-Report

## Abhängigkeiten

- Input: Ein klar formuliertes Recherche-Thema (1–2 Sätze) und optional: geografischer Fokus (DE / EN / global) und maximales Quellen-Alter in Monaten
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill für Research-Kategorie)

## Output

Markdown-Report mit 5 Abschnitten: (1) Recherche-Rahmen (3 Suchwinkel), (2) Quellen-Tabelle mit 10 Einträgen und 5 Spalten (Name/URL, Datum, Kernaussage, Score, Winkel), (3) 3 belegte Schlüssel-Erkenntnisse mit Quellen-Verweisen, (4) 3–5 Wissenslücken, (5) Markt-Einschätzung (3 Sätze). Gesamtlänge: max. 1.200 Wörter.
