# S03: Agent Layer — 16 Star Trek Agenten — Research

**Date:** 2026-03-11

## Summary

S03 ist ein reiner Schreibslice — keine externen Libraries, keine APIs, kein ausführbarer Code. Aufgabe: 16 Agent-Dateien (`agent/*.md`) und ein Verifikationsskript (`scripts/verify-s03.sh`) erstellen. Die Foundations sind vollständig vorhanden: 10 Soul-Dateien mit klaren Agent-Mappings in "## Geeignet für" und 16 Identity-Dateien als Persönlichkeitsgrundlage.

Das Hauptrisiko ist konzeptueller Natur: Die Agent-Schicht muss sauber von der Identity-Schicht getrennt bleiben (D012 — Agent = WAS, Identity = WER). Worf ist bereits als vollständiges Beispiel im `templates/agent-template.md` ausgearbeitet und dient als Benchmark für alle weiteren Agents. Das Worf-Beispiel kann direkt extrahiert werden, die anderen 15 Agents müssen neu geschrieben werden.

Sekundäres Risiko: "## Primäre Skills" referenziert Skills, die erst in S04–S07 erstellt werden. Die Agent-Dateien müssen geplante Skill-Namen vorwegnehmen — konsistent mit dem Skill-Naming-Plan aus den späteren Slices. Diese Forward References sind architektonisch korrekt (reine Markdown, kein Code), müssen aber Naming-Konventionen exakt einhalten damit S09-Verifikation keine Brüche findet.

Sonderfall autonome Agenten: Picard, Q, Borg, Troi und Uhura benötigen gemäß D007 explizite Safeguards im Constraints-Block — Max-Limit, Approval-Gate, Stop-Bedingung und Rollback-Hinweis. Diese müssen fett-formatiert sein gemäß D013 (`**Max-Limit:** ...`).

## Recommendation

**Ansatz: Template-Extraktion für Worf + Direktes Schreiben für alle anderen via Bash-Heredoc-Pipeline.**

Reihenfolge nach konzeptueller Komplexität:
1. Verifikationsskript zuerst (definiert die Stopping-Condition — D015-Prinzip)
2. Worf aus Template extrahieren (sofortige grüne Baseline)
3. Klassische Agenten in Gruppen: Kirk + McCoy (execution), Spock (researcher), Riker (growth), Scotty + LaForge (automation/builder), Data (creator), Seven + Troi (analyst), Sulu + Uhura (operator), Picard + Tuvok + Worf (strategist)
4. Sonderfälle zuletzt: Q und Borg (höchste Komplexität — D007 Safeguards)

Write-Tool schreibt auf diesem System in falschen Pfad (bekannter Bug aus S01/S02 — D001/T01-SUMMARY). Alle Dateien via Bash-Heredocs erstellen.

## Don't Hand-Roll

| Problem | Existing Solution | Why Use It |
|---------|------------------|------------|
| Agent-Format | `templates/agent-template.md` | 7 Sektionen, Worf-Beispiel, HTML-Kommentare entfernbar via perl |
| Worf-Extraktion | `templates/agent-template.md` ab `---` Trennlinie | Direkt nutzbar — gleiche Pipeline wie S02 (tail + perl + sed) |
| Soul-zu-Agent-Mapping | `grep "## Geeignet für" soul/*.md -A 10` | Autoritative Zuordnung, keine manuelles Nachschlagen |
| Sektionen-Check | Muster aus `scripts/verify-s02.sh` | Selbe ERRORS-Zähl-Logik, selbe pass/fail-Funktionen, selbe Exit-Code-Konvention |

## Existing Code and Patterns

- `templates/agent-template.md` — 7 Pflichtfelder: Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills. Worf-Beispiel ab der `---` Trennlinie ist production-ready.
- `scripts/verify-s02.sh` — Blueprint für `verify-s03.sh`: ERRORS-Zähler, pass/fail-Funktionen, 3-Gruppen-Struktur (Datei-Existenz → Pflichtfelder), Exit-Code = Fehleranzahl (D014)
- `soul/*/geeignet-für` — Autoritative Soul-zu-Agent-Zuordnung (16 Agents auf 9 Souls verteilt — minimalist hat keinen primären Agenten)
- `identity/*.md` — Charakter-Grundlage, wird in Agent-Dateien referenziert aber nicht inhaltlich wiederholt

