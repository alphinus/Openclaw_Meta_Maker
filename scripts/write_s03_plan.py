
import os

plan = """# S03: Agent Layer — 16 Star Trek Agenten

**Goal:** 16 vollständige Agent-Dateien (`agent/*.md`) plus ein Verifikationsskript — jeder Agent hat 7 Pflichtfelder, 5 autonome Agenten haben D007-konforme Safeguards, alle Forward-References nutzen `/elvis-*` Prefix.
**Demo:** `bash scripts/verify-s03.sh` läuft mit Exit-Code 0 — alle 148 Checks grün (16 Datei-Existenz + 112 Sektions-Checks + 20 Safeguard-Checks).

## Must-Haves

- 16 `agent/*.md` Dateien existieren (kirk.md bis uhura.md)
- Jede Datei enthält alle 7 Pflichtfelder: Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills
- Picard, Q, Borg, Troi, Uhura enthalten im Constraints-Block `**Max-Limit:**`, `**Approval-Gate:**`, `**Stop-Bedingung:**`, `**Rollback-Hinweis:**` (fett, D007/D013)
- Alle Skills nutzen `/elvis-*` Prefix (D001)
- Alle Dateien auf Deutsch, Dateinamen englisch Kleinbuchstaben (D002)
- Kein Persönlichkeitsinhalt in Agent-Dateien — ausschließlich Mission, Capabilities, Loop, Constraints (D012)
- `scripts/verify-s03.sh` mit 148 Checks, Exit-Code = Fehleranzahl (D014/D015)

## Proof Level

- This slice proves: contract
- Real runtime required: no
- Human/UAT required: no

## Verification

- `bash scripts/verify-s03.sh` — Exit-Code 0, alle 148 Checks grün
- `ls agent/*.md | wc -l` — ergibt 16
- `grep -rl "**Max-Limit:**" agent/ | wc -l` — ergibt 5

## Observability / Diagnostics

- Runtime signals: none (reiner Schreibslice — kein ausführbarer Code)
- Inspection surfaces: `bash scripts/verify-s03.sh` — 148-Check Report mit Haken/Kreuz pro Datei und Sektion, Exit-Code = Fehleranzahl
- Failure visibility: Jeder fehlgeschlagene Check zeigt Dateiname + fehlende Sektion — direkt lokalisierbar ohne weitere Inspektion
- Redaction constraints: none

## Integration Closure

- Upstream surfaces consumed: `templates/agent-template.md` (7 Pflichtfelder, Worf-Beispiel), `soul/*.md` (Soul-zu-Agent-Mapping via `## Geeignet für`), `identity/*.md` (werden referenziert, Inhalte aber nicht wiederholt)
- New wiring introduced in this slice: `agent/*.md` — die operative Schicht zwischen Identity und Skills; jeder Agent verweist auf einen primären Soul und konkrete Skill-Handles
- What remains before the milestone is truly usable end-to-end: Skills (S04–S06), Meta-Skills (S07), Commands (S08), README + Integrations-Verifikation (S09)

## Tasks

- [ ] **T01: Stopping-Condition — scripts/verify-s03.sh schreiben** `est:30m`
  - Why: D015-Prinzip — das Verifikationsskript definiert den Vertrag bevor ein einziger Agent geschrieben wird; 148 initiale Fehler sind der Ausgangszustand und beweisen, dass die Checks korrekt greifen
  - Files: `scripts/verify-s03.sh`
  - Do: Schreibe verify-s03.sh nach dem Muster von verify-s02.sh — ERRORS-Zähler, pass/fail-Funktionen, 3 Gruppen: [1/3] Datei-Existenz (16 Checks), [2/3] Agent-Sektionen 7×16=112 Checks, [3/3] Autonome-Agenten-Safeguards 4×5=20 Checks; alle 16 Agent-Dateinamen in einem Array; Exit-Code = ERRORS; ausschließlich via Bash-Heredoc (kein Write-Tool)
  - Verify: `bash scripts/verify-s03.sh` — Skript läuft ohne Bash-Fehler durch, zeigt 148 Fehler, Exit-Code = 148
  - Done when: Exit-Code = 148 (alle fail initial); kein Bash-Syntaxfehler

- [ ] **T02: Worf aus Template extrahieren + Execution Agents (Kirk, McCoy)** `est:45m`
  - Why: Worf ist das fertige Referenzbeispiel aus dem Template — direkte Extraktion gibt sofortige grüne Baseline; Kirk (Haupt-Execution-Agent) und McCoy (zweiter Execution-Agent mit anderem Fokus) bilden den execution-Soul-Block
  - Files: `agent/worf.md`, `agent/kirk.md`, `agent/mccoy.md`
  - Do: Worf via tail+perl+sed-Pipeline aus templates/agent-template.md (ab --- Trennlinie); Kirk: execution-Soul, 6 Capabilities (Entscheidung unter Unsicherheit, Ressourcenallokation, Schnell-Briefing, Eskalations-Routing, Execution-Überwachung, Kurskorrektur), 5-Schritt Loop, Skills: /elvis-execution-plan /elvis-decision-framework /elvis-rapid-response; McCoy: execution-Soul, differenzierter Fokus auf direkte Ausführung und Lieferung (nicht Entscheidung), Skills: /elvis-execution-plan /elvis-rapid-execution /elvis-direct-action; kein Persönlichkeitsinhalt (D012); alle via Bash-Heredocs
  - Verify: `bash scripts/verify-s03.sh` — Fehleranzahl sinkt von 148 auf ≤ 121
  - Done when: 3 Dateien mit je 7 Sektionen bestehen alle Checks; Kirk und McCoy sind klar differenziert (Entscheidung vs. Ausführung)

- [ ] **T03: Research/Growth/Automation/Builder Agents (Spock, Riker, Scotty, LaForge)** `est:60m`
  - Why: 4 Agenten aus 4 unterschiedlichen Souls — researcher, growth, automation, builder; kritische Differenzierung: Scotty (Systeme am Laufen halten) vs. LaForge (neue Systeme bauen)
  - Files: `agent/spock.md`, `agent/riker.md`, `agent/scotty.md`, `agent/laforge.md`
  - Do: Spock (researcher-Soul): 6 Caps — Recherche-Protokoll aufsetzen, Quellen auswerten, Fakten prüfen, Hypothesen testen, Wissenskodifizieren, Briefing erstellen; Skills: /elvis-market-scan /elvis-ai-research /elvis-data-analysis /elvis-fact-check; Riker (growth-Soul): 6 Caps — Audience-Analyse, Content-Wachstum, Distribution-Optimierung, Engagement-Tracking, Growth-Loop-Design, Kanal-Skalierung; Skills: /elvis-growth-audit /elvis-audience-builder /elvis-x-growth /elvis-growth-loop; Scotty (automation-Soul): System-Betrieb, Automatisierungs-Aufbau, Monitor-Einrichtung; Skills: /elvis-workflow-builder /elvis-automation /elvis-system-monitor /elvis-integration; LaForge (builder-Soul): Infrastruktur- und System-Aufbau, Prozess-Design, Dokumentation; Skills: /elvis-workflow-builder /elvis-system-builder /elvis-process-design /elvis-infrastructure; alle via Bash-Heredocs; Scotty vs. LaForge durch Capability-Vokabular explizit differenzieren
  - Verify: `bash scripts/verify-s03.sh` — Fehleranzahl ≤ 93
  - Done when: alle 4 Dateien mit 7 Sektionen; Scotty-Capabilities enthalten kein Aufbau-Vokabular, LaForge-Capabilities kein reines Betriebs-Vokabular

- [ ] **T04: Creator/Analyst/Operator/Strategist Agents (Data, Seven, Sulu, Tuvok)** `est:60m`
  - Why: 4 weitere Agenten aus creator, analyst, operator, strategist-Souls; Tuvok teilt strategist-Soul mit Picard und Worf — muss sich durch Security/Systemintegrität klar abgrenzen; Capabilities dürfen kein Delegations- oder Orchestrierungsvokabular enthalten
  - Files: `agent/data.md`, `agent/seven.md`, `agent/sulu.md`, `agent/tuvok.md`
  - Do: Data (creator-Soul): 6 Caps — Hook-Writing, Content-Erstellung, Format-Varianten entwickeln, Content-Kalender planen, Themen-Ideation, Qualitäts-Review; Skills: /elvis-x-hook-writer /elvis-x-content /elvis-copywriting /elvis-content-calendar; Seven (analyst-Soul): 6 Caps — Performance-Tracking, System-Audit, Pattern-Erkennung, Reporting, Benchmark-Vergleich, Anomalie-Detektion; Skills: /elvis-growth-audit /elvis-market-scan /elvis-performance-tracker /elvis-data-audit /elvis-reporting; Sulu (operator-Soul): 5 Caps — Aufgaben-Routing, Ausführungs-Tracking, Priorisierungs-Queue, Status-Reporting, Engpass-Erkennung; Skills: /elvis-workflow-builder /elvis-task-router /elvis-execution-tracker; Tuvok (strategist-Soul/Sicherheit): 6 Caps — System-Integrität prüfen, Sicherheitsanalyse, Logik-Validierung, Risiko-Assessment, Taktische Planung, Schwachstellen-Identifikation; KEIN Delegations-Vokabular; Skills: /elvis-execution-plan /elvis-system-audit /elvis-security-check /elvis-logic-validator; alle via Bash-Heredocs
  - Verify: `bash scripts/verify-s03.sh` — Fehleranzahl ≤ 65; `grep -i "delegier\|orchestrier" agent/tuvok.md | wc -l` = 0
  - Done when: alle 4 Dateien mit 7 Sektionen; Tuvok hat kein Picard/Worf-Overlap in Capabilities

- [ ] **T05: Autonome Agents mit Safeguards (Picard, Q, Borg, Troi, Uhura) + Final Verification** `est:90m`
  - Why: Die 5 komplexesten Agenten — alle mit D007-konformen Safeguards; Picard orchestriert andere Agenten; Q und Borg sind die kreativsten Sonderfälle; Safeguards müssen konkret und hart sein (keine Kann-Formulierungen)
  - Files: `agent/picard.md`, `agent/q.md`, `agent/borg.md`, `agent/troi.md`, `agent/uhura.md`
  - Do: Constraints-Block aller 5 Agenten enthält fett formatierte Bullet-Points: **Max-Limit:** [konkrete Zahl] pro Durchlauf, **Approval-Gate:** [Bedingung], **Stop-Bedingung:** [automatischer Halt], **Rollback-Hinweis:** [Rückgängig-Mechanismus]; Picard (strategist/Orchestrator): delegiert an andere Agenten, 6 Caps inkl. Agent-Koordination, Max-Limit ≤ 3 aktive Delegationen gleichzeitig; Q (creator/Agent Creator): generiert Agents/Skills/Konzepte, Max-Limit ≤ 3 neue Objekte pro Durchlauf, Approval-Gate vor jeder Erstellung; Borg (automation/Skill Expander): assimiliert und erweitert Skills, Max-Limit ≤ 5 Skills pro Durchlauf, Stop-Bedingung wenn kein klarer Mehrwert erkennbar; Troi (analyst/System Analyzer): Schwachstellen-Erkennung und Signal-Analyse, Max-Limit ≤ 1 vollständige System-Analyse pro Durchlauf; Uhura (operator/Library Manager): strukturiert Skill-Library, Max-Limit ≤ 10 Bibliotheks-Änderungen pro Durchlauf; alle via Bash-Heredocs; abschließend bash scripts/verify-s03.sh
  - Verify: `bash scripts/verify-s03.sh` — Exit-Code 0, alle 148 Checks grün; `grep -rl "**Max-Limit:**" agent/ | wc -l` = 5
  - Done when: Exit-Code 0; alle 5 autonomen Agenten haben alle 4 Safeguard-Marker fett formatiert mit konkreten Werten

## Files Likely Touched

- `scripts/verify-s03.sh`
- `agent/kirk.md`
- `agent/spock.md`
- `agent/picard.md`
- `agent/data.md`
- `agent/worf.md`
- `agent/scotty.md`
- `agent/laforge.md`
- `agent/seven.md`
- `agent/sulu.md`
- `agent/tuvok.md`
- `agent/mccoy.md`
- `agent/riker.md`
- `agent/q.md`
- `agent/borg.md`
- `agent/troi.md`
- `agent/uhura.md`
"""

path = r'C:\Dev\Openclaw_Meta_Maker\.gsd\milestones\M001\slices\S03\S03-PLAN.md'
with open(path, 'w', encoding='utf-8') as f:
    f.write(plan.lstrip())
print(f'Written {len(plan.splitlines())} lines')
