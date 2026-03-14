# Pitfalls Research

**Domain:** Markdown-basiertes Meta-Agent- und Command-System (Erweiterung eines bestehenden Ökosystems)
**Researched:** 2026-03-14
**Confidence:** HIGH — Basiert auf direkter Analyse des bestehenden Ökosystems (81 Skills, Templates, Safeguard-Anforderungen) kombiniert mit bekannten Mustern aus dem Bereich AI-Agent-Framework-Design.

---

## Critical Pitfalls

### Pitfall 1: Safeguard-Washing — Safeguards die keine sind

**What goes wrong:**
Meta- und Autonomous-Skills enthalten die vier Safeguard-Sektionen (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback) als Pflichtfelder, aber der Inhalt ist leer oder symbolisch. Ein Max-Limit von "max. 100 Skills" ist kein Limit. Ein Approval-Gate das lautet "Operator kann bei Bedarf eingreifen" ist kein Gate. Die Safeguards wirken strukturell vorhanden, greifen aber nicht.

**Why it happens:**
Der Generator (ein zukünftiger Meta-Skill) folgt dem Template-Format und befüllt alle Pflichtfelder — er optimiert auf Vollständigkeit, nicht auf Wirksamkeit. Ohne konkrete Zahlen und explizite Warte-Punkte degeneriert jeder Safeguard zur Floskel.

**How to avoid:**
Safeguard-Kriterien direkt im Template als Constraints definieren, nicht als Freitext-Felder. Konkret:
- Max-Limit muss eine Zahl <= 10 enthalten
- Approval-Gate muss das Trigger-Wort ("ok", "bestätigt") und den Warte-Punkt ("bevor Schritt X ausgeführt wird") benennen
- Stop-Bedingung muss mindestens zwei Bedingungen listen (regulär + vorzeitig)
- Rollback-Hinweis muss eine konkrete Aktion beschreiben, nicht "Fehler melden"

Verifikationskriterium bei der Skill-Erstellung: Jeder Safeguard-Bullet enthält mindestens eine Zahl oder ein Schlüsselwort aus der Menge {max., mindestens, nach N Versuchen, bevor, explizit}.

**Warning signs:**
- Einschränkungen-Sektion enthält ausschließlich "soll", "möglichst", "bei Bedarf"
- Approval-Gate-Formulierung ohne Warte-Punkt im Ausführungsschritt-Fluss
- Stop-Bedingung ohne explizites Trigger-Ereignis

**Phase to address:**
Skill-Generierungsphase (S07 Meta Skills) — das Template für Meta/Autonomous-Skills muss die Safeguard-Constraints als ausfüllbare Zahlenfelder definieren, bevor ein einziger autonomer Skill geschrieben wird.

---

### Pitfall 2: Command-Namespace-Kollision mit bestehenden Skills

**What goes wrong:**
Commands wie `/build-agent` oder `/generate-skills` sind konzeptionell neue Entitäten, aber ihre Namen können mit bestehenden `/elvis-*`-Skills überlappen oder verwechselt werden. Ein Operator ruft `/elvis-skill-generator` auf und erhält einen regulären Skill — erwartet aber das Command-System-Verhalten mit Orchestrierungs-Logik. Oder ein neuer Command heißt `/build-agent` und ein existierender Skill heißt `/elvis-agent-builder` — zwei Entitäten, gleiche Funktion, unterschiedliches Verhalten.

**Why it happens:**
Commands und Skills sind verschiedene Schichten des Systems, aber das Benennungssystem trennt sie nicht hart genug. Skills folgen `/elvis-*`, Commands folgen einem anderen Schema — aber wenn dieses Schema nicht explizit vorab festgelegt wird, entstehen bei der Generierung Kollisionen durch unbeabsichtigte Namens-Parallelität.

