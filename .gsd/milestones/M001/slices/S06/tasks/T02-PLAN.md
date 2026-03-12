---
estimated_steps: 5
estimated_files: 5
---

# T02: Restliche 5 Analysis Skills

**Slice:** S06 — Automation + Analysis Skills (~20 Skills)
**Milestone:** M001

## Description

Vervollständigt die 10 Analysis Skills in `skills/analysis/`. Die zweiten 5 Skills decken Reporting-Systeme, Growth-Tracking, Konversions-Analyse, Konkurrenz-Monitoring und Revenue-Tracking ab. Nach diesem Task sind alle 10 Analysis Skills vorhanden und `verify-s06.sh` sollte [1/4] 10/19 ✓ melden (die 9 Automation-Dateien fehlen noch).

Besonderer Fokus auf inhaltliche Differenzierung:
- `elvis-growth-tracker` muss sich klar von `elvis-growth-audit` (S01) abgrenzen: Tracker = fortlaufendes Mess-System mit 90-Tage-Kurve; Audit = einmaliger Snapshot
- `elvis-competitor-monitor` muss sich von `elvis-competitor-analysis` (S04, einmaliger 4-Wochen-Scan) und `elvis-competitor-deep-dive` (S05, qualitative Einzeltiefenanalyse) durch Ongoing-Monitoring-Charakter mit Alarm-Triggern unterscheiden
- `elvis-revenue-tracker` misst Ist-Ergebnisse (Tracking), während `elvis-monetization-planner` (S04) Soll-Pläne erstellt und `elvis-monetization-strategy` (S05) Strategien definiert

## Steps

1. `skills/analysis/elvis-reporting-system.md` schreiben:
   - **Kern:** Baut wöchentliches + monatliches Reporting-System: 5 Pflicht-Metriken, Report-Template, Verteilungs-Prozess
   - Differenzierung: System (wer/was/wann/Format) statt einmaliger Report
   - Failure-Indikator: Wenn Datenquellen für >2 Pflicht-Metriken nicht verfügbar → Meldung
   - Abhängigkeiten: `elvis-performance-tracker` als empfohlener Vorgänger (existiert aus T01)

2. `skills/analysis/elvis-growth-tracker.md` schreiben:
   - **Kern:** Trackt Wachstums-Metriken über 90 Tage: Follower-Wachstum, Reichweite, Engagement-Rate — wöchentliche Fortschritts-Kurve
   - `## Beschreibung` muss explizit "fortlaufendes Tracking" und Abgrenzung zu `elvis-growth-audit` (einmaliger Snapshot) enthalten
   - Failure-Indikator: Wenn <4 Wochen Daten vorhanden → Meldung (Trend nicht aussagekräftig)

3. `skills/analysis/elvis-conversion-analyzer.md` schreiben:
   - **Kern:** Analysiert Konversionsraten für 3 Ziel-Aktionen: CTA-Klicks, Opt-Ins, Käufe — mit Optimierungs-Hypothesen
   - Differenzierung: analysiert einzelne Konversionspunkte tiefer als `elvis-funnel-analyzer` (der gesamten Funnel)
   - Failure-Indikator: Wenn Konversionsrate für >1 Ziel-Aktion nicht messbar → Meldung

4. `skills/analysis/elvis-competitor-monitor.md` schreiben:
   - **Kern:** Richtet fortlaufendes Konkurrenz-Monitoring ein: 5 Accounts × 4 Metriken, wöchentliche Alerts, Benchmark-Vergleich
   - `## Beschreibung` muss "fortlaufendes Monitoring-System" und Abgrenzung zu `elvis-competitor-analysis` (S04) und `elvis-competitor-deep-dive` (S05) enthalten
   - Failure-Indikator: Wenn <3 der 5 Accounts konsistent trackbar → Meldung

5. `skills/analysis/elvis-revenue-tracker.md` schreiben:
   - **Kern:** Trackt Umsatz und Monetarisierungs-Metriken: 3 Einkommensquellen × monatliche Trends, CLV-Entwicklung, MRR-Berechnung
   - Differenzierung: misst Ist-Ergebnisse vs. `elvis-monetization-planner` (S04, plant Soll) und `elvis-monetization-strategy` (S05, definiert Strategie)
   - Scoring-Formel in Ausführungsschritten: `CLV = Kaufwert × Kauffrequenz × Kundendauer` (D028)
   - Failure-Indikator: Wenn <2 der 3 Einkommensquellen mit konkreten Zahlen trackbar → Meldung

## Must-Haves

