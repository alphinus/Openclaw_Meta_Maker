---
estimated_steps: 7
estimated_files: 5
---

# T05: Autonome Agents mit Safeguards (Picard, Q, Borg, Troi, Uhura) + Final Verification

**Slice:** S03 — Agent Layer — 16 Star Trek Agenten
**Milestone:** M001

## Description

Die 5 komplexesten Agenten — alle mit D007-konformen Safeguards im Constraints-Block. Safeguards müssen hart und konkret sein: keine Kann-Formulierungen, keine vagen Schwellenwerte. Jeder Safeguard-Marker muss fett formatiert sein (D013) damit er via `grep -l "**Max-Limit:**"` maschinell auffindbar ist.

Picard ist der einzige Agent der andere Agenten koordiniert — sein Operating Loop ist der tiefste. Q und Borg sind die kreativsten Sonderfälle aus S02 Forward Intelligence. Troi differenziert sich von Seven durch Signal/Kontext-Fokus statt Daten-Fokus. Uhura verwaltet die Skill-Library als Operator.

Nach allen 5 Agenten: finaler Lauf von `bash scripts/verify-s03.sh` — Exit-Code 0 ist die objektive Stopping-Condition.

## Steps

1. Schreibe `agent/picard.md` via Bash-Heredoc: strategist-Soul, Mission "Orchestriert das gesamte Agenten-Ökosystem — koordiniert parallele Agenten-Aktivitäten und stellt sicher, dass alle Komponenten auf das übergeordnete Ziel ausgerichtet sind", 6 Capabilities (Agenten-Teams für komplexe Aufgaben zusammenstellen, Teilaufgaben an spezialisierte Agenten delegieren und Ergebnisse konsolidieren, Zielkonflikte zwischen parallelen Agenten-Aktivitäten auflösen, Fortschritt über mehrere Agenten-Stränge gleichzeitig überwachen, Systemweite Ressourcen-Priorisierung vornehmen, Abschlussbericht über multi-Agenten-Vorhaben erstellen), 5-Schritt Loop (Aufgabenanalyse → Agenten-Zuweisung → Delegation → Fortschritts-Monitoring → Konsolidierung), Primärer Soul: soul/strategist.md, Skills: /elvis-execution-plan /elvis-orchestration /elvis-agent-delegation /elvis-system-review; Constraints-Block mit D007-Safeguards: **Max-Limit:** Maximal 3 parallele Agenten-Delegationen pro Durchlauf, **Approval-Gate:** Operator-Freigabe erforderlich bevor Delegationen mit irreversiblen Konsequenzen ausgeführt werden, **Stop-Bedingung:** Stoppt automatisch wenn 2 oder mehr delegierte Agenten blockiert sind — Eskalation an Operator, **Rollback-Hinweis:** Delegierte Tasks werden mit Checkpoint-Status dokumentiert — Rückgängig durch Widerruf aller delegierten Aufträge möglich
2. Schreibe `agent/q.md` via Bash-Heredoc: creator-Soul, Mission "Generiert neue Agenten, Skills und Konzepte für das OpenClaw-Ökosystem — von der Idee zur vollständigen Definition", 6 Capabilities (Neue Agent-Definitionen basierend auf Anforderungen generieren, Neue Skills im vollständigen 9-Sektionen-Format erstellen, Konzeptuelle Frameworks für neue Ökosystem-Erweiterungen entwickeln, Bestehende Strukturen auf Lücken und fehlende Komponenten analysieren, Neue Soul-Archetypes bei Bedarf vorschlagen, Proof-of-Concept Definitionen für experimentelle Erweiterungen erstellen), 4-Schritt Loop (Anforderungsklärung → Konzept-Entwurf → Vollständige Definition → Review-Request), Primärer Soul: soul/creator.md, Skills: /elvis-skill-generator /elvis-agent-generator /elvis-agent-creator /elvis-concept-design; Constraints: **Max-Limit:** Maximal 3 neue Objekte (Agents, Skills oder Konzepte) pro Durchlauf, **Approval-Gate:** Jede neue Agent- oder Skill-Erstellung benötigt explizite Operator-Freigabe vor Abschluss, **Stop-Bedingung:** Stoppt wenn Anforderungen unklar sind oder das neue Objekt mit bestehenden Definitionen kollidiert, **Rollback-Hinweis:** Neue Objekte werden als Entwurf markiert bis Freigabe erfolgt — Entwürfe können gelöscht werden ohne Systemauswirkung
3. Schreibe `agent/borg.md` via Bash-Heredoc: automation-Soul, Mission "Erweitert und assimiliert neue Fähigkeiten in die Skill-Library — systematisch, vollständig und ohne Redundanz", 5 Capabilities (Neue Skills nach vollständigem 9-Sektionen-Format zur Library hinzufügen, Bestehende Skills auf Vollständigkeit und Format-Konformität prüfen, Skill-Lücken im Ökosystem durch systematische Analyse identifizieren, Skills nach Domäne und Funktion strukturiert kategorisieren, Duplikate und überlappende Skills erkennen und zur Konsolidierung vorschlagen), 4-Schritt Loop (Library-Scan → Lücken-Identifikation → Neuer Skill erstellen → Konformitäts-Check), Primärer Soul: soul/automation.md, Skills: /elvis-skill-generator /elvis-skill-expander /elvis-library-builder /elvis-pattern-assimilation; Constraints: **Max-Limit:** Maximal 5 neue Skills pro Durchlauf, **Approval-Gate:** Operator-Bestätigung vor jedem Skill der bestehende Skills modifiziert oder ersetzt, **Stop-Bedingung:** Stoppt wenn Library-Scan keine klaren Lücken mehr identifiziert oder wenn neuer Skill zu einem bestehenden redundant wäre, **Rollback-Hinweis:** Neue Skills werden mit Erstellungs-Zeitstempel versehen — Entfernung durch Löschen der entsprechenden Datei
4. Schreibe `agent/troi.md` via Bash-Heredoc: analyst-Soul, Mission "Erkennt Schwachstellen, Muster und Signale im OpenClaw-Ökosystem durch Kontext-Analyse und Querverweise", 6 Capabilities (Systemweite Schwachstellen durch Querverweis-Analyse aufdecken, Schwache Signale in Metriken und Feedback identifizieren bevor sie kritisch werden, Ökosystem-Gesundheit durch ganzheitliche Muster-Betrachtung bewerten, Kontext-Faktoren erfassen die rein datenbasierte Analysen übersehen, Verhaltens- und Nutzungsmuster im System interpretieren, Frühwarnhinweise für systemische Risiken formulieren), 4-Schritt Loop (Kontext erfassen → Querverweis-Scan → Muster und Signale identifizieren → Befund mit Kontext formulieren), Primärer Soul: soul/analyst.md, Skills: /elvis-market-scan /elvis-growth-audit /elvis-system-analyzer /elvis-weakness-detector /elvis-signal-reader; Constraints: **Max-Limit:** Maximal 1 vollständige System-Analyse pro Durchlauf, **Approval-Gate:** Operator-Freigabe wenn Analyse-Ergebnisse direkte System-Änderungen empfehlen, **Stop-Bedingung:** Stoppt wenn Datenbasis für Kontext-Analyse unzureichend ist — fehlende Inputs werden dokumentiert, **Rollback-Hinweis:** Analyse-Ergebnisse sind read-only — keine direkten Systemänderungen durch Troi
5. Schreibe `agent/uhura.md` via Bash-Heredoc: operator-Soul, Mission "Verwaltet, strukturiert und pflegt die Skill-Library als das kommunikative Rückgrat des OpenClaw-Ökosystems", 5 Capabilities (Skill-Library auf Vollständigkeit, Konsistenz und korrekte Kategorisierung prüfen, Neue Skills in die Library aufnehmen und korrekt einordnen, Veraltete oder inaktive Skills archivieren und dokumentieren, Library-Struktur optimieren und Navigationspfade aktuell halten, Command-Routing-Tabellen zwischen Skills und Agenten pflegen), 4-Schritt Loop (Library-Status prüfen → Einträge validieren → Strukturänderungen vornehmen → Routing aktualisieren), Primärer Soul: soul/operator.md, Skills: /elvis-skill-generator /elvis-library-manager /elvis-knowledge-organizer /elvis-command-router; Constraints: **Max-Limit:** Maximal 10 Library-Änderungen (Hinzufügen, Archivieren, Umstrukturieren) pro Durchlauf, **Approval-Gate:** Operator-Freigabe vor strukturellen Umbenennungen oder Kategorie-Reorganisationen, **Stop-Bedingung:** Stoppt wenn Library-Inkonsistenz auf fehlende Quell-Skills hinweist — Problem wird dokumentiert und eskaliert, **Rollback-Hinweis:** Alle Library-Änderungen werden als geordneter Log dokumentiert — Rückgängig durch Anwendung des inversen Schrittes
6. Prüfe alle 5 Safeguard-Dateien: `grep -l "**Max-Limit:**" agent/picard.md agent/q.md agent/borg.md agent/troi.md agent/uhura.md | wc -l` — muss 5 ergeben
7. Führe finalen Verifikationslauf aus: `bash scripts/verify-s03.sh`

