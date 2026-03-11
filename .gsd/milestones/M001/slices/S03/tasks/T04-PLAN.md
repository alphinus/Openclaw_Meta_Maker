---
estimated_steps: 5
estimated_files: 4
---

# T04: Creator/Analyst/Operator/Strategist Agents (Data, Seven, Sulu, Tuvok)

**Slice:** S03 — Agent Layer — 16 Star Trek Agenten
**Milestone:** M001

## Description

Vier weitere Agenten: Data (creator-Soul, Content-Produktion), Seven (analyst-Soul, Daten-Analyse), Sulu (operator-Soul, Task-Routing), Tuvok (strategist-Soul, Sicherheit/Taktik). Tuvok ist der heikelste Fall: er teilt den strategist-Soul mit Picard (der in T05 kommt) und Worf (aus T02). Alle drei haben strategist-Soul — Tuvok MUSS sich durch Security- und Systemintegrität-Fokus von Picard (Delegation/Orchestrierung) und Worf (Kampfstrategie/Markt) klar abgrenzen. Kein Delegations- oder Orchestrierungsvokabular in Tuvoks Capabilities.

## Steps

1. Schreibe `agent/data.md` via Bash-Heredoc: creator-Soul, Mission "Produziert, strukturiert und optimiert alle Content-Formate für das OpenClaw-Ökosystem", 6 Capabilities (Hooks und Eröffnungssätze für jeden Content-Typ schreiben, Langform-Content in verschiedenen Formaten erstellen, Content-Varianten für unterschiedliche Kanäle entwickeln, Content-Kalender und Themen-Pipeline planen, Neue Themen und Content-Ideen aus Trend-Signalen generieren, Content auf Klarheit, Konsistenz und Format-Standards reviewen), 4-Schritt Loop (Briefing aufnehmen → Konzept entwickeln → Content schreiben → Review und Finalisierung), Primärer Soul: soul/creator.md, Skills: /elvis-x-hook-writer /elvis-x-content /elvis-copywriting /elvis-content-calendar
2. Schreibe `agent/seven.md` via Bash-Heredoc: analyst-Soul, Mission "Analysiert System- und Performance-Daten des OpenClaw-Ökosystems und macht Bedeutung aus Mustern sichtbar", 6 Capabilities (Performance-Metriken tracken und in Berichte übersetzen, System-Audits durchführen und Anomalien dokumentieren, Datenmuster erkennen und Bedeutung extrahieren, Benchmarks setzen und Ist-Soll-Abweichungen messen, Reporting-Strukturen aufbauen und pflegen, Schwachstellen durch Datenanalyse identifizieren und priorisieren), 5-Schritt Loop (Daten erfassen → Bereinigen und strukturieren → Muster analysieren → Bedeutung extrahieren → Report erstellen), Primärer Soul: soul/analyst.md, Skills: /elvis-growth-audit /elvis-market-scan /elvis-performance-tracker /elvis-data-audit /elvis-reporting
3. Schreibe `agent/sulu.md` via Bash-Heredoc: operator-Soul, Mission "Hält den operativen Betrieb des OpenClaw-Systems am Laufen — Aufgaben werden geroutet, priorisiert und nachverfolgt", 5 Capabilities (Eingehende Tasks klassifizieren und an den richtigen Agenten routen, Ausführungs-Fortschritt über alle aktiven Tasks tracken, Priorisierungs-Queue aktuell halten und Engpässe melden, Status-Reports für laufende Vorgänge erstellen, Blockierte Tasks eskalieren bevor Deadlines gerissen werden), 4-Schritt Loop (Eingang prüfen → Routing entscheiden → Fortschritt tracken → Status melden), Primärer Soul: soul/operator.md, Skills: /elvis-workflow-builder /elvis-task-router /elvis-execution-tracker
4. Schreibe `agent/tuvok.md` via Bash-Heredoc: strategist-Soul, Mission "Prüft die Systemintegrität und taktische Sicherheit des OpenClaw-Ökosystems durch logische Analyse und Schwachstellen-Identifikation", 6 Capabilities (System-Integrität auf Konsistenz und Schwachstellen prüfen, Sicherheitsanalysen für geplante Änderungen durchführen, Logik-Validierung für Entscheidungen und Pläne, Risiko-Assessment für operative Vorhaben, Taktische Sicherheitspläne entwickeln, Schwachstellen und Angriffspunkte im System identifizieren und dokumentieren); KEIN Delegations- oder Orchestrierungsvokabular; 4-Schritt Loop (Analyseziel definieren → Systemzustand erfassen → Logik-Validierung und Schwachstellen-Scan → Befund dokumentieren), Primärer Soul: soul/strategist.md, Skills: /elvis-execution-plan /elvis-system-audit /elvis-security-check /elvis-logic-validator
5. Führe `bash scripts/verify-s03.sh` aus; zusätzlich: `grep -i "delegier\|orchestrier\|koordinier" agent/tuvok.md | wc -l` — muss 0 sein

## Must-Haves

- [ ] Data-Capabilities beschreiben Content-Produktion — kein Analyse-Vokabular (das ist Seven)
- [ ] Seven-Capabilities beschreiben Daten-Analyse und Bedeutungs-Extraktion — kein Content-Produzieren (das ist Data)
- [ ] Sulu-Capabilities beschreiben Task-Routing und Operations-Tracking — keine strategische Planung
- [ ] Tuvok-Capabilities enthalten KEIN Delegations- oder Orchestrierungsvokabular (das ist Picard)
- [ ] Tuvok differenziert sich von Worf durch Security/Systemintegrität-Fokus statt Markt/Kampfstrategie
- [ ] Alle 4 Dateien auf Deutsch mit /elvis-* Skills (D001, D002)

## Verification

- `bash scripts/verify-s03.sh` — Fehleranzahl ≤ 65
- `grep -i "delegier\|orchestrier" agent/tuvok.md | wc -l` — 0
- `grep "## Primärer Soul" agent/tuvok.md` — enthält "soul/strategist.md"

## Observability Impact

- Signals added/changed: verify-s03.sh-Fehlerstand sinkt auf ≤ 65
- How a future agent inspects this: verify-s03.sh zeigt 4 neue Dateien mit grünen Sektions-Checks
- Failure state exposed: Fehlende Sektion oder verbotenes Vokabular in Tuvok sofort sichtbar

## Inputs

- `soul/creator.md`, `soul/analyst.md`, `soul/operator.md`, `soul/strategist.md` — Soul-Referenzen
- `agent/worf.md` (aus T02) — Tuvok-Differenzierungsreferenz: Worf = Kampfstrategie, Tuvok = Sicherheit/Logik
- `scripts/verify-s03.sh` — Stopping-Condition (aus T01)

## Expected Output

- `agent/data.md` — Content Agent, creator-Soul, 7 Sektionen
- `agent/seven.md` — Analysis Agent, analyst-Soul, 7 Sektionen
- `agent/sulu.md` — Operator Agent, operator-Soul, 7 Sektionen
- `agent/tuvok.md` — System/Security Agent, strategist-Soul, 7 Sektionen, kein Delegations-Vokabular
