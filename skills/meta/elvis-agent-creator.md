# Skill

## Name

/elvis-agent-creator

## Beschreibung

Orchestriert die Erstellung eines vollständigen Agenten — Soul, Identity und Agent-Definition — in einem einzigen Workflow mit einem Approval-Gate. Der Operator beschreibt die Anforderung, erhält ein Gesamtkonzept zur Freigabe, und bekommt danach alle drei Definitionen als zusammenhängendes Paket generiert. Unter 2 Minuten Operator-Interaktion von Anforderung bis fertigem Agent.

## Ziele

- 1 vollständiger Agent pro Durchlauf: Soul-Definition (6-Sektionen), Identity-Definition (7-Sektionen), Agent-Definition (7-Sektionen) als untrennbares Paket
- Operator hat das Gesamtkonzept vor der Generierung explizit freigegeben — kein stiller Auto-Commit
- Alle Querverweise (Soul-Datei, Skills `/elvis-*`) validiert bevor der Agent generiert wird — keine Phantomreferenzen
- Unter 2 Minuten Operator-Interaktion: ein Approval-Gate nach Konzept-Entwurf, ein Review nach Fertigstellung
- Jede der 3 Definitionen ist D006-konform und Template-konform — keine [PFLICHTFELD]-Marker im Output

## Strategie

Der Agent-Creator folgt dem Concept→Approve→Orchestrate-Pattern: Erst ein Gesamtkonzept (Soul-Typ, Identity-Charakter, Agent-Mission, Skill-Set) als kompakte Tabelle entwerfen und vom Operator bestätigen lassen, dann Soul, Identity und Agent intern sequentiell generieren — ohne weitere Halte zwischen diesen Schritten. Die Trennung in Konzept-Phase (ein Gate) und Ausführungs-Phase (kein weiterer Halt) ist der zentrale Safeguard: Der Operator entscheidet einmal über das Gesamtbild, nicht dreimal über Teilschritte.

Soul, Identity und Agent werden als untrennbare Einheit behandelt. Ein Agent ohne passende Soul-Definition ist semantisch leer. Eine Identity ohne zugehörigen Agent hat keinen operativen Rahmen. Das Paket wird deshalb vollständig generiert oder gar nicht — kein Partial-Output.

Interne Referenz: Der Agent-Creator folgt den Templates der Phase-1-Generatoren (`elvis-soul-generator`, `elvis-identity-generator`, `elvis-agent-generator`) ohne diese separat aufzurufen. Er wendet die gleichen Formate an, aber intern sequentiell als eine zusammenhängende Sequenz.

## Einschränkungen

- **Max-Limit:** Max. 1 kompletter Agent pro Durchlauf. Soul + Identity + Agent sind eine untrennbare Einheit — kein Partial-Output (nur Soul ohne Agent ist kein valider Abschluss). Mehrere Agenten werden in separaten Durchläufen bearbeitet.
- **Approval-Gate:** Einmaliger Halt nach Konzept-Entwurf (Schritt 3): Gesamtplan als Tabelle präsentieren und auf explizite Operator-Bestätigung ("ok", "bestätigt") warten. Ein einziger Gate für den Gesamtworkflow — nicht drei separate für Soul, Identity und Agent. Nach Bestätigung des Gesamtkonzepts werden Soul, Identity und Agent intern sequentiell generiert — kein weiterer Halt zwischen diesen Schritten.
- **Stop-Bedingung:** Regulär wenn vollständiges 3-Datei-Paket (Soul + Identity + Agent) generiert und vom Operator freigegeben wurde. Vorzeitig wenn Operator explizit abbricht ("stop", "abbrechen") oder wenn nach 3 Revisionsversuchen am Konzept-Entwurf keine Einigung erzielt wird.
- **Rollback-Hinweis:** Wenn eine der 3 Definitionen nicht dem Template entspricht, den fehlerhaften Teil (Soul, Identity oder Agent) vollständig neu generieren — nicht iterativ korrigieren. Konzept-Entwurf aus Schritt 3 als Basis behalten.
- Kein automatisches Speichern oder Commiten — der Operator führt das manuelle Speichern aller 3 Dateien durch
- Scope: Soul, Identity und Agent-Definition — keine Skill-Generierung im gleichen Durchlauf (dafür `/elvis-skill-generator` aufrufen)

