# Phase 2: Composition + Autonomous - Context

**Gathered:** 2026-03-14
**Status:** Ready for planning

<domain>
## Phase Boundary

7 neue Meta-Skills erstellen: `/elvis-agent-creator`, `/elvis-skill-expander`, `/elvis-system-analyzer`, `/elvis-library-manager`, `/elvis-ecosystem-health`, `/elvis-agent-optimizer`, `/elvis-concept-design`. Alle mit vollständigem Safeguard-Quartet (SAFE-01–04 Pattern aus Phase 1). META-11 (`/elvis-pattern-assimilation`) wird nach v2 verschoben. Kein Command-System (Phase 3).

</domain>

<decisions>
## Implementation Decisions

### Scope-Bereinigung META-10/11
- **META-11 (`/elvis-pattern-assimilation`) → v2 verschoben.** Begründung: Kein konkreter Use Case identifiziert. "Patterns aus externen Quellen assimilieren" ist zu vage für einen robusten Skill. Borg hat bereits `/elvis-skill-expander` für interne Erweiterung — externe Assimilation braucht erst einen definierten Workflow mit klaren Input-Formaten. STATE.md Blocker bestätigt.
- **META-10 (`/elvis-agent-optimizer`) → bleibt in v1.** Begründung: Natürlicher Complement zu Agent-Creator. Bestehende Agenten verbessern ist ein klarer, abgrenzbarer Use Case: Agent-Definition lesen → Schwächen identifizieren (fehlende Skills, schwache Constraints, veraltete Soul-Referenzen) → optimierte Version vorschlagen. Scope: nur Agent-Definitionen optimieren, keine Souls/Identities/Skills.
- **META-12 (`/elvis-concept-design`) → bleibt in v1.** Q's Kernfähigkeit: neue Agent-Konzepte entwerfen und validieren bevor sie gebaut werden. Klarer Use Case als Vorstufe zu Agent-Creator.

### Agent-Creator Workflow (META-04)
- **Orchestrierungsmodell:** Sequentieller 3-Phasen-Workflow mit einem einzigen Approval-Gate nach der Planungsphase. Nicht 3 separate Approval-Gates pro Generator — das würde den <2-Minuten-Constraint brechen.
- **Workflow-Schritte:**
  1. Anforderung lesen → Gesamtkonzept entwerfen (Soul-Typ, Identity-Charakter, Agent-Mission, Skill-Set)
  2. [APPROVAL-GATE] Kompletten Plan präsentieren — auf Bestätigung warten
  3. Soul generieren (intern, nach soul-template.md)
  4. Identity generieren (intern, nach identity-template.md)
  5. Agent generieren (intern, nach agent-template.md, mit validen Querverweisen)
  6. Komplettes Paket präsentieren — auf Freigabe oder Korrektur warten
- **Begründung Single-Approval:** Phase-1-Generatoren haben je einen eigenen Approval-Gate. Agent-Creator ORCHESTRIERT diese — er nutzt die Generatoren als interne Referenz, nicht als separate Aufrufe. Ein Approval auf Gesamtkonzept-Ebene ist robuster als 3 Einzel-Approvals die den Flow fragmentieren.
- **<2 Minuten Constraint:** Bezieht sich auf die Operator-Interaktion (Anforderung → fertiger Agent). Die LLM-Generierung selbst zählt nicht — der Operator wartet nur einmal (am Approval-Gate) und einmal am Ende (Freigabe).
- **Output:** 3 zusammengehörige Markdown-Dateien (soul/, identity/, agent/) + Zusammenfassung mit Speicher-Hinweisen.

