# Phase 1: Generators + Router - Research

**Researched:** 2026-03-14
**Domain:** Markdown-based skill authoring — Meta-Skill design, Safeguard patterns, routing logic
**Confidence:** HIGH

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**Generator-Granularität**
- Soul-Generator: 1 Soul pro Aufruf. Keine Batch-Variante.
- Identity-Generator: 1 Identity pro Aufruf. Keine Batch-Variante.
- Agent-Generator: 1 Agent pro Aufruf. Keine Batch-Variante.
- Begründung: Souls/Identities/Agents sind inhaltlich dichter — Batch würde zu Qualitätsverlust führen.

**Router-Verhalten**
- `/elvis-command-router` arbeitet mit statischer Routing-Tabelle: Keyword → Agent + Skill-Chain.
- Routing-Tabelle ist explizit im Skill-Body definiert — kein NLP, kein intelligentes Matching.
- Bei Mehrdeutigkeit: 2–3 passendste Routen listen, Operator fragt werden. Kein automatisches Raten.
- Bei unbekannten Anfragen: "Keine Route gefunden" + vollständige Routing-Tabelle als Hilfe ausgeben.
- Router KENNT die Routes; Command-Dateien (Phase 3) sind die formale Deklaration davon.

**Safeguard-Abstufung**
- Alle 4 Safeguards (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback) sind Pflicht für JEDEN der 4 neuen Meta-Skills — keine Ausnahmen.
- Max-Limit-Werte: Soul-Generator = 1, Identity-Generator = 1, Agent-Generator = 1, Command-Router = 5 Routing-Entscheidungen pro Durchlauf.
- Approval-Gate MUSS als nummerierter Ausführungsschritt erscheinen (nicht nur in Einschränkungen).

**Orchestrierung & Skill-Kommunikation**
- Jeder Generator-Skill dokumentiert in "Abhängigkeiten" explizit welche Vorgänger-Skills empfohlen sind.
- Output-Format jedes Generators ist so definiert, dass der nächste Skill in der Chain ihn direkt konsumieren kann.
- Dependency-Chain für Phase 2: Agent-Creator braucht Outputs von Soul-Generator + Identity-Generator + Agent-Generator — diese Chain muss in Abhängigkeiten sauber dokumentiert sein.
- Command-Router referenziert ALLE Meta-Skills in seiner Routing-Tabelle.

### Claude's Discretion
- Exakte Formulierungen der Ausführungsschritte (solange D006-konform: Menge, Format, Zeitangabe)
- Reihenfolge der Ausführungsschritte innerhalb jedes Generators
- Verifikations-Kriterien im Detail (solange Failure-Indikator und Akzeptanzkriterium enthalten)

### Deferred Ideas (OUT OF SCOPE)
None — discussion stayed within phase scope
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| META-01 | User kann mit `/elvis-soul-generator` eine neue Soul-Definition generieren die dem Template entspricht | Soul-Template hat 6 Sektionen; Generator muss Plan→Approve→Execute-Pattern from skill-generator Gold Standard anwenden |
| META-02 | User kann mit `/elvis-identity-generator` eine neue Identity-Definition generieren die dem Template entspricht | Identity-Template hat 7 Sektionen; Identity≠Agent-Unterscheidung muss in Verifikation enthalten sein |
| META-03 | User kann mit `/elvis-agent-generator` eine neue Agent-Definition generieren die dem Template entspricht | Agent-Template hat 7 Sektionen; Querverweise (Soul-Datei, Skills-Liste) müssen auf Validität geprüft werden |
| META-08 | User kann mit `/elvis-command-router` Anfragen an den richtigen Agent + Skill-Chain routen (Picard) | Statische Routing-Tabelle im Skill-Body; Mehrdeutigkeits- und Unbekannt-Handling definiert |
| SAFE-01 | Alle autonomen Meta Skills haben Max-Limit pro Durchlauf (≤ 10) | Konkrete Werte: 1/1/1/5 für die vier Skills; muss in Einschränkungen als harte Zahl stehen |
| SAFE-02 | Alle autonomen Meta Skills haben Approval-Gate als nummerierter Ausführungsschritt | Gate als expliziter Schritt im Ausführungsschritte-Block, nicht nur in Einschränkungen |
| SAFE-03 | Alle autonomen Meta Skills haben explizite Stop-Bedingung | Zwei Stop-Bedingungen pro Skill: reguläre Abschluss-Bedingung + vorzeitige Abbruch-Bedingung |
| SAFE-04 | Alle autonomen Meta Skills haben Rollback-Hinweis | Benannte Rollback-Aktion mit konkreter Anweisung (was der Operator tun soll) |
</phase_requirements>

