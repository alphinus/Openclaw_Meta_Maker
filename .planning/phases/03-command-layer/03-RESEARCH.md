# Phase 3: Command Layer - Research

**Researched:** 2026-03-14
**Domain:** Markdown-based command routing declarations + routing table extension
**Confidence:** HIGH

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**Command-Datei Format**
- Minimale Routing-Deklaration — Command-Dateien sind KEINE Skills (kein 9-Sektionen-Format, keine Ausführungsschritte, keine Safeguards). Sie sind reine Routing-Deklarationen mit maximal 5 Feldern:
  1. **Command** — Der Aufruf-Name (z.B. `/build-agent`)
  2. **Beschreibung** — 1 Satz was der Command tut (für den Operator als Hilfe)
  3. **Agent** — Welcher Agent zuständig ist (z.B. Q, Borg, Picard)
  4. **Skill-Chain** — Welche `/elvis-*` Skills aufgerufen werden (geordnete Liste)
  5. **Hinweis** — Optional: Kontext-Info (z.B. "Erstellt Soul + Identity + Agent als Paket")
- Begründung: Success Criterion 4 ist explizit: "Kein Command-File enthält Ausführungslogik — jedes File ist eine reine Routing-Deklaration." Jede Logik gehört in den Skill, nicht in den Command.
- Kein Template nötig: Commands sind zu minimal für ein Template. Das Format ist in 10 Zeilen definiert und konsistent über alle 10 Dateien.
- Sprache: Deutsch mit englischen Fachbegriffen (konsistent mit dem gesamten Projekt).

**Verzeichnisstruktur**
- Neues `commands/` Verzeichnis auf Root-Ebene — parallel zu `skills/`, `agent/`, `soul/`, `identity/`.
- Begründung: Commands sind eine eigene Entity-Klasse im Ökosystem (wie Skills, Agents, Souls, Identities). Sie in `skills/meta/` unterzubringen wäre semantisch falsch — Commands sind keine Skills. Ein eigenes Verzeichnis ist konsistent mit der bestehenden Architektur.
- Dateinamen: `{command-name}.md` ohne Präfix. Beispiel: `commands/build-agent.md`, `commands/create-soul.md`.
- Kein Unterverzeichnis: 10 Dateien sind flach organisierbar. Keine Kategorie-Ordner nötig.

**Router-Update**
- Ja — als Teil von Phase 3. Die Routing-Tabelle im `/elvis-command-router` wird von 4 auf 12+ Einträge erweitert.
- Neue Einträge für Phase-2-Skills:
  - Agent zusammenstellen → Q → /elvis-agent-creator
  - Skills erweitern, Varianten → Borg → /elvis-skill-expander
  - System analysieren, Schwächen → Troi → /elvis-system-analyzer
  - Library verwalten, Katalog → Uhura → /elvis-library-manager
  - Gesundheitscheck, Health → Picard → /elvis-ecosystem-health
  - Agent optimieren → Picard → /elvis-agent-optimizer
  - Konzept entwerfen → Q → /elvis-concept-design
- Hinweis in Routing-Tabelle entfernen: "Hinweis: Diese Tabelle wird in Phase 2 um weitere Meta-Skills erweitert" → ersetzen durch aktuelle, vollständige Tabelle.

**CMD-10 Abgrenzung (`/route-command`)**
- CMD-10 ist ein Alias/Redirect zum bestehenden `/elvis-command-router`. Keine eigene Logik, kein Wrapper.
- Die Command-Datei `commands/route-command.md` routet einfach zu: Agent: Picard → Skill-Chain: /elvis-command-router.
- Begründung: Der Router existiert bereits als vollständiger Skill (META-08, Phase 1). CMD-10 als eigenständiger Skill wäre Duplikation. Als Command-Datei ist `/route-command` konsistent mit den anderen 9 Commands — ein Shortcut, kein neues Feature.
- Praktischer Nutzen: User kann `/route-command` oder `/elvis-command-router` verwenden — beide führen zum selben Ergebnis. `/route-command` ist der einprägsame Shortcut, `/elvis-command-router` ist der technische Skill-Name.

### Claude's Discretion
- Exakte Formulierung der Beschreibungs-Zeile in jeder Command-Datei
- Reihenfolge der Erstellung der 10 Command-Dateien
- Ob der optionale "Hinweis"-Abschnitt in jeder Command-Datei enthalten ist oder nur bei komplexeren Chains
- Genaue Keywords in der erweiterten Routing-Tabelle (solange eindeutig und konsistent)