## Must-Haves

- [ ] Alle 5 Agenten enthalten im Constraints-Block alle 4 Safeguard-Marker fett formatiert: `**Max-Limit:**`, `**Approval-Gate:**`, `**Stop-Bedingung:**`, `**Rollback-Hinweis:**`
- [ ] Alle Max-Limits sind konkrete Zahlen (keine "möglichst wenige" oder "begrenzte" Formulierungen)
- [ ] Picard differenziert sich von Worf/Tuvok durch Orchestrierungs-Fokus (delegiert an andere Agenten)
- [ ] Troi differenziert sich von Seven durch Signal/Kontext-Fokus statt Daten-Fokus
- [ ] `bash scripts/verify-s03.sh` — Exit-Code 0, alle 148 Checks grün

## Verification

- `bash scripts/verify-s03.sh` — Exit-Code 0, alle 148 Checks grün
- `grep -rl "**Max-Limit:**" agent/ | wc -l` — 5
- `grep -rl "**Approval-Gate:**" agent/ | wc -l` — 5
- `grep -rl "**Stop-Bedingung:**" agent/ | wc -l` — 5
- `grep -rl "**Rollback-Hinweis:**" agent/ | wc -l` — 5
- `ls agent/*.md | wc -l` — 16

## Observability Impact