---

## Summary

Phase 1 erstellt 4 neue Markdown-Skill-Dateien: `/elvis-soul-generator`, `/elvis-identity-generator`, `/elvis-agent-generator`, `/elvis-command-router`. Das Projekt ist ein reines Markdown-Authoring-Projekt — kein Code, keine Bibliotheken, kein Runtime. Die "Technologie" ist das etablierte 9-Sektionen-Skill-Format mit D006-Konformität (konkrete Mengen, Formate, Zeitangaben in jedem Ausführungsschritt).

Der Gold Standard für alle 4 Skills ist `/skills/meta/elvis-skill-generator.md`. Dieses File demonstriert das vollständige Safeguard-Quartet in Praxis: Max-Limit in Einschränkungen, Approval-Gate als nummerierter Schritt, zwei Stop-Bedingungen, Rollback-Hinweis. Der entscheidende Unterschied zu Standard-Skills: das Approval-Gate erscheint als expliziter nummerierter Ausführungsschritt (z.B. "Schritt 2: Präsentiere Übersicht — warte auf Bestätigung"), nicht nur als passive Einschränkung. Dies ist die zentrale Qualitätsanforderung aus dem Context.

Für den Command-Router gilt ein abweichendes Muster: Er ist kein Generator (erzeugt keine Datei), sondern ein Routing-Mechanismus. Seine Ausführungsschritte folgen einer Match→Clarify→Route-Logik. Die statische Routing-Tabelle im Skill-Body ist die einzige Quelle der Wahrheit — Phase 3 Commands werden diese Tabelle formalisieren, der Router bleibt unabhängig davon.

**Primary recommendation:** Modelliere alle 4 Skills direkt nach `elvis-skill-generator.md` — übernimm die Struktur der Einschränkungen und die Plan→Approve→Execute-Schrittfolge, passe Inhalte und Max-Limit-Werte an die jeweilige Domäne an.

---

## Standard Stack

### Core — Skill-Dateien

| Komponente | Typ | Zweck | Warum bindend |
|-----------|-----|-------|---------------|
| `templates/skill-template.md` | Markdown-Template | 9-Sektionen-Struktur für alle Skills | Alle 81 existierenden Skills folgen diesem Format |
| `templates/soul-template.md` | Markdown-Template | 6-Sektionen Soul-Struktur | Soul-Generator muss Output genau nach dieser Vorlage erzeugen |
| `templates/identity-template.md` | Markdown-Template | 7-Sektionen Identity-Struktur | Identity-Generator muss Output genau nach dieser Vorlage erzeugen |
| `templates/agent-template.md` | Markdown-Template | 7-Sektionen Agent-Struktur | Agent-Generator muss Output genau nach dieser Vorlage erzeugen |
| `skills/meta/elvis-skill-generator.md` | Gold-Standard-Skill | Referenz-Implementierung für Meta-Skills mit vollem Safeguard-Quartet | Direktes Vorbild für Schrittstruktur und Einschränkungsformulierungen |

### Keine externen Abhängigkeiten

Dieses Projekt hat keinen Build-Prozess, keine npm-Pakete, keine API-Calls. Alle "Libraries" sind die Markdown-Templates im `templates/`-Verzeichnis.

---

## Architecture Patterns

### Empfohlene Dateistruktur (Output dieser Phase)

```
skills/meta/
├── elvis-skill-generator.md      ← bereits vorhanden (Gold Standard)
├── elvis-soul-generator.md       ← NEU (META-01)
├── elvis-identity-generator.md   ← NEU (META-02)
├── elvis-agent-generator.md      ← NEU (META-03)
└── elvis-command-router.md       ← NEU (META-08)
```

### Pattern 1: Generator-Skill (Plan→Approve→Execute)

**Was:** Ein Meta-Skill der Markdown-Definitionen generiert. Besteht aus zwei Phasen: Planung (Vorschau zeigen, warten) und Ausführung (generieren nach Bestätigung).

**Wann verwenden:** Immer wenn der Skill eine neue Datei oder Definition erzeugt (Soul, Identity, Agent).