### Deferred Ideas (OUT OF SCOPE)
- META-11 (`/elvis-pattern-assimilation`) — weiterhin v2. Kein Command nötig solange der Skill nicht existiert.
- Command-Template — Falls in Zukunft >20 Commands existieren, könnte ein formales Template sinnvoll sein. Aktuell bei 10 Commands nicht nötig.
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| CMD-01 | `/build-agent` — Routet zu Agent Creator Workflow | Command-Datei mit 5 Feldern: Command=/build-agent, Agent=Q, Skill-Chain=/elvis-agent-creator; Q ist der definierte Agent für Agent-Erstellung (agent/q.md) |
| CMD-02 | `/generate-skills` — Routet zu Skill Generator + Expander | Command-Datei; Skill-Chain hat zwei Einträge: /elvis-skill-generator + /elvis-skill-expander (Reihenfolge: Discretion); Agent = Elvis (Skill Generator) oder Borg (Skill Expander) — Klärung unten |
| CMD-03 | `/analyze-system` — Routet zu System Analyzer | Command-Datei: Agent=Troi, Skill-Chain=/elvis-system-analyzer |
| CMD-04 | `/optimize-agent` — Routet zu Agent Optimizer | Command-Datei: Agent=Picard, Skill-Chain=/elvis-agent-optimizer |
| CMD-05 | `/manage-library` — Routet zu Library Manager | Command-Datei: Agent=Uhura, Skill-Chain=/elvis-library-manager |
| CMD-06 | `/expand-skills` — Routet zu Skill Expander | Command-Datei: Agent=Borg, Skill-Chain=/elvis-skill-expander |
| CMD-07 | `/health-check` — Routet zu Ecosystem Health | Command-Datei: Agent=Picard, Skill-Chain=/elvis-ecosystem-health |
| CMD-08 | `/create-soul` — Routet zu Soul Generator | Command-Datei: Agent=Elvis, Skill-Chain=/elvis-soul-generator |
| CMD-09 | `/create-identity` — Routet zu Identity Generator | Command-Datei: Agent=Elvis, Skill-Chain=/elvis-identity-generator |
| CMD-10 | `/route-command` — Meta-Router für alle Commands (Picard) | Alias-Command-Datei: Agent=Picard, Skill-Chain=/elvis-command-router; kein neuer Skill, reiner Shortcut |
</phase_requirements>

---

## Summary

Phase 3 ist die dünnste Schicht des gesamten Projekts. Es werden 11 Artefakte erstellt: 10 Command-Dateien im `commands/` Verzeichnis und 1 Update der Routing-Tabelle in `skills/meta/elvis-command-router.md`. Kein neuer Skill-Typ, keine neuen Ausführungslogiken, kein Template-Format. Jede Command-Datei ist maximal 10 Zeilen lang und enthält ausschließlich deklarative Felder (Command, Beschreibung, Agent, Skill-Chain, optional Hinweis).

Das einzige nicht-triviale Artefakt ist das Router-Update. Der bestehende `elvis-command-router.md` hat eine Routing-Tabelle mit 4 Einträgen (alle Phase-1-Skills). Diese muss auf 12+ Einträge erweitert werden, um alle Phase-2-Skills abzudecken. Der "Hinweis: Diese Tabelle wird in Phase 2 erweitert" muss gleichzeitig entfernt werden — er ist nach diesem Update obsolet. Die Verifikations-Sektion des Routers muss ebenfalls aktualisiert werden, da sie explizit die 4 Phase-1-Skills auflistet.

Die Command-Dateien sind konzeptuell eindeutig, aber CMD-02 (`/generate-skills`) hat eine Besonderheit: Requirements definieren "Skill Generator + Expander" als Ziel, was zwei unterschiedliche Agenten (Elvis für Skill Generator, Borg für Skill Expander) impliziert. Die empfohlene Lösung: CMD-02 routet zu beiden Skills als geordnete Skill-Chain mit Hinweis auf die Entscheidungslogik.

**Primary recommendation:** Erstelle alle 10 Command-Dateien in einem einzigen Plan-Wave. Sie sind so minimal (10 Zeilen je Datei) und voneinander unabhängig, dass Parallelisierung das Risiko von Inkonsistenz erhöht. Sequenzielle Erstellung in einem Task sichert Konsistenz in Beschreibungs-Formulierungen quer über alle 10 Commands. Router-Update als separater Task im gleichen Wave.

---

## Standard Stack

### Core — Command-Datei Format