- [ ] Alle 5 Analysis Skills haben alle 9 Pflicht-Sektionen (`## Name`, `## Beschreibung`, `## Ziele`, `## Strategie`, `## Einschränkungen`, `## Ausführungsschritte`, `## Verifikation`, `## Abhängigkeiten`, `## Output`)
- [ ] Alle 5 Skills enthalten `/elvis-*` im `## Name`-Block (D001)
- [ ] Alle 5 Skills enthalten `Failure-Indikator:` mit konkreter Schwelle und Meldungstext
- [ ] `elvis-growth-tracker.md` enthält "fortlaufend" oder "Tracking" + explizite Abgrenzung zu `elvis-growth-audit`
- [ ] `elvis-competitor-monitor.md` enthält "fortlaufendes Monitoring-System" + explizite Abgrenzung zu `elvis-competitor-analysis` und `elvis-competitor-deep-dive`
- [ ] `elvis-revenue-tracker.md` enthält `CLV = Kaufwert × Kauffrequenz × Kundendauer` als explizite Formel (D028)
- [ ] Alle Inhalte auf Deutsch (D002); Dateinamen auf Englisch
- [ ] Keine Phantom-Referenzen: `## Abhängigkeiten` referenziert nur S01-Benchmark + S04 + S05 + bereits erstellte S06-Analysis-Skills (T01-Output)
- [ ] `elvis-reporting-system.md` darf `elvis-performance-tracker` referenzieren (existiert aus T01)

## Verification

```bash
# Alle 10 Analysis Skills vorhanden
ls skills/analysis/*.md | wc -l
# → 10 (plus .gitkeep)

# Differenzierungs-Check Growth-Tracker
grep -c "fortlaufend\|Tracking\|wöchentlich" skills/analysis/elvis-growth-tracker.md
# → ≥2

# Differenzierungs-Check Competitor-Monitor
grep -c "Monitoring-System\|fortlaufend" skills/analysis/elvis-competitor-monitor.md
# → ≥1

# CLV-Formel im Revenue-Tracker
grep -c "CLV" skills/analysis/elvis-revenue-tracker.md
# → ≥1

# Failure-Indikatoren alle vorhanden
grep -l "Failure-Indikator" skills/analysis/*.md | wc -l
# → 10

# Sektions-Vollständigkeit Spot-Check
grep "^## " skills/analysis/elvis-reporting-system.md | wc -l
# → 9

# verify-s06.sh: 10 Analysis grün, 9 Automation noch fehlend
bash scripts/verify-s06.sh 2>&1 | grep -c "✓"
# → ≥90 (10 Datei-Checks + 90 Sektions-Checks + 10 Prefix-Checks)
```

## Observability Impact

- Signals added/changed: Erhöht verify-s06.sh ✓-Zähler von ~5 auf ~100+ (10 Dateien × 9 Sektionen + Prefix-Checks)
- How a future agent inspects this: `bash scripts/verify-s06.sh` zeigt exakten Fortschritt; `grep "✗" <(bash scripts/verify-s06.sh 2>&1)` listet nur fehlende Elemente
- Failure state exposed: Exakte Datei/Sektions-Paare im Fehlerfall sichtbar

## Inputs

- `skills/analysis/elvis-performance-tracker.md` (T01) — Abhängigkeits-Kandidat für `elvis-reporting-system`
- `skills/analysis/elvis-funnel-analyzer.md` (T01) — inhaltliche Abgrenzung für `elvis-conversion-analyzer`
- S04-Skills `elvis-competitor-analysis.md`, `elvis-monetization-planner.md` — Differenzierungs-Benchmark
- S05-Skills `elvis-competitor-deep-dive.md`, `elvis-monetization-strategy.md` — Differenzierungs-Benchmark
- S01-Skill `elvis-growth-audit.md` — Differenzierungs-Benchmark für `elvis-growth-tracker`

## Expected Output

- `skills/analysis/elvis-reporting-system.md` — Wöchentliches + monatliches Reporting-System mit 5 Pflicht-Metriken und Verteilungs-Prozess
- `skills/analysis/elvis-growth-tracker.md` — 90-Tage-Wachstums-Tracking mit wöchentlicher Fortschritts-Kurve, explizite Abgrenzung zu Growth-Audit
- `skills/analysis/elvis-conversion-analyzer.md` — Tiefenanalyse von 3 Konversionspunkten (CTA/Opt-In/Kauf)
- `skills/analysis/elvis-competitor-monitor.md` — Fortlaufendes 5-Accounts × 4-Metriken Monitoring mit Alarm-System
- `skills/analysis/elvis-revenue-tracker.md` — MRR + CLV-Tracking über 3 Einkommensquellen mit CLV-Formel