### Autonome Skills — Analysetiefe
- **System-Analyzer (Troi, META-06):** Detaillierter Report mit benannten Lücken, konkreten Empfehlungen und Schweregrad-Einstufung (kritisch/mittel/niedrig). Kein oberflächlicher Scan — Troi's Wert liegt in der Tiefe der Kontext-Analyse. Output: strukturierter Gesundheitsbericht mit Handlungsempfehlungen.
- **Skill-Expander (Borg, META-05):** Generiert neue Skill-Varianten mit konkreten Sub-Skill-Referenzen in jedem Ausführungsschritt. Nicht nur "Variante A, B, C" als Liste — jede Variante ist eine vollständige 9-Sektionen-Skill-Definition. Borg arbeitet wie der Skill-Generator, aber ausgehend von einem bestehenden Skill als Basis.
- **Library-Manager (Uhura, META-07):** Produziert kategorisierten, durchsuchbaren Katalog. Nicht nur Auflistung — aktive Strukturierung mit Kategorie-Tags, Abhängigkeits-Graph und Vollständigkeits-Check. Output: Katalog-Datei die als Nachschlagewerk nutzbar ist.
- **Ecosystem-Health (META-09):** Quantitativer Gesundheits-Score (0-100) mit benannten Issues. Prüft: Template-Konformität aller Skills, Querverweis-Integrität (Soul→Agent, Agent→Skills), Safeguard-Vollständigkeit, Kategorie-Balance. Unterschied zu System-Analyzer: Health ist ein schneller Check mit Score, Analyzer ist eine tiefe Kontext-Analyse.
- **Agent-Optimizer (META-10):** Liest bestehende Agent-Definition → identifiziert konkrete Schwächen (fehlende Skills, schwache Constraints, veraltete Referenzen) → generiert optimierte Version. Ein Agent pro Durchlauf — Optimierung braucht Tiefe.
- **Concept-Design (Q, META-12):** Entwirft und validiert neue Agent-Konzepte als Vorstufe zum Agent-Creator. Output: Konzept-Dokument mit Mission, empfohlenem Soul, Skill-Bedarf und Machbarkeits-Einschätzung. Kein fertiger Agent — nur die validierte Blaupause.

### Max-Limits Phase 2
- **Agent-Creator (Q):** Max. 1 kompletter Agent pro Durchlauf. Multi-Step-Workflow (Soul+Identity+Agent) erfordert volle Aufmerksamkeit. Batch wäre unverantwortlich.
- **Skill-Expander (Borg):** Max. 5 neue Skill-Varianten pro Durchlauf. Konsistent mit bestehender Borg Agent-Definition (Constraints: "Maximal 5 neue Skills pro Durchlauf").
- **System-Analyzer (Troi):** Max. 1 vollständige System-Analyse pro Durchlauf. Konsistent mit bestehender Troi Agent-Definition.
- **Library-Manager (Uhura):** Max. 10 Library-Änderungen pro Durchlauf. Konsistent mit bestehender Uhura Agent-Definition.
- **Ecosystem-Health:** Max. 1 Health-Check pro Durchlauf. Ein Check = ein vollständiger Scan des gesamten Ökosystems.
- **Agent-Optimizer:** Max. 1 Agent-Optimierung pro Durchlauf. Tiefe Analyse erfordert Einzelbehandlung.
- **Concept-Design (Q):** Max. 1 Konzept pro Durchlauf. Konzeptvalidierung braucht sorgfältige Prüfung gegen bestehendes Ökosystem.
- **Begründung:** Max-Limits orientieren sich an den bestehenden Agent-Definitionen (borg.md, troi.md, uhura.md, q.md) — Konsistenz mit dem was die Agenten bereits versprechen.

### Safeguard-Pattern (aus Phase 1 übernommen)
- Identisches Safeguard-Quartet wie Phase 1 — keine Abstufung, keine Ausnahmen.
- Approval-Gate MUSS als nummerierter Ausführungsschritt erscheinen mit "warte auf" Formulierung.
- Zwei Stop-Bedingungen pro Skill: regulär + vorzeitig.
- Rollback als konkrete Operator-Anweisung, nicht als Prinzip.
- Agent-Creator hat nur EINEN Approval-Gate (nach Gesamtplan), nicht drei separate.