| Komponente | Typ | Zweck | Warum bindend |
|-----------|-----|-------|---------------|
| 5-Felder-Deklaration | Markdown-Struktur | Routing-Deklaration pro Command | CONTEXT.md: explizit definiertes Format, kein Template nötig |
| `commands/` Verzeichnis | Dateisystem-Struktur | Root-Level Entity-Klasse für Commands | Konsistent mit skills/, agent/, soul/, identity/ Pattern |
| `skills/meta/elvis-command-router.md` | Bestehender Skill | Routing-Tabelle wird auf 12+ Einträge erweitert | Existiert seit Phase 1, nur Update nötig |

### Agent-Skill Zuordnungen (vollständig, verifiziert gegen agent/*.md)

| Command | Agent | Skill-Chain | Quelle |
|---------|-------|-------------|--------|
| /build-agent | Q | /elvis-agent-creator | CONTEXT.md + agent/q.md |
| /generate-skills | Elvis + Borg | /elvis-skill-generator, /elvis-skill-expander | CONTEXT.md code_context |
| /analyze-system | Troi | /elvis-system-analyzer | CONTEXT.md code_context |
| /optimize-agent | Picard | /elvis-agent-optimizer | CONTEXT.md code_context |
| /manage-library | Uhura | /elvis-library-manager | CONTEXT.md code_context |
| /expand-skills | Borg | /elvis-skill-expander | CONTEXT.md code_context |
| /health-check | Picard | /elvis-ecosystem-health | CONTEXT.md code_context |
| /create-soul | Elvis | /elvis-soul-generator | REQUIREMENTS.md + CONTEXT.md |
| /create-identity | Elvis | /elvis-identity-generator | REQUIREMENTS.md + CONTEXT.md |
| /route-command | Picard | /elvis-command-router | CONTEXT.md CMD-10 Abgrenzung |

### Router-Erweiterung — vollständige Zieltabelle (12 Einträge)

Aktuelle 4 Einträge bleiben unverändert. 7 neue Einträge aus Phase 2:

| Keyword / Anfrage-Typ | Agent | Skill-Chain |
|---|---|---|
| Soul erstellen, neue Soul, Soul generieren | Picard | /elvis-soul-generator |
| Identity erstellen, neue Identity, Identity generieren | Picard | /elvis-identity-generator |
| Agent erstellen, neuer Agent, Agent generieren | Picard | /elvis-agent-generator |
| Skills generieren, neue Skills, Skill erstellen | Elvis | /elvis-skill-generator |
| Agent zusammenstellen, vollständiger Agent, Agent Creator | Q | /elvis-agent-creator |
| Skills erweitern, Skill-Varianten, Borg | Borg | /elvis-skill-expander |
| System analysieren, Schwächen, Lücken, Troi | Troi | /elvis-system-analyzer |
| Library verwalten, Katalog, Skill-Katalog, Uhura | Uhura | /elvis-library-manager |
| Gesundheitscheck, Health-Check, System-Score | Picard | /elvis-ecosystem-health |
| Agent optimieren, Agent verbessern | Picard | /elvis-agent-optimizer |
| Konzept entwerfen, neues Konzept, Blaupause | Q | /elvis-concept-design |
| Route command, routen, welcher Agent | Picard | /elvis-command-router |

### Keine externen Abhängigkeiten

Kein Build-Prozess, keine npm-Pakete, keine API-Calls. Phase 3 ist reines Markdown-Authoring plus ein Textfile-Update.

---

## Architecture Patterns

### Empfohlene Dateistruktur (Output dieser Phase)

```
commands/                          ← NEU (10 Dateien)
├── build-agent.md                 ← CMD-01
├── generate-skills.md             ← CMD-02
├── analyze-system.md              ← CMD-03
├── optimize-agent.md              ← CMD-04
├── manage-library.md              ← CMD-05
├── expand-skills.md               ← CMD-06
├── health-check.md                ← CMD-07
├── create-soul.md                 ← CMD-08
├── create-identity.md             ← CMD-09
└── route-command.md               ← CMD-10

skills/meta/
└── elvis-command-router.md        ← UPDATE (Routing-Tabelle 4→12 Einträge)
```

### Pattern 1: Standard-Command (Single-Skill-Route)

**Was:** Eine Command-Datei mit genau einem Ziel-Skill.
**Wann verwenden:** CMD-01, CMD-03, CMD-04, CMD-05, CMD-06, CMD-07, CMD-08, CMD-09, CMD-10.