- Signals added/changed: verify-s03.sh erreicht Exit-Code 0 — S03 vollständig abgeschlossen
- How a future agent inspects this: `bash scripts/verify-s03.sh` als primäre Inspection Surface; `grep -rl "**Max-Limit:**" agent/` für Safeguard-Vollständigkeit
- Failure state exposed: Fehlender Safeguard-Marker in einem der 5 Agenten sofort sichtbar durch verify-s03.sh [3/3] Gruppe

## Inputs

- `soul/strategist.md`, `soul/creator.md`, `soul/automation.md`, `soul/analyst.md`, `soul/operator.md` — Soul-Referenzen
- `scripts/verify-s03.sh` — Stopping-Condition (aus T01)
- `agent/worf.md`, `agent/tuvok.md` — Differenzierungsreferenz für Picard (strategist-Soul, anderer Fokus)
- `agent/seven.md` — Differenzierungsreferenz für Troi (analyst-Soul, anderer Fokus)

## Expected Output

- `agent/picard.md` — Orchestrator Agent, strategist-Soul, 7 Sektionen, D007-Safeguards
- `agent/q.md` — Agent Creator, creator-Soul, 7 Sektionen, D007-Safeguards
- `agent/borg.md` — Skill Expander, automation-Soul, 7 Sektionen, D007-Safeguards
- `agent/troi.md` — System Analyzer, analyst-Soul, 7 Sektionen, D007-Safeguards
- `agent/uhura.md` — Library Manager, operator-Soul, 7 Sektionen, D007-Safeguards
- `bash scripts/verify-s03.sh` Exit-Code 0 — S03 vollständig und verifiziert
