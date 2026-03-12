---
estimated_steps: 7
estimated_files: 7
---

# T01: skills/analysis/ anlegen + verify-s06.sh schreiben + 5 Analysis Skills

**Slice:** S06 — Automation + Analysis Skills (~20 Skills)
**Milestone:** M001

## Description

Legt das neue `skills/analysis/`-Verzeichnis an (in S01 bewusst ausgelassen, gemäß ROADMAP S06-Output), schreibt `scripts/verify-s06.sh` als objektive Stopping-Condition für die gesamte Slice, und erstellt die ersten 5 Analysis Skills. Das verify-Skript wird sofort ausführbar sein, aber mit Fehlern enden (14 von 19 Dateien fehlen noch) — das ist korrekt und erwartet.

Analysis Skills unterscheiden sich von bestehenden Growth-Skills durch **Ongoing-Charakter**: Sie definieren Mess-Systeme und Tracking-Cadences statt einmalige Analysen. Jeder der 5 Skills muss in `## Beschreibung` explizit "fortlaufend", "wöchentlich", "Mess-System" oder ähnliche Formulierungen enthalten.

## Steps

1. Verzeichnis anlegen: `mkdir skills/analysis` und `echo "" > skills/analysis/.gitkeep` (analog zu bestehenden `.gitkeep`-Dateien in soul/, identity/ etc.)

2. `scripts/verify-s06.sh` schreiben — 4 Check-Gruppen nach Muster von `scripts/verify-s05.sh`:
   - [1/4] Datei-Existenz: Array mit allen 19 Skills (9 Automation + 10 Analysis)
   - [2/4] Sektions-Vollständigkeit: 19 × 9 = 171 Checks; alle 9 Pflicht-Sektionen
   - [3/4] /elvis-Prefix: 19 Checks via `grep -A5 "^## Name" | grep "/elvis-"`
   - [4/4] Phantomreferenz-Check: iteriert über `growth content research strategy automation meta analysis` als subdir-Liste
   - `set -euo pipefail`, `ERRORS=0`, `pass()/fail()` Helper, Exit-Code = `$ERRORS` (D014)

3. `skills/analysis/elvis-performance-tracker.md` schreiben:
   - **Kern:** Baut systematisches Performance-Tracking-System mit 10 Kern-Metriken, wöchentlicher Mess-Cadence und Trend-Visualisierungsformat
   - Differenzierung in `## Beschreibung`: "fortlaufendes Tracking-System" vs. `elvis-growth-audit` (einmaliger Snapshot)
   - Failure-Indikator: Wenn <5 Metriken messbar → Meldung

4. `skills/analysis/elvis-kpi-dashboard.md` schreiben:
   - **Kern:** Definiert KPI-Dashboard-Struktur mit 5 Ziel-KPIs, 10 unterstützenden Metriken, Zielwerten und Alarm-Schwellen
   - Differenzierung: Dashboard visualisiert und priorisiert, `elvis-performance-tracker` misst
   - Failure-Indikator: Wenn Zielwerte für >2 KPIs unbekannt → Meldung

5. `skills/analysis/elvis-funnel-analyzer.md` schreiben:
   - **Kern:** Analysiert Konversions-Funnel Schritt für Schritt: 5 Funnel-Stufen × Conversion-Rate, Drop-Off-Punkte, Optimierungs-Prioritäten
   - Failure-Indikator: Wenn <3 Funnel-Stufen messbar → Meldung

6. `skills/analysis/elvis-content-analyzer.md` schreiben:
   - **Kern:** Analysiert Content-Performance kanalübergreifend: Top-10 Posts × 5 Metriken, Content-Typ-Vergleich, Format-Empfehlungen
   - Differenzierung: Multi-Channel vs. `elvis-x-analytics` (nur X/Twitter)
   - Failure-Indikator: Wenn <10 Posts mit vollständigen Metriken → Meldung

7. `skills/analysis/elvis-ab-tester.md` schreiben:
   - **Kern:** Entwirft A/B-Tests und wertet Ergebnisse statistisch aus: 2 Varianten × 1 Variable, Stichprobengröße, Signifikanz-Schwelle 95%
   - Failure-Indikator: Wenn Stichprobe <100 pro Variante → Meldung

## Must-Haves