**Format:**
```markdown
# Command

## Command
/[command-name]

## Beschreibung
[1 Satz — was der Command tut, für wen er gedacht ist]

## Agent
[Agent-Name]

## Skill-Chain
- /elvis-[skill-name]

## Hinweis
[Optional — nur wenn zusätzlicher Kontext für den Operator wertvoll ist]
```

**Beispiel — CMD-08 `/create-soul`:**
```markdown
# Command

## Command
/create-soul

## Beschreibung
Generiert eine neue Soul-Definition im verbindlichen 6-Sektionen-Format.

## Agent
Elvis

## Skill-Chain
- /elvis-soul-generator
```

### Pattern 2: Multi-Skill-Chain-Command

**Was:** Eine Command-Datei mit zwei Ziel-Skills in geordneter Reihenfolge.
**Wann verwenden:** CMD-02 (`/generate-skills`) — einziger Fall in Phase 3.
**Begründung:** Requirements.md sagt explizit "Skill Generator + Expander". Zwei separate Commands (CMD-02 und CMD-06) decken verschiedene Nutzungsintentionen ab — `/generate-skills` für neue Skills, `/expand-skills` für Varianten. CMD-02 ist der breitere Einstiegspunkt.

**Format:**
```markdown
## Skill-Chain
- /elvis-skill-generator
- /elvis-skill-expander

## Hinweis
Für neue Skills: starte mit /elvis-skill-generator (Elvis). Für Varianten bestehender Skills: starte mit /elvis-skill-expander (Borg). Der /elvis-command-router hilft bei der Auswahl.
```

### Pattern 3: Alias-Command (CMD-10)

**Was:** Command-Datei die auf einen bestehenden Skill zeigt ohne neuen Skill zu erstellen.
**Wann verwenden:** Nur CMD-10 (`/route-command`).

**Format:**
```markdown
# Command

## Command
/route-command

## Beschreibung
Meta-Router für alle Commands — routet Anfragen an den richtigen Agent und Skill anhand einer statischen Routing-Tabelle.

## Agent
Picard

## Skill-Chain
- /elvis-command-router

## Hinweis
Alias für /elvis-command-router. Beide Aufrufe führen zum gleichen Ergebnis.
```

### Pattern 4: Router-Update

**Was:** Bestehende Routing-Tabelle in `skills/meta/elvis-command-router.md` erweitern.
**Zwei Stellen im Dokument müssen geändert werden:**

1. **Strategie-Abschnitt** — Routing-Tabelle von 4 auf 12 Einträge erweitern, Hinweis-Zeile entfernen:
   - Entfernen: "Hinweis: Diese Tabelle wird in Phase 2 um weitere Meta-Skills erweitert..."
   - Ersetzen durch: vollständige 12-Einträge-Tabelle (siehe Standard Stack oben)

2. **Verifikations-Abschnitt** — Akzeptanzkriterium anpassen:
   - Aktuell: "Routing-Tabelle enthält mindestens 4 Einträge, alle Phase-1-Skills"
   - Neu: "Routing-Tabelle enthält mindestens 12 Einträge, alle Phase-1- und Phase-2-Skills"
   - Verifikations-Liste der Phase-1-Skills auf alle 12 Skills erweitern

### Anti-Patterns to Avoid

- **Ausführungslogik in Command-Dateien:** Commands dürfen keine Schritte, Strategie, Einschränkungen oder Safeguards enthalten. Jede Logik gehört in den Skill. Eine Command-Datei mit Ausführungsschritten ist ungültig.
- **Command-Format wie Skill-Format:** Das 9-Sektionen-Format gilt für Skills, nicht für Commands. Commands sind 5-Felder-Deklarationen.
- **Routing-Tabelle zeigt auf Commands:** Die Tabelle in `elvis-command-router.md` zeigt auf `/elvis-*`-Skills, niemals auf Commands (`/build-agent`, `/create-soul` etc.). Commands sind Shortcuts die den Router aufrufen — nicht umgekehrt.
- **CMD-10 als neuer Skill implementieren:** CMD-10 ist eine Command-Datei die auf den bestehenden `/elvis-command-router`-Skill zeigt. Kein neuer Skill, kein Wrapper.
- **Partielles Router-Update:** Beide Stellen im Router-Skill müssen aktualisiert werden (Strategie-Tabelle + Verifikations-Abschnitt). Ein halbfertiges Update hinterlässt widersprüchliche Dokumente.

---

## Don't Hand-Roll