## Ausführungsschritte

1. Lies die Anforderung des Operators: Beschreibung des gewünschten Agenten (Aufgabenbereich, Charakter-Idee, benötigte Fähigkeiten). Prüfe Max-Limit: Wenn mehr als 1 Agent beschrieben wird, informiere sofort: "Anforderung beschreibt [N] Agenten — max. 1 pro Durchlauf. Ich bearbeite den ersten jetzt, die restlichen folgen in separaten Durchläufen." Prüfe ob die Anforderung einen einzelnen, abgrenzbaren Agenten beschreibt — wenn unklar, stelle maximal 2 präzisierende Rückfragen.

2. Entwirf das Gesamtkonzept mit 5 Elementen: (a) **Soul-Typ** — prüfe alle bestehenden `soul/*.md`-Dateien auf Passung (liste 2–3 Kandidaten mit kurzer Begründung, empfehle die beste Wahl oder schlage neuen Archetyp vor wenn kein bestehender Soul passt), (b) **Identity-Charakter** — Star Trek Referenz (Charakter-Name + Spezies + Funktion) + 1-Satz-Skizze des Charakterkerns, (c) **Agent-Mission** — genau 1 aktionsorientierter Satz (kein Konjunktiv, keine Persönlichkeitsmerkmale), (d) **Skill-Set** — empfohlene 5–8 Skills im `/elvis-*`-Format mit je 1-Satz-Begründung warum dieser Skill passt, (e) **Dateipfade** — vorgeschlagene Ziel-Pfade für alle 3 Dateien (`soul/[name].md`, `identity/[name].md`, `agent/[name].md`).

3. **[APPROVAL-GATE]** Präsentiere das Gesamtkonzept als formatierte Tabelle:

   | Element | Entwurf |
   |---------|---------|
   | Agent-Name | [star-trek-name in Kleinbuchstaben] |
   | Mission | [1 aktionsorientierter Satz] |
   | Soul-Typ | `soul/[name].md` (bestehend) oder [neuer Archetyp] |
   | Identity-Charakter | [Star Trek Referenz + 1-Satz-Skizze] |
   | Kern-Skills (5–8) | `/elvis-[a]`, `/elvis-[b]`, `/elvis-[c]`, ... |
   | Dateipfade | `soul/[name].md`, `identity/[name].md`, `agent/[name].md` |

   Frage explizit: "Bitte bestätigen ("ok") um Soul, Identity und Agent zu generieren — oder Korrekturen angeben." **Schritt endet hier. Keine weiteren Aktionen ohne explizite Bestätigung.**

4. Nach Bestätigung: Generiere die Soul-Definition vollständig nach `templates/soul-template.md` — alle 6 Sektionen müssen befüllt sein. Wenn der Operator im Konzept einen bestehenden Soul gewählt hat (`soul/[name].md` existiert bereits), überspringe diesen Schritt und vermerke: "Soul `soul/[name].md` wird referenziert — kein neuer Soul nötig." D006-Konformität: Soul-Ausführungsschritte enthalten konkrete Mengen und Formate wo sinnvoll. Keine [PFLICHTFELD]-Marker im Output.

5. Generiere die Identity-Definition vollständig nach `templates/identity-template.md` — alle 7 Sektionen müssen befüllt sein. Identity beschreibt Persönlichkeit, Charakter und Kommunikationsstil (WER ist der Agent) — keine Aufgaben oder Fähigkeiten (die gehören in den Agent). D006-Konformität: Identity-Ausführungsschritte sind konkret wo sinnvoll. Keine [PFLICHTFELD]-Marker im Output.