**Zentrale Eigenschaft:** Das Approval-Gate erscheint als NUMMERIERTER SCHRITT in Ausführungsschritte — nicht nur als Bullet in Einschränkungen. Ohne dieses Muster interpretiert das LLM den Gate als optionalen Hinweis.

**Schrittstruktur (abgeleitet aus elvis-skill-generator.md):**
```
1. Anforderung lesen + Limit prüfen
2. [APPROVAL-GATE] Vorschau präsentieren — auf explizite Bestätigung warten
3. Generierung ausführen (Section-by-Section nach Template)
4. Output präsentieren — auf Freigabe oder Korrektur warten
5. Abschluss-Zusammenfassung + manueller Speicher-Hinweis
```

**Safeguard-Quartet-Platzierung (wie in elvis-skill-generator.md):**
```
## Einschränkungen
- **Max-Limit:** Max. [N] [Einheiten] pro Durchlauf. [Overflow-Handling]
- **Approval-Gate:** [Gate-Beschreibung] — wartet auf "[explizites Keyword]"
- **Stop-Bedingung:** Endet regulär wenn [Bedingung]. Endet vorzeitig wenn [Bedingung 1] oder [Bedingung 2].
- **Rollback-Hinweis:** [Konkrete Anweisung was Operator tun soll wenn Output falsch]
```

### Pattern 2: Router-Skill (Match→Clarify→Route)

**Was:** Ein Meta-Skill der eingehende Anfragen gegen eine statische Tabelle matcht und an den richtigen Skill-Chain leitet.

**Wann verwenden:** Command-Router (META-08). Kein Generator — erzeugt keine Datei.

**Routing-Tabellen-Struktur (im Skill-Body, Abschnitt Strategie oder Ausführungsschritte):**
```markdown
| Keyword / Anfrage-Typ | Agent | Skill-Chain |
|----------------------|-------|-------------|
| Soul erstellen       | Picard → Elvis-Soul-Generator | /elvis-soul-generator |
| Identity erstellen   | Picard → Identity-Generator | /elvis-identity-generator |
| Agent erstellen      | Picard → Agent-Generator | /elvis-agent-generator |
| Skills generieren    | Elvis → Skill-Generator | /elvis-skill-generator |
| ...                  | ...   | ... |
```

**Schrittstruktur Router:**
```
1. Anfrage lesen + gegen Routing-Tabelle matchen
2. Wenn eindeutig: Route + Agent + Skill-Chain ausgeben
3. Wenn mehrdeutig: 2–3 Kandidaten listen, Operator nach Auswahl fragen [APPROVAL-GATE]
4. Wenn unbekannt: "Keine Route gefunden" + vollständige Tabelle ausgeben
5. Nach Bestätigung: Routing-Anweisung mit konkretem Aufruf-Befehl ausgeben
```

### Pattern 3: D006-Konformität in Ausführungsschritten

**Was:** Jeder Ausführungsschritt enthält drei Elemente wo sinnvoll: Menge (wie viele), Format (was für ein Objekt/Struktur), Zeitangabe (wann/wie lange).

**Beispiel gut (D006-konform):**
> "Lies die Anforderung des Operators. Prüfe: Entspricht die Beschreibung einer gültigen Soul-Definition (hat Philosophie, Core Values, mindestens 3 Operating Principles)? Wenn nicht, gib innerhalb von 1 Satz Anweisung zurück was fehlt."

**Beispiel schlecht (nicht D006-konform):**
> "Analysiere die Anforderung."

### Anti-Patterns to Avoid

- **Approval-Gate nur in Einschränkungen:** Der Gate wird vom LLM als Hinweis gelesen, nicht als Halt. Es MUSS ein nummerierter Schritt sein mit dem Wort "warte".
- **Rollback als vages Prinzip:** "Bei Fehler: Prozess neu starten" ist kein Rollback. Korrekt: "Wenn generierter Output nicht dem Template entspricht, verwirf ihn vollständig und sende die Original-Anforderung erneut — korrigiere nicht iterativ."
- **Stop-Bedingung ohne zwei Varianten:** Jeder Skill braucht zwei Stop-Bedingungen: reguläre Vollendung UND vorzeitiger Abbruch (Operator-Befehl oder technisches Scheitern nach N Versuchen).
- **Abhängigkeiten ignorieren:** Jeder Generator-Skill muss in "Abhängigkeiten" dokumentieren welche anderen Generatoren als Vorgänger empfohlen sind (für Phase-2-Chain).
- **Querverweise nicht validieren:** Der Agent-Generator muss prüfen ob der referenzierte Soul und die referenzierten Skills tatsächlich im Ökosystem existieren. Ungeprüfte Referenzen sind ein Fehlertyp.
- **Identity und Agent vermischen:** Der Identity-Generator generiert WER (Persönlichkeit). Der Agent-Generator generiert WAS (Aufgaben, Skills). Verifikations-Kriterien müssen diesen Unterschied aktiv prüfen.

