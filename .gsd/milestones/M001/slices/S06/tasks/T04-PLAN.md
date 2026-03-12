---
estimated_steps: 4
estimated_files: 4
---

# T04: Letzte 4 neue Automation Skills

**Slice:** S06 — Automation + Analysis Skills (~20 Skills)
**Milestone:** M001

## Description

Vervollständigt die 9 neuen Automation Skills mit den letzten 4 Dateien: Integration-Mapper (Übersichts-Skill der vorhandene Tool-Verbindungen kartiert), System-Optimizer (bestehende Systeme verbessern), Batch-Processor (Mengen-basierte Verarbeitung) und Autopilot-Setup (End-to-End "Set & Forget"-System).

`elvis-autopilot-setup` ist der integrierende Abschluss-Skill des Automation-Bereichs: Er kann andere Automation-Skills aus S06 als Vorgänger referenzieren (alle sind nach T03 bereits vorhanden). Vor dem Schreiben der `## Abhängigkeiten`-Sektion für jeden Skill: manuell prüfen ob referenzierte Dateien tatsächlich existieren.

Nach diesem Task: alle 9 neuen + 1 S01-Benchmark = **10 Automation Skills total**. `verify-s06.sh` sollte 18 von 19 Dateien grün melden (ein Automation-File noch ausstehend falls Task-Reihenfolge abweicht — alle 4 in einem Task).

## Steps

1. `skills/automation/elvis-integration-mapper.md` schreiben:
   - **Kern:** Kartiert die Tool-Integrations-Landschaft: alle verwendeten Tools, verfügbare Verbindungen, Integrations-Lücken, Handlungs-Empfehlungen
   - Differenzierung: Übersichts-Skill vor spezifischen Automations; zeigt welche Verbindungen bereits existieren und wo Lücken sind (Vorläufer-Skill für `elvis-workflow-builder` und `elvis-data-pipeline`)
   - Ausführungsschritte: Tool-Inventar (≥10 Tools in Tabelle), Verbindungs-Matrix, Lücken-Analyse, Prioritäts-Empfehlungen
   - Failure-Indikator: Wenn <5 verwendete Tools identifizierbar → Meldung

2. `skills/automation/elvis-system-optimizer.md` schreiben:
   - **Kern:** Optimiert ein bestehendes System nach 4 Effizienz-Dimensionen (Geschwindigkeit/Zuverlässigkeit/Wartbarkeit/Kosten) mit Maßnahmen-Priorisierung
   - Differenzierung: Bestehende Systeme verbessern statt neue bauen; Complement zu `elvis-automation-audit` (Audit = Entdecken, Optimizer = Verbessern)
   - Scoring-Formel: Effizienz-Score = (Geschwindigkeit + Zuverlässigkeit + Wartbarkeit + Kosten-Effizienz) / 4, je 1–10 (D028)
   - Failure-Indikator: Wenn Gesamt-Effizienz-Score >7 → Meldung (System bereits gut optimiert, minimaler Handlungsbedarf)

3. `skills/automation/elvis-batch-processor.md` schreiben:
   - **Kern:** Entwirft Batch-Verarbeitungs-Workflows für wiederkehrende Datenmengen: Batch-Größe, Zeitfenster, Fehlerquoten-Schwelle
   - Differenzierung: Mengen-basierte Verarbeitung statt Event-basierter Trigger; für Content-Erstellung, Daten-Analysen, Report-Generierung
   - Mengenangaben: Batch-Größe in Einheiten, Zeitfenster in Stunden, Fehlerquoten-Schwelle in % (konkrete Zahlen D006)
   - Failure-Indikator: Wenn Fehlerquote >5% im Testlauf → Batch-Prozessor nicht produktionsbereit → Meldung

4. `skills/automation/elvis-autopilot-setup.md` schreiben:
   - **Kern:** Richtet vollständige "Set & Forget"-Automatisierungs-Systeme ein: Monitoring, Alarm-Regeln, manuelle Override-Optionen
   - Differenzierung: End-to-End-Setup statt Einzel-Workflows; integriert mehrere Automation-Skills zu einem autonomen System
   - Abhängigkeiten: darf andere S06-Automation-Skills referenzieren (alle existieren nach T03 + dieser Task)
   - Failure-Indikator: Wenn System >2 manuelle Eingriffe/Woche benötigt → kein echter Autopilot → Meldung

## Must-Haves