**How to avoid:**
Command-Naming-Convention explizit vorab definieren und von Skills abgrenzen. Vorschlag: Commands nutzen Verben ohne Prefix (`/build-agent`, `/generate-skills`) oder einen eigenen Prefix (`/cmd-build-agent`). Skills bleiben immer `/elvis-*`. Diese Regel muss in der Command-Template-Datei stehen und vor Generierung der Commands verabschiedet werden. Deduplizierungs-Check gegen alle 81+ bestehenden Skill-Namen vor der Command-Benennung.

**Warning signs:**
- Ein Command-Name beschreibt dieselbe Funktion wie ein existierender Skill-Name
- Commands-Verzeichnis enthält eine Datei die `/elvis-*` im Namen-Feld hat
- Operator fragt "Wann nutze ich `/build-agent` vs. `/elvis-agent-builder`?"

**Phase to address:**
Früheste Command-System-Phase (S07) — Naming-Convention für Commands muss als erste Entscheidung getroffen werden, bevor Commands generiert werden.

---

### Pitfall 3: Abstraktes Orchestrierungs-Verhalten ohne Ausführungsschritte

**What goes wrong:**
Meta-Skills wie ein "Picard Orchestrator" beschreiben was Orchestrierung bedeutet (koordiniert, delegiert, strategisch) aber nicht wie ein LLM den Skill konkret ausführt. Der Skill liest sich wie eine Persona-Beschreibung, nicht wie eine Arbeitsanweisung. Wenn der Operator `/picard-orchestrate` aufruft, weiß das Modell nicht welche Schritte es ausführen soll.

**Why it happens:**
Orchestrierung ist konzeptionell abstrakt — "delegiere an Spock für Research, dann an Data für Content". Das ist kein Ausführungsschritt. Das bestehende D006-Prinzip (Menge, Format, Zeitangabe in jedem Schritt) wurde für Content- und Growth-Skills entwickelt, lässt sich aber direkt auf Orchestrierungs-Skills anwenden — wird aber oft nicht angewendet weil Orchestrierung anders "anfühlt".

**How to avoid:**
Orchestrierungs-Skills müssen in den Ausführungsschritten explizit formulieren: Welcher Sub-Skill wird aufgerufen, mit welchem Input, in welcher Reihenfolge, unter welcher Bedingung, mit welchem erwarteten Output. Schritt-Format für Orchestrierung: "Rufe `/elvis-[skill]` auf mit Input [X]. Erwarte Output-Format [Y]. Wenn Output nicht vorliegt oder fehlerhaft: [Z]."

Verifikationskriterium: Jeder Ausführungsschritt eines Orchestrierungs-Skills nennt mindestens einen konkreten Sub-Skill-Namen.

**Warning signs:**
- Ausführungsschritte eines Meta-Skills enthalten keine `/elvis-*`-Referenzen
- Strategie-Sektion ist länger als Ausführungsschritte-Sektion bei einem Orchestrierungs-Skill
- Schritte enthalten nur Verben wie "analysiere", "koordiniere", "delegiere" ohne konkretes Ziel-Objekt

**Phase to address:**
S07 Meta Skills — Qualitätsprüfung vor Abschluss jedes Orchestrierungs-Skills: Ausführungsschritte müssen mindestens einen konkreten Sub-Skill-Namen enthalten.

---

### Pitfall 4: Autonome Borg/Q-Skills ohne Exit-Pfad bei Fehler

**What goes wrong:**
Ein Borg-Skill (Skill Expander) oder Q-Skill (Agent Creator) schlägt während einer mehrstufigen Ausführung fehl — z.B. bei Schritt 4 von 7. Der Rollback-Hinweis in der Einschränkungen-Sektion beschreibt was zu tun ist, aber der Ausführungsfluss enthält keine Fehlerbehandlung im Ablauf selbst. Das Modell führt weiter aus, springt zurück zu Schritt 1, oder hängt in einem impliziten Retry-Loop.