---

## Don't Hand-Roll

| Problem | Nicht neu bauen | Verwende stattdessen | Warum |
|---------|-----------------|---------------------|-------|
| Soul-Struktur definieren | Eigene Sektionen erfinden | `templates/soul-template.md` — 6 Sektionen bindend | Template ist bereits validiert, Querverweise im Ökosystem erwarten dieses Format |
| Identity-Struktur definieren | Abweichende Sektionen | `templates/identity-template.md` — 7 Sektionen bindend | Identities referenzieren Star Trek Zeichen — Template ist kanonisch |
| Agent-Struktur definieren | Eigene Mission/Capability-Definitionen | `templates/agent-template.md` — 7 Sektionen bindend | Agents haben feste Primärer-Soul-Referenz — Format nicht ändern |
| Safeguard-Formulierungen | Neue Safeguard-Sprache entwickeln | `skills/meta/elvis-skill-generator.md` Einschränkungs-Block als Vorlage | Konsistenz im gesamten Ökosystem ist wichtiger als Variation |
| Approval-Gate-Pattern | Neue Halt-Logik erfinden | Nummerierter Schritt "Präsentiere X — warte auf Bestätigung" aus skill-generator übernehmen | Getestetes Pattern das tatsächlich als Halt-Punkt funktioniert |

---

## Common Pitfalls

### Pitfall 1: Approval-Gate landet in Einschränkungen statt in Ausführungsschritten

**Was schiefgeht:** Gate steht nur als Bullet in `## Einschränkungen`. LLM behandelt es als passive Richtlinie — überspringt ihn bei Geschwindigkeit.

**Warum es passiert:** Einschränkungen fühlen sich wie der "richtige Ort" für Regeln an. Aber Ausführungsschritte sind was das LLM sequentiell abarbeitet.

**Wie vermeiden:** SAFE-02 explizit: Gate muss als nummerierter Schritt erscheinen UND in Einschränkungen. Beide Stellen, nicht nur eine.

**Warnzeichen:** Wenn der Approval-Gate-Schritt kein "warte auf" / "warte auf explizite Bestätigung" Formulierung enthält.

### Pitfall 2: Rollback ist ein Prinzip statt eine Anweisung

**Was schiefgeht:** "Bei Fehler: Skill neu starten." Operator weiß nicht was er konkret tun soll.

**Warum es passiert:** Rollback wird als Kontroll-Mechanismus gedacht statt als Operator-Anweisung.

**Wie vermeiden:** Rollback immer aus Operator-Perspektive formulieren: "Wenn [Situation], dann [konkrete Handlung des Operators]."

**Warnzeichen:** Rollback-Text hat kein Subjekt oder beschreibt was das System tut statt was der Operator tut.

### Pitfall 3: Agent-Generator validiert Querverweise nicht

**Was schiefgeht:** Generator erzeugt Agent-Definition mit `soul/strategist.md` Referenz, aber Operator wollte einen neuen Soul — der noch nicht existiert.

**Warum es passiert:** Generator nimmt Input-Anforderung und setzt direkt in Template ein ohne zu prüfen ob referenzierte Dateien existieren.

**Wie vermeiden:** Ausführungsschritt: "Prüfe ob alle in der Anforderung genannten Souls und Skills im Ökosystem existieren. Liste fehlende Referenzen auf und frage den Operator ob diese zuerst erstellt werden sollen."

**Warnzeichen:** Abhängigkeits-Abschnitt enthält keine Querverweisvalidierung.

### Pitfall 4: Identity-Generator erzeugt Agenten-Beschreibungen

**Was schiefgeht:** Identity-Generator füllt Charakter-Beschreibung mit Aufgaben ("analysiert Daten, plant Strategien") statt Persönlichkeit.

**Warum es passiert:** Identity/Agent-Trennung ist eine der häufigsten Fehlerquellen im Ökosystem (templates warnen explizit davor).

