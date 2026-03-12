# Skill

## Name

/elvis-kpi-dashboard

## Beschreibung

Definiert eine KPI-Dashboard-Struktur mit 5 strategischen Ziel-KPIs, 10 unterstützenden Metriken, konkreten Zielwerten und Alarm-Schwellen. Im Gegensatz zu `elvis-performance-tracker` (der wöchentlich misst und verfolgt) visualisiert und priorisiert dieses Dashboard: Es zeigt auf einen Blick, welche KPIs auf Kurs sind, welche Aufmerksamkeit brauchen und wo sofortige Maßnahmen erforderlich sind. Das Dashboard wird monatlich reviewed und bei Strategie-Änderungen aktualisiert.

## Ziele

- Definierte 5 strategische Ziel-KPIs mit Zielwert, aktuellem Wert und Trend (steigend / stabil / fallend)
- 10 unterstützende Metriken zugeordnet zu den 5 KPIs (je 2 pro KPI) als Frühwarnindikatoren
- Alarm-Schwellen für alle 5 KPIs: kritischer Grenzwert der sofortiges Handeln auslöst
- Priorisierte Handlungsliste: 3 KPIs mit dem größten Hebel für sofortige Maßnahmen
- Dashboard-Vorlage die monatlich mit neuen Werten befüllbar ist (ohne Restrukturierung)

## Strategie

Das Dashboard fokussiert auf 5 strategische KPIs weil mehr Hauptkennzahlen die Priorität verwischen. Jeder KPI bekommt 2 unterstützende Metriken als Frühwarnindikatoren — sie zeigen Ursachen bevor der KPI selbst ins Rote fällt. Die Alarm-Schwellen sind bewusst konservativ gesetzt: Lieber früh reagieren als eine Krise verwalten. Die monatliche Review-Cadence ist der richtige Rhythmus für strategische KPIs — zu häufige Reviews führen zu Überreaktionen auf natürliche Schwankungen.

## Einschränkungen

- Exakt 5 strategische Ziel-KPIs — nicht mehr (zu viele KPIs = kein Fokus), nicht weniger (zu wenige = blinde Flecken)
- Jeder KPI bekommt exakt 2 unterstützende Metriken (10 insgesamt) — keine Ausnahmen
- Alle KPIs müssen quantitativ messbar sein — keine qualitativen oder gefühlsmäßigen KPIs
- Keine KPIs die ausschließlich von externen Faktoren abhängen (z.B. "Algorithmus-Reichweite" unkontrollierbar)
- Zielwerte müssen vom Operator bestätigt sein — keine Annahmen oder Benchmark-Werte ohne Rückfrage

## Ausführungsschritte

1. Ermittle mit dem Operator die übergeordneten Geschäftsziele für die nächsten 90 Tage (max. 3 Ziele, z.B. "Audience verdoppeln", "Ersten zahlenden Kunden gewinnen", "Content-Konsistenz aufbauen"). Leite aus jedem Ziel den einen messbaren KPI ab der den Fortschritt am direktesten abbildet. Reduziere auf 5 finale Ziel-KPIs.
2. Definiere für jeden der 5 KPIs: Aktueller Wert (Stand heute), Zielwert (in 90 Tagen), Alarm-Schwelle (kritischer Mindestwert), Trend (steigend / stabil / fallend basierend auf letzten 4 Wochen), Verantwortung (wer misst und reported diesen KPI?).
3. Weise jedem der 5 KPIs exakt 2 unterstützende Metriken zu. Kriterium: Diese Metriken müssen sich verschlechtern bevor der KPI selbst unter die Alarm-Schwelle fällt (Frühwarnindikatoren). Dokumentiere den Zusammenhang in einem Satz pro Metrik: "Wenn [Metrik X] sinkt, folgt [KPI Y] innerhalb von [Zeitraum]."
4. Erstelle die Dashboard-Übersichtstabelle mit 6 Spalten: KPI-Name, Aktuell, Ziel (90 Tage), Alarm-Schwelle, Trend, Status (🟢/🟡/🔴). Fülle alle 5 KPIs ein. Setze den Status anhand der Alarm-Schwellen-Logik: 🟢 = auf Kurs, 🟡 = Tendenz zur Alarm-Schwelle (< 80 % Fortschritt), 🔴 = Alarm-Schwelle erreicht oder unterschritten.
5. Priorisiere die 3 KPIs mit dem größten sofortigen Handlungsbedarf (nach Status und Hebel). Formuliere für jeden der 3 eine konkrete Sofortmaßnahme (1–2 Sätze): Was kann in den nächsten 7 Tagen getan werden um den KPI zu verbessern?
6. Erstelle die monatliche Review-Vorlage: Tabelle mit Datum, allen 5 KPI-Werten und einem Freitext-Feld "Anpassungen diese Woche". Die Vorlage ist für 12 Monate vorbereitet (12 leere Zeilen).
7. Schreibe eine Dashboard-Legende (max. 1 Seite): Wie wird das Dashboard gelesen? Was bedeutet jeder Status? Wann wird welche Maßnahme ausgelöst? Wer muss bei 🔴 informiert werden?

## Verifikation

- KPI-Vollständigkeit: Alle 5 KPIs haben Aktuell, Ziel, Alarm-Schwelle, Trend und Status ausgefüllt
- Metrik-Zuordnung: Jeder KPI hat exakt 2 unterstützende Metriken mit dokumentiertem Frühwarn-Zusammenhang
- Alarm-Logik: Alle Alarm-Schwellen sind quantitativ (keine "zu niedrig" oder "deutlich gesunken")
- Sofortmaßnahmen: Alle 3 priorisierten KPIs haben eine konkrete 7-Tage-Maßnahme
- Failure-Indikator: Wenn für mehr als 2 der 5 KPIs der Zielwert unbekannt oder nicht bestätigt ist → Skill gibt aus: "Zielwerte für mehr als 2 KPIs fehlen — Dashboard nicht aussagekräftig. Bitte Ziele mit dem Operator klären bevor das Dashboard aufgebaut wird."
- Akzeptanzkriterium: Dashboard-Tabelle vollständig befüllt, 10 unterstützende Metriken zugeordnet, monatliche Review-Vorlage vorhanden

## Abhängigkeiten

- Input: Geschäftsziele für die nächsten 90 Tage (vom Operator bestätigt), aktuelle Werte für mindestens 3 der 5 KPIs
- Empfohlene Vorgänger-Skills: /elvis-growth-audit (liefert Ist-Werte als Ausgangspunkt), /elvis-performance-tracker (liefert Trend-Daten für KPI-Einschätzung)

## Output

Markdown-Dokument mit 4 Abschnitten: (1) KPI-Übersichtstabelle (5 KPIs × 6 Spalten, vollständig befüllt), (2) Unterstützende Metriken-Matrix (5 KPIs × je 2 Frühwarnindikatoren mit Zusammenhang-Beschreibung), (3) Priorisierte Sofortmaßnahmen (Top-3 KPIs mit je 1 konkreten 7-Tage-Maßnahme), (4) Monatliche Review-Vorlage (12 Monate vorbereitet) + Dashboard-Legende. Einsatzbereit als strategisches Steuerungs-Dokument für monatliche Reviews.
