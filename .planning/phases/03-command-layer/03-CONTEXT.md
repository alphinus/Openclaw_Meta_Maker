# Phase 3: Command Layer - Context

**Gathered:** 2026-03-14
**Status:** Ready for planning

<domain>
## Phase Boundary

10 Command-Dateien erstellen als reine Routing-Deklarationen. Jede Command-Datei ist ein Shortcut: kurzer, einprägsamer Name → Agent + Skill-Chain. Keine Ausführungslogik in Command-Dateien. Zusätzlich: Command-Router Routing-Tabelle um alle Phase-2-Skills erweitern.

</domain>

<decisions>
## Implementation Decisions

### Command-Datei Format
- **Minimale Routing-Deklaration** — Command-Dateien sind KEINE Skills (kein 9-Sektionen-Format, keine Ausführungsschritte, keine Safeguards). Sie sind reine Routing-Deklarationen mit maximal 5 Feldern:
  1. **Command** — Der Aufruf-Name (z.B. `/build-agent`)
  2. **Beschreibung** — 1 Satz was der Command tut (für den Operator als Hilfe)
  3. **Agent** — Welcher Agent zuständig ist (z.B. Q, Borg, Picard)
  4. **Skill-Chain** — Welche `/elvis-*` Skills aufgerufen werden (geordnete Liste)
  5. **Hinweis** — Optional: Kontext-Info (z.B. "Erstellt Soul + Identity + Agent als Paket")
- **Begründung:** Success Criterion 4 ist explizit: "Kein Command-File enthält Ausführungslogik — jedes File ist eine reine Routing-Deklaration." Jede Logik gehört in den Skill, nicht in den Command.
- **Kein Template nötig:** Commands sind zu minimal für ein Template. Das Format ist in 10 Zeilen definiert und konsistent über alle 10 Dateien.
- **Sprache:** Deutsch mit englischen Fachbegriffen (konsistent mit dem gesamten Projekt).

### Verzeichnisstruktur
- **Neues `commands/` Verzeichnis auf Root-Ebene** — parallel zu `skills/`, `agent/`, `soul/`, `identity/`.
- **Begründung:** Commands sind eine eigene Entity-Klasse im Ökosystem (wie Skills, Agents, Souls, Identities). Sie in `skills/meta/` unterzubringen wäre semantisch falsch — Commands sind keine Skills. Ein eigenes Verzeichnis ist konsistent mit der bestehenden Architektur.
- **Dateinamen:** `{command-name}.md` ohne Präfix. Beispiel: `commands/build-agent.md`, `commands/create-soul.md`.
- **Kein Unterverzeichnis:** 10 Dateien sind flach organisierbar. Keine Kategorie-Ordner nötig.

### Router-Update
- **Ja — als Teil von Phase 3.** Die Routing-Tabelle im `/elvis-command-router` wird von 4 auf 12+ Einträge erweitert.
- **Neue Einträge für Phase-2-Skills:**
  - Agent zusammenstellen → Q → /elvis-agent-creator
  - Skills erweitern, Varianten → Borg → /elvis-skill-expander
  - System analysieren, Schwächen → Troi → /elvis-system-analyzer
  - Library verwalten, Katalog → Uhura → /elvis-library-manager
  - Gesundheitscheck, Health → Picard → /elvis-ecosystem-health
  - Agent optimieren → Picard → /elvis-agent-optimizer
  - Konzept entwerfen → Q → /elvis-concept-design
- **Begründung:** Der Router ist der zentrale Knotenpunkt. Ohne die Phase-2-Einträge ist er unvollständig. Phase 3 ist der logische Zeitpunkt — nach Abschluss aller Skills, vor Finalisierung des Command-Layers.
- **Hinweis in Routing-Tabelle entfernen:** "Hinweis: Diese Tabelle wird in Phase 2 um weitere Meta-Skills erweitert" → ersetzen durch aktuelle, vollständige Tabelle.

### CMD-10 Abgrenzung (`/route-command`)
- **CMD-10 ist ein Alias/Redirect zum bestehenden `/elvis-command-router`.** Keine eigene Logik, kein Wrapper.
- **Die Command-Datei `commands/route-command.md` routet einfach zu:** Agent: Picard → Skill-Chain: /elvis-command-router.
- **Begründung:** Der Router existiert bereits als vollständiger Skill (META-08, Phase 1). CMD-10 als eigenständiger Skill wäre Duplikation. Als Command-Datei ist `/route-command` konsistent mit den anderen 9 Commands — ein Shortcut, kein neues Feature.
- **Praktischer Nutzen:** User kann `/route-command` oder `/elvis-command-router` verwenden — beide führen zum selben Ergebnis. `/route-command` ist der einprägsame Shortcut, `/elvis-command-router` ist der technische Skill-Name.

### Claude's Discretion
- Exakte Formulierung der Beschreibungs-Zeile in jeder Command-Datei
- Reihenfolge der Erstellung der 10 Command-Dateien
- Ob der optionale "Hinweis"-Abschnitt in jeder Command-Datei enthalten ist oder nur bei komplexeren Chains
- Genaue Keywords in der erweiterten Routing-Tabelle (solange eindeutig und konsistent)

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `skills/meta/elvis-command-router.md`: Bestehender Router mit 4-Einträge-Routing-Tabelle — wird in Phase 3 auf 12+ Einträge erweitert
- Alle 12 Meta-Skills in `skills/meta/`: Die Ziel-Skills auf die jeder Command routet — vollständig und verifiziert

### Established Patterns
- Entity-Verzeichnisse auf Root-Ebene: `skills/`, `agent/`, `soul/`, `identity/` → `commands/` folgt diesem Pattern
- Deutsch mit englischen Fachbegriffen
- `/elvis-*` Naming Convention für Skills, kurze Namen ohne Präfix für Commands
- Statische Routing-Tabelle: Keyword → Agent → Skill-Chain

### Integration Points
- Jeder Command → referenziert genau einen Agent + eine Skill-Chain
- Commands → werden in der Routing-Tabelle des Command-Routers referenziert (als Keywords, nicht als Ziele)
- Command-Router → routet zu `/elvis-*` Skills, nicht zu Commands

### Bestehende Agent-Zuordnungen
- Q (Agent Creator): /elvis-agent-creator, /elvis-concept-design
- Borg (Skill Expander): /elvis-skill-expander, /elvis-skill-generator
- Troi (System Analyzer): /elvis-system-analyzer
- Uhura (Library Manager): /elvis-library-manager
- Picard (Router/Command): /elvis-command-router, /elvis-ecosystem-health, /elvis-agent-optimizer
- Elvis (Skill Generator): /elvis-soul-generator, /elvis-identity-generator, /elvis-agent-generator

</code_context>

<specifics>
## Specific Ideas

- User-Anweisung: "Best Practice, State of the Art, langlebig und fehlerfrei"
- Command-Dateien sind die dünnste Schicht des Systems — maximal 10 Zeilen pro Datei
- Der Router ist nach dem Update der einzige Ort der alle Routen kennt — Commands sind die formale Deklaration davon
- 10 Commands + 1 Router-Update = 11 Artefakte in Phase 3

</specifics>

<deferred>
## Deferred Ideas

- **META-11 (`/elvis-pattern-assimilation`)** — weiterhin v2. Kein Command nötig solange der Skill nicht existiert.
- **Command-Template** — Falls in Zukunft >20 Commands existieren, könnte ein formales Template sinnvoll sein. Aktuell bei 10 Commands nicht nötig.

</deferred>

---

*Phase: 03-command-layer*
*Context gathered: 2026-03-14*