**Why it happens:**
Rollback-Hinweise werden als Sektion in "Einschränkungen" dokumentiert — ein passiver Hinweis für den Operator, kein aktiver Bestandteil des Ausführungsflusses. Der Ausführungsschritte-Abschnitt behandelt den Happy Path. Fehler-Pfade werden nicht in die Schritt-Sequenz integriert.

**How to avoid:**
Für alle Multi-Step-Autonomous-Skills (Borg, Q, Picard): Jeden Ausführungsschritt mit einer expliziten Fehler-Bedingung ausstatten. Format pro Schritt: "Wenn [Fehlerfall eintritt]: Stoppe sofort, ausgebe '[Status] fehlgeschlagen bei Schritt [N]', warte auf Operator-Anweisung." Der letzte Schritt eines jeden autonomen Skills muss immer ein Zusammenfassungs-Schritt sein der den Gesamtstatus ausgibt — auch bei vorzeitigem Abbruch.

**Warning signs:**
- Ausführungsschritte bei autonomen Skills enthalten kein "Wenn/Falls"-Konstrukt
- Rollback-Hinweis steht nur in "Einschränkungen", nicht als Schritt im Ausführungsfluss
- Kein dedizierter Abschluss-Schritt der Status + offene Punkte + nächste Aktion zusammenfasst

**Phase to address:**
S07 Meta Skills — gilt spezifisch für Borg, Q, Picard, Troi, Uhura als die fünf designierten autonomen Agenten.

---

### Pitfall 5: Command-Dateien als Skill-Duplikate

**What goes wrong:**
Das `commands/`-Verzeichnis enthält 10 Command-Definitionen. Wenn diese Commands lediglich Wrappers um bereits existierende Meta-Skills sind ("`/build-agent` ruft `/elvis-skill-generator` und `/elvis-agent-builder` auf"), ohne eigenständigen Mehrwert, dann sind Commands keine neue Schicht — sie sind Aliases. Das System hat dann 10 redundante Dateien und der Operator ist verwirrt was er aufrufen soll.

**Why it happens:**
Commands und Meta-Skills werden parallel geplant ohne klare Aufgabentrennung vorab. Commands fühlen sich "mächtiger" an und werden deshalb mit Orchestrierungs-Logik befüllt die eigentlich in die Meta-Skills gehört — oder umgekehrt werden Commands zu dünn und delegieren vollständig an Skills.

**How to avoid:**
Commands definieren vor der Skill-Generierungsphase. Commands sind keine Skills. Commands sind Einstiegspunkte für vollständige User-Workflows die mehrere Skills koordinieren. Ein Command hat immer: (1) einen klaren Anwendungsfall der sich von einzelnen Skills unterscheidet, (2) einen expliziten Orchestrierungs-Plan (welche Skills, in welcher Reihenfolge), (3) kein inhaltliches Duplikat zu einem einzelnen Skill. Wenn ein Command == ein einzelner Skill, dann ist es kein Command.

**Warning signs:**
- Command-Beschreibung ist inhaltlich identisch mit einem Meta-Skill
- Command-Ausführungsschritte listen nur einen einzigen Sub-Skill-Aufruf
- Commands-Verzeichnis enthält Dateien mit `/elvis-*` im Namen-Feld

**Phase to address:**
S07 (Planungsphase Commands) — Command-Architektur muss vor Skill-Generierung definiert sein.

---

## Technical Debt Patterns

Shortcuts die im Moment vernünftig wirken aber langfristige Probleme erzeugen.

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
|----------|-------------------|----------------|-----------------|
| Vage Safeguards ("max. viele") | Skill schneller generiert | Autonome Skills greifen unkontrolliert; Operator verliert Vertrauen ins System | Nie |
| Orchestrierungs-Skills ohne Sub-Skill-Referenzen | Skill bleibt flexibel | Nicht ausführbar; Operator weiß nicht welche Skills verwendet werden | Nie |
| Commands als Thin Wrappers | Commands schnell generiert | Redundante Dateien; Operator-Verwirrung; Wartungsaufwand doppelt | Nie bei 10 Commands — zu klein für Wrapper-Logik |
| Einheitliches Template für Meta- und Standard-Skills | Weniger Templates zu pflegen | Meta-Safeguard-Anforderungen nicht erzwingbar im Standard-Template | Akzeptabel wenn Meta-Template als Erweiterung existiert |
| Approval-Gate nur in Einschränkungen, nicht in Schritten | Kürzerer Ausführungsfluss | LLM überspringt Gate weil es nicht als Schritt-Halt im Fluss steht | Nie bei autonomen Skills |