- [ ] `skills/analysis/.gitkeep` existiert (Verzeichnis angelegt)
- [ ] `scripts/verify-s06.sh` ist syntaktisch korrekt und ausführbar (`bash scripts/verify-s06.sh` läuft ohne Bash-Fehler)
- [ ] verify-s06.sh enthält alle 19 Skill-Dateien in den Arrays (9 Automation + 10 Analysis)
- [ ] verify-s06.sh prüft alle 9 Pflicht-Sektionen: `## Name`, `## Beschreibung`, `## Ziele`, `## Strategie`, `## Einschränkungen`, `## Ausführungsschritte`, `## Verifikation`, `## Abhängigkeiten`, `## Output`
- [ ] verify-s06.sh iteriert Phantomreferenz-Check über alle 7 Subdirs: `growth content research strategy automation meta analysis`
- [ ] Alle 5 Analysis Skills haben alle 9 Pflicht-Sektionen
- [ ] Alle 5 Analysis Skills enthalten `/elvis-*` im `## Name`-Block
- [ ] Alle 5 Analysis Skills enthalten `Failure-Indikator:` mit konkreter Schwelle in `## Verifikation`
- [ ] Alle 5 Analysis Skills enthalten mindestens eine Formulierung wie "fortlaufend", "wöchentlich", "Mess-System" in `## Beschreibung`
- [ ] Alle Inhalte auf Deutsch (D002); Dateinamen auf Englisch
- [ ] Keine Phantom-Referenzen: `## Abhängigkeiten` referenziert nur S01-Benchmark + S04 + S05 Skills

## Verification

```bash
# Verzeichnis-Check
ls skills/analysis/.gitkeep

# Skript-Syntax prüfen (kein Exit auf Fehler da Dateien noch fehlen)
bash -n scripts/verify-s06.sh && echo "Syntax OK"

# Skript ausführen (Fehler erwartet — nur 5/19 Dateien existieren)
bash scripts/verify-s06.sh; echo "Exit-Code: $?"
# Erwartetes Ergebnis: ✗ für fehlende Dateien, ✓ für die 5 erstellten

# Sektion-Spot-Check
grep "^## " skills/analysis/elvis-performance-tracker.md | wc -l
# → 9

# Failure-Indikator
grep -c "Failure-Indikator" skills/analysis/elvis-performance-tracker.md
# → 1

# Differenzierungs-Check
grep -c "fortlaufend\|wöchentlich\|Mess-System" skills/analysis/elvis-performance-tracker.md
# → ≥1

# Prefix-Check
grep -A2 "^## Name" skills/analysis/elvis-ab-tester.md | grep "/elvis-"
# → /elvis-ab-tester
```

## Observability Impact

- Signals added/changed: `scripts/verify-s06.sh` als neue Inspection Surface für S06 — gibt strukturierten ✓/✗-Report pro Datei/Sektion aus; Exit-Code = Fehleranzahl
- How a future agent inspects this: `bash scripts/verify-s06.sh` — vollständiger Check-Report; `grep "✗" <(bash scripts/verify-s06.sh 2>&1)` für nur fehlende Elemente
- Failure state exposed: Fehlende Dateien als `✗ [Pfad] — Datei fehlt`; fehlende Sektionen als `✗ [Dateiname]: [Sektion] — Sektion fehlt`; Phantom-Referenzen als `✗ [Dateiname]: Abhängigkeit '[dep]' — Phantomreferenz!`

## Inputs

- `scripts/verify-s05.sh` — Vorlage für verify-s06.sh (gleiche 4 Check-Gruppen, gleiche Skript-Struktur; anzupassen: Datei-Arrays, Phantom-Check Subdirs um `analysis` erweitern)
- `skills/automation/elvis-workflow-builder.md` — Qualitäts-Benchmark: kein Analysis-Skill darf abstrakter sein als der Automation-Benchmark
- `templates/skill-template.md` — verbindliches 9-Sektionen-Format mit Anweisungs-Block
- S05-SUMMARY.md Forward Intelligence: Abhängigkeits-Whitelist (S01-Benchmark + alle S04 + alle S05 Skills)

## Expected Output

- `skills/analysis/.gitkeep` — Verzeichnis-Marker für neues `analysis/`-Unterverzeichnis
- `scripts/verify-s06.sh` — ausführbares Verifikations-Skript mit 4 Check-Gruppen, 19 Dateien in Arrays, 7 Subdirs im Phantom-Check
- `skills/analysis/elvis-performance-tracker.md` — Ongoing Performance-Tracking-System, 10 Metriken, wöchentliche Cadence
- `skills/analysis/elvis-kpi-dashboard.md` — KPI-Dashboard-Design, 5 Ziel-KPIs + 10 unterstützende Metriken + Alarm-Schwellen
- `skills/analysis/elvis-funnel-analyzer.md` — 5-Stufen-Funnel-Analyse mit Conversion-Rates und Drop-Off-Punkten
- `skills/analysis/elvis-content-analyzer.md` — Multi-Channel Content-Performance, Top-10 Posts × 5 Metriken
- `skills/analysis/elvis-ab-tester.md` — A/B-Test-Framework mit 2 Varianten, 1 Variable, 95% Signifikanz-Schwelle