| Problem | Nicht neu bauen | Verwende stattdessen | Warum |
|---------|-----------------|---------------------|-------|
| CMD-10 Routing-Logik | Neuen Meta-Router-Skill erstellen | Bestehende `skills/meta/elvis-command-router.md` (META-08) als Ziel der Alias-Command | Router ist vollständig und in Phase 1 verifiziert |
| Command-Template | Formales Template-Dokument erstellen | 5-Felder-Format direkt in jede Command-Datei | Zu minimal für Template — 10 Zeilen definieren das Format vollständig |
| Agent-Zuordnungslogik | Neue Zuordnungsregeln erfinden | Bestehende Agent-Definitionen in `agent/*.md` als Referenz | Alle Zuordnungen sind in CONTEXT.md bereits festgelegt und entsprechen den Agent-Skills |

**Key insight:** Phase 3 baut keine neuen Mechanismen. Alle Routing-Entscheidungen sind bereits in CONTEXT.md festgelegt. Die Phase ist reine Formalisierung einer bestehenden impliziten Struktur.

---

## Common Pitfalls

### Pitfall 1: Command-Datei enthält Ausführungslogik

**Was schiefgeht:** Command-Datei enthält Strategie, Ausführungsschritte oder Safeguards — wie ein Skill aufgebaut.
**Warum es passiert:** Alle bisherigen Markdown-Dateien im Projekt sind entweder Skills (9 Sektionen) oder Entity-Definitionen (Agent, Soul, Identity). Das Gehirn greift zum bekannten Muster.
**Wie vermeiden:** CONTEXT.md ist explizit: "Kein Command-File enthält Ausführungslogik — jedes File ist eine reine Routing-Deklaration." Verifikation: Wenn eine Command-Datei mehr als 15 Zeilen hat, ist sie zu lang.
**Warnzeichen:** Command-Datei enthält einen der Sektions-Header: `## Strategie`, `## Ausführungsschritte`, `## Einschränkungen`, `## Verifikation`.

### Pitfall 2: Router-Update ist unvollständig

**Was schiefgeht:** Routing-Tabelle im Strategie-Abschnitt wird aktualisiert, aber Verifikations-Abschnitt referenziert noch die alten 4 Phase-1-Skills.
**Warum es passiert:** `elvis-command-router.md` hat zwei Stellen die konsistent sein müssen — Strategie (Tabelle) und Verifikation (Akzeptanzkriterium + Failure-Indikator).
**Wie vermeiden:** Router-Update als atomare Operation: beide Stellen im selben Task, verify-Schritt prüft explizit beide Stellen.
**Warnzeichen:** Verifikations-Abschnitt nennt "mindestens 4 Einträge" oder listet nur "elvis-soul-generator, elvis-identity-generator, elvis-agent-generator, elvis-skill-generator".

### Pitfall 3: CMD-02 und CMD-06 Dopplung unklar

**Was schiefgeht:** CMD-02 (`/generate-skills`) und CMD-06 (`/expand-skills`) überlappen konzeptuell. Ohne Hinweis-Feld ist nicht klar wann welcher zu verwenden ist.
**Warum es passiert:** `/elvis-skill-expander` ist bereits Teil der CMD-02 Skill-Chain laut Requirements. CMD-06 fokussiert auf denselben Skill.
**Wie vermeiden:** CMD-02 Hinweis-Feld erklärt die Abgrenzung: "Für neue Skills von Grund auf: /build-agent → /elvis-skill-generator (Elvis). Für Varianten bestehender Skills: /expand-skills → /elvis-skill-expander (Borg)." CMD-02 ist der breitere Einstieg, CMD-06 der fokussierte.
**Warnzeichen:** Beide Commands haben identische Beschreibungen oder identische Skill-Chains.

### Pitfall 4: Hinweis-Feld fehlt bei CMD-01

**Was schiefgeht:** CMD-01 (`/build-agent`) hat keinen Hinweis obwohl der Workflow (Soul + Identity + Agent als Paket) für Operator wichtig ist.
**Warum es passiert:** Hinweis-Feld ist optional — bei einfachen Commands vernünftig wegzulassen.
**Wie vermeiden:** CMD-01 ist der komplexeste Workflow (3-Datei-Output). Ein Hinweis "Erstellt Soul + Identity + Agent als vollständiges Paket — max. 1 Agent pro Durchlauf" gibt dem Operator wertvolle Erwartungs-Kalibrierung.
**Warnzeichen:** CMD-01 hat keine Hinweis-Zeile, obwohl der Downstream-Effekt (3 Dateien) nicht offensichtlich ist.

---

## Code Examples

Alle Beispiele basieren auf bestehenden Projektdateien.

### Vollständiges Beispiel — CMD-07 `/health-check`