**Wie vermeiden:** Verifikations-Kriterium im Identity-Generator: "Failure-Indikator: Wenn Charakter-Beschreibung oder Persönlichkeitsmerkmale Verben wie 'analysiert', 'erstellt', 'plant' enthalten statt Charaktereigenschaften — Output ist ungültig."

**Warnzeichen:** Charakter-Beschreibung enthält stellenbeschreibungs-artige Formulierungen.

### Pitfall 5: Router-Tabelle referenziert Phase-3-Commands statt Skills

**Was schiefgeht:** Routing-Tabelle zeigt `/build-agent` (Phase 3 Command) als Ziel — aber Commands existieren noch nicht in Phase 1.

**Warum es passiert:** Router KENNT die Routes, Commands sind die formale Deklaration. Die Tabelle muss auf Skills zeigen, nicht auf Commands.

**Wie vermeiden:** Routing-Tabelle zeigt immer auf Skills (`/elvis-*`) und Agenten, nicht auf Commands. Commands sind zukünftige Aufrufer des Routers.

---

## Code Examples

Alle Beispiele sind aus existierenden Dateien im Projekt — keine externen Quellen.

### Safeguard-Quartet (aus elvis-skill-generator.md, Einschränkungen)

```markdown
## Einschränkungen

- **Max-Limit:** Max. 10 neue Skills pro Durchlauf. Anforderungen über 10 Skills werden in mehrere
  Durchläufe aufgeteilt. Der Operator wird darauf hingewiesen bevor der erste Skill generiert wird.
- **Approval-Gate:** Vor der Erstellung eines jeden Skills zeigt der Generator die geplante Skill-Übersicht
  (Name, Kategorie, 1-Satz-Beschreibung) und wartet auf explizite Operator-Bestätigung ("bestätigt" oder
  "ok"). Kein Skill wird ohne Bestätigung erstellt.
- **Stop-Bedingung:** Der Prozess endet regulär wenn alle angeforderten Skills erstellt und vom Operator
  bestätigt wurden. Der Prozess endet vorzeitig wenn der Operator explizit abbricht ("stop", "abbrechen")
  oder wenn nach 3 Iterationen auf einem Skill keine valide Anforderung formulierbar ist.
- **Rollback-Hinweis:** Wenn ein generierter Skill nicht den Anforderungen entspricht, die
  Original-Anforderung erneut senden — den fehlerhaften Skill nicht weiter anpassen.
```

### Approval-Gate als nummerierter Schritt (aus elvis-skill-generator.md, Ausführungsschritte)

```markdown
2. Erstelle für jeden angeforderten Skill (max. 10) einen Übersichts-Eintrag: Skill-Name im `/elvis-*`-Format,
   Kategorie, 1-Satz-Beschreibung des Zwecks. Präsentiere die vollständige Übersichts-Tabelle an den Operator
   und warte auf explizite Bestätigung.
```

Muster: Schritt endet mit "warte auf explizite Bestätigung" — das ist der Halt-Punkt.

### Angepasste Max-Limits für Phase-1-Skills

```markdown
# Soul-Generator
- **Max-Limit:** Max. 1 Soul pro Durchlauf. Der Soul-Generator ist für Einzel-Generierung ausgelegt —
  jede Anforderung endet mit genau einer vollständigen Soul-Datei oder einem dokumentierten Abbruch.

# Identity-Generator
- **Max-Limit:** Max. 1 Identity pro Durchlauf. Identities sind zu nuancenreich (Charakter, Stil,
  Stärken/Schwächen) für sinnvolles Batching — Qualität erfordert Einzelbehandlung.

# Agent-Generator
- **Max-Limit:** Max. 1 Agent pro Durchlauf. Jede Agent-Referenz (Soul, Skills) muss einzeln
  auf Validität geprüft werden — Batch würde unkontrollierte Referenz-Fehler erzeugen.

# Command-Router
- **Max-Limit:** Max. 5 Routing-Entscheidungen pro Durchlauf. Einzelne Anfragen die mehr als
  5 Routen berühren werden aufgeteilt und sequentiell abgearbeitet.
```

### Soul-Template Sektionsübersicht (bindend für Soul-Generator Output)

```markdown
## Name          ← Einzelnes englisches Substantiv/Adjektiv, Kleinbuchstaben
## Philosophie   ← 2–4 Sätze Weltanschauung (kein Aufgaben-Beschrieb)
## Core Values   ← 3–5 Bullet Points, jeder Wert mit konkreter Verhaltens-Ausprägung
## Operating Principles  ← 3–5 konkrete Handlungsprinzipien (was immer/nie getan wird)
## Success Metrics  ← 3–5 messbare Erfolgs-Indikatoren aus Soul-Perspektive
## Geeignet für  ← Agenten-Typen und Einsatzgebiete
```