## Agent-zu-Soul-Mapping (autoritativ aus soul/*.md)

| Agent | Funktion | Soul | Datei |
|-------|----------|------|-------|
| Kirk | Haupt-Agent | execution | soul/execution.md |
| McCoy | Execution Agent | execution | soul/execution.md |
| Spock | Research Agent | researcher | soul/researcher.md |
| Picard | Orchestrator | strategist | soul/strategist.md |
| Worf | Strategy Agent | strategist | soul/strategist.md |
| Tuvok | System Agent | strategist | soul/strategist.md |
| Riker | Growth Agent | growth | soul/growth.md |
| Data | Content Agent | creator | soul/creator.md |
| Q | Agent Creator | creator | soul/creator.md |
| Scotty | Automation Agent | automation | soul/automation.md |
| Borg | Skill Expander | automation | soul/automation.md |
| LaForge | Builder Agent | builder | soul/builder.md |
| Seven | Analysis Agent | analyst | soul/analyst.md |
| Troi | System Analyzer | analyst | soul/analyst.md |
| Sulu | Operator Agent | operator | soul/operator.md |
| Uhura | Library Manager | operator | soul/operator.md |

## Constraints

- Alle 16 Agent-Dateien auf Deutsch (D002) — Dateinamen bleiben englisch (Kleinbuchstaben, snake_case: `laforge.md`, `seven.md`)
- Agent-Dateien enthalten **keinen** Persönlichkeitsinhalt — ausschließlich Mission, Capabilities, Operating Loop, Constraints, Soul-Referenz, Skill-Referenzen (D012)
- Picard, Q, Borg, Troi, Uhura: Constraints-Block **muss** D007/D013-Safeguards enthalten mit `**Max-Limit:**`, `**Approval-Gate:**`, `**Stop-Bedingung:**`, `**Rollback-Hinweis:**` als fett-formatierte Bullet-Points
- Tuvok teilt strategist-Soul mit Picard und Worf — Capabilities müssen klar differenzieren (Tuvok = Sicherheit/Systemintegrität/Taktik, Picard = Orchestrierung/Delegation, Worf = Kampfbereitschaft/Planung)
- "## Primäre Skills" darf nur `/elvis-*` Prefix verwenden — keine Skills ohne Prefix
- Forward References zu noch nicht existierenden Skills (S04–S07) sind explizit erlaubt — Naming muss Konventionen antizipieren
- Write-Tool-Bug: Alle Dateien via Bash-Heredocs, nicht via Write-Tool

## Skill-Referenzen pro Agent (geplante Forward References)

Agents referenzieren Skills aus allen Domänen. Da S04–S07 noch nicht abgeschlossen sind, orientieren sich die Referenzen an den geplanten Skill-Namen aus dem Kontext und den Benchmark-Skills:

| Agent | Existierende Skills | Geplante Skills (Forward Reference) |
|-------|--------------------|------------------------------------|
| Kirk | /elvis-execution-plan | /elvis-decision-framework, /elvis-rapid-response |
| Picard | /elvis-execution-plan | /elvis-orchestration, /elvis-agent-delegation, /elvis-system-review |
| Riker | /elvis-growth-audit | /elvis-audience-builder, /elvis-x-growth, /elvis-growth-loop |
| Spock | /elvis-market-scan | /elvis-ai-research, /elvis-data-analysis, /elvis-fact-check |
| Worf | /elvis-execution-plan, /elvis-market-scan | /elvis-strategy-audit, /elvis-competitive-scan, /elvis-risk-assessment |
| Data | /elvis-x-hook-writer | /elvis-x-content, /elvis-copywriting, /elvis-content-calendar |
| Scotty | /elvis-workflow-builder | /elvis-automation, /elvis-system-monitor, /elvis-integration |
| LaForge | /elvis-workflow-builder | /elvis-system-builder, /elvis-process-design, /elvis-infrastructure |
| Seven | /elvis-growth-audit, /elvis-market-scan | /elvis-performance-tracker, /elvis-data-audit, /elvis-reporting |
| Sulu | /elvis-workflow-builder | /elvis-task-router, /elvis-execution-tracker |
| Tuvok | /elvis-execution-plan | /elvis-system-audit, /elvis-security-check, /elvis-logic-validator |
| McCoy | /elvis-execution-plan | /elvis-rapid-execution, /elvis-direct-action |
| Q | /elvis-skill-generator | /elvis-agent-generator, /elvis-agent-creator, /elvis-concept-design |
| Borg | /elvis-skill-generator | /elvis-skill-expander, /elvis-library-builder, /elvis-pattern-assimilation |
| Troi | /elvis-market-scan, /elvis-growth-audit | /elvis-system-analyzer, /elvis-weakness-detector, /elvis-signal-reader |
| Uhura | /elvis-skill-generator | /elvis-library-manager, /elvis-knowledge-organizer, /elvis-command-router |