---

## Integration Gotchas

Für dieses Projekt: "Integration" = Zusammenspiel zwischen Schichten (Skills → Meta-Skills → Commands → Agents).

| Integration | Common Mistake | Correct Approach |
|-------------|----------------|------------------|
| Meta-Skill → Sub-Skill | Sub-Skill-Output-Format ist nicht spezifiziert | Meta-Skill definiert explizit welches Output-Format er von jedem Sub-Skill erwartet |
| Command → Meta-Skill | Command übergibt keinen strukturierten Input | Command-Schritt 1 immer: Input-Parameter aufnehmen und strukturiert an Sub-Skill übergeben |
| Autonomous-Skill → Operator | Operator wird nicht über Teilergebnis informiert | Nach jedem autonomen Schritt: Zwischenstand ausgeben mit "Schritt N/Gesamt: [Status]" |
| Agent-Definition → Meta-Skill | Agent-Mapping (Star Trek → Funktion) stimmt nicht mit Meta-Skill-Zuordnung überein | Q = Agent Creator, Borg = Skill Expander, Picard = Orchestrator — Abweichungen sind Fehler |
| Skill-Template → Meta-Skill-Generator | Generator erfindet neue Sektionen oder benennt bestehende um | Template-Header-Namen sind bindend; Generator-Verifikationsschritt prüft exakte Übereinstimmung |

---

## Performance Traps

In diesem Markdown-System: "Performance" = Ausführungsqualität des LLM bei Skill-Interpretation.

| Trap | Symptoms | Prevention | When It Breaks |
|------|----------|------------|----------------|
| Zu viele Skills in einem Batch | LLM verliert Konsistenz ab Skill 6-7 in einer Generierungsrunde | Max-10-Limit konsequent einhalten; nie mehr als 10 Skills pro Durchlauf | Ab 11 Skills gleichzeitig |
| Überlange Ausführungsschritte | Schritte werden von LLM zu Paraphrase-Zusammenfassungen zusammengefasst statt ausgeführt | Jeden Schritt als einzelne, abgeschlossene Aktion formulieren; max. 4 Sätze pro Schritt | Wenn Schritt > 100 Wörter |
| Zu viele Cross-Skill-Referenzen in einem Meta-Skill | LLM verliert Kontext welcher Sub-Skill gerade aktiv ist | Max. 5 Sub-Skill-Referenzen pro Meta-Skill | Ab 6 Sub-Skills in einem Orchestrierungs-Skill |
| Mehrdeutige Persona-Beschreibungen in Agent-Definitionen | Agent verhält sich inkonsistent zwischen Sessions | Agent-Definition enthält konkrete Verhaltensregeln, nicht nur Charakterbeschreibung | Wenn Identity/Soul zu abstrakt ist |

---

## Security Mistakes

In diesem Kontext: Autonome Agents die unkontrolliert agieren können.