### Identity-Template Sektionsübersicht (bindend für Identity-Generator Output)

```markdown
## Name                     ← Star Trek Charakter-Name, Kleinbuchstaben
## Charakter-Beschreibung   ← 3–5 Sätze WER (nicht WAS — kein Aufgaben-Beschrieb)
## Persönlichkeitsmerkmale  ← 5–8 Bullet Points, beobachtbare Eigenschaften
## Kommunikationsstil       ← 3–5 konkrete Stil-Merkmale
## Stärken                  ← 4–6 persönlichkeitsbasierte Stärken
## Schwächen                ← 3–5 authentische Schwächen (Kehrseite der Stärken)
## Star Trek Referenz       ← 1 unverwechselbares Zitat oder charakteristische Szene
```

### Agent-Template Sektionsübersicht (bindend für Agent-Generator Output)

```markdown
## Name           ← Star Trek Charakter-Name (muss mit Identity übereinstimmen)
## Mission        ← Genau 1 Satz, aktionsorientiert (WAS, nicht WER)
## Capabilities   ← 5–8 konkrete ausführbare Fähigkeiten
## Operating Loop ← Nummerierte Liste — der wiederholbare Arbeitsprozess
## Constraints    ← Harte Grenzen der Autonomie (irreversible Aktionen, Scope)
## Primärer Soul  ← soul/[name].md (Querverweisformat bindend)
## Primäre Skills ← Bullet Points mit /elvis-[skill-name] (validierte Querverweise)
```

---

## State of the Art

| Alter Ansatz | Aktueller Ansatz | Wann geändert | Impact |
|--------------|------------------|---------------|--------|
| Safeguards nur in Einschränkungen | Approval-Gate als nummerierter Ausführungsschritt | Phase-1-Entscheidung (CONTEXT.md) | LLM behandelt Gate als Halt statt als Hinweis |
| Routing über Command-Dateien | Routing-Tabelle direkt im Router-Skill-Body | Phase-1-Entscheidung | Router unabhängig von Phase-3-Commands — phasenweise Umsetzung möglich |

---

## Open Questions

1. **Routing-Tabelle Vollständigkeit**
   - Was wir wissen: Router soll ALLE Meta-Skills referenzieren. Phase 1 liefert 4 neue Skills, Phase 2 liefert weitere ~10.
   - Was unklar ist: Soll die Routing-Tabelle in Phase 1 bereits Platzhalter für Phase-2-Skills haben, oder nur aktuelle Skills?
   - Empfehlung: Tabelle enthält nur Phase-1-Skills + bestehende Skills (skill-generator). Phase 2 aktualisiert die Tabelle. Platzhalter erzeugen falsche Routen.

2. **Naming-Konvention für neue Soul/Identity/Agent-Dateien**
   - Was wir wissen: Bestehende Souls liegen in `soul/[name].md`, Identities in `identity/[name].md`, Agents in `agent/[name].md`.
   - Was unklar ist: Generatoren geben Markdown-Text aus (kein automatisches Speichern). Wie explizit soll der Dateipfad-Hinweis im Output sein?
   - Empfehlung: Output jedes Generators endet mit konkretem Dateipfad-Hinweis: "Speichern unter: `soul/[name].md`". Konsistent mit skill-generator Pattern.

---

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | Kein Testrunner — reines Markdown-Projekt ohne ausführbaren Code |
| Config file | none |
| Quick run command | Manuelle Verifikation anhand der Verifikations-Kriterien im Skill |
| Full suite command | Manuelle Vollprüfung aller 4 neuen Skill-Dateien gegen Checkliste |

### Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| META-01 | Soul-Generator erzeugt valide Soul-Datei im 6-Sektionen-Format | manual | Manuelle Prüfung: Soul hat alle 6 Sektionen, keine [PFLICHTFELD]-Marker, Philosophie ≠ Aufgabenbeschreibung | ❌ Wave 0 |
| META-02 | Identity-Generator erzeugt valide Identity-Datei im 7-Sektionen-Format | manual | Manuelle Prüfung: Identity hat alle 7 Sektionen, Charakter-Beschreibung enthält keine Aufgaben-Verben | ❌ Wave 0 |
| META-03 | Agent-Generator erzeugt valide Agent-Datei im 7-Sektionen-Format | manual | Manuelle Prüfung: Agent hat alle 7 Sektionen, Soul-Querverweise valide, Skills-Querverweise valide | ❌ Wave 0 |
| META-08 | Command-Router matcht Anfragen korrekt gegen Routing-Tabelle | manual | Manuelle Prüfung: Routing-Tabelle vollständig, Mehrdeutigkeits-Handling dokumentiert, Unbekannt-Fall dokumentiert | ❌ Wave 0 |
| SAFE-01 | Alle 4 Skills haben Max-Limit mit konkreter Zahl (≤ 10) | manual | Prüfe Einschränkungen-Block auf "Max-Limit: Max. [N]" Muster mit expliziter Zahl | ❌ Wave 0 |
| SAFE-02 | Approval-Gate als nummerierter Schritt in Ausführungsschritte | manual | Prüfe ob ein Ausführungsschritt "warte auf" + explizites Bestätigungs-Keyword enthält | ❌ Wave 0 |
| SAFE-03 | Zwei Stop-Bedingungen: regulär + vorzeitig | manual | Prüfe Stop-Bedingung auf zwei Varianten (regulär/vorzeitig) mit je konkreter Bedingung | ❌ Wave 0 |
| SAFE-04 | Rollback-Hinweis als Operator-Anweisung formuliert | manual | Prüfe Rollback auf Operator-Perspektive: "Wenn X, dann [Operator-Aktion]" | ❌ Wave 0 |

**Hinweis:** Da dieses Projekt reines Markdown ist, sind alle Tests manuell. Keine Wave-0-Infrastruktur nötig — Tests sind Checklisten-Verifikation nach Erstellung jedes Skills.

### Sampling Rate
- **Per task commit:** Manuelle Checkliste: alle 4 Safeguards vorhanden? 9 Sektionen vorhanden? D006-Konformität in Ausführungsschritten?
- **Per wave merge:** Alle 4 Skills vollständig + Querverweise zwischen Skills geprüft (Router referenziert alle 3 Generatoren)
- **Phase gate:** Manueller Smoke-Test — jeden der 4 Skills mit einer Beispiel-Anforderung aufrufen und Output gegen Template validieren, vor `/gsd:verify-work`

### Wave 0 Gaps
- [ ] Verifikations-Checkliste für Meta-Skills (4 Safeguards + 9 Sektionen + D006) — wird als Teil von Wave 1 Task erstellt

*(Kein Test-Framework-Setup nötig — Markdown-Projekt)*

---

## Sources

### Primary (HIGH confidence)
- `skills/meta/elvis-skill-generator.md` — Gold Standard für Safeguard-Quartet-Pattern, Approval-Gate als nummerierter Schritt, D006-Konformität
- `templates/soul-template.md` — Bindende 6-Sektionen-Struktur für Soul-Generator Output, inkl. Beispiel (strategist)
- `templates/identity-template.md` — Bindende 7-Sektionen-Struktur für Identity-Generator Output, inkl. Beispiel (spock)
- `templates/agent-template.md` — Bindende 7-Sektionen-Struktur für Agent-Generator Output, inkl. Beispiel (worf)
- `.planning/phases/01-generators-router/01-CONTEXT.md` — Alle locked decisions, Max-Limit-Werte, Routing-Verhalten

### Secondary (MEDIUM confidence)
- `agent/picard.md` — Zeigt Safeguard-Quartet in Agent-Definition (leicht abweichendes Format von Skills — Constraints direkt mit Bullet-Labels)
- `templates/skill-template.md` — D006-Anforderungen explizit dokumentiert

---

## Metadata

**Confidence breakdown:**
- Skill-Format und Templates: HIGH — alle Dateien im Projekt vorhanden und geprüft
- Safeguard-Pattern: HIGH — Gold Standard (elvis-skill-generator.md) ist kanonisch und vollständig
- Routing-Tabellen-Design: HIGH — Entscheidungen in CONTEXT.md sind vollständig und eindeutig
- Querverweisvalidierung im Agent-Generator: MEDIUM — Muster ist logisch abgeleitet, kein direktes Vorbild im Ökosystem

**Research date:** 2026-03-14
**Valid until:** 2026-06-14 (stabiles Markdown-Projekt — keine Versionsabhängigkeiten)
