# Skill

## Name

/elvis-growth-tracker

## Beschreibung

Richtet ein fortlaufendes Wachstums-Tracking-System über 90 Tage ein: Follower-Wachstum, Reichweite und Engagement-Rate werden wöchentlich gemessen und als Fortschritts-Kurve visualisiert. Abgrenzung zu `elvis-growth-audit`: Der Audit ist ein einmaliger Snapshot der aktuellen Situation (wo stehe ich heute?). Dieser Skill baut dagegen ein dauerhaftes Tracking-System auf, das Wachstums-Trends über 12 aufeinanderfolgende Wochen sichtbar macht und Frühwarnsignale bei Abweichungen vom Wachstumspfad gibt. Das Ergebnis ist ein wöchentlich aktualisierbares 90-Tage-Wachstumsbericht-System.

## Ziele

- Definiertes Tracking-System für 3 Kern-Wachstumsmetriken (Follower-Wachstum, Reichweite, Engagement-Rate) mit wöchentlicher Mess-Cadence
- 90-Tage-Wachstumskurve: 12 Wochen-Datenpunkte pro Metrik in einer Trend-Visualisierung
- Wöchentliche Wachstumsrate-Berechnung: `Wachstumsrate (%) = (Aktuell - Vorwoche) / Vorwoche × 100`
- Frühwarnsystem: Automatische Alarm-Trigger wenn Wachstumsrate für 2 aufeinanderfolgende Wochen negativ
- Quartals-Wachstumsziel: Für jede der 3 Metriken ein 90-Tage-Ziel mit wöchentlichem Soll-Ist-Vergleich

## Strategie

Das Tracking-System setzt auf Konsistenz der Messung über Vollständigkeit der Daten: Dieselben Metriken, zur selben Zeit, auf dieselbe Weise gemessen, ergeben zuverlässige Trends. Die 90-Tage-Perspektive ist bewusst gewählt — zu kurz (< 4 Wochen) liefert keine aussagekräftigen Trends, zu lang (> 6 Monate) verliert die Relevanz für aktuelle Entscheidungen. Die wöchentliche Wachstumsrate übersetzt absolute Zahlen in vergleichbare Prozentsätze. Das Frühwarnsystem identifiziert Stagnation bevor sie zum Problem wird.

## Einschränkungen

- Exakt 3 Kern-Wachstumsmetriken im fortlaufenden Tracking — keine sporadischen Zusatzmetriken
- Tracking-Zeitraum: 90 Tage (12 Wochen) als Standard-Zyklus — danach neuer 90-Tage-Zyklus mit Reset
- Mindestens 4 Wochen Daten erforderlich für aussagekräftige Trendaussagen (Frühwarnsystem erst ab Woche 5 aktiv)
- Keine plattformspezifischen Algorithmus-Änderungen als Erklärung akzeptiert ohne Nachbelege — Tracking dokumentiert Zahlen, nicht Ausreden
- Wöchentliche Messung an festem Wochentag (nicht flexibel) — Konsistenz der Zeitreihe ist Pflicht

## Ausführungsschritte

