---
estimated_steps: 5
estimated_files: 5
---

# T03: Erste 5 neue Automation Skills

**Slice:** S06 — Automation + Analysis Skills (~20 Skills)
**Milestone:** M001

## Description

Erstellt die ersten 5 neuen Automation Skills in `skills/automation/`. Diese Skills decken die konzeptionellen Kern-Bausteine der Automatisierung ab: systematischer Audit (was hat Automatisierungspotenzial?), Implementierung einer Einzelaufgabe, Content-Scheduling-Setup, Event-basierte Trigger-Logik und Daten-Pipeline-Design.

**Qualitäts-Benchmark:** Kein Skill darf abstrakter sein als `skills/automation/elvis-workflow-builder.md` (S01). Der Benchmark verwendet 5-Schritte-Workflows, ROI-Berechnungen in Break-Even-Wochen, konkrete Mengenangaben pro Schritt.

**Abgrenzung zu Growth-Skills:** Automation Skills fokussieren auf **Systemdenken** (wie baue ich einen Prozess?) statt auf **Taktik** (wie wachse ich auf X?). Jeder Skill muss in `## Beschreibung` explizit den Systemdesign-Charakter betonen. Kein Code (kein Python, kein JSON, keine API-Aufrufe) — nur Prompt-Anweisungen für Workflow-Design und Tool-Empfehlungen.

## Steps

1. `skills/automation/elvis-automation-audit.md` schreiben:
   - **Kern:** Scannt alle Prozesse systematisch auf Automatisierungspotenzial: 5-Kriterien-Score (Häufigkeit/Volumen/Fehleranfälligkeit/Regelbasiert/Zeitaufwand, je 1–5 Punkte, Max 25)
   - Differenzierung: Breiter als `elvis-workflow-builder` (fokussiert nur auf Workflow-Design); Audit liefert Automatisierungs-Prioritäten-Liste als Entscheidungsgrundlage
   - Failure-Indikator: Wenn <5 Prozesse mit Score >10 identifiziert → Meldung

2. `skills/automation/elvis-task-automator.md` schreiben:
   - **Kern:** Wandelt eine einzelne repetitive Aufgabe in vollständige Automations-Sequenz mit Fehlerbehandlung und Monitoring um
   - Differenzierung: Tiefer als `elvis-workflow-builder` (Top-3 Workflows); fokussiert auf **eine** Aufgabe mit vollständiger Implementierungs-Spezifikation
   - Ausführungsschritte: Aufgabe analysieren → Trigger definieren → Aktions-Sequenz → Fehlerbehandlung → Monitoring-Setup (5 Schritte)
   - Failure-Indikator: Wenn Aufgabe menschliche Entscheidung ohne klar definierte Regeln erfordert → Meldung

3. `skills/automation/elvis-content-scheduler.md` schreiben:
   - **Kern:** Richtet automatisierten Content-Veröffentlichungsplan ein: Zeitslots, Plattform-Konfiguration, Fallback-Regeln für 4 Wochen
   - Differenzierung: Kombiniert `elvis-content-calendar` (Ideen) mit Automatisierungs-Logik; Output ist Tool-Konfigurations-Spezifikation (nicht Code)
   - Mengenangaben: Mindestens 3 Zeitslots pro Tag/Woche, 2 Plattformen, 1 Fallback-Regel
   - Failure-Indikator: Wenn Content-Vorrat für <2 Wochen vorhanden → Meldung

4. `skills/automation/elvis-trigger-builder.md` schreiben:
   - **Kern:** Definiert Event-basierte If/Then-Trigger-Ketten: 5 Trigger-Typen (Zeit / Event / Daten-Schwelle / Nutzer-Aktion / System-Status), Bedingungs-Logik, Fehlerfall-Routing
   - Differenzierung: Baustein für komplexe Automatisierungen; `elvis-workflow-builder` beschreibt Workflows, dieser Skill definiert die auslösenden Bedingungen
   - Failure-Indikator: Wenn Trigger-Bedingung nicht eindeutig formulierbar → Meldung

5. `skills/automation/elvis-data-pipeline.md` schreiben:
   - **Kern:** Entwirft Daten-Fluss-Pipelines zwischen Tools: 3 Datenquellen → Transformation → 2 Ausgaben, Validierungs-Checkpoints
   - Differenzierung: Daten-Ebene der Automation; `elvis-workflow-builder` fokussiert auf Aufgaben-Flows, dieser Skill auf Daten-Flüsse
   - Failure-Indikator: Wenn >1 Datenquelle keine API/Export-Funktion hat → Meldung

## Must-Haves

