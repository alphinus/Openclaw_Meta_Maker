# Skill

## Name

/elvis-conversion-analyzer

## Beschreibung

Analysiert monatlich die Konversionsraten für 3 definierte Ziel-Aktionen (CTA-Klicks, Opt-Ins, Käufe) mit Tiefenanalyse einzelner Konversionspunkte. Im Gegensatz zu `elvis-funnel-analyzer` (der den gesamten Funnel von Awareness bis Conversion betrachtet) fokussiert sich dieser Skill auf die tiefere Analyse einzelner kritischer Konversionspunkte: Warum klicken Nutzer nicht auf den CTA? Was hindert Interessenten am Opt-In? Wo brechen Käufer ab? Das Ergebnis ist eine monatlich aktualisierbare Konversionsanalyse mit konkreten Optimierungs-Hypothesen je Ziel-Aktion.

## Ziele

- Konversionsrate für 3 Ziel-Aktionen gemessen mit monatlicher Cadence (CTA-Klicks, Opt-Ins, Käufe)
- Tiefenanalyse je Konversionspunkt: 5 identifizierte Optimierungspotenziale mit Prioritäts-Ranking
- Hypothesen-basierte Optimierungsempfehlungen: Für jeden Konversionspunkt 2 testbare Hypothesen
- Benchmark-Vergleich: Wie liegt die eigene Conversion-Rate im Vergleich zu Branchen-Richtwerten?
- Monatlicher Trend-Vergleich: Entwicklung der 3 Konversionsraten über 3 Monate

## Strategie

Der Skill arbeitet mit dem Tiefenbohr-Prinzip: Statt den gesamten Funnel oberflächlich zu analysieren, wird jeder der 3 kritischen Konversionspunkte einzeln in die Tiefe analysiert. Die Hypothesen-Generierung folgt dem "5-Why"-Prinzip: Nicht nur "was" ist das Problem, sondern "warum" konvertieren Nutzer nicht? Jede Hypothese muss testbar sein (A/B-Test oder zeitlich begrenzte Anpassung). Die monatliche Cadence erlaubt Trend-Beobachtung ohne Tagesrauschen.

## Einschränkungen

- Exakt 3 Ziel-Aktionen pro Analyse-Zyklus — mehr verwässern die Tiefe
- Nur Konversionspunkte analysieren für die >100 Interaktionen pro Monat vorliegen (Mindest-Stichprobe)
- Keine Optimierungsempfehlungen ohne messbare Baseline — erst messen, dann optimieren
- Max. 2 testbare Hypothesen pro Konversionspunkt (Fokus statt Feature-Overload)
- Monatliche Mess-Cadence nicht verkürzen — wöchentliche Schwankungen sind Rauschen, nicht Trend

## Ausführungsschritte

