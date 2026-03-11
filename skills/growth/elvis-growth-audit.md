# Skill

## Name

/elvis-growth-audit

## Beschreibung

Analysiert die Wachstums-Performance eines X/Twitter-Accounts über die letzten 14 Tage. Identifiziert die Top-20 Posts nach Engagement-Rate, extrahiert die 5 häufigsten Engagement-Muster und erstellt eine Liste von 10 Wachstums-Hypothesen mit Begründung — fertig in einer einzigen Analyse-Session.

## Ziele

- Identifizierte Top-20 Posts der letzten 14 Tage, sortiert nach Engagement-Rate (Likes + Reposts + Replies / Impressionen × 100)
- Extrahierte 5 Engagement-Muster mit Frequenz und durchschnittlicher Rate pro Muster
- Liste von 10 priorisierten Wachstums-Hypothesen, jede mit einer konkreten Begründung aus den Daten
- Vergleich der Posting-Frequenz (Posts/Woche) vs. Engagement-Rate-Entwicklung über die 14 Tage

## Strategie

Der Skill analysiert von oben nach unten: erst die Rohdaten strukturieren, dann quantifizieren, dann interpretieren. Engagement-Rate wird über absolute Zahlen gestellt, da sie Accounts unterschiedlicher Größe vergleichbar macht. Hypothesen werden nach Daten-Evidenz gewichtet — stark belegte Hypothesen stehen oben, spekulative unten. Keine Empfehlung ohne Datenpunkt als Anker.

## Einschränkungen

- Max. 20 Posts pro Analyse-Durchlauf (die neuesten 20 innerhalb der letzten 14 Kalendertage)
- Keine automatischen Posts oder Account-Aktionen — reine Lese- und Analyse-Operation
- Nur öffentlich zugängliche Metriken auswerten (keine API-Calls ohne Operator-Freigabe)
- Keine Analyse von Accounts Dritter ohne explizite Freigabe durch den Operator
- Ergebnis wird nur ausgegeben, nicht gespeichert oder an externe Dienste weitergeleitet

## Ausführungsschritte

1. Rufe die letzten 20 Posts des Accounts ab (Zeitraum: die zurückliegenden 14 Kalendertage). Für jeden Post erfasse: Post-Text, Datum/Uhrzeit, Impressionen, Likes, Reposts, Replies. Fehlende Werte als 0 setzen und im Report markieren.
2. Berechne für jeden Post die Engagement-Rate: (Likes + Reposts + Replies) / Impressionen × 100, gerundet auf zwei Dezimalstellen. Sortiere alle 20 Posts absteigend nach Engagement-Rate.
3. Analysiere die Top-10 Posts auf gemeinsame Muster: Content-Format (Nur-Text, Bild, Video, Thread, Poll), Themen-Cluster (Nischen-Keywords, max. 5 Cluster), Posting-Uhrzeit in 3-Stunden-Blöcken (06–09, 09–12, 12–15, 15–18, 18–21, 21–00), Post-Länge in Kategorien (kurz ≤140 Zeichen, mittel 141–220, lang 221–280).
4. Zähle die Häufigkeit jedes Musters unter den Top-10 Posts und berechne die Durchschnitts-Engagement-Rate pro Muster-Ausprägung. Identifiziere die 5 Muster mit dem stärksten Einfluss auf die Engagement-Rate (größte Differenz zur Gesamtdurchschnitts-Rate).
5. Formuliere 10 Wachstums-Hypothesen im Format: "Wenn [Bedingung], dann [erwartetes Ergebnis], weil [Datenpunkt aus der Analyse]." Ordne die Hypothesen nach Evidenzstärke: Rang 1–3 = stark belegt (≥5 Datenpunkte), Rang 4–7 = moderat (2–4 Datenpunkte), Rang 8–10 = schwach/spekulativ (1 Datenpunkt oder Ableitung).
6. Schreibe den Analyse-Report im Markdown-Format mit 5 Abschnitten: (1) Executive Summary (5 Sätze), (2) Top-20-Tabelle mit 5 Spalten (Rang, Post-Vorschau 40 Zeichen, Datum, Engagement-Rate %, Muster-Tags), (3) Die 5 stärksten Muster mit Häufigkeit und Rate, (4) 10 Wachstums-Hypothesen mit Evidenzgrad, (5) Nächste-Schritte-Empfehlungen (3 konkrete Aktionen für die nächsten 7 Tage). Gesamtlänge: max. 1.000 Wörter.

## Verifikation

- Vollständigkeitsprüfung: Report enthält alle 5 Abschnitte — Executive Summary, Top-20-Tabelle, Muster-Analyse, Hypothesen-Liste, Nächste Schritte
- Datenintegrität: Jede Engagement-Rate in der Tabelle ist aus den Rohdaten (Likes + Reposts + Replies / Impressionen) nachvollziehbar
- Hypothesen-Format: Alle 10 Hypothesen folgen dem "Wenn … dann … weil …"-Format mit einem konkreten Datenpunkt
- Failure-Indikator: Weniger als 5 Posts im 14-Tage-Zeitraum → Skill bricht ab mit Meldung "Datenbasis zu klein (< 5 Posts) — Muster-Analyse nicht aussagekräftig"
- Akzeptanzkriterium: Report ist vollständig, alle 5 Abschnitte befüllt, genau 5 Muster und genau 10 Hypothesen identifiziert, alle Engagement-Rates auf 2 Dezimalstellen gerundet

## Abhängigkeiten

- Input: Zugang zu X/Twitter-Account-Metriken (Analytics-Export oder Analytics-Dashboard der letzten 14 Tage) mit Impressionen, Likes, Reposts, Replies pro Post
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill für Growth-Kategorie)

## Output

Markdown-Report (max. 1.000 Wörter) mit 5 Abschnitten: Executive Summary, Top-20-Tabelle mit Engagement-Rates, 5 Muster-Befunde mit Häufigkeiten, 10 priorisierte Wachstums-Hypothesen mit Evidenzgrad, 3 konkrete Nächste-Schritte-Empfehlungen für 7 Tage.
