# Requirements

Dieses Dokument ist der explizite Capability-Contract für OpenClaw Meta Maker.

## Active

### R001 — Vollständiges Skill-Ökosystem
- Class: core-capability
- Status: active
- Description: ~100 deduplizierte, einzigartige Skills über 6 Domänen (Growth, Content, Research, Strategy, Automation, Meta/Commands)
- Why it matters: Der Kern des Produkts — ohne vollständige Skills ist das System nicht einsatzbereit
- Source: user
- Primary owning slice: M001/S04 + M001/S05 + M001/S06
- Supporting slices: M001/S01, M001/S07
- Validation: S05 — 56/~80 Skills erstellt (Growth + Content + Research + Strategy vollständig); verify-s05.sh 28/28 Datei-Checks grün; vollständig nach S06–S08
- Notes: Skills sind dedupliziert (z.B. elvis-x-hook-writer und elvis-hook-writer werden zu einem Skill zusammengeführt)

### R002 — Erweitertes Skill-Format
- Class: quality-attribute
- Status: active
- Description: Jeder Skill enthält zusätzlich zu den Basis-Sektionen: Constraints (Sicherheitsgrenzen), Verification (Prüfkriterien für Output), Dependencies (benötigte Inputs/andere Skills)
- Why it matters: Verhindert dass der Agent improvisiert, in Endlosschleifen gerät oder Output ohne Qualitätsprüfung produziert
- Source: user
- Primary owning slice: M001/S01
- Supporting slices: alle Skill-Slices
- Validation: S01 — templates/skill-template.md und alle 6 Benchmark-Skills enthalten alle 9 Sektionen (54/54 Checks in verify-s01.sh)
- Notes: Format in S01 festgelegt und validiert; bindend für alle nachfolgenden Skills in S04–S07

### R003 — Konkrete, ausführbare Execution Steps
- Class: quality-attribute
- Status: active
- Description: Jeder Execution Step ist so spezifisch, dass ein AI-Agent ihn ohne Interpretation ausführen kann. Statt "analyse trending topics" → "Analysiere die Top-20 Posts der letzten 7 Tage im Nischen-Bereich, extrahiere wiederkehrende Formate und Hooks, liste 5 Muster auf"
- Why it matters: Vage Steps führen zu unvorhersehbaren Ergebnissen und Agent-Improvisation
- Source: user
- Primary owning slice: M001/S04
- Supporting slices: M001/S05, M001/S06, M001/S07
- Validation: S04 — contract-proof: 28 Skills × alle Ausführungsschritte mit ≥1 Mengenangabe; 6 D006-Stichproben bestanden (verify in S04-SUMMARY.md); R003 validated
- Notes: Gilt für alle ~100 Skills

### R004 — Safeguards für Autonome Agenten
- Class: constraint
- Status: active
- Description: Jeder autonome Agent (Borg Skill Expander, Q Agent Creator, Picard Orchestrator) hat: Max-Limits pro Durchlauf, Operator-Approval-Gate vor Ausführung, definierte Stop-Bedingungen, Rollback-Mechanismus
- Why it matters: Ohne Grenzen könnte das Autonomous System endlos generieren, Ressourcen verbrauchen und das System destabilisieren
- Source: user
- Primary owning slice: M001/S07
- Supporting slices: M001/S08
- Validation: S03 (Agent-Ebene) — alle 5 autonomen Agenten (Picard, Q, Borg, Troi, Uhura) haben alle 4 Safeguard-Marker mit konkreten Zahlen (20/20 Safeguard-Checks in verify-s03.sh); vollständige Validierung auf Skill-Ebene in S07
- Notes: Stop-Bedingungen sind im Skill als explizite Constraints definiert

