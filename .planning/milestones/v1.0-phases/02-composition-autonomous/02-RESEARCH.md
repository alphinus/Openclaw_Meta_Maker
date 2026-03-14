# Phase 2: Composition + Autonomous - Research

**Researched:** 2026-03-14
**Domain:** Markdown-based meta-skill authoring — Orchestration, Analysis, Catalog Management, Safeguard-Pattern
**Confidence:** HIGH

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**Scope-Bereinigung META-10/11**
- META-11 (`/elvis-pattern-assimilation`) → v2 verschoben. Kein Use Case identifiziert. Borg hat intern bereits `/elvis-skill-expander`.
- META-10 (`/elvis-agent-optimizer`) → bleibt in v1. Klarer Use Case: Agent-Definition lesen → Schwächen identifizieren → optimierte Version vorschlagen. Scope: nur Agent-Definitionen optimieren, keine Souls/Identities/Skills.
- META-12 (`/elvis-concept-design`) → bleibt in v1. Q's Kernfähigkeit: neue Agent-Konzepte entwerfen und validieren bevor sie gebaut werden.

**Agent-Creator Workflow (META-04)**
- Orchestrierungsmodell: Sequentieller 3-Phasen-Workflow mit EINEM Approval-Gate nach der Planungsphase.
- Workflow-Schritte:
  1. Anforderung lesen → Gesamtkonzept entwerfen (Soul-Typ, Identity-Charakter, Agent-Mission, Skill-Set)
  2. [APPROVAL-GATE] Kompletten Plan präsentieren — auf Bestätigung warten
  3. Soul generieren (intern, nach soul-template.md)
  4. Identity generieren (intern, nach identity-template.md)
  5. Agent generieren (intern, nach agent-template.md, mit validen Querverweisen)
  6. Komplettes Paket präsentieren — auf Freigabe oder Korrektur warten
- Single-Approval (nicht Triple-Approval): Agent-Creator orchestriert die Generatoren als interne Referenz, nicht als separate Aufrufe.
- <2 Minuten Constraint: bezieht sich auf Operator-Interaktion (Anforderung → fertiger Agent). Operator wartet nur einmal (Approval-Gate) und einmal am Ende.
- Output: 3 zusammengehörige Markdown-Dateien (soul/, identity/, agent/) + Zusammenfassung mit Speicher-Hinweisen.

**Autonome Skills — Analysetiefe**
- System-Analyzer (Troi, META-06): Detaillierter Report mit benannten Lücken, konkreten Empfehlungen, Schweregrad-Einstufung (kritisch/mittel/niedrig).
- Skill-Expander (Borg, META-05): Generiert neue Skill-Varianten als vollständige 9-Sektionen-Definitionen, nicht nur Listen. Basis: bestehender Skill.
- Library-Manager (Uhura, META-07): Kategorisierter, durchsuchbarer Katalog mit Kategorie-Tags, Abhängigkeits-Graph, Vollständigkeits-Check.
- Ecosystem-Health (META-09): Quantitativer Score (0-100) mit benannten Issues. Prüft Template-Konformität, Querverweis-Integrität, Safeguard-Vollständigkeit, Kategorie-Balance.
- Agent-Optimizer (META-10): Liest bestehende Agent-Definition → identifiziert Schwächen (fehlende Skills, schwache Constraints, veraltete Referenzen) → generiert optimierte Version. Ein Agent pro Durchlauf.
- Concept-Design (Q, META-12): Konzept-Dokument mit Mission, empfohlenem Soul, Skill-Bedarf, Machbarkeits-Einschätzung. Kein fertiger Agent — nur validierte Blaupause.

**Max-Limits Phase 2**
- Agent-Creator (Q): Max. 1 kompletter Agent pro Durchlauf.
- Skill-Expander (Borg): Max. 5 neue Skill-Varianten pro Durchlauf.
- System-Analyzer (Troi): Max. 1 vollständige System-Analyse pro Durchlauf.
- Library-Manager (Uhura): Max. 10 Library-Änderungen pro Durchlauf.
- Ecosystem-Health: Max. 1 Health-Check pro Durchlauf.
- Agent-Optimizer: Max. 1 Agent-Optimierung pro Durchlauf.
- Concept-Design (Q): Max. 1 Konzept pro Durchlauf.

**Safeguard-Pattern (aus Phase 1 übernommen)**
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