```markdown
# Command

## Command
/health-check

## Beschreibung
Führt einen quantitativen Gesundheitscheck des Ökosystems durch und gibt einen Score (0–100) mit Breakdown nach 4 Kategorien aus.

## Agent
Picard

## Skill-Chain
- /elvis-ecosystem-health
```

### Vollständiges Beispiel — CMD-01 `/build-agent` (mit Hinweis)

```markdown
# Command

## Command
/build-agent

## Beschreibung
Erstellt einen vollständigen Agenten (Soul + Identity + Agent-Definition) aus einer Anforderungs-Beschreibung.

## Agent
Q

## Skill-Chain
- /elvis-agent-creator

## Hinweis
Erstellt Soul + Identity + Agent als untrennbares Paket — max. 1 Agent pro Durchlauf. Ein Approval-Gate nach Konzept-Entwurf.
```

### Vollständiges Beispiel — CMD-10 `/route-command` (Alias)

```markdown
# Command

## Command
/route-command

## Beschreibung
Meta-Router — routet Anfragen an den richtigen Agent und Skill anhand einer statischen Routing-Tabelle.

## Agent
Picard

## Skill-Chain
- /elvis-command-router

## Hinweis
Alias für /elvis-command-router. Beide Aufrufe führen zum gleichen Ergebnis.
```

### Router-Update — Diff der kritischen Stellen

**Strategie-Abschnitt (Routing-Tabelle) — zu ersetzen:**

```markdown
<!-- ALT: entfernen -->
**Routing-Tabelle (Phase 1 — aktuelle Skills):**

| Keyword / Anfrage-Typ | Agent | Skill-Chain |
|---|---|---|
| Soul erstellen, neue Soul, Soul generieren | Picard | /elvis-soul-generator |
| Identity erstellen, neue Identity, Identity generieren | Picard | /elvis-identity-generator |
| Agent erstellen, neuer Agent, Agent generieren | Picard | /elvis-agent-generator |
| Skills generieren, neue Skills, Skill erstellen | Elvis | /elvis-skill-generator |

Hinweis: Diese Tabelle wird in Phase 2 um weitere Meta-Skills erweitert...
```

```markdown
<!-- NEU: vollständige Tabelle ohne Hinweis -->
**Routing-Tabelle (vollständig — alle Phase-1- und Phase-2-Skills):**

| Keyword / Anfrage-Typ | Agent | Skill-Chain |
|---|---|---|
| Soul erstellen, neue Soul, Soul generieren | Picard | /elvis-soul-generator |
| Identity erstellen, neue Identity, Identity generieren | Picard | /elvis-identity-generator |
| Agent erstellen, neuer Agent, Agent generieren | Picard | /elvis-agent-generator |
| Skills generieren, neue Skills, Skill erstellen | Elvis | /elvis-skill-generator |
| Agent zusammenstellen, vollständiger Agent, Agent Creator | Q | /elvis-agent-creator |
| Skills erweitern, Skill-Varianten, Borg | Borg | /elvis-skill-expander |
| System analysieren, Schwächen, Lücken | Troi | /elvis-system-analyzer |
| Library verwalten, Katalog, Skill-Katalog | Uhura | /elvis-library-manager |
| Gesundheitscheck, Health-Check, System-Score | Picard | /elvis-ecosystem-health |
| Agent optimieren, Agent verbessern | Picard | /elvis-agent-optimizer |
| Konzept entwerfen, neues Konzept, Blaupause | Q | /elvis-concept-design |
| Route command, routen, welcher Agent | Picard | /elvis-command-router |
```

**Verifikations-Abschnitt — Akzeptanzkriterium zu ersetzen:**

```markdown
<!-- ALT -->
Akzeptanzkriterium: Jede Anfrage wird einem der drei Fälle zugeordnet (eindeutig/mehrdeutig/unbekannt), Routing-Tabelle enthält mindestens 4 Einträge, alle Routen zeigen auf `/elvis-*`-Skills

<!-- NEU -->
Akzeptanzkriterium: Jede Anfrage wird einem der drei Fälle zugeordnet (eindeutig/mehrdeutig/unbekannt), Routing-Tabelle enthält mindestens 12 Einträge (alle Phase-1- und Phase-2-Skills), alle Routen zeigen auf `/elvis-*`-Skills
```

---

## State of the Art

