# Phase 1: Generators + Router - Context

**Gathered:** 2026-03-14
**Status:** Ready for planning

<domain>
## Phase Boundary

4 neue Meta-Skills erstellen: `/elvis-soul-generator`, `/elvis-identity-generator`, `/elvis-agent-generator`, `/elvis-command-router`. Alle mit vollständigem Safeguard-Quartet (SAFE-01–04). Kein Command-System (Phase 3), keine Composition-Skills (Phase 2).

</domain>

<decisions>
## Implementation Decisions

### Generator-Granularität
- Soul-Generator: 1 Soul pro Aufruf. Souls sind philosophische Grundlagen — Qualität > Quantität. Kein Batch-Modus.
- Identity-Generator: 1 Identity pro Aufruf. Identities haben zu viele Nuancen (Charakter, Kommunikationsstil, Stärken/Schwächen) für sinnvolles Batching.
- Agent-Generator: 1 Agent pro Aufruf. Agents referenzieren Souls und Skills — jede Referenz muss valide sein, das erfordert Einzelprüfung.
- Begründung: Der Skill-Generator macht Batch (max 10), weil Skills kompakter und gleichförmiger sind. Souls/Identities/Agents sind inhaltlich dichter — Batch würde zu Qualitätsverlust führen.

### Router-Verhalten
- `/elvis-command-router` arbeitet mit einer statischen Routing-Tabelle: Anfrage-Keyword → Agent + Skill-Chain.
- Routing-Tabelle ist explizit im Skill-Body definiert — kein intelligentes Matching, kein NLP. Operator sieht die Tabelle und weiß was passiert.
- Bei mehrdeutigen Anfragen: Router listet die 2-3 passendsten Routen und fragt den Operator welche gemeint ist. Kein automatisches Raten.
- Bei unbekannten Anfragen: Router gibt "Keine Route gefunden" aus + zeigt die vollständige Routing-Tabelle als Hilfe.
- Die Routing-Tabelle referenziert die Commands aus Phase 3. Der Router selbst ist unabhängig von den Command-Dateien — er KENNT die Routes, die Commands sind die formale Deklaration davon.

### Safeguard-Abstufung
- Alle 4 Safeguards (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback) sind Pflicht für JEDEN Meta-Skill — keine Ausnahmen, keine Abstufung.
- Begründung: Konsistenz ist wichtiger als Minimalismus. Wenn ein Generator nur 1 Entity pro Aufruf macht, ist das Max-Limit eben 1 — aber es steht explizit drin.
- Approval-Gate MUSS als nummerierter Ausführungsschritt erscheinen (nicht nur in Einschränkungen). Research-Finding: Approval-Gates nur in Einschränkungen werden von LLMs als passive Hinweise interpretiert, nicht als Halt-Punkte.
- Konkrete Werte: Soul-Generator Max-Limit = 1, Identity-Generator Max-Limit = 1, Agent-Generator Max-Limit = 1, Command-Router Max-Limit = 5 Routing-Entscheidungen pro Durchlauf.

### Orchestrierung & Skill-Kommunikation
- Jeder Generator-Skill dokumentiert explizit in "Abhängigkeiten" welche Vorgänger-Skills empfohlen sind.
- Output-Format jedes Generators ist so definiert, dass der nächste Skill in der Chain ihn direkt konsumieren kann.
- Dependency-Chain für Phase 2: Agent-Creator → braucht Outputs von Soul-Generator + Identity-Generator + Agent-Generator. Diese Chain muss in den Abhängigkeiten sauber dokumentiert sein.
- Command-Router referenziert ALLE Meta-Skills in seiner Routing-Tabelle — er ist der Knotenpunkt der das System zusammenhält.

### Claude's Discretion
- Exakte Formulierungen der Ausführungsschritte (solange D006-konform: Menge, Format, Zeitangabe)
- Reihenfolge der Ausführungsschritte innerhalb jedes Generators
- Verifikations-Kriterien im Detail (solange Failure-Indikator und Akzeptanzkriterium enthalten)

</decisions>

<specifics>
## Specific Ideas

- Orientierung am bestehenden `/elvis-skill-generator` als Gold-Standard für Format und Safeguard-Tiefe
- User-Zitat: "Keine Chaos, dauerhaft funktional, Orchestrierung wichtig, Kommunikation zwischen Skills sicherstellen"
- Jeder Generator muss Template-konform generieren (soul-template.md, identity-template.md, agent-template.md)
- Alle generierten Entities müssen valide Querverweise haben (Agent → Soul, Agent → Skills)

</specifics>

<code_context>
## Existing Code Insights

### Reusable Assets
- `templates/soul-template.md`: Bindende Vorlage für Soul-Generator Output (6 Sektionen: Name, Philosophie, Core Values, Operating Principles, Success Metrics, Geeignet für)
- `templates/identity-template.md`: Bindende Vorlage für Identity-Generator Output (7 Sektionen: Name, Charakter-Beschreibung, Persönlichkeitsmerkmale, Kommunikationsstil, Stärken, Schwächen, Star Trek Referenz)
- `templates/agent-template.md`: Bindende Vorlage für Agent-Generator Output (7 Sektionen: Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills)
- `skills/meta/elvis-skill-generator.md`: Referenz-Implementierung für Meta-Skills — exaktes Safeguard-Pattern (Plan→Approve→Execute)

### Established Patterns
- 9-Sektionen-Format für Skills (Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output)
- D006-Konformität: Konkrete Mengen, Formate, Zeitangaben in Ausführungsschritten
- Safeguard-Quartet: Max-Limit, Approval-Gate, Stop-Bedingung, Rollback-Hinweis
- `/elvis-*` Naming Convention
- Deutsch mit englischen Fachbegriffen

### Integration Points
- Generierte Souls → referenziert von Agent-Definitionen (`soul/[name].md`)
- Generierte Identities → parallel zu Agent-Definitionen (`identity/[name].md`)
- Generierte Agents → referenzieren Souls und Skills
- Command-Router → referenziert alle Meta-Skills in Routing-Tabelle → wird von Phase 3 Commands formalisiert

</code_context>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 01-generators-router*
*Context gathered: 2026-03-14*
