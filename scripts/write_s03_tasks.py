
import os

base = r'C:\Dev\Openclaw_Meta_Maker\.gsd\milestones\M001\slices\S03\tasks'
os.makedirs(base, exist_ok=True)

tasks = {}

tasks['T01-PLAN.md'] = """---
estimated_steps: 4
estimated_files: 1
---

# T01: Stopping-Condition — scripts/verify-s03.sh schreiben

**Slice:** S03 — Agent Layer — 16 Star Trek Agenten
**Milestone:** M001

## Description

Das Verifikationsskript wird vor allen Agent-Dateien erstellt (D015-Prinzip). Es definiert die objektive Stopping-Condition für S03: 148 Checks in 3 Gruppen. Beim ersten Lauf zeigt es 148 Fehler — das ist korrekt und beweist, dass die Checks greifen. Jeder Task in S03 reduziert den Fehlerstand, bis T05 Exit-Code 0 erreicht.

Das Skript folgt exakt dem Muster von `scripts/verify-s02.sh`: ERRORS-Zähler, pass/fail-Hilfsfunktionen, 3 Gruppen mit Überschrift, abschließende Zusammenfassung, Exit-Code = ERRORS (D014).

## Steps

1. Lies `scripts/verify-s02.sh` als Referenz für Struktur, Funktionen und Stil
2. Erstelle `scripts/verify-s03.sh` via Bash-Heredoc mit:
   - Array `AGENT_FILES` mit allen 16 Dateinamen (kirk, spock, picard, data, worf, scotty, laforge, seven, sulu, tuvok, mccoy, riker, q, borg, troi, uhura)
   - Array `AGENT_SECTIONS` mit 7 Pflichtfeldern: `## Name`, `## Mission`, `## Capabilities`, `## Operating Loop`, `## Constraints`, `## Primärer Soul`, `## Primäre Skills`
   - Array `AUTONOMOUS_AGENTS` mit 5 Dateinamen (picard, q, borg, troi, uhura)
   - Array `SAFEGUARD_MARKERS` mit 4 fett-formatierten Markers: `**Max-Limit:**`, `**Approval-Gate:**`, `**Stop-Bedingung:**`, `**Rollback-Hinweis:**`
   - Gruppe [1/3]: 16 Datei-Existenz-Checks (für jede Datei in AGENT_FILES)
   - Gruppe [2/3]: 7×16=112 Sektions-Checks (für jede Datei × jede Sektion)
   - Gruppe [3/3]: 4×5=20 Safeguard-Checks (für jeden autonomen Agenten × jeden Marker)
3. Mache die Datei ausführbar: `chmod +x scripts/verify-s03.sh`
4. Führe das Skript aus: `bash scripts/verify-s03.sh`

## Must-Haves

- [ ] Skript enthält alle 16 Agent-Dateinamen
- [ ] Skript prüft alle 7 Pflichtfelder (`## Name`, `## Mission`, `## Capabilities`, `## Operating Loop`, `## Constraints`, `## Primärer Soul`, `## Primäre Skills`)
- [ ] Skript prüft alle 4 Safeguard-Marker für die 5 autonomen Agenten (Picard, Q, Borg, Troi, Uhura)
- [ ] Exit-Code = ERRORS (D014)
- [ ] Beim ersten Lauf: Exit-Code = 148 (alle fail)

## Verification

- `bash scripts/verify-s03.sh` — läuft ohne Bash-Syntaxfehler, zeigt 148 Fehler, Exit-Code = 148
- `echo $?` nach dem Lauf — gibt 148 aus
- `grep -c "fail " scripts/verify-s03.sh` — zeigt > 0 (fail-Funktion vorhanden)

## Observability Impact

- Signals added/changed: verify-s03.sh als primäre Inspection Surface für S03 — strukturierter Check-Report mit Haken/Kreuz
- How a future agent inspects this: `bash scripts/verify-s03.sh` — Exit-Code + Report zeigen exakt welche Dateien/Sektionen fehlen
- Failure state exposed: Jeder fehlende Agent oder jede fehlende Sektion wird mit Dateiname + Sektionsname benannt

## Inputs

- `scripts/verify-s02.sh` — Referenz für Skript-Struktur, ERRORS-Muster, pass/fail-Funktionen
- `templates/agent-template.md` — autoritative Liste der 7 Pflichtfelder

## Expected Output

- `scripts/verify-s03.sh` — lauffähiges 148-Check-Verifikationsskript, Exit-Code = 148 beim Erstlauf
"""

tasks['T02-PLAN.md'] = """---
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
"""

tasks['T03-PLAN.md'] = """---
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
"""

tasks['T04-PLAN.md'] = """---
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
"""

tasks['T05-PLAN.md'] = """---
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
"""

for fname, content in tasks.items():
    path = os.path.join(base, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.lstrip())
    print(f'Written {fname}: {len(content.splitlines())} lines')

print('All task plans written.')