| Alter Ansatz | Aktueller Ansatz | Wann geändert | Impact |
|--------------|------------------|---------------|--------|
| Router nur mit Phase-1-Skills (4 Einträge) | Router mit allen 12 Skills (Phase 1 + Phase 2) | Phase 3 (jetzt) | Router ist vollständig und als einzige Routing-Quelle der Wahrheit nutzbar |
| Kein Commands-Verzeichnis | `commands/` auf Root-Ebene als eigene Entity-Klasse | Phase 3 (jetzt) | Shortcuts für alle Kern-Workflows formalisiert, konsistent mit bestehender Verzeichnisstruktur |
| Direkte Skill-Namen als Einstiegspunkt | Kurze Commands als mnemonische Shortcuts | Phase 3 (jetzt) | Operator-Erfahrung: `/build-agent` statt `/elvis-agent-creator` |

**Keine deprecations:** Phase 3 ersetzt nichts. Alle bestehenden `/elvis-*`-Skills bleiben direkt verwendbar. Commands sind additive Shortcuts.

---

## Open Questions

1. **CMD-02 Agent-Feld bei Dual-Skill-Chain**
   - Was wir wissen: CMD-02 hat zwei Ziel-Skills: `/elvis-skill-generator` (Agent: Elvis) und `/elvis-skill-expander` (Agent: Borg). Beide haben unterschiedliche Agenten.
   - Was unklar ist: Soll das Agent-Feld "Elvis / Borg" oder nur den primären Agenten nennen?
   - Empfehlung: Agent-Feld mit "Elvis (für /elvis-skill-generator) / Borg (für /elvis-skill-expander)" oder beide Agenten als Liste. Alternativ: Hinweis-Feld klärt die Auswahl, Agent-Feld nennt Elvis als primären Einstieg. Claude's Discretion — wähle die klarere Formulierung.

2. **Routing-Tabelle Keyword-Abgrenzung für Mehrsprachigkeit**
   - Was wir wissen: Bestehende Tabelle hat deutsche Keywords. Neue Phase-2-Einträge sollen konsistent sein.
   - Was unklar ist: Sind englische Keywords (z.B. "health check", "optimize") als Aliases sinnvoll?
   - Empfehlung: Deutsche Keywords beibehalten (konsistent mit bestehendem Projekt). Englische Begriffe können als zweite Spalten-Einträge ergänzt werden wenn Discretion es erlaubt. Primär: deutsche Schreibweise wie in CONTEXT.md spezifiziert.

---

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | Kein Testrunner — reines Markdown-Projekt ohne ausführbaren Code |
| Config file | none |
| Quick run command | Manuelle Verifikation: Datei vorhanden + 5 Felder-Check |
| Full suite command | Manuelle Vollprüfung aller 10 Command-Dateien + Router-Update gegen Checkliste |

### Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| CMD-01 | `commands/build-agent.md` existiert mit 5 Feldern, Agent=Q, Skill=/elvis-agent-creator | manual | `grep -q "/elvis-agent-creator" commands/build-agent.md && grep -q "Q" commands/build-agent.md` | ❌ Wave 0 |
| CMD-02 | `commands/generate-skills.md` existiert mit /elvis-skill-generator und /elvis-skill-expander in Skill-Chain | manual | `grep -q "elvis-skill-generator" commands/generate-skills.md && grep -q "elvis-skill-expander" commands/generate-skills.md` | ❌ Wave 0 |
| CMD-03 | `commands/analyze-system.md` existiert mit Agent=Troi, Skill=/elvis-system-analyzer | manual | `grep -q "/elvis-system-analyzer" commands/analyze-system.md && grep -q "Troi" commands/analyze-system.md` | ❌ Wave 0 |
| CMD-04 | `commands/optimize-agent.md` existiert mit Skill=/elvis-agent-optimizer | manual | `grep -q "/elvis-agent-optimizer" commands/optimize-agent.md` | ❌ Wave 0 |
| CMD-05 | `commands/manage-library.md` existiert mit Skill=/elvis-library-manager | manual | `grep -q "/elvis-library-manager" commands/manage-library.md` | ❌ Wave 0 |
| CMD-06 | `commands/expand-skills.md` existiert mit Agent=Borg, Skill=/elvis-skill-expander | manual | `grep -q "/elvis-skill-expander" commands/expand-skills.md && grep -q "Borg" commands/expand-skills.md` | ❌ Wave 0 |
| CMD-07 | `commands/health-check.md` existiert mit Skill=/elvis-ecosystem-health | manual | `grep -q "/elvis-ecosystem-health" commands/health-check.md` | ❌ Wave 0 |
| CMD-08 | `commands/create-soul.md` existiert mit Skill=/elvis-soul-generator | manual | `grep -q "/elvis-soul-generator" commands/create-soul.md` | ❌ Wave 0 |
| CMD-09 | `commands/create-identity.md` existiert mit Skill=/elvis-identity-generator | manual | `grep -q "/elvis-identity-generator" commands/create-identity.md` | ❌ Wave 0 |
| CMD-10 | `commands/route-command.md` existiert mit Agent=Picard, Skill=/elvis-command-router | manual | `grep -q "/elvis-command-router" commands/route-command.md && grep -q "Picard" commands/route-command.md` | ❌ Wave 0 |