### Deferred Ideas (OUT OF SCOPE)
- META-11 (`/elvis-pattern-assimilation`) — nach v2 verschoben. Braucht erst definierte Input-Formate für externe Quellen.
- Command-Router Update — Routing-Tabelle um Phase-2-Skills erweitern. Gehört zu Phase 3 (Command Layer) oder als separater Update-Task.
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| META-04 | User kann mit `/elvis-agent-creator` einen kompletten Agenten aus Soul + Identity + Agent + Skills in < 2 Minuten zusammenstellen | Orchestration-Pattern: 1-Approval-Gate nach Konzept-Phase, dann sequentielle interne Generierung; direkte Vorlage in Phase-1-Generatoren + agent-template.md |
| META-05 | User kann mit `/elvis-skill-expander` bestehende Skills erweitern und neue Varianten ableiten (Borg) | Skill-Expander basiert auf bestehendem Skill als Input; Varianten sind vollständige 9-Sektionen-Definitionen; Max. 5 pro Durchlauf; Muster aus skill-generator Gold Standard |
| META-06 | User kann mit `/elvis-system-analyzer` das gesamte Ökosystem auf Schwächen und Lücken analysieren (Troi) | Read-Only Analyse-Skill; scannt skills/, agent/, soul/, identity/; Output ist strukturierter Bericht mit Schweregrad-Einstufung; Troi-Agent-Definition definiert Scope |
| META-07 | User kann mit `/elvis-library-manager` den Skill-Katalog organisieren, kategorisieren und durchsuchen (Uhura) | Katalog-Verwaltung mit Kategorie-Tags; Max. 10 Änderungen pro Durchlauf; Approval-Gate vor strukturellen Änderungen; Uhura-Agent-Definition definiert Scope |
| META-09 | User kann mit `/elvis-ecosystem-health` einen Gesundheitscheck des gesamten Systems durchführen | Quantitativer Score (0-100); 4 Prüfbereiche: Template-Konformität, Querverweis-Integrität, Safeguard-Vollständigkeit, Kategorie-Balance; Unterschied zu System-Analyzer: schneller Check vs. tiefe Analyse |
| META-10 | User kann mit `/elvis-agent-optimizer` bestehende Agenten-Definitionen verbessern und optimieren | Input: bestehende agent/*.md Datei; Output: optimierte Agent-Definition; Scope nur Agent-Definitionen, keine Souls/Skills; Max. 1 pro Durchlauf |
| META-12 | User kann mit `/elvis-concept-design` neue Agent-Konzepte entwerfen und validieren (Q) | Konzept-Dokument als Vorstufe zum Agent-Creator; validiert Machbarkeit gegen bestehendes Ökosystem; Max. 1 Konzept pro Durchlauf; kein fertiger Agent |
</phase_requirements>

---

## Summary

Phase 2 erstellt 7 neue Markdown-Skill-Dateien. Das Projekt bleibt ein reines Markdown-Authoring-Projekt — kein Code, keine Bibliotheken, kein Runtime. Alle 7 Skills folgen dem 9-Sektionen-Format mit vollständigem Safeguard-Quartet aus Phase 1. Der einzige neue Komplexitätsfaktor ist die Orchestrierung: `/elvis-agent-creator` koordiniert die Phase-1-Generatoren intern als eine zusammenhängende 6-Schritt-Sequenz.

Die 7 Skills teilen sich in drei funktionale Gruppen auf. Erstens Kompositions-Skills (META-04, META-05, META-12): produzieren neue Definitionen durch Zusammensetzung oder Ableitung aus bestehenden. Zweitens Analyse-Skills (META-06, META-09): sind read-only, scannen das Ökosystem und geben strukturierte Reports aus. Drittens Verwaltungs-Skills (META-07, META-10): modifizieren oder optimieren bestehende Definitionen mit Approval-Gate vor jeder Änderung.

Der kritische Planungspunkt: Agent-Creator hat bewusst nur EIN Approval-Gate (nach Gesamtplan), nicht drei für jeden Sub-Generator. Das verhindert Flow-Fragmentierung und sichert den <2-Minuten-Constraint. Alle anderen Skills übernehmen das bewährte Plan→Approve→Execute-Pattern aus Phase 1 unverändert.

**Primary recommendation:** Modelliere alle 7 Skills direkt nach `skills/meta/elvis-skill-generator.md` (Gold Standard) für das Safeguard-Quartet und die D006-konformen Ausführungsschritte. Agent-Creator folgt dem Orchestrierungs-Pattern: 1 Approval-Gate auf Konzept-Ebene, dann alle Generierungen intern sequentiell ohne weitere Halte bis zum abschließenden Review.

---

## Standard Stack

### Core — Skill-Dateien und Templates

| Komponente | Typ | Zweck | Warum bindend |
|-----------|-----|-------|---------------|
| `templates/skill-template.md` | Markdown-Template | 9-Sektionen-Struktur für alle Skills | Alle Phase-1-Skills und bestehende Skills folgen diesem Format |
| `templates/soul-template.md` | Markdown-Template | 6-Sektionen Soul-Struktur | Agent-Creator generiert Souls intern nach dieser Vorlage |
| `templates/identity-template.md` | Markdown-Template | 7-Sektionen Identity-Struktur | Agent-Creator generiert Identities intern nach dieser Vorlage |
| `templates/agent-template.md` | Markdown-Template | 7-Sektionen Agent-Struktur | Agent-Creator + Agent-Optimizer produzieren/verarbeiten Agent-Dateien nach dieser Vorlage |
| `skills/meta/elvis-skill-generator.md` | Gold-Standard-Skill | Referenz-Implementierung für Safeguard-Quartet, D006, Plan→Approve→Execute | Direktes Vorbild für alle 7 neuen Skills |
| `skills/meta/elvis-agent-generator.md` | Phase-1-Skill | Querverweisvalidierung-Pattern, Agent-Vorschau-Struktur | Agent-Creator + Agent-Optimizer übernehmen dieses Prüf-Pattern |

### Keine externen Abhängigkeiten

Kein Build-Prozess, keine npm-Pakete, keine API-Calls. Alle "Libraries" sind die Markdown-Templates im `templates/`-Verzeichnis und die bestehenden Skill/Agent/Soul/Identity-Dateien im Ökosystem.

---

## Architecture Patterns

### Empfohlene Dateistruktur (Output dieser Phase)

```
skills/meta/
├── elvis-skill-generator.md       ← Phase 1 (Gold Standard, unveränderlich)
├── elvis-soul-generator.md        ← Phase 1
├── elvis-identity-generator.md    ← Phase 1
├── elvis-agent-generator.md       ← Phase 1
├── elvis-command-router.md        ← Phase 1
├── elvis-agent-creator.md         ← NEU (META-04)
├── elvis-skill-expander.md        ← NEU (META-05)
├── elvis-system-analyzer.md       ← NEU (META-06)
├── elvis-library-manager.md       ← NEU (META-07)
├── elvis-ecosystem-health.md      ← NEU (META-09)
├── elvis-agent-optimizer.md       ← NEU (META-10)
└── elvis-concept-design.md        ← NEU (META-12)
```

### Pattern 1: Orchestrierungs-Skill (Concept→Approve→Orchestrate) — Agent-Creator

**Was:** Ein Meta-Skill der mehrere Phase-1-Generatoren als interne Referenz koordiniert. Erzeugt 3 Dateien (Soul + Identity + Agent) in einer zusammenhängenden Sequenz nach einem einzigen Approval-Gate.

**Wann verwenden:** Nur Agent-Creator (META-04). Kein anderer Phase-2-Skill orchestriert Sub-Generatoren.

**Schrittstruktur:**
```
1. Anforderung lesen + Einzelbeschränkung prüfen (Max. 1 Agent)
2. Konzept entwerfen: Soul-Typ (welches soul/*.md oder neu?), Identity-Charakter,
   Agent-Mission (1 Satz), empfohlene 5–8 Skills im /elvis-*-Format
3. [APPROVAL-GATE] Gesamtkonzept als Tabelle präsentieren — auf Bestätigung warten.
   Schritt endet hier. Keine weiteren Aktionen ohne explizite Bestätigung.
4. Soul generieren: vollständige 6-Sektionen-Definition nach soul-template.md
5. Identity generieren: vollständige 7-Sektionen-Definition nach identity-template.md
6. Agent generieren: vollständige 7-Sektionen-Definition nach agent-template.md
   — Querverweisvalidierung: Soul (soul/[name].md) + alle Skills (/elvis-*) prüfen
7. Komplettes Paket (alle 3 Definitionen) präsentieren — auf Freigabe oder Korrektur warten
8. Abschluss-Zusammenfassung: 3 Dateipfade, Status, Speicher-Hinweis für alle 3 Dateien
```

**Kritischer Unterschied zu Phase-1-Generatoren:** Agent-Creator hat EINEN Approval-Gate auf Konzept-Ebene. Die drei Generierungsschritte (Soul, Identity, Agent) laufen intern sequentiell ohne weitere Halte. Drei separate Approval-Gates würden die <2-Minuten-Zielvorgabe brechen.

**Safeguard-Formulierung für Einschränkungen:**
```
- **Max-Limit:** Max. 1 kompletter Agent pro Durchlauf. Soul + Identity + Agent als
  Einheit behandeln — kein Partial-Output (z.B. nur Soul ohne Identity).
- **Approval-Gate:** Nach Konzept-Entwurf (Schritt 3) — auf Bestätigung warten bevor
  erste Zeile Soul-Text generiert wird. Ein einziger Gate für den Gesamtworkflow.
- **Stop-Bedingung:** Regulär wenn alle 3 Definitionen generiert und vom Operator
  freigegeben. Vorzeitig wenn Operator abbricht oder nach 3 Revisionsversuchen
  am Gesamtpaket keine Einigung erzielt wird.
- **Rollback-Hinweis:** Wenn eine der 3 Definitionen nicht dem Template entspricht,
  den kompletten Schritt (Soul, Identity oder Agent) neu generieren — nicht iterativ
  korrigieren. Original-Konzept (Schritt 3) als Basis beibehalten.
```

### Pattern 2: Generator-Skill (Plan→Approve→Execute) — Skill-Expander, Concept-Design

**Was:** Direkte Übernahme des Phase-1-Patterns. Erzeugt neue Definitionen nach Approval-Gate. Skill-Expander arbeitet von einem bestehenden Skill als Basis, Concept-Design entwirft Konzept-Dokumente statt fertiger Definitionen.

**Skill-Expander Besonderheit:**
```
1. Basis-Skill lesen + analysieren (welcher bestehende Skill dient als Vorlage?)
2. Varianten-Übersicht erstellen: max. 5 neue Skill-Namen, je 1-Satz-Beschreibung,
   Kategorie, Abgrenzung vom Basis-Skill
3. [APPROVAL-GATE] Übersichts-Tabelle präsentieren — auf Bestätigung warten
4. Jede Variante vollständig generieren (9-Sektionen-Format, D006-konform)
5–6. (wie skill-generator) Präsentation + Abschluss
```

**Concept-Design Besonderheit:**
```
Konzept-Dokument ≠ fertiger Agent. Output-Format:
- Konzept-Name + Mission (1 Satz)
- Empfohlener Soul (soul/*.md Verweis oder "neuer Soul nötig: [Archetyp]")
- Skill-Bedarf (Liste /elvis-* Skills die nötig/fehlend sind)
- Machbarkeits-Einschätzung (hoch/mittel/niedrig + Begründung)
- Empfohlene nächste Schritte (z.B. "aufrufen: /elvis-agent-creator")
```

### Pattern 3: Analyse-Skill (Read-Only) — System-Analyzer, Ecosystem-Health

**Was:** Scannt das gesamte Ökosystem (skills/, agent/, soul/, identity/), analysiert und gibt einen strukturierten Report aus. Keine Schreiboperationen — read-only.

**System-Analyzer (qualitative Tiefenanalyse):**
```
1. Ökosystem-Scan: alle Dateien in soul/, identity/, agent/, skills/ aufnehmen
2. Lücken-Analyse: fehlende Querverweise, nicht referenzierte Skills, Agents ohne Soul
3. Schwächen-Analyse: unvollständige Definitionen, fehlende Safeguards, D006-Verstöße
4. Kategorie-Balance: Welche skill-Kategorien sind überbesetzt/unterbesetzt?
5. [APPROVAL-GATE — nur wenn Empfehlungen direkte Änderungen implizieren]
   Befunde präsentieren — Operator entscheidet ob Empfehlungen umgesetzt werden
6. Report ausgeben: strukturiert nach Schweregrad (kritisch/mittel/niedrig)
   mit konkreten Handlungsempfehlungen pro Issue
```

**Ecosystem-Health (quantitativer Quick-Check):**
```
Score-Berechnung (0-100):
- Template-Konformität (alle 4 Entity-Typen): 25 Punkte
- Querverweis-Integrität (Soul→Agent, Agent→Skills): 25 Punkte
- Safeguard-Vollständigkeit (alle 4 Safeguards in Meta-Skills): 25 Punkte
- Kategorie-Balance (6 Kategorien gleichmäßig besetzt): 25 Punkte

Output: Score + Breakdown pro Kategorie + benannte Issues mit Zähler
```

**Kritischer Unterschied:** Ecosystem-Health = schneller Score mit Zähler. System-Analyzer = tiefe qualitative Analyse mit Kontext und Empfehlungen. Beide ergänzen sich, überschneiden sich nicht.

### Pattern 4: Verwaltungs-Skill (Read-Write mit Approval) — Library-Manager, Agent-Optimizer

**Was:** Liest bestehende Definitionen, modifiziert oder produziert eine verbesserte Version. Approval-Gate schützt vor ungewollten strukturellen Änderungen.

**Library-Manager:**
```
1. Library-Status prüfen: alle skills/* inventarisieren (Name, Kategorie, Dateipfad)
2. Katalog-Erstellung/Aktualisierung: Kategorie-Tags, Duplikat-Erkennung,
   Vollständigkeits-Check (alle 9 Sektionen vorhanden?)
3. [APPROVAL-GATE] vor strukturellen Änderungen (Umkategorisierung, Archivierung)
4. Änderungen durchführen (max. 10 pro Durchlauf): als Anweisung an Operator ausgeben
5. Abschluss: Katalog-Datei als Markdown-Tabelle ausgeben
```

**Agent-Optimizer:**
```
1. Agent-Datei lesen (agent/[name].md)
2. Schwächen analysieren:
   - Fehlende Skills (in Capabilities beschrieben aber nicht in Primäre Skills)
   - Schwache Constraints (vage Formulierungen statt harter Grenzen)
   - Veraltete Soul-Referenz (soul/*.md Datei existiert noch?)
   - Capabilities die Persönlichkeit statt Aufgaben beschreiben
3. [APPROVAL-GATE] Schwächen-Report präsentieren (Tabelle: Issue, Typ, Empfehlung)
   — auf Bestätigung vor Generierung optimierter Version warten
4. Optimierte Agent-Definition generieren (7-Sektionen, Templates-konform)
5. Vorher/Nachher-Vergleich als Diff-Tabelle präsentieren
6. Abschluss: Dateipfad + Speicher-Hinweis
```

### Anti-Patterns to Avoid

- **Agent-Creator mit drei Approval-Gates:** Drei separate Gates (nach Soul-Konzept, nach Identity-Konzept, nach Agent-Konzept) fragmentieren den Flow und brechen den <2-Minuten-Constraint. Ein Gate nach Gesamtplan ist die richtige Entscheidung.
- **System-Analyzer schreibt Dateien:** System-Analyzer ist read-only (Troi's Constraint: "Analyse-Ergebnisse sind read-only"). Schreiboperationen gehören in Library-Manager oder Agent-Optimizer.
- **Skill-Expander erzeugt Varianten-Listen statt vollständige Skills:** Jede Variante MUSS eine vollständige 9-Sektionen-Definition sein. "Variante A: Fokus auf Twitter-Content" als Stichpunkt ist kein valider Output.
- **Ecosystem-Health ohne Zahlen:** Score ohne Breakdown ist wertlos. Jede der 4 Kategorien braucht Teilpunkte + Begründung.
- **Agent-Optimizer optimiert Souls oder Skills:** Scope ist explizit auf agent/*.md beschränkt. Kein Zugriff auf soul/ oder skills/.
- **Concept-Design liefert fertige Agent-Definition:** Output ist ein Konzept-Dokument, kein fertiger Agent. Wer einen fertigen Agenten will, ruft anschließend `/elvis-agent-creator` auf.

---

## Don't Hand-Roll

| Problem | Nicht neu bauen | Verwende stattdessen | Warum |
|---------|-----------------|---------------------|-------|
| Soul-Generierung im Agent-Creator | Eigene Soul-Logik | soul-template.md 6-Sektionen-Format (wie Soul-Generator) | Template ist kanonisch — Agent-Creator folgt dem gleichen Format wie elvis-soul-generator |
| Identity-Generierung im Agent-Creator | Abweichende Identity-Struktur | identity-template.md 7-Sektionen-Format (wie Identity-Generator) | Querverweise in agent-template.md erwarten dieses Format |
| Querverweisvalidierung im Agent-Creator | Eigene Prüflogik | Pattern aus elvis-agent-generator.md Schritt 2 | Bereits definiert: Soul-Datei + Skills prüfen bevor generiert wird |
| Approval-Gate-Formulierung | Neue Halt-Sprache entwickeln | "warte auf explizite Bestätigung" aus Phase-1-Skills | Bewährt als tatsächlicher LLM-Halt-Punkt |
| Safeguard-Quartet-Block | Neue Einschränkungs-Sprache | elvis-skill-generator.md Einschränkungs-Block als Vorlage | Konsistenz im Ökosystem — alle 11 Skills sollen identisch formuliert sein |
| Health-Score-Berechnung | Komplexe Gewichtungslogik | Einfache 4×25-Punkte-Verteilung (Discretion: Gewichtung ist Claude's Ermessen) | Einfachheit ist Stärke: schneller verständlich, einfacher zu erklären |

---

## Common Pitfalls

### Pitfall 1: Agent-Creator generiert Partial-Output

**Was schiefgeht:** Agent-Creator erzeugt nur Soul + Identity aber hört vor dem Agent auf (weil Operator nicht explizit "weiter" sagt).

**Warum es passiert:** Jeder Sub-Generator in Phase 1 hat seinen eigenen Approval-Gate. Agent-Creator erbt dieses Muster falsch und baut einen impliziten Gate nach jedem Sub-Output.

**Wie vermeiden:** Ausführungsschritte explizit formulieren: "Nach Bestätigung des Gesamtkonzepts (Schritt 3) werden Soul, Identity und Agent intern sequentiell generiert — kein weiterer Halt zwischen diesen Schritten." Max-Limit-Formulierung: "1 kompletter Agent = Soul + Identity + Agent als untrennbare Einheit."

**Warnzeichen:** Stop-Bedingung nennt Sub-Output-Stufen (nach Soul, nach Identity) statt "nach vollständigem Paket".

### Pitfall 2: Skill-Expander produziert Beschreibungs-Listen statt vollständige Skills

**Was schiefgeht:** Skill-Expander gibt 5 Skill-Namen mit 1-Satz-Beschreibungen aus und bezeichnet das als "Varianten". CONTEXT.md verlangt vollständige 9-Sektionen-Definitionen für jede Variante.

**Warum es passiert:** Die Übersichts-Tabelle (Approval-Gate-Phase) sieht wie der Output aus. Ausführungsschritte sind nicht explizit genug über die Post-Approval-Generierung.

**Wie vermeiden:** Ausführungsschritte nach Approval-Gate explizit: "Generiere Variante 1 vollständig im 9-Sektionen-Format gemäß skill-template.md — identisch zum Prozess in /elvis-skill-generator Schritt 3." Verifikation: "Jede Variante hat exakt 9 Sektionen — eine Variante als Beschreibungsliste ist ein Fehler."

**Warnzeichen:** Output-Sektion beschreibt "Varianten-Übersicht" statt "vollständig generierte Skill-Dateien".

### Pitfall 3: System-Analyzer und Ecosystem-Health überschneiden sich zu stark

**Was schiefgeht:** Beide Skills prüfen dasselbe und es ist unklar welcher wann zu verwenden ist.

**Warum es passiert:** Beide haben "Ökosystem-Analyse" als Domäne. Die Unterscheidung Quick-Check vs. Deep-Dive ist in den Skill-Beschreibungen nicht scharf genug.

**Wie vermeiden:** Explizite Abgrenzung in beiden Skill-Beschreibungen: "Ecosystem-Health: 0-100-Score in < 2 Minuten, keine Empfehlungen, nur Zähler. System-Analyzer: vollständiger qualitativer Bericht mit Kontext und Handlungsempfehlungen, 1 Analyse pro Durchlauf."

**Warnzeichen:** Ecosystem-Health-Beschreibung nennt "Empfehlungen" oder System-Analyzer produziert einen Score.

### Pitfall 4: Agent-Optimizer greift auf Souls oder Skills zu

**Was schiefgeht:** Agent-Optimizer "verbessert" Soul-Referenzen indem er Soul-Dateien modifiziert, oder schlägt Skill-Überarbeitungen vor.

**Warum es passiert:** "Optimierung" fühlt sich wie umfassende Verbesserung an. CONTEXT.md begrenzt den Scope explizit auf agent/*.md.

**Wie vermeiden:** Scope-Beschränkung als eigener Einschränkungs-Bullet: "Scope: Nur agent/*.md — kein Zugriff auf soul/*.md, identity/*.md oder skills/*. Wenn Soul oder Skills als Problem identifiziert, als Issue im Report nennen und auf entsprechende Skills verweisen (/elvis-soul-generator, /elvis-skill-generator)."

**Warnzeichen:** Ausführungsschritte erwähnen soul/ oder skills/ Verzeichnisse als Schreib-Ziele.

### Pitfall 5: Library-Manager fehlt Approval-Gate vor strukturellen Änderungen

**Was schiefgeht:** Library-Manager inventarisiert und reorganisiert ohne Halt-Punkt — Umkategorisierungen passieren automatisch.

**Warum es passiert:** Library-Manager fühlt sich wie ein Analyse-Tool an (ähnlich System-Analyzer). Tatsächlich schreibt er Änderungen vor.

**Wie vermeiden:** Approval-Gate explizit NACH Analyse und VOR Änderungsausgabe: "[APPROVAL-GATE] Vorgeschlagene Änderungen als Tabelle präsentieren (Aktion, Objekt, Begründung) — auf Operator-Bestätigung warten bevor eine einzige Änderungs-Anweisung ausgegeben wird."

**Warnzeichen:** Ausführungsschritte zeigen keine "[APPROVAL-GATE]"-Markierung vor dem Änderungs-Output.

### Pitfall 6: Approval-Gate nur in Einschränkungen (aus Phase 1 geerbt)

Unverändertes Pitfall aus Phase 1 — weiterhin gültig für alle 7 neuen Skills. Gate MUSS als nummerierter Ausführungsschritt erscheinen. Nur-Einschränkungen-Placement = LLM ignoriert den Halt.

---

## Code Examples

Alle Beispiele aus existierenden Projektdateien — keine externen Quellen.

### Orchestrierungs-Konzept-Preview (Agent-Creator Approval-Gate Inhalt)

```markdown
**Konzept-Vorschau — Agent-Creator:**

| Element | Entwurf |
|---------|---------|
| Agent-Name | [star-trek-name] |
| Mission | [1 aktionsorientierter Satz] |
| Soul-Typ | soul/[name].md (bestehend) oder [neuer Archetyp] |
| Identity-Charakter | [Star Trek Referenz + 1-Satz-Skizze] |
| Kern-Skills | /elvis-[a], /elvis-[b], /elvis-[c] (3–5 Skills) |

Bitte bestätigen ("ok") um Soul, Identity und Agent zu generieren.
```

### Safeguard-Quartet Agent-Creator (Einschränkungen-Block)

```markdown
## Einschränkungen

- **Max-Limit:** Max. 1 kompletter Agent pro Durchlauf. Soul + Identity + Agent sind
  eine untrennbare Einheit — kein Partial-Output (nur Soul ohne Agent ist kein valider Abschluss).
- **Approval-Gate:** Einmaliger Halt nach Konzept-Entwurf (Schritt 3): Gesamtplan
  präsentieren und auf explizite Operator-Bestätigung ("ok", "bestätigt") warten.
  Soul, Identity und Agent werden danach intern sequentiell ohne weitere Halte generiert.
- **Stop-Bedingung:** Regulär wenn vollständiges 3-Datei-Paket generiert und vom Operator
  freigegeben wurde. Vorzeitig wenn Operator explizit abbricht ("stop", "abbrechen") oder
  wenn nach 3 Revisionsversuchen am Konzept-Entwurf keine Einigung erzielt wird.
- **Rollback-Hinweis:** Wenn eine der 3 Definitionen nicht dem Template entspricht, den
  fehlerhaften Teil (Soul, Identity oder Agent) vollständig neu generieren — nicht iterativ
  korrigieren. Konzept-Entwurf aus Schritt 3 als Basis behalten.
```

### Safeguard-Quartet Analyse-Skills (System-Analyzer / Ecosystem-Health)

```markdown
## Einschränkungen

- **Max-Limit:** Max. 1 vollständige Analyse pro Durchlauf.
- **Approval-Gate:** [System-Analyzer] Operator-Freigabe wenn Analyse-Ergebnisse direkte
  System-Änderungen empfehlen — warte auf explizite Bestätigung bevor Empfehlungen
  als Aktions-Liste ausgegeben werden.
  [Ecosystem-Health] kein Approval-Gate notwendig — read-only Score-Output.
- **Stop-Bedingung:** Regulär wenn vollständiger Report / Score ausgegeben. Vorzeitig wenn
  Ökosystem-Dateien nicht zugänglich sind — fehlende Inputs dokumentieren.
- **Rollback-Hinweis:** Analyse und Score sind read-only — keine direkten Systemänderungen.
  Rollback nicht anwendbar.
```

### Skill-Expander Schrittstruktur (Kernausführung nach Approval-Gate)

```markdown
4. Nach Bestätigung: Generiere Variante 1 vollständig im 9-Sektionen-Format gemäß
   `templates/skill-template.md`. Alle 9 Sektionen müssen befüllt sein. D006-Konformität:
   jeder Ausführungsschritt enthält Menge, Format und Zeitangabe wo sinnvoll.
   Abgrenzung zum Basis-Skill muss in Beschreibung und Strategie explizit benannt sein.
5. Präsentiere Variante 1 im Volltext — warte auf Freigabe oder Korrektur.
   Bei Korrektur: max. 2 Versuche, dann als "Offen" markieren und weiter zu Variante 2.
6. Wiederhole Schritte 4–5 für jede weitere Variante (max. 5 gesamt).
   Zähle explizit: "Variante [N/Gesamt] abgeschlossen."
```

### Agent-Optimizer Schwächen-Report (Approval-Gate Inhalt)

```markdown
**Schwächen-Report — Agent: [name]**

| # | Issue | Typ | Schwere | Empfehlung |
|---|-------|-----|---------|-----------|
| 1 | Capability "denkt logisch" (Identity-Merkmal) | Format | mittel | Ersetzen durch ausführbare Fähigkeit |
| 2 | Soul-Referenz soul/builder.md — Datei existiert nicht | Querverweis | kritisch | soul/builder.md erstellen oder bestehenden Soul verwenden |
| 3 | Constraints enthalten keine Max-Limit-Angabe | Safeguard | niedrig | Max-Limit-Constraint hinzufügen |

Soll ich die optimierte Version auf Basis dieser Analyse generieren? ("ok" / "abbrechen")
```

---

## State of the Art

| Alter Ansatz | Aktueller Ansatz | Wann geändert | Impact |
|--------------|------------------|---------------|--------|
| Drei Approval-Gates für zusammengesetzte Agent-Workflows | Ein Approval-Gate auf Konzept-Ebene | CONTEXT.md Phase-2-Entscheidung | Flow-Effizienz, <2-Minuten-Constraint erfüllbar |
| Safeguards nur in Einschränkungen | Approval-Gate als nummerierter Ausführungsschritt | Phase-1-Entscheidung (CONTEXT.md) | LLM behandelt Gate als Halt statt Hinweis |
| Analyse-Skills ohne Scope-Trennung | Ecosystem-Health (Score) vs. System-Analyzer (Deep-Dive) als separete Skills | CONTEXT.md Phase-2-Entscheidung | Klare Arbeitsteilung, kein Feature-Overlap |

---

## Open Questions

1. **Command-Router Update**
   - Was wir wissen: Router-Tabelle referenziert nur Phase-1-Skills. Phase 2 fügt 7 neue Skills hinzu. CONTEXT.md stellt Command-Router-Update als deferred/Phase-3 ein.
   - Was unklar ist: Soll der Router-Skill als separater Task in Phase 2 aktualisiert werden, oder erst in Phase 3?
   - Empfehlung: Separater Update-Task in Phase 2 (Wave 2 oder als optionaler Task). Der Router funktioniert mit veralteter Tabelle aber leitet keine Phase-2-Skills korrekt. Wenn Phase 3 lange dauert, ist der Router in der Zwischenzeit unvollständig.

2. **Agent-Creator: Neue Soul vs. Bestehende Soul**
   - Was wir wissen: Agent-Creator entwirft im Konzept-Schritt einen Soul-Typ. Es gibt 9 bestehende Souls in soul/. Manche Anforderungen passen zu bestehenden Souls, andere erfordern neue.
   - Was unklar ist: Wie soll Agent-Creator entscheiden ob er einen neuen Soul generiert oder einen bestehenden referenziert?
   - Empfehlung: Konzept-Schritt prüft explizit bestehende souls/ auf Passung ("Verfügbare Souls: [Liste]. Empfehlung: soul/creator.md — oder neuer Soul [Archetyp]?"). Operator entscheidet im Approval-Gate.

---

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | Kein Testrunner — reines Markdown-Projekt ohne ausführbaren Code |
| Config file | none |
| Quick run command | Manuelle Verifikation anhand der Verifikations-Kriterien im Skill |
| Full suite command | Manuelle Vollprüfung aller 7 neuen Skill-Dateien gegen Safeguard-Checkliste |

### Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| META-04 | Agent-Creator erzeugt vollständiges 3-Datei-Paket (Soul + Identity + Agent) nach einem Approval-Gate | manual | Prüfe: 1 Approval-Gate in Ausführungsschritten, Soul/Identity/Agent je vollständig nach Template, Abschluss mit 3 Dateipfaden | ❌ Wave 0 |
| META-05 | Skill-Expander erzeugt bis zu 5 vollständige Skill-Definitionen im 9-Sektionen-Format | manual | Prüfe: Basis-Skill als Input dokumentiert, max. 5 Varianten, jede Variante hat 9 Sektionen, D006-konform | ❌ Wave 0 |
| META-06 | System-Analyzer erzeugt strukturierten Report mit Schweregrad-Einstufung | manual | Prüfe: Report enthält Schweregrad-Kategorien (kritisch/mittel/niedrig), Querverweise geprüft, Handlungsempfehlungen konkret | ❌ Wave 0 |
| META-07 | Library-Manager produziert kategorisierten Katalog, Approval-Gate vor Änderungen | manual | Prüfe: Approval-Gate als nummerierter Schritt vor Änderungs-Output, max. 10 Änderungen, Katalog-Format als Tabelle | ❌ Wave 0 |
| META-09 | Ecosystem-Health produziert 0-100-Score mit Breakdown nach 4 Kategorien | manual | Prüfe: Score 0-100, 4 Kategorien mit Teilpunkten, benannte Issues mit Zähler, keine Handlungsempfehlungen (nur Score) | ❌ Wave 0 |
| META-10 | Agent-Optimizer liest Agent-Definition und produziert optimierte Version | manual | Prüfe: Scope auf agent/*.md, Schwächen-Report als Approval-Gate-Inhalt, Vorher/Nachher-Vergleich im Output | ❌ Wave 0 |
| META-12 | Concept-Design produziert Konzept-Dokument (kein fertiger Agent) | manual | Prüfe: Output enthält Mission + Soul-Empfehlung + Skill-Bedarf + Machbarkeits-Einschätzung, kein agent/*.md Output | ❌ Wave 0 |

**Gemeinsame Safeguard-Prüfung (für alle 7 Skills):**

| Check | Prüfung |
|-------|---------|
| SAFE-01 | Einschränkungen-Block enthält "Max-Limit: Max. [N]" mit expliziter Zahl |
| SAFE-02 | Ein Ausführungsschritt enthält "[APPROVAL-GATE]" + "warte auf" |
| SAFE-03 | Stop-Bedingung hat zwei Varianten: regulär + vorzeitig |
| SAFE-04 | Rollback-Hinweis formuliert konkrete Operator-Handlung (nicht Systemaktion) |

### Sampling Rate
- **Per task commit:** Manuelle Checkliste: alle 4 Safeguards vorhanden? 9 Sektionen vorhanden? D006-Konformität in Ausführungsschritten?
- **Per wave merge:** Alle Skills des Waves + Querverweise zwischen Skills geprüft (Agent-Creator referenziert Templates korrekt)
- **Phase gate:** Manueller Smoke-Test — Beschreibung jedes der 7 Skills prüfen ob er den Anforderungen aus CONTEXT.md entspricht, vor `/gsd:verify-work`

### Wave 0 Gaps
- [ ] Keine Test-Infrastruktur nötig — Markdown-Projekt, rein manuelle Verifikation

*(Kein Test-Framework-Setup nötig — Markdown-Projekt)*

---

## Sources

### Primary (HIGH confidence)
- `skills/meta/elvis-skill-generator.md` — Gold Standard für Safeguard-Quartet-Pattern, Approval-Gate als nummerierter Schritt, D006-Konformität
- `skills/meta/elvis-agent-generator.md` — Querverweisvalidierung-Pattern für Agent-Creator und Agent-Optimizer
- `templates/soul-template.md` — Bindende 6-Sektionen-Struktur, Agent-Creator generiert intern nach dieser Vorlage
- `templates/identity-template.md` — Bindende 7-Sektionen-Struktur, Agent-Creator generiert intern nach dieser Vorlage
- `templates/agent-template.md` — Bindende 7-Sektionen-Struktur, Agent-Creator + Agent-Optimizer
- `templates/skill-template.md` — Bindende 9-Sektionen-Struktur, Skill-Expander produziert nach dieser Vorlage
- `.planning/phases/02-composition-autonomous/02-CONTEXT.md` — Alle locked decisions, Max-Limit-Werte, Approval-Gate-Architektur
- `agent/q.md`, `agent/borg.md`, `agent/troi.md`, `agent/uhura.md` — Agent-Definitionen als Scope-Referenz für jeden Skills (Max-Limits aus Constraints, Operating Loops als Workflow-Basis)

### Secondary (MEDIUM confidence)
- `.planning/phases/01-generators-router/01-RESEARCH.md` — Phase-1-Pattern-Dokumentation (direkt übertragbar)
- `soul/*.md` — 9 bestehende Souls (für Agent-Creator Konzept-Schritt: Passung zu bestehendem Soul prüfen)

---

## Metadata

**Confidence breakdown:**
- Skill-Format und Templates: HIGH — alle Vorlagen-Dateien im Projekt vorhanden und geprüft
- Safeguard-Pattern: HIGH — Gold Standard (elvis-skill-generator.md) ist kanonisch und vollständig
- Orchestrierungs-Pattern (Agent-Creator): HIGH — vollständig in CONTEXT.md spezifiziert
- Analyse-Pattern (Ecosystem-Health Score-Gewichtung): MEDIUM — Gewichtung ist Claude's Discretion, kein kanonisches Vorbild
- Agent-Optimizer Scope-Abgrenzung: HIGH — CONTEXT.md ist explizit (nur agent/*.md)

**Research date:** 2026-03-14
**Valid until:** 2026-06-14 (stabiles Markdown-Projekt — keine Versionsabhängigkeiten)
