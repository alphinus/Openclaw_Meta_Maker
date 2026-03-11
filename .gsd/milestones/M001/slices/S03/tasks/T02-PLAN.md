---
estimated_steps: 5
estimated_files: 3
---

# T02: Worf aus Template extrahieren + Execution Agents (Kirk, McCoy)

**Slice:** S03 — Agent Layer — 16 Star Trek Agenten
**Milestone:** M001

## Description

Drei Agenten werden geschrieben: Worf (aus Template extrahiert als Qualitäts-Baseline), Kirk (Haupt-Execution-Agent, Entscheidungsfokus) und McCoy (zweiter Execution-Agent, Ausführungsfokus). Alle drei teilen den execution-Soul — Kirk und McCoy müssen trotzdem klar differenziert werden: Kirk trifft Entscheidungen unter Unsicherheit, McCoy führt direkt aus ohne Zögern.

Kritische Regel D012: Kein Persönlichkeitsinhalt. "Kirk entscheidet mutig" ist Identity. Richtig: "Entscheidet bei unvollständiger Datenlage innerhalb von 2 Minuten und dokumentiert die Entscheidung mit Begründung."

## Steps

1. Extrahiere Worf aus `templates/agent-template.md`: `tail -n +$(grep -n "^# Agent$" templates/agent-template.md | tail -1 | cut -d: -f1) templates/agent-template.md | perl -0777 -pe 's/<!--.*?-->//gs' | cat -s > agent/worf.md`
2. Schreibe `agent/kirk.md` via Bash-Heredoc: execution-Soul, Mission "Koordiniert und überwacht die Ausführung aller operativen Tasks im OpenClaw-System", 6 Capabilities (Entscheidung bei unvollständiger Datenlage in ≤ 2 Min, Ressourcen zuweisen, Schnell-Briefings erstellen, Eskalationen routen, Execution-Fortschritt überwachen, Kurskorrektur einleiten), 5-Schritt Operating Loop (Auftragsklärung → Ressourcencheck → Entscheidung → Delegation → Abschluss-Review), Primärer Soul: soul/execution.md, Skills: /elvis-execution-plan /elvis-decision-framework /elvis-rapid-response
3. Schreibe `agent/mccoy.md` via Bash-Heredoc: execution-Soul, Mission "Führt operative Tasks direkt und ohne Verzögerung aus — der schnellste Weg von Auftrag zu Ergebnis", 5 Capabilities (Tasks sofort aufnehmen und ausführen ohne Rückfragen wenn Auftrag klar, Blockeridentifikation und Umgehung, Lieferung in ≤ definierten Zeitfenster, Abweichungen sofort melden, Ergebnisse dokumentieren), 4-Schritt Loop (Aufnahme → Ausführung → Blockerhandling → Lieferung), Primärer Soul: soul/execution.md, Skills: /elvis-execution-plan /elvis-rapid-execution /elvis-direct-action
4. Prüfe alle 3 Dateien auf D012-Compliance: `grep -i "mutig\|intuitiv\|leidenschaft\|charakter\|persönlich" agent/kirk.md agent/mccoy.md agent/worf.md` — kein Treffer erwartet
5. Führe `bash scripts/verify-s03.sh` aus und notiere neuen Fehlerstand

## Must-Haves

- [ ] `agent/worf.md` ist vollständiger Agent mit 7 Sektionen (aus Template extrahiert)
- [ ] `agent/kirk.md` enthält 6 Capabilities mit konkreten, messbaren Formulierungen
- [ ] `agent/mccoy.md` differenziert sich von Kirk: McCoy führt aus, Kirk entscheidet
- [ ] Kein Persönlichkeitsinhalt in allen 3 Dateien (D012)
- [ ] Alle Skills mit `/elvis-*` Prefix (D001)
- [ ] Alle Dateien auf Deutsch (D002)

## Verification

- `bash scripts/verify-s03.sh` — Fehleranzahl ≤ 121 (27 Checks durch 3 Dateien gedeckt)
- `grep "## Mission\|## Capabilities\|## Operating Loop\|## Constraints\|## Primärer Soul\|## Primäre Skills\|## Name" agent/worf.md | wc -l` — ergibt 7
- `grep "/elvis-" agent/kirk.md | wc -l` — ergibt ≥ 3

## Observability Impact

- Signals added/changed: verify-s03.sh-Fehlerstand sinkt von 148 auf ≤ 121
- How a future agent inspects this: `bash scripts/verify-s03.sh` zeigt welche der 3 Dateien alle Checks bestehen
- Failure state exposed: Fehlende Sektion in worf/kirk/mccoy direkt sichtbar

## Inputs

- `templates/agent-template.md` — Worf-Beispiel ab --- Trennlinie
- `soul/execution.md` — Referenz für Soul-Zuweisung
- `scripts/verify-s03.sh` — Stopping-Condition (aus T01)

## Expected Output

- `agent/worf.md` — vollständiger Strategy Agent, 7 Sektionen
- `agent/kirk.md` — vollständiger Execution Agent (Entscheidung), 7 Sektionen
- `agent/mccoy.md` — vollständiger Execution Agent (Ausführung), 7 Sektionen