**Gemeinsame Command-Format-Prüfung (für alle 10 Commands):**

| Check | Prüfung |
|-------|---------|
| Format-Check | Datei hat maximal 20 Zeilen (sonst enthält sie Ausführungslogik) |
| Keine Skill-Sektionen | Datei enthält NICHT: "## Strategie", "## Ausführungsschritte", "## Einschränkungen", "## Verifikation" |
| Pflichtfelder | Datei enthält: "## Command", "## Beschreibung", "## Agent", "## Skill-Chain" |
| Skill-Referenz | Alle Skill-Chain-Einträge beginnen mit `/elvis-` |

**Router-Update Prüfung:**

| Check | Prüfung |
|-------|---------|
| Tabellengröße | `grep -c "|.*|.*|" skills/meta/elvis-command-router.md` ergibt ≥ 14 (Header + 12 Einträge) |
| Kein veralteter Hinweis | `grep -c "Phase 2 um weitere" skills/meta/elvis-command-router.md` ergibt 0 |
| Neue Skills enthalten | `grep -q "elvis-agent-creator" skills/meta/elvis-command-router.md` |

### Sampling Rate
- **Per task commit:** Manuelle Checkliste: Datei vorhanden? 5 Pflichtfelder vorhanden? Skill-Chain zeigt auf `/elvis-*`? Datei < 20 Zeilen?
- **Per wave merge:** Alle 10 Commands + Router-Update als Gesamtprüfung
- **Phase gate:** Manueller Smoke-Test — für jeden Command prüfen ob Skill-Referenz auf existierenden Skill in `skills/meta/` zeigt, vor `/gsd:verify-work`

### Wave 0 Gaps
- [ ] Alle 10 Command-Dateien — `commands/*.md` (neue Dateien, Wave 0 = Erstellung)
- [ ] Router-Update — `skills/meta/elvis-command-router.md` (bestehende Datei, Update)

*(Kein Test-Framework-Setup nötig — Markdown-Projekt)*

---

## Sources

### Primary (HIGH confidence)
- `C:/Dev/Openclaw_Meta_Maker/.planning/phases/03-command-layer/03-CONTEXT.md` — Alle locked decisions, Command-Format-Spezifikation, Router-Update-Scope, CMD-10-Abgrenzung
- `C:/Dev/Openclaw_Meta_Maker/skills/meta/elvis-command-router.md` — Aktueller Zustand der Routing-Tabelle (4 Einträge), Verifikations-Abschnitt der angepasst werden muss
- `C:/Dev/Openclaw_Meta_Maker/.planning/REQUIREMENTS.md` — CMD-01 bis CMD-10 Definitionen, Agent-Skill-Zuordnungen
- `C:/Dev/Openclaw_Meta_Maker/agent/picard.md` — Picard als Orchestrator-Agent, bestätigt Routing-Zuständigkeit

### Secondary (MEDIUM confidence)
- `C:/Dev/Openclaw_Meta_Maker/.planning/phases/02-composition-autonomous/02-RESEARCH.md` — Agent-Skill-Zuordnungen für Phase-2-Skills, Router-Update als Open Question dokumentiert
- `C:/Dev/Openclaw_Meta_Maker/.planning/phases/01-generators-router/01-01-PLAN.md` — Plan-Format-Referenz für Phase-3-Planung

---

## Metadata

**Confidence breakdown:**
- Command-Format: HIGH — vollständig in CONTEXT.md spezifiziert, 5-Felder-Deklaration ist explizit
- Agent-Skill-Zuordnungen: HIGH — alle aus CONTEXT.md code_context und REQUIREMENTS.md verifiziert
- Router-Update Inhalt: HIGH — bestehende Routing-Tabelle eingesehen, alle neuen Einträge aus CONTEXT.md
- CMD-02 Dual-Agent-Handling: MEDIUM — Diskretions-Bereich, empfohlene Lösung mit Hinweis-Feld

**Research date:** 2026-03-14
**Valid until:** 2026-06-14 (stabiles Markdown-Projekt — keine Versionsabhängigkeiten)