1. Definiere die 3 Ziel-Aktionen gemeinsam mit dem Operator: (A) CTA-Klicks: Welcher Call-to-Action ist der wichtigste? (z.B. "Newsletter abonnieren" / "Produkt ansehen" / "Demo buchen"). (B) Opt-Ins: Welcher Lead-Magnet oder welche Anmeldung ist das primäre Wachstums-Ziel? (C) Käufe: Welches Produkt oder welcher Service ist die Haupteinnahmequelle? Dokumentiere für jede Ziel-Aktion die exakte Definition und wo sie gemessen wird.
2. Erhebe für jede der 3 Ziel-Aktionen die Baseline-Konversionsrate über den letzten 30-Tage-Zeitraum: `Konversionsrate (%) = Ziel-Aktion abgeschlossen / Ziel-Aktion-Möglichkeit × 100`. Beispiel CTA: `Klicks auf CTA / Impressionen des CTA × 100`. Dokumentiere Stichprobengröße (Anzahl Impressionen / Besucher / potenzielle Konvertierer).
3. Vergleiche jede der 3 Konversionsraten mit Branchen-Benchmarks: Typische Richtwerte — CTA-Klickrate: 2–5 %, Opt-In-Rate: 3–10 %, Kauf-Conversion: 1–3 % (E-Commerce) / 5–15 % (Info-Produkte). Markiere jede Rate als "✓ im Bereich", "⚡ über Benchmark" oder "⚠️ unter Benchmark". Füge Quellenangabe für Benchmarks hinzu.
4. Führe für jeden der 3 Konversionspunkte eine 5-Warum-Analyse durch: Warum ist die Konversionsrate (nicht) im Zielbereich? Identifiziere 5 mögliche Hinderungsgründe (z.B. CTA zu generisch / Formular zu lang / Preis nicht sichtbar / Trust-Signale fehlen / Ladezeit zu hoch). Priorisiere die Top-3 Hinderungsgründe nach vermuteter Impact-Größe.
5. Erstelle für jeden Konversionspunkt 2 testbare Hypothesen: "Wenn wir [Änderung X], dann wird die Konversionsrate um [Y %] steigen, weil [Begründung Z]." Beispiel: "Wenn wir den CTA-Text von 'Mehr erfahren' zu 'Jetzt kostenlos starten' ändern, dann steigt die Klickrate um 15 %, weil konkrete Benefits höher konvertieren als generische Phrasen." Dokumentiere für jede Hypothese den Test-Aufwand (Niedrig / Mittel / Hoch).
6. Berechne das theoretische Potenzial jeder Optimierung: Wenn die Hypothese zutrifft, wie viele zusätzliche Conversions pro Monat würde das generieren? Multipliziere Stichprobengröße × erwartete Steigerung × durchschnittlicher Wert pro Conversion. Beispiel: 1000 CTA-Impressionen × 15 % Steigerung × 5 € durchschnittlicher Opt-In-Wert = 750 € monatliches Potenzial.
7. Erstelle die Optimierungs-Prioritätsliste mit 3 Spalten: Konversionspunkt | Hypothese | Monatliches Potenzial | Test-Aufwand | Prioritäts-Score (Potenzial / Aufwand). Sortiere nach Prioritäts-Score absteigend. Empfehle die Top-2 Hypothesen für sofortigen Test im nächsten Monat.

## Verifikation

- Baseline gemessen: Alle 3 Konversionsraten mit Stichprobengröße und Datum dokumentiert
- Benchmark-Vergleich: Alle 3 Raten gegen Branchen-Richtwerte bewertet (✓ / ⚡ / ⚠️)
- Hypothesen konkret: Jede der 6 Hypothesen (2 pro Konversionspunkt) folgt dem "Wenn-Dann-Weil"-Format
- Potenzial berechnet: Für jede Hypothese monatliches Conversion-Potenzial in konkreter Zahl (nicht "wird besser")
- Failure-Indikator: Wenn für mehr als 1 der 3 Ziel-Aktionen die Konversionsrate nicht messbar ist (z.B. keine Tracking-Daten oder <100 Interaktionen) → Skill gibt aus: "Konversionsrate für >1 Ziel-Aktion nicht messbar — Analyse nicht valide. Bitte Tracking einrichten oder Stichprobenanzahl erhöhen (min. 100 Interaktionen pro Monat)."
- Akzeptanzkriterium: Konversionsraten-Tabelle (3 Ziel-Aktionen × Baseline × Benchmark-Status), 6 testbare Hypothesen, Optimierungs-Prioritätsliste mit Potenzial-Berechnung

## Abhängigkeiten

- Input: Tracking-Daten für CTA-Klicks, Opt-Ins und Käufe über mindestens 30 Tage (z.B. aus Google Analytics, ConvertKit, Stripe)
- Empfohlene Vorgänger-Skills: /elvis-funnel-analyzer (liefert Überblick über gesamten Funnel, identifiziert kritische Konversionspunkte), /elvis-performance-tracker (liefert Baseline-Metriken für Trend-Vergleich)

## Output

Markdown-Dokument mit 4 Abschnitten: (1) Konversionsraten-Tabelle (3 Ziel-Aktionen × Baseline × Stichprobengröße × Benchmark-Status), (2) 5-Warum-Analyse je Konversionspunkt (Top-3 Hinderungsgründe identifiziert), (3) 6 testbare Hypothesen (je 2 pro Konversionspunkt im Wenn-Dann-Weil-Format), (4) Optimierungs-Prioritätsliste mit Potenzial-Berechnung und Top-2-Empfehlung für nächsten Monat. Sofort einsatzbereit als Grundlage für A/B-Tests.