- [ ] Alle 5 Automation Skills haben alle 9 Pflicht-Sektionen
- [ ] Alle 5 Skills enthalten `/elvis-*` im `## Name`-Block (D001)
- [ ] Alle 5 Skills enthalten `Failure-Indikator:` mit konkreter Schwelle und Meldungstext
- [ ] Kein Skill enthält Python-Code, JSON-Strukturen oder API-Aufrufe (Prompt-Anweisungen und Tool-Empfehlungen statt Code — R030)
- [ ] `elvis-automation-audit.md` enthält 5-Kriterien-Score als Bewertungsmatrix mit Punkteskala
- [ ] `elvis-content-scheduler.md` enthält Mengenangaben für Zeitslots, Plattformen und Fallback-Regeln
- [ ] `elvis-trigger-builder.md` listet alle 5 Trigger-Typen explizit auf
- [ ] Alle Inhalte auf Deutsch (D002); Dateinamen auf Englisch
- [ ] Keine Phantom-Referenzen: `## Abhängigkeiten` referenziert nur S01-Benchmark + S04 + S05 Skills (keine S06-Automation-Skills die noch nicht existieren)

## Verification

```bash
# Alle 5 neuen Automation Skills vorhanden
ls skills/automation/elvis-automation-audit.md \
   skills/automation/elvis-task-automator.md \
   skills/automation/elvis-content-scheduler.md \
   skills/automation/elvis-trigger-builder.md \
   skills/automation/elvis-data-pipeline.md

# Sektions-Vollständigkeit Spot-Check
grep "^## " skills/automation/elvis-automation-audit.md | wc -l
# → 9

# Failure-Indikatoren
grep -l "Failure-Indikator" skills/automation/elvis-automation-audit.md \
  skills/automation/elvis-task-automator.md \
  skills/automation/elvis-content-scheduler.md \
  skills/automation/elvis-trigger-builder.md \
  skills/automation/elvis-data-pipeline.md | wc -l
# → 5

# 5-Kriterien-Score im Automation-Audit
grep -c "Häufigkeit\|Volumen\|Fehleranfälligkeit\|Regelbasiert\|Zeitaufwand" \
  skills/automation/elvis-automation-audit.md
# → ≥5

# 5 Trigger-Typen im Trigger-Builder
grep -c "Zeit\|Event\|Daten-Schwelle\|Nutzer-Aktion\|System-Status" \
  skills/automation/elvis-trigger-builder.md
# → ≥5

# Kein Code in Skills (Python/JSON)
grep -l "```python\|```json\|import " skills/automation/elvis-*.md 2>/dev/null | wc -l
# → 0

# Prefix-Check
grep -A2 "^## Name" skills/automation/elvis-data-pipeline.md | grep "/elvis-"
# → /elvis-data-pipeline
```

## Observability Impact

- Signals added/changed: verify-s06.sh ✓-Zähler steigt nach diesem Task auf ~145+ (5 neue Automation-Dateien × 9 Sektionen + Prefix-Checks)
- How a future agent inspects this: `bash scripts/verify-s06.sh` zeigt exakten Fortschritt per Datei
- Failure state exposed: Fehlende Sektionen oder Phantom-Referenzen sind pro Datei sichtbar

## Inputs

- `skills/automation/elvis-workflow-builder.md` (S01) — Qualitäts-Benchmark: 5-Schritte-Format, ROI-Berechnung, Tool-Empfehlungen; kein S06-Skill darf abstrakter sein
- S04-Skills `skills/content/elvis-content-calendar.md` — Differenzierungs-Basis für `elvis-content-scheduler`
- S06-Analysis-Skills (T01/T02) — können in `## Abhängigkeiten` als Vorgänger genannt werden wenn semantisch sinnvoll
- `templates/skill-template.md` — verbindliches 9-Sektionen-Format

## Expected Output

- `skills/automation/elvis-automation-audit.md` — 5-Kriterien-Score-Matrix, Prioritäten-Liste als Entscheidungsgrundlage
- `skills/automation/elvis-task-automator.md` — Einzelaufgaben-Automations-Spezifikation mit Fehlerbehandlung und Monitoring
- `skills/automation/elvis-content-scheduler.md` — 4-Wochen-Zeitplan-Spezifikation mit Zeitslots, Plattform-Config und Fallback-Regeln
- `skills/automation/elvis-trigger-builder.md` — If/Then-Trigger-Ketten mit 5 Trigger-Typen und Fehlerfall-Routing
- `skills/automation/elvis-data-pipeline.md` — Daten-Fluss-Pipeline-Spezifikation: 3 Quellen → Transformation → 2 Ausgaben