### Claude's Discretion
- Exakte Formulierungen der Ausführungsschritte (solange D006-konform)
- Reihenfolge der Ausführungsschritte innerhalb jedes Skills
- Interne Struktur des Ecosystem-Health-Scores (Gewichtung der Kategorien)
- Genaues Format des Library-Manager-Katalogs (solange durchsuchbar und kategorisiert)
- Verifikations-Kriterien im Detail (solange Failure-Indikator und Akzeptanzkriterium enthalten)

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `skills/meta/elvis-skill-generator.md`: Gold-Standard für Safeguard-Quartet Pattern — direkte Vorlage für alle 7 neuen Skills
- `skills/meta/elvis-soul-generator.md`: Phase-1 Generator mit Plan→Approve→Execute — Vorlage für Agent-Creator Sub-Workflows
- `skills/meta/elvis-identity-generator.md`: Phase-1 Generator — Agent-Creator referenziert diesen intern
- `skills/meta/elvis-agent-generator.md`: Phase-1 Generator mit Querverweisvalidierung — Agent-Creator und Agent-Optimizer nutzen dieses Pattern
- `skills/meta/elvis-command-router.md`: Routing-Tabelle muss nach Phase 2 um alle neuen Skills erweitert werden

### Established Patterns
- 9-Sektionen-Format bindend für alle neuen Skills
- D006-Konformität: Konkrete Mengen, Formate, Zeitangaben in Ausführungsschritten
- Safeguard-Quartet: Max-Limit, Approval-Gate (nummerierter Schritt), Stop-Bedingung, Rollback
- `/elvis-*` Naming Convention
- Deutsch mit englischen Fachbegriffen
- Approval-Gate als Halt-Punkt mit "warte auf explizite Bestätigung"

### Integration Points
- Agent-Creator → nutzt Phase-1-Generatoren als interne Referenz (soul-template, identity-template, agent-template)
- Skill-Expander → braucht Zugriff auf bestehende Skills als Basis für Varianten
- System-Analyzer → scannt alle Verzeichnisse (skills/, agent/, soul/, identity/)
- Library-Manager → verwaltet skills/ Verzeichnisstruktur
- Ecosystem-Health → Querverweis-Prüfung über alle Entity-Typen
- Agent-Optimizer → liest agent/ Definitionen + prüft Soul/Skill-Referenzen
- Command-Router (Phase 1) → Routing-Tabelle muss alle neuen Phase-2-Skills aufnehmen (Update in Phase 2 oder Phase 3)

### Agent-Definitionen als Referenz
- `agent/q.md`: Q's Capabilities und Operating Loop definieren den Rahmen für Agent-Creator + Concept-Design
- `agent/borg.md`: Borg's Operating Loop definiert den Rahmen für Skill-Expander
- `agent/troi.md`: Troi's Operating Loop definiert den Rahmen für System-Analyzer
- `agent/uhura.md`: Uhura's Operating Loop definiert den Rahmen für Library-Manager

</code_context>

<specifics>
## Specific Ideas

- User-Anweisung: "Best Practice und State of the Art, langlebiger und fehlerfreier Betrieb"
- Max-Limits orientieren sich an bestehenden Agent-Definitionen — keine willkürlichen Zahlen
- Agent-Creator Single-Approval statt Triple-Approval für Flow-Effizienz
- Ecosystem-Health als quantitativer Quick-Check, System-Analyzer als qualitative Deep-Dive — klare Arbeitsteilung
- META-11 Verschiebung nach v2 ist konservativ-korrekt: besser kein Skill als ein vager Skill

</specifics>

<deferred>
## Deferred Ideas

- **META-11 (`/elvis-pattern-assimilation`)** — nach v2 verschoben. Braucht erst definierte Input-Formate für externe Quellen. Borg hat intern bereits Skill-Expander.
- **Command-Router Update** — Routing-Tabelle um Phase-2-Skills erweitern. Gehört logisch zu Phase 3 (Command Layer) oder als separater Update-Task.

</deferred>

---

*Phase: 02-composition-autonomous*
*Context gathered: 2026-03-14*