6. Generiere die Agent-Definition vollständig nach `templates/agent-template.md` — alle 7 Sektionen müssen befüllt sein (Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills). Querverweisvalidierung vor der Generierung: (a) Soul-Datei — `soul/[name].md` existiert oder wurde in Schritt 4 generiert; (b) Skills — alle `/elvis-*` aus dem genehmigten Konzept existieren oder sind im gleichen Durchlauf generiert worden. Fehlende Referenzen explizit nennen und Operator entscheiden lassen bevor weitergemacht wird. D006-Konformität: Mission = genau 1 aktionsorientierter Satz, Capabilities = 5–8 ausführbare Fähigkeiten (keine Persönlichkeitsmerkmale), Operating Loop = nummerierte wiederholbare Schritte.

7. Präsentiere das vollständige 3-Datei-Paket (Soul, Identity, Agent) im Volltext an den Operator. Warte auf Freigabe ("ok", "freigegeben") oder Korrektur-Anforderung. Bei Korrektur: max. 3 Versuche am Gesamtpaket, dann als "Offen" markieren. Falls nur eine einzelne Definition korrigiert werden muss: diese vollständig neu generieren (nicht iterativ ändern) — Konzept aus Schritt 3 als Basis behalten.

8. Abschluss-Zusammenfassung: Liste alle 3 Dateipfade (`soul/[name].md`, `identity/[name].md`, `agent/[name].md`) mit Status (Erstellt / Referenziert / Offen). Hinweis zum manuellen Speichern: "Alle 3 Definitionen wurden noch nicht gespeichert. Bitte kopiere jeden Inhalt in die entsprechende Datei und führe aus: `git add soul/[name].md identity/[name].md agent/[name].md && git commit -m 'feat: agent [name] — soul + identity + agent'`"

## Verifikation

- Approval-Gate eingehalten: Kein einziger Generierungsschritt (Soul, Identity oder Agent) wurde vor Bestätigung in Schritt 3 ausgeführt
- 3-Datei-Paket vollständig: Soul hat exakt 6 Sektionen nach `templates/soul-template.md`, Identity hat exakt 7 Sektionen nach `templates/identity-template.md`, Agent hat exakt 7 Sektionen nach `templates/agent-template.md`
- D006-Konformität: Agent-Mission ist genau 1 aktionsorientierter Satz, Capabilities enthalten keine Persönlichkeitsmerkmale ("denkt logisch", "ist geduldig" sind Failure-Indikatoren), Operating Loop beschreibt wiederholbare Schritte
- Querverweise validiert: Soul-Datei und alle `/elvis-*`-Skills existieren im Ökosystem oder wurden im gleichen Durchlauf generiert — keine Phantomreferenzen
- Failure-Indikator: Wenn nach Schritt 3 nur Soul oder nur Identity generiert wird (ohne Agent) — Partial-Output-Fehler; Workflow neu starten. Wenn Capabilities Persönlichkeitsbeschreibungen enthalten — Agent neu generieren.
- Akzeptanzkriterium: Vollständiges 3-Datei-Paket generiert oder mit Status "Offen" dokumentiert, ein einziger Approval-Gate nach Konzept-Entwurf eingehalten, Operator über jeden Schritt informiert

## Abhängigkeiten

- Input: Anforderungs-Beschreibung des gewünschten Agenten (Aufgabenbereich, Charakter-Idee, optionale Soul/Skill-Präferenzen)
- Empfohlene Vorgänger-Skills: `/elvis-concept-design` (wenn Anforderung noch vage ist und erst ein Konzept validiert werden soll); `/elvis-skill-generator` (wenn benötigte Skills noch nicht existieren)
- Interne Referenz (kein separater Aufruf): `templates/soul-template.md`, `templates/identity-template.md`, `templates/agent-template.md`

## Output

Konzept-Tabelle (vor Bestätigung: Soul-Typ, Identity-Charakter, Mission, Skill-Set, Dateipfade) + vollständiges 3-Datei-Paket im Volltext (nach Bestätigung: Soul-Definition nach `templates/soul-template.md`, Identity-Definition nach `templates/identity-template.md`, Agent-Definition nach `templates/agent-template.md`) + Abschluss-Zusammenfassung mit 3 Dateipfaden, Status und Speicher-Hinweis. Alle Inhalte im Chat ausgegeben — kein automatisches Speichern.