- [ ] Alle 4 Automation Skills haben alle 9 Pflicht-Sektionen
- [ ] Alle 4 Skills enthalten `/elvis-*` im `## Name`-Block (D001)
- [ ] Alle 4 Skills enthalten `Failure-Indikator:` mit konkreter Schwelle und Meldungstext
- [ ] `elvis-system-optimizer.md` enthält explizite Effizienz-Score-Formel als Gleichung (D028)
- [ ] `elvis-integration-mapper.md` spezifiziert Mindest-Tabellenformat mit ≥10 Tools in Ausführungsschritten
- [ ] `elvis-batch-processor.md` enthält konkrete Mengenangaben für Batch-Größe, Zeitfenster und Fehlerquoten-Schwelle in % (D006)
- [ ] `elvis-autopilot-setup.md` Abhängigkeiten referenzieren nur tatsächlich existierende Dateien (manueller Check vor Schreiben)
- [ ] Kein Skill enthält Python-Code, JSON-Strukturen oder API-Aufrufe (R030)
- [ ] Alle Inhalte auf Deutsch (D002); Dateinamen auf Englisch

## Verification

```bash
# Alle 4 neuen Automation Skills vorhanden
ls skills/automation/elvis-integration-mapper.md \
   skills/automation/elvis-system-optimizer.md \
   skills/automation/elvis-batch-processor.md \
   skills/automation/elvis-autopilot-setup.md

# Effizienz-Score-Formel im System-Optimizer
grep -c "Effizienz-Score\|Geschwindigkeit.*Zuverlässigkeit\|/ 4" \
  skills/automation/elvis-system-optimizer.md
# → ≥1

# Fehlerquoten-Schwelle im Batch-Processor
grep -c "Fehlerquote\|%" skills/automation/elvis-batch-processor.md
# → ≥1

# Failure-Indikatoren alle vorhanden
grep -l "Failure-Indikator" \
  skills/automation/elvis-integration-mapper.md \
  skills/automation/elvis-system-optimizer.md \
  skills/automation/elvis-batch-processor.md \
  skills/automation/elvis-autopilot-setup.md | wc -l
# → 4

# Gesamter Automation-Bestand: 10 Skills (9 neu + 1 S01-Benchmark)
ls skills/automation/*.md | wc -l
# → 10

# verify-s06.sh: jetzt alle 19 Dateien vorhanden
bash scripts/verify-s06.sh; echo "Exit-Code: $?"
# Erwartetes Ergebnis: Exit-Code 0 (oder sehr wenige Fehler für Hotfixes in T05)
```

## Observability Impact

- Signals added/changed: Nach T04 sollte `bash scripts/verify-s06.sh` nahe Exit-Code 0 sein — alle 19 Dateien vorhanden
- How a future agent inspects this: `bash scripts/verify-s06.sh 2>&1 | grep "✗"` zeigt verbleibende Probleme; `bash scripts/verify-s06.sh; echo $?` zeigt Fehleranzahl
- Failure state exposed: Phantom-Referenzen werden pro Datei/Abhängigkeit ausgegeben falls `## Abhängigkeiten` auf nicht-existierende Skills zeigt

## Inputs

- `skills/automation/elvis-automation-audit.md` (T03) — Differenzierungs-Basis für `elvis-system-optimizer` (Audit = Entdecken, Optimizer = Verbessern)
- `skills/automation/elvis-trigger-builder.md` (T03) — kann in `## Abhängigkeiten` von `elvis-autopilot-setup` referenziert werden
- `skills/automation/elvis-workflow-builder.md` (S01) — kann in `## Abhängigkeiten` von `elvis-integration-mapper` referenziert werden
- `scripts/verify-s06.sh` (T01) — Verifikations-Tool das nach dem Schreiben ausgeführt wird

## Expected Output

- `skills/automation/elvis-integration-mapper.md` — Tool-Integrations-Landkarte: ≥10-Tools-Tabelle, Verbindungs-Matrix, Lücken-Analyse
- `skills/automation/elvis-system-optimizer.md` — 4-Dimensionen-Effizienz-Audit mit Score-Formel und Maßnahmen-Priorisierung
- `skills/automation/elvis-batch-processor.md` — Batch-Workflow-Spezifikation mit Batch-Größe, Zeitfenster und Fehlerquoten-Schwelle
- `skills/automation/elvis-autopilot-setup.md` — End-to-End "Set & Forget"-System-Setup mit Monitoring, Alarm-Regeln und Override-Optionen
