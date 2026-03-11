# Skill

## Name

/elvis-x-analytics

## Beschreibung

Wertet die 90-Tage-Analytics eines X/Twitter-Accounts systematisch in 5 Abschnitten aus: Follower-Wachstumskurve (13 Datenpunkte), beste 3 Wochen nach Impressionen, Engagement-Rate-Trend, Top-5 Content-Kategorien und Wachstums-Score-Berechnung. Output: Analytics-Report mit 5 Abschnitten, max. 800 Wörter.

## Ziele

- Follower-Wachstumskurve mit 13 wöchentlichen Delta-Werten dokumentiert
- Beste 3 Wochen nach Impressionen identifiziert und Ursachen benannt
- Engagement-Rate-Entwicklung als Wochen-Durchschnitt mit Trend (up/down/stabil) bewertet
- Top-5 Content-Kategorien nach Engagement-Rate gerankt (Kategorien aus Posting-Schedule)
- Wachstums-Score berechnet: (Follower-Delta 90 Tage / Ausgangs-Follower) × 100 = % Wachstum

## Strategie

90 Tage sind der minimale Zeitraum für verlässliche Muster auf X — kürzer und Noise überwiegt Signal. Die 5-Abschnitte-Struktur folgt der Daten-Hierarchie: erst Wachstum (quantitativ), dann Ursachen (qualitativ), dann Effizienz (Engagement), dann Inhalt (Kategorien), dann Gesamt-Score (Synthese). Der Wachstums-Score als Prozent-Wert normiert den Vergleich über verschiedene Account-Größen — ein kleiner Account mit 30% Wachstum schlägt einen großen mit 5%.

## Einschränkungen

- Auswertungszeitraum: genau 90 Tage (13 Wochen), keine Abkürzungen
- Follower-Wachstumskurve: genau 13 Datenpunkte (wöchentliche Deltas, nicht monatlich)
- Beste 3 Wochen: genau 3 (keine Top-5-Liste)
- Top-5 Kategorien: genau 5, aus denselben Kategorien wie in elvis-posting-schedule definiert
- Wachstums-Score-Formel: (Follower-Delta 90 Tage / Ausgangs-Follower) × 100 — keine Abweichung

## Ausführungsschritte

1. Erstelle die Follower-Wachstumskurve: Erhebe wöchentliche Follower-Delta-Werte für die letzten 13 Wochen (Woche 1 = älteste, Woche 13 = aktuellste). Delta = Follower-Zahl Ende der Woche − Follower-Zahl Anfang der Woche. Dokumentiere als Tabelle: Woche | Datum (KW) | Follower-Zahl am Ende | Delta (+ oder −) | Kumuliertes Delta. Markiere die 3 Wochen mit dem höchsten positiven Delta mit einem ★-Symbol.
2. Identifiziere die 3 besten Wochen nach Impressionen-Gesamt: Vergleiche Impressionen-Summe pro Woche über alle 13 Wochen. Dokumentiere Rang 1–3 mit: KW, Impressionen-Summe, Anzahl Posts in dieser Woche. Benenne je Woche die wahrscheinlichste Ursache für die hohen Impressionen (1 Satz je Woche): z.B. viraler Post, Trend-Thema, kollaborativer Post, erhöhte Posting-Frequenz. Ursachen-Typen aus 5 Kategorien wählen: (A) Content-Qualität, (B) Trend-Reaktion, (C) Kollaboration, (D) Frequenz-Erhöhung, (E) Algorithmischer Boost.
3. Analysiere die Engagement-Rate-Entwicklung: Berechne wöchentlichen Durchschnitt der Engagement-Rate für alle 13 Wochen (Engagement-Rate = (Likes + Replies + Reposts) / Impressionen × 100). Dokumentiere als 13-zeilige Tabelle: Woche | Ø Engagement-Rate (%). Bestimme den Trend über die 13 Wochen: "up" = Woche-13-Schnitt ≥ 10% über Woche-1-Schnitt, "down" = ≥ 10% darunter, "stabil" = Abweichung < 10%. Benenne 1 Faktor, der den Trend begünstigt hat (1 Satz).
4. Ranke die Top-5 Content-Kategorien nach durchschnittlicher Engagement-Rate: Verwende dieselben 5 Kategorien wie in elvis-posting-schedule definiert. Pro Kategorie: Anzahl Posts im 90-Tage-Zeitraum, Ø Engagement-Rate, bester Einzel-Post (Titel/Thema und Engagement-Rate). Dokumentiere als Tabelle: Rang | Kategorie | Anzahl Posts | Ø Engagement-Rate | Bester Post. Markiere Kategorie auf Rang 1 als primären Content-Fokus für die nächsten 30 Tage.
5. Berechne den Wachstums-Score: Formel = (Follower-Delta 90 Tage / Ausgangs-Follower) × 100 = % Wachstum. Ausgangs-Follower = Follower-Zahl vor 90 Tagen. Follower-Delta 90 Tage = aktuelle Follower − Ausgangs-Follower. Beispielrechnung dokumentieren: "Von 1.000 auf 1.300 Follower = 300 Delta / 1.000 Ausgangs × 100 = 30% Wachstum in 90 Tagen." Bewertung des Scores: < 5% = kritisch (Strategie-Review empfohlen), 5–15% = solide, 15–30% = gut, > 30% = ausgezeichnet. Schreibe Analytics-Report-Einleitung (2 Sätze): aktueller Score + Gesamt-Bewertung.

## Verifikation

- Follower-Wachstumskurve: Tabelle mit genau 13 Zeilen (Woche 1–13), alle 4 Spalten befüllt
- Beste 3 Wochen: Genau 3 Wochen benannt mit Impressionen-Summe und Ursachen-Typ (A–E)
- Engagement-Trend: Tabelle 13 Wochen + explizite Trend-Aussage (up/down/stabil) + 1 Faktor
- Top-5-Kategorien-Tabelle: 5 Zeilen, alle Spalten befüllt, Rang-1-Kategorie als primärer Fokus markiert
- Failure-Indikator: Wachstums-Score < 5% UND Engagement-Trend "down" → Meldung: "Kritischer Zustand — Wachstumsstagnation und sinkende Engagement-Rate. Sofort elvis-growth-audit vollständig ausführen, dann elvis-niche-finder und elvis-viral-formula überprüfen."

## Abhängigkeiten

- Input: 90-Tage-Analytics-Export (Follower-History, Impressionen pro Woche, Engagement-Rate pro Post), Kategorien-Liste aus elvis-posting-schedule
- Empfohlene Vorgänger-Skills: elvis-growth-audit (Qualitäts-Framework für Analyse), elvis-posting-schedule (Content-Kategorien für Abschnitt 4)

## Output

Analytics-Report mit 5 nummerierten Abschnitten: (1) Follower-Wachstumskurve (Tabelle 13 × 4), (2) Beste 3 Wochen (Tabelle 3 × 4 + Ursachen), (3) Engagement-Trend (Tabelle 13 × 2 + Bewertung), (4) Top-5-Kategorien (Tabelle 5 × 5), (5) Wachstums-Score (Formel + Berechnung + Bewertung). Gesamtlänge: max. 800 Wörter.