| Mistake | Risk | Prevention |
|---------|------|------------|
| Approval-Gate fehlt in autonomem Multi-Schritt-Skill | LLM führt alle Schritte ohne Operator-Input durch; irreversible Aktionen möglich | Approval-Gate als expliziter Schritt im Ausführungsfluss, nicht nur als Einschränkungs-Hinweis |
| Kein Max-Limit bei Skill-Expansions-Skill (Borg) | Borg-Skill generiert unbegrenzt neue Skills; Qualität sinkt; Duplikate entstehen | Max. 10 Skills pro Durchlauf, hardcodiert im Einschränkungen-Abschnitt als Zahl |
| Stop-Bedingung fehlt bei Q Agent Creator | Q-Skill erstellt rekursiv neue Agenten ohne Halt-Bedingung | Stop-Bedingung muss explizit Timer oder Mengen-Limit enthalten |
| Rollback ohne konkreten Wiederherstellungs-Pfad | Fehlerhafter autonomer Schritt kann nicht rückgängig gemacht werden | Rollback-Hinweis nennt immer: welche Dateien betroffen, welcher Zustand wiederhergestellt wird, wie |

---

## UX Pitfalls

Operator-Erfahrung bei der Nutzung des Systems.

| Pitfall | User Impact | Better Approach |
|---------|-------------|-----------------|
| Unklare Unterscheidung Skill vs. Command | Operator weiß nicht was er aufrufen soll | README-Einstiegsdatei mit klarer Schichtenübersicht: wann Skills, wann Commands |
| Skills ohne Abhängigkeits-Kette dokumentiert | Operator ruft Skill auf ohne nötigen Input, bekommt nutzlosen Output | Abhängigkeits-Sektion jedes Skills enthält explizite "Vorgänger-Skills"-Empfehlung |
| Meta-Skills ohne Beispiel-Output | Operator weiß nicht was er bekommt; Erwartungsmanagement fehlt | Output-Sektion jedes Meta-Skills beschreibt Beispiel-Struktur des erwarteten Ergebnisses |
| Zu viele Agents mit ähnlicher Funktion | Operator verwechselt Picard (Orchestrator) und Uhura (Library Manager) | Agent-Definitionen enthalten expliziten Abgrenzungs-Satz: "Im Unterschied zu [Agent X] fokussiert sich [dieser Agent] auf..." |
| Approval-Gate-Wording unklar | Operator weiß nicht welche Eingabe den Prozess fortsetzt | Jedes Approval-Gate nennt explizit die erwarteten Operator-Eingaben: ("ok", "bestätigt", "weiter") |

---

## "Looks Done But Isn't" Checklist

Dinge die abgeschlossen wirken aber kritische Teile missen.

- [ ] **Meta-Skill mit Safeguards:** Einschränkungen-Sektion enthält vier Safeguard-Punkte — aber Ausführungsschritte enthalten keinen Approval-Halt-Schritt. Prüfe: Gibt es einen nummerierten Schritt der explizit auf Operator-Input wartet?
- [ ] **Command-Datei erstellt:** Commands-Verzeichnis hat 10 Dateien — aber kein Command unterscheidet sich inhaltlich von einem einzelnen Meta-Skill. Prüfe: Jeder Command orchestriert mindestens 2 verschiedene Sub-Skills.
- [ ] **Borg-Skill generiert:** Borg-Skill hat Max-Limit-Formulierung — aber die Zahl ist > 10 oder fehlt ganz. Prüfe: Einschränkungen-Sektion enthält "max. [Zahl <= 10] Skills pro Durchlauf" als erste Bullet.
- [ ] **Rollback-Hinweis vorhanden:** Rollback-Hinweis steht in Einschränkungen-Sektion — aber kein Ausführungsschritt behandelt Fehler. Prüfe: Mindestens ein Schritt enthält "Wenn [Fehler]: stoppe und gib [Status] aus".
- [ ] **9 Sektionen vollständig:** Alle 9 Sektionen befüllt — aber [PFLICHTFELD]-Platzhalter sind im Inhalt. Prüfe: Kein [PFLICHTFELD]-Marker im generierten Skill vorhanden.
- [ ] **Command-Naming abgeschlossen:** Commands-Dateien erstellt — aber kein Naming-Convention-Dokument vorhanden. Prüfe: Commands haben konsistentes Schema das sich von `/elvis-*` unterscheidet.
- [ ] **Autonomer Skill "fertig":** Skill hat Stop-Bedingung dokumentiert — aber Stop-Bedingung enthält nur regulären Abschluss, kein vorzeitiges Abbruch-Szenario. Prüfe: Stop-Bedingung listet mindestens regulär + vorzeitig.