## Common Pitfalls

- **Persönlichkeit in Agent-Dateien** — "Kirk entscheidet mutig unter Unsicherheit" ist Identity-Inhalt, nicht Agent-Inhalt. Richtig: "Entscheidet bei unvollständiger Datenlage innerhalb von < 2 Minuten und dokumentiert die Entscheidung". Jede Formulierung gegen Faustregel D012 prüfen.
- **Operating Loop = Capabilities wiederholen** — Der Loop beschreibt die REIHENFOLGE und LOGIK der Arbeit, nicht nochmals was der Agent kann. Lo
op-Schritte sind Phasen (Lageerfassung → Analyse → Ausführung → Abschluss), keine Capability-Liste.
- **Safeguards ohne Fett-Formatierung** — Bei den 5 autonomen Agenten müssen die 4 Safeguard-Marker fett sein (D013): `**Max-Limit:**` etc. Ohne Fett-Formatierung sind sie nicht grep-fähig.
- **Tuvok vs. Picard vs. Worf Verwischung** — Alle drei haben strategist-Soul. Capabilities müssen differenzieren: Picard delegiert an andere Agenten, Worf plant Kampf-/Marktstrategien, Tuvok prüft Systemintegrität und Sicherheit.
- **Forward-Referenz-Naming-Fehler** — Skill-Namen wie `/elvis-systemAnalyzer` (camelCase) statt `/elvis-system-analyzer` (kebab-case) sind inkonsistent mit der Naming-Konvention aller existierenden Skills.
- **Zu wenige Capabilities** — Template verlangt 5–8 Bullets. Weniger als 5 deutet auf unvollständige Agent-Definition, mehr als 8 auf fehlende Fokussierung.

## Open Risks

- **Forward-Reference-Validierung in S09** — Wenn S04–S06 andere Skill-Namen wählen als hier antizipiert, entstehen tote Referenzen. Risiko: mittel. Mitigation: S09-Verifikation prüft explizit alle Skill-Referenzen gegen existierende Dateien — dann wird ggf. ein Korrektur-Pass nötig.
- **Tuvok-Strategen-Kollision** — Drei Agenten mit strategist-Soul. Wenn Capabilities nicht klar differenzieren, entstehen redundante Agent-Definitionen. Risiko: niedrig mit expliziter Differenzierungsstrategie aus Constraints-Block.
- **Q/Borg Scope-Creep in Operating Loop** — Q und Borg sind die kreativsten Sonderfälle (S02 Forward Intelligence). Safeguard-Constraints müssen hart und konkret sein (Max. X pro Durchlauf), keine Kann-Formulierungen.
- **verify-s03.sh Sektionen-Check Granularität** — Je mehr Sektions-Checks, desto robuster die Stopping-Condition. Mindestens: Datei-Existenz (16 Checks) + 7 Pflichtfelder pro Datei (112 Checks) = 128 Checks minimum.

## Skills Discovered

| Technology | Skill | Status |
|------------|-------|--------|
| Markdown file generation | — | none found — not applicable |

_Keine externe Technologie involviert — reiner Schreibslice._

## Sources

- Soul-zu-Agent-Mapping (source: `grep "## Geeignet für" soul/*.md -A 10` — alle 10 Soul-Dateien gelesen)
- Agent-Template-Format (source: `templates/agent-template.md` — vollständiges Worf-Beispiel)
- S02 Forward Intelligence (source: S02-SUMMARY.md — Write-Tool-Bug, Tuvok-Sonderfälle, Q/Borg-Komplexität)
- Safeguard-Format (source: DECISIONS.md D007/D013)
- Stopping-Condition-Konvention (source: DECISIONS.md D014/D015, `scripts/verify-s02.sh`)
