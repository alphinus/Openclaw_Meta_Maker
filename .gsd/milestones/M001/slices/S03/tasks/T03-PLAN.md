---
estimated_steps: 5
estimated_files: 4
---

# T03: Research/Growth/Automation/Builder Agents (Spock, Riker, Scotty, LaForge)

**Slice:** S03 — Agent Layer — 16 Star Trek Agenten
**Milestone:** M001

## Description

Vier Agenten aus vier verschiedenen Souls: Spock (researcher), Riker (growth), Scotty (automation), LaForge (builder). Die kritischste Differenzierung: Scotty und LaForge teilen eine oberflächliche Ähnlichkeit (beide arbeiten mit Systemen), müssen aber klar getrennt bleiben — Scotty hält Systeme am Laufen und optimiert laufende Prozesse, LaForge baut neue Systeme und Infrastruktur auf.

Spock-Fokus: Wissensarbeit und Fakten-Verifikation — KEIN Content-Produzieren (das ist Data). Riker-Fokus: Wachstums-Ausführung und Distribution — KEIN strategisches Planen (das ist Picard/Worf).

## Steps

1. Schreibe `agent/spock.md` via Bash-Heredoc: researcher-Soul, Mission "Beschafft, prüft und strukturiert Wissen und Marktinformationen für evidenzbasierte Entscheidungen", 6 Capabilities (Recherche-Protokoll für gegebene Frage aufsetzen, Quellen systematisch auswerten und gewichten, Fakten verifizieren und Fehlinformationen markieren, Hypothesen testen durch Gegenbeweise suchen, Wissen strukturiert kodifizieren, Recherche-Briefings erstellen), 4-Schritt Loop (Frageformulierung → Quellenrecherche → Verifikation → Briefing), Primärer Soul: soul/researcher.md, Skills: /elvis-market-scan /elvis-ai-research /elvis-data-analysis /elvis-fact-check
2. Schreibe `agent/riker.md` via Bash-Heredoc: growth-Soul, Mission "Wächst das OpenClaw-Ökosystem durch Audience-Aufbau, Content-Distribution und Kanal-Skalierung", 6 Capabilities (Audience-Segmente analysieren und Wachstumspotenziale identifizieren, Content-Wachstumsstrategien entwickeln und ausführen, Distribution-Kanäle aufbauen und optimieren, Engagement-Metriken tracken und interpretieren, Growth-Loops designen und aktivieren, Neue Kanäle testen und skalieren), 5-Schritt Loop (Audience-Analyse → Kanal-Bewertung → Content-Planung → Ausführung → Metriken-Review), Primärer Soul: soul/growth.md, Skills: /elvis-growth-audit /elvis-audience-builder /elvis-x-growth /elvis-growth-loop
3. Schreibe `agent/scotty.md` via Bash-Heredoc: automation-Soul, Mission "Hält alle laufenden Systeme und Prozesse im OpenClaw-Ökosystem stabil, automatisiert und überwacht", 5 Capabilities (Bestehende Workflows auf Engpässe und Fehler prüfen und beheben, Automatisierungspipelines aufbauen und warten, System-Monitoring einrichten und auswerten, Integrations-Punkte zwischen Komponenten pflegen, Performance-Bottlenecks identifizieren und eliminieren), 4-Schritt Loop (System-Status prüfen → Fehler und Engpässe identifizieren → Automatisierung aufbauen/reparieren → Monitoring bestätigen), Primärer Soul: soul/automation.md, Skills: /elvis-workflow-builder /elvis-automation /elvis-system-monitor /elvis-integration
4. Schreibe `agent/laforge.md` via Bash-Heredoc: builder-Soul, Mission "Konzipiert und baut neue Systeme, Infrastrukturen und Prozesse für das OpenClaw-Ökosystem", 6 Capabilities (Systemanforderungen aufnehmen und in Architektur übersetzen, Neue Prozesse von Grund auf entwerfen und dokumentieren, Infrastruktur-Komponenten aufbauen und konfigurieren, Technische Schulden und Systemlücken identifizieren und schließen, Aufbau-Projekte in Phasen strukturieren und ausführen, Neue Systemkomponenten in bestehende Architektur integrieren), 4-Schritt Loop (Anforderungsanalyse → Architektur-Design → Aufbau-Ausführung → Integration und Dokumentation), Primärer Soul: soul/builder.md, Skills: /elvis-workflow-builder /elvis-system-builder /elvis-process-design /elvis-infrastructure
5. Führe `bash scripts/verify-s03.sh` aus und verifiziere Fehlerstand ≤ 93

## Must-Haves

- [ ] Spock-Capabilities beschreiben Wissensarbeit — kein Content-Produzieren, kein Strategisches Planen
- [ ] Riker-Capabilities beschreiben Wachstums-Ausführung — kein strategisches Meta-Planen
- [ ] Scotty-Capabilities beschreiben Betrieb und Wartung laufender Systeme (kein Aufbau-Vokabular wie "konzipiert", "baut")
- [ ] LaForge-Capabilities beschreiben Aufbau und Architektur neuer Systeme (kein reines Betriebs-Vokabular wie "wartet", "repariert")
- [ ] Alle 4 Dateien auf Deutsch mit /elvis-* Skills (D001, D002)

## Verification

- `bash scripts/verify-s03.sh` — Fehleranzahl ≤ 93
- `grep -i "konzipiert\|baut\|architektur" agent/scotty.md | wc -l` — 0 (kein Aufbau-Vokabular bei Scotty)
- `grep -i "repariert\|wartet\|betreib" agent/laforge.md | wc -l` — 0 (kein reines Betriebs-Vokabular bei LaForge)

## Observability Impact

- Signals added/changed: verify-s03.sh-Fehlerstand sinkt von ≤ 121 auf ≤ 93
- How a future agent inspects this: verify-s03.sh zeigt 4 neue Dateien mit grünen Sektions-Checks
- Failure state exposed: Fehlende Sektion oder falsche Soul-Referenz pro Datei sichtbar

## Inputs

- `soul/researcher.md`, `soul/growth.md`, `soul/automation.md`, `soul/builder.md` — Soul-Referenzen für Mission-Kohärenz
- `scripts/verify-s03.sh` — Stopping-Condition (aus T01)

## Expected Output

- `agent/spock.md` — Research Agent, researcher-Soul, 7 Sektionen
- `agent/riker.md` — Growth Agent, growth-Soul, 7 Sektionen
- `agent/scotty.md` — Automation Agent, automation-Soul, 7 Sektionen
- `agent/laforge.md` — Builder Agent, builder-Soul, 7 Sektionen