---

## Recovery Strategies

Wenn Pitfalls trotz Prävention auftreten.

| Pitfall | Recovery Cost | Recovery Steps |
|---------|---------------|----------------|
| Safeguard-Washing entdeckt (nach Generierung) | LOW | Einschränkungen-Sektion jedes betroffenen Skills neu schreiben; Zahlen einfügen; Approval-Gate-Schritt in Ausführungsschritte integrieren |
| Command-Namespace-Kollision | LOW | Kollidierende Command-Datei umbenennen; Naming-Convention-Dokument nachträglich erstellen; Referenzen in README aktualisieren |
| Orchestrierungs-Skill ohne Sub-Skill-Referenzen | MEDIUM | Ausführungsschritte komplett neu schreiben; mindestens ein konkreter Sub-Skill-Aufruf pro Schritt |
| Autonomer Skill ohne Exit-Pfad | MEDIUM | Fehler-Bedingungen als "Wenn/Falls"-Klauseln in jeden Schritt integrieren; Abschluss-Schritt hinzufügen |
| 10 Command-Duplikate aller Meta-Skills | HIGH | Commands komplett neu konzipieren; zuerst Differenzierungs-Architektur festlegen, dann neu generieren |

---

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase | Verification |
|---------|------------------|--------------|
| Safeguard-Washing | S07 Meta Skills (erster Schritt: Meta-Template mit Zahlen-Constraints) | Jeder autonome Skill: Einschränkungen-Sektion enthält mindestens 3 Zahlen |
| Command-Namespace-Kollision | S07 Commands (vor Generierung: Naming-Convention festlegen) | Deduplizierungs-Check Commands vs. alle 81+ Skill-Namen |
| Abstraktes Orchestrierungs-Verhalten | S07 Meta Skills (Qualitätsprüfung nach jedem Orchestrierungs-Skill) | Jeder Orchestrierungs-Schritt enthält `/elvis-*`-Referenz |
| Autonome Skills ohne Exit-Pfad | S07 Meta Skills (Template-Erweiterung für Borg/Q/Picard/Troi/Uhura) | Mindestens ein "Wenn Fehler: Stoppe"-Konstrukt pro autonomem Skill |
| Command-Dateien als Skill-Duplikate | S07 Commands (Architektur-Definition vor Generierung) | Kein Command hat identische Beschreibung wie ein existierender Skill |
| Approval-Gate nicht im Fluss | S07 Meta Skills (Schritt-Sequenz-Review) | Ausführungsschritte enthalten expliziten Warte-Punkt als nummerierten Schritt |
| Zu viele Cross-Skill-Referenzen | S07 Meta Skills (Komplexitäts-Limit) | Kein Meta-Skill referenziert mehr als 5 Sub-Skills |

---

## Sources

- Direktanalyse: `skills/meta/elvis-skill-generator.md` — bestehende Safeguard-Implementierung als Referenz-Baseline
- Direktanalyse: `.gsd/milestones/M001/M001-CONTEXT.md` — offizielle Safeguard-Anforderungen (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback)
- Direktanalyse: `templates/skill-template.md` — Template-Constraints und D006-Anforderungen
- Direktanalyse: Bestehendes Skill-Ökosystem (81 Skills) — Namenskonventionen, Format-Standards, Qualitätsniveau
- Bekannte AI-Agent-Framework-Muster: Recursive agent loops, safeguard theater, orchestration without grounding
- Konfidenz: HIGH — Pitfalls direkt aus Analyse der bestehenden Artefakte abgeleitet, nicht aus allgemeinen Best Practices

---

*Pitfalls research for: Meta-Agent- und Command-System-Erweiterung, OpenClaw Meta Maker*
*Researched: 2026-03-14*