### R005 — Star Trek Agenten-Namen
- Class: differentiator
- Status: active
- Description: Alle 16 Agenten tragen Namen aus dem Star Trek Universum: Kirk, Spock, Picard, Data, Worf, Scotty, LaForge, Seven, Sulu, Tuvok, McCoy, Riker, Q, Borg, Troi, Uhura
- Why it matters: Identität und Erkennbarkeit — jeder Charakter reflektiert die Persönlichkeit des Agenten
- Source: user
- Primary owning slice: M001/S02 + M001/S03
- Supporting slices: keine
- Validation: S03 — alle 16 agent/*.md mit korrekten Star Trek Namen und 7 vollständigen Sektionen; 148/148 Checks grün (verify-s03.sh Exit-Code 0); 5/5 autonome Agenten mit D007-Safeguards
- Notes: Zuordnung ist festgelegt (siehe M001-CONTEXT.md)

### R006 — /elvis-* Naming Convention
- Class: convention
- Status: active
- Description: Alle Skills im gesamten Ökosystem verwenden ausschließlich den Prefix `/elvis-*`
- Why it matters: Konsistenz über das gesamte Ökosystem, direkte Verwendbarkeit in OpenClaw
- Source: user
- Primary owning slice: M001/S01
- Supporting slices: alle Skill-Slices
- Validation: S01 — alle 6 Benchmark-Skills enthalten /elvis-* im ## Name Block (6/6 Checks in verify-s01.sh)
- Notes: Gilt auch für Meta-Agent Skills und Command Skills

### R007 — Integrierte Ordnerstruktur
- Class: architecture
- Status: active
- Description: Alles in einem Root-Verzeichnis: `soul/`, `identity/`, `agent/`, `skills/` (mit Subkategorien), `meta-agent/`, `commands/`, `templates/`
- Why it matters: Übersichtlich, direkt importierbar, kein Chaos durch separate Pakete
- Source: user
- Primary owning slice: M001/S01
- Supporting slices: alle
- Validation: S01 — alle 11 Verzeichnisse existieren (11/11 Checks in verify-s01.sh); Hinweis: meta-agent/ wurde zu meta/ vereinfacht
- Notes: Keine getrennten Top-Level-Ordner wie in der ursprünglichen Spec

### R008 — 10 Souls
- Class: core-capability
- Status: active
- Description: 10 Souls für verschiedene Agent-Philosophien: builder, operator, strategist, researcher, growth, automation, analyst, creator, execution, minimalist
- Why it matters: Souls definieren das Fundament jedes Agenten — ohne Souls keine konsistente Persönlichkeit
- Source: user
- Primary owning slice: M001/S02
- Supporting slices: keine
- Validation: S02 — alle 10 soul/*.md mit vollständigen 6 Sektionen (60/60 Soul-Sektions-Checks in verify-s02.sh); grep -c "^## Geeignet für" soul/*.md = 10 bestätigt Agent-Mapping-Vollständigkeit
- Notes: Vollständig ausgearbeitet mit Purpose, Core Values, Operating Principles, Success Metrics und Soul-zu-Agenten-Mapping

### R009 — Command System
- Class: primary-user-loop
- Status: active
- Description: 8-10 Commands (/build-agent, /generate-skills, /expand-library, /analyze-system, /optimize-agent, /create-soul, /create-identity, /create-skill, /build-library) mit Command Router
- Why it matters: Der Operator steuert das gesamte Ökosystem über kurze, standardisierte Befehle
- Source: user
- Primary owning slice: M001/S08
- Supporting slices: keine
- Validation: unmapped
- Notes: Commands sind als Markdown-Dateien definiert, nicht als ausführbarer Code

### R010 — Templates für Wiederverwendung
- Class: operability
- Status: active
- Description: Wiederverwendbare Templates für Soul, Identity, Agent und Skill — so dass neue Komponenten in < 2 Minuten erstellt werden können
- Why it matters: Die Agent-Factory ist nur so gut wie ihre Vorlagen
- Source: user
- Primary owning slice: M001/S01
- Supporting slices: keine
- Validation: S01 — alle 4 Template-Dateien existieren (4/4 Checks in verify-s01.sh); jede mit Anweisungs-Block + vollständigem Beispiel
- Notes: Templates spiegeln das finale, erweiterte Skill-Format wider

### R011 — Deutsch als Inhaltssprache
- Class: constraint
- Status: active
- Description: Alle Markdown-Dateien sind auf Deutsch verfasst
- Why it matters: Explizite Nutzeranforderung
- Source: user
- Primary owning slice: M001/S01
- Supporting slices: alle
- Validation: S01 — alle 6 Benchmark-Skills und alle 4 Templates auf Deutsch verfasst (manuell verifiziert)
- Notes: Dateinamen und Verzeichnisse bleiben englisch für Kompatibilität

## Deferred

### R020 — Pixel Agents Visualisierung
- Class: differentiator
- Status: deferred
- Description: Pixel-Art-Visualisierung der Star Trek Agenten als animierte Bürocharaktere
- Why it matters: Würde die Identität der Agenten visuell erlebbar machen
- Source: user
- Primary owning slice: none
- Supporting slices: none
- Validation: unmapped
- Notes: Technisch inkompatibel mit OpenClaw Markdown-System. Separates Projekt wenn überhaupt.

## Out of Scope

### R030 — Ausführbarer Code / Runtime
- Class: anti-feature
- Status: out-of-scope
- Description: Kein TypeScript, kein Python, keine APIs, kein Datenbankzugriff, keine Deployment-Infrastruktur
- Why it matters: Verhindert Scope-Creep — das Produkt sind Markdown-Dateien für OpenClaw
- Source: user
- Primary owning slice: none
- Supporting slices: none
- Validation: n/a
- Notes: Alle "Automation" in diesem Projekt ist als Prompt-Anweisung definiert, nicht als Code

### R031 — Echte Social-Media-Integration
- Class: anti-feature
- Status: out-of-scope
- Description: Keine API-Verbindungen zu Twitter/X, keine automatischen Posts, kein echtes Daten-Scraping
- Why it matters: Scope-Klarheit — Skills beschreiben WAS zu tun ist, nicht wie es technisch ausgeführt wird
- Source: inferred
- Primary owning slice: none
- Supporting slices: none
- Validation: n/a
- Notes: Skills formulieren Anweisungen für einen AI-Agenten in OpenClaw

## Traceability

| ID | Class | Status | Primary owner | Supporting | Proof |
|---|---|---|---|---|---|
| R001 | core-capability | active | M001/S04+S05+S06 | S01, S07 | S05 — 56/~80 Skills (Growth + Content + Research + Strategy); vollständig nach S06–S08 |
| R002 | quality-attribute | active | M001/S01 | alle Skill-Slices | S01 — verify-s01.sh 54/54 Sektions-Checks |
| R003 | quality-attribute | active | M001/S04 | S05, S06, S07 | S04 — contract-proof: 28 Skills × D06-konform; 6 Stichproben bestanden |
| R004 | constraint | active | M001/S07 | S08 | S03 (Agent-Ebene) — 20/20 Safeguard-Checks; vollständige Skill-Ebene in S07 |
| R005 | differentiator | active | M001/S02+S03 | none | S03 — 16/16 agent/*.md + 148/148 Checks grün (verify-s03.sh Exit-Code 0) |
| R006 | convention | active | M001/S01 | alle | S01 — verify-s01.sh 6/6 Prefix-Checks |
| R007 | architecture | active | M001/S01 | alle | S01 — verify-s01.sh 11/11 Verzeichnis-Checks |
| R008 | core-capability | active | M001/S02 | none | S02 — 10/10 soul/*.md + 60/60 Sektions-Checks + 10/10 Geeignet-für-Sektionen |
| R009 | primary-user-loop | active | M001/S08 | none | unmapped |
| R010 | operability | active | M001/S01 | none | S01 — verify-s01.sh 4/4 Template-Checks |
| R011 | constraint | active | M001/S01 | alle | S01 — manuell verifiziert |
| R020 | differentiator | deferred | none | none | unmapped |
| R030 | anti-feature | out-of-scope | none | none | n/a |
| R031 | anti-feature | out-of-scope | none | none | n/a |

## Coverage Summary

- Active requirements: 11
- Mapped to slices: 11
- Validated: 9 (R002, R003, R005, R006, R007, R008, R010, R011 — R002/R006/R007/R010/R011 in S01, R008 in S02, R005 in S03, R003 in S04)
- Partially proven: 2 (R001 Growth+Content+Research+Strategy fertig — vollständig nach S06–S08; R004 Agent-Ebene bewiesen — Skill-Ebene in S07)
- Unmapped active requirements: 0