1. Definiere die 3 Kern-Wachstumsmetriken mit exakter Mess-Methode: (A) Follower-Wachstum: Gesamtzahl der Follower am Mess-Tag, gemessen auf der Hauptplattform (welche Plattform? dokumentieren). (B) Reichweite: Impressionen der letzten 7 Tage, summiert über alle Posts der Woche. (C) Engagement-Rate: `(Likes + Kommentare + Reposts) / Impressionen × 100`, Durchschnitt über alle Posts der Woche. Dokumentiere Quelle und Klickpfad für jede Metrik.
2. Lege das 90-Tage-Wachstumsziel für alle 3 Metriken fest: Was soll Woche 12 zeigen im Vergleich zu Woche 1 (Baseline)? Formuliere Ziele als absolute Zahl (z.B. +500 Follower) UND als prozentuale Wachstumsrate (z.B. +25%). Berechne daraus das wöchentliche Soll: `Wöchentliches Soll = Gesamtziel / 12 Wochen`.
3. Erhebe die Baseline-Werte in Woche 1: Alle 3 Metriken messen und als unveränderliche Baseline dokumentieren (Datum + exakter Messwert). Berechne den notwendigen durchschnittlichen wöchentlichen Wachstumspfad von Baseline zu 90-Tage-Ziel.
4. Erstelle die 90-Tage-Tracking-Tabelle mit 14 Spalten: Woche | Datum | Follower | Follower-Wachstum (absolut) | Follower-Wachstumsrate (%) | Reichweite | Reichweite-Δ (%) | Engagement-Rate | Engagement-Δ (pp) | Soll-Follower | Soll-Reichweite | Soll-Engagement | Abweichung Soll-Ist | Alarm (🟢/🟡/🔴). Befülle Woche 1 mit Baseline-Werten.
5. Definiere die Frühwarn-Logik: 🟢 = Wachstumsrate positiv, auf oder über Soll-Pfad. 🟡 = Wachstumsrate positiv aber unter Soll-Pfad (< 80% des Wochenziels). 🔴 = Wachstumsrate negativ ODER 2 aufeinanderfolgende Wochen unter 80% des Wochenziels. Bei 🔴: Alarm-Text generieren mit konkreter Abweichung und empfohlener Reaktion.
6. Schreibe die wöchentliche Mess-Anleitung (max. 10 Schritte): Wann messen (Wochentag + Uhrzeit), wo die Daten abrufen (Klickpfad pro Plattform), wie die Wachstumsrate berechnen (`(Aktuell - Vorwoche) / Vorwoche × 100`), wie die Tabelle aktualisieren, wie den Alarm-Status setzen. Füge einen Kalender-Template-Text für die wöchentliche Erinnerung bei.
7. Führe nach Woche 4 einen ersten Trend-Review durch: Berechne die durchschnittliche wöchentliche Wachstumsrate für alle 3 Metriken. Ist der aktuelle Trend ausreichend um das 90-Tage-Ziel zu erreichen? Falls nein: Welche konkrete Maßnahme wird in Woche 5 getestet?

## Verifikation

- Baseline vorhanden: Alle 3 Metriken mit Woche-1-Baseline-Wert und Datum dokumentiert
- Ziel definiert: 90-Tage-Ziel für alle 3 Metriken als Absolut- und Prozentzahl vorhanden
- Tracking-Tabelle: 12 Wochen-Zeilen angelegt (Woche 1 befüllt, Wochen 2–12 als Platzhalter)
- Wachstumsrate-Formel: `Wachstumsrate (%) = (Aktuell - Vorwoche) / Vorwoche × 100` explizit dokumentiert
- Failure-Indikator: Wenn weniger als 4 Wochen Daten vorhanden → Skill gibt aus: "Weniger als 4 Wochen Daten — Wachstumstrend nicht aussagekräftig. Bitte Tracking fortführen bis mindestens Woche 4 bevor Trendaussagen gemacht werden."
- Akzeptanzkriterium: Befüllte Tracking-Tabelle (Woche 1 + Baseline), 90-Tage-Ziele, Frühwarn-Logik und Mess-Anleitung — System sofort einsatzbereit für wöchentliche Aktualisierung

## Abhängigkeiten

- Input: Zugang zu mindestens einer Analytics-Plattform (X Analytics / Instagram Insights / YouTube Studio) für wöchentliche Datenerhebung
- Empfohlene Vorgänger-Skills: /elvis-growth-audit (liefert ersten Überblick über aktuelle Wachstumssituation und Benchmark), /elvis-performance-tracker (liefert weiteres Tracking-Framework-Muster)

## Output

Markdown-Dokument mit 4 Abschnitten: (1) 3 Wachstumsmetriken-Steckbriefe (Formel, Quelle, Klickpfad, 90-Tage-Ziel), (2) 90-Tage-Tracking-Tabelle (14 Spalten × 12 Wochen, Woche 1 mit Baseline befüllt), (3) Frühwarn-System (Ampel-Logik, Alarm-Trigger, Reaktions-Empfehlungen), (4) Mess-Anleitung für wöchentliche Aktualisierung. Sofort einsatzbereit als wöchentliches Tracking-Ritual.
