# Phase 4: Integration Fixes + Tech Debt - Context

**Gathered:** 2026-03-14
**Status:** Ready for planning
**Source:** v1.0-MILESTONE-AUDIT.md gap closure

<domain>
## Phase Boundary

Alle Wiring-Inkonsistenzen aus dem Milestone-Audit bereinigen. Keine neuen Features, keine neuen Skills. Nur Korrekturen und Dokumentationsergänzungen an bestehenden Dateien.

Scope: 6 Dateien in skills/meta/, 3 Dateien in commands/, 1 neue Datei in commands/

</domain>

<decisions>
## Implementation Decisions

### INT-01: Agent-Zuweisung create-soul/create-identity
- Router-Tabelle sagt Picard, Commands sagen Elvis
- Entscheidung: Commands sind korrekt (Elvis ist der kreative Agent für Generatoren) — Router-Tabelle korrigieren
- Zeilen 1-2 der Router-Tabelle: Picard → Elvis für Soul/Identity-Generierung

### INT-02: Soul-Sektionsnamen in ecosystem-health
- elvis-ecosystem-health Step 2 prüft Agent-Sektionsnamen statt Soul-Sektionsnamen
- Korrekte Soul-Sektionen: Name, Philosophie, Core Values, Operating Principles, Success Metrics, Geeignet für
- Nur Step 2 ändern, Rest des Skills bleibt unverändert

### Agent-Creator Generator-Bypass Dokumentation
- elvis-agent-creator implementiert Generator-Logik intern — by design
- Abhängigkeiten-Abschnitt muss dies explizit dokumentieren
- Kein funktionaler Change, nur Klarstellung

### Agent-Optimizer Scope-Widerspruch
- Step 2c prüft Soul-Referenz-Plausibilität, aber Scope verbietet soul/*.md Zugriff
- Lösung: Step 2c klarstellen dass Plausibilitätsprüfung nur via Namenskonvention erfolgt (kein Dateizugriff)

### Fehlender Command für concept-design
- Alle Phase-2-Skills haben Commands ausser concept-design
- Neuen Command commands/design-concept.md erstellen
- Agent: Q, Skill-Chain: /elvis-concept-design

### generate-skills Dual-Agent Dokumentation
- commands/generate-skills.md hat Split-Agent aber Router hat zwei separate Einträge
- Hinweis-Feld in generate-skills.md erweitern um UX-Klarstellung

### Claude's Discretion
- Exakte Formulierungen der Dokumentationsergänzungen
- Ob Router-Tabelle einen neuen Eintrag für concept-design braucht (ja — Konsistenz)

</decisions>

<specifics>
## Specific References

- v1.0-MILESTONE-AUDIT.md: INT-01, INT-02, tech_debt items
- templates/soul-template.md: Authoritative source für Soul-Sektionsnamen
- skills/meta/elvis-ecosystem-health.md: Step 2 Soul-Check
- skills/meta/elvis-command-router.md: Routing-Tabelle Zeilen 1-2
- commands/create-soul.md, commands/create-identity.md: Agent-Feld
- skills/meta/elvis-agent-creator.md: Abhängigkeiten-Abschnitt
- skills/meta/elvis-agent-optimizer.md: Step 2c + Einschränkungen

</specifics>

<deferred>
## Deferred Ideas

- META-11 (/elvis-pattern-assimilation) — v2, kein aktueller Use Case

</deferred>

---

*Phase: 04-integration-fixes*
*Context gathered: 2026-03-14 via Milestone Audit gap closure*
