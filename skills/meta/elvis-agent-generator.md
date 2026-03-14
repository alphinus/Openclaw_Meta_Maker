# Skill

## Name

/elvis-agent-generator

## Beschreibung

Generiert eine neue Agent-Definition auf Basis einer Anforderungs-Beschreibung des Operators. Max. 1 Agent pro Durchlauf. Output im bindenden 7-Sektionen-Format (Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills) gemäß `templates/agent-template.md`. Validiert alle Querverweise auf Soul-Dateien (`soul/*.md`) und Skills (`/elvis-*`) vor der Generierung. Approval-Gate verhindert jeden Agent ohne explizite Operator-Freigabe.

## Ziele

- 1 vollständige Agent-Datei pro Durchlauf, im verbindlichen 7-Sektionen-Format nach `templates/agent-template.md`
- Operator hat vor der Generierung explizit freigegeben — kein stiller Auto-Commit
- Alle Querverweise (Soul-Datei, Skills) sind vor der Generierung validiert — kein Agent mit ungültigen Referenzen
- D006-Konformität: Mission ist genau 1 aktionsorientierter Satz, Capabilities sind ausführbare Fähigkeiten (keine Persönlichkeitsmerkmale), Operating Loop ist eine nummerierte wiederholbare Ablaufbeschreibung
- Reproduzierbares Ergebnis: Gleiche Anforderung → gleiches Agent-Format (keine kreativen Abweichungen)

## Strategie

Der Agent-Generator arbeitet nach dem Plan-Approve-Execute-Pattern: Erst eine kompakte Agent-Vorschau erstellen und vom Operator bestätigen lassen, dann den vollständigen Agent Section-by-Section generieren. Die Trennung ist der zentrale Safeguard — der Operator sieht Name, 1-Satz-Mission, Soul-Zuordnung und 3–5 Kern-Skills bevor eine einzige Zeile Agent-Text geschrieben wird. Das Template (`templates/agent-template.md`) ist die verbindliche Vorlage — der Generator darf keine Sektionen erfinden oder weglassen. Alle 7 Sektionen müssen befüllt sein, [PFLICHTFELD]-Platzhalter sind ein sofortiger Fehler.

Kritische Unterscheidung: Ein Agent beschreibt WAS getan wird (Aufgaben, Fähigkeiten, Arbeitsprozesse). Eine Identity beschreibt WER jemand ist (Persönlichkeit, Charakter). Capabilities wie "denkt logisch" oder "ist geduldig" sind Identity-Merkmale und in einer Agent-Definition ungültig. Querverweisvalidierung ist nicht optional — jede referenzierte `soul/*.md`-Datei und jeder referenzierte `/elvis-*`-Skill muss im Ökosystem existieren, bevor der Agent generiert wird.

## Einschränkungen

- **Max-Limit:** Max. 1 Agent pro Durchlauf. Jede Agent-Referenz (Soul, Skills) muss einzeln auf Validität geprüft werden — Batching würde unkontrollierte Referenz-Fehler erzeugen. Anforderungen für mehrere Agents werden sequentiell in separaten Durchläufen bearbeitet.
- **Approval-Gate:** Vor der Erstellung zeigt der Generator die geplante Agent-Übersicht (Name, 1-Satz-Mission, Soul-Zuordnung, Skill-Liste mit 3–5 Kern-Skills) und wartet auf explizite Operator-Bestätigung ("bestätigt" oder "ok"). Kein Agent wird ohne Bestätigung erstellt.
- **Stop-Bedingung:** Der Prozess endet regulär wenn der Agent erstellt und vom Operator freigegeben wurde. Der Prozess endet vorzeitig wenn der Operator explizit abbricht ("stop", "abbrechen") oder wenn nach 3 Iterationen keine valide Anforderung formulierbar ist.
- **Rollback-Hinweis:** Wenn der generierte Agent nicht dem Template entspricht oder ungültige Querverweise enthält, die Original-Anforderung erneut senden und komplett neu generieren — nicht iterativ korrigieren. Präzisierte Neu-Generierung ist schneller als schrittweise Reparatur.
- Kein automatisches Speichern oder Commiten — der Operator führt das manuelle Speichern durch

## Ausführungsschritte

1. Lies die Anforderung des Operators: Beschreibung des gewünschten Agenten (Aufgabenbereich, Soul-Zuordnung, Skill-Liste). Prüfe zwei Dinge: (a) Anzahl — bei mehr als 1 Agent informiere den Operator: "Anforderung enthält [N] Agents — max. 1 pro Durchlauf. Ich bearbeite den ersten jetzt." (b) Typ — prüfe ob die Anforderung Aufgaben beschreibt (Agent) oder Persönlichkeit (Identity). Bei Verwechslung: "Die Anforderung beschreibt Persönlichkeit — das gehört in eine Identity-Definition. Bitte `/elvis-identity-generator` aufrufen für Charakter-Eigenschaften."
2. Querverweisvalidierung: Prüfe ob alle in der Anforderung genannten Souls (`soul/[name].md`) und Skills (`/elvis-[name]`) im Ökosystem existieren. Liste fehlende Referenzen explizit auf und frage den Operator: "Folgende Referenzen fehlen: [Liste]. Sollen diese zuerst erstellt werden? (Empfehlung: `/elvis-soul-generator` für Souls, `/elvis-skill-generator` für Skills)" — fahre erst fort wenn alle Referenzen validiert sind oder der Operator entscheidet, vorhandene Alternativen zu verwenden.
3. **[APPROVAL-GATE]** Erstelle die Agent-Vorschau mit 4 Elementen: Name (Star Trek Charakter-Name, Kleinbuchstaben), 1-Satz-Mission (aktionsorientiert, keine Konjunktive), Soul-Zuordnung (`soul/[name].md`), Skill-Liste (3–5 Kern-Skills im `/elvis-*`-Format). Präsentiere die Vorschau an den Operator und warte auf explizite Bestätigung ("bestätigt" oder "ok"). Schritt endet hier — warte auf explizite Bestaetigung, keine weiteren Aktionen ohne Bestätigung.
4. Nach Bestätigung: Generiere den Agent vollständig Section-by-Section nach `templates/agent-template.md`. Alle 7 Sektionen müssen befüllt sein: Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills. D006-Konformität: Mission = genau 1 aktionsorientierter Satz (kein Konjunktiv), Capabilities = 5–8 ausführbare Fähigkeiten (keine Persönlichkeitsmerkmale — "denkt logisch", "ist geduldig" sind ungültig), Operating Loop = nummerierte wiederholbare Schritte die den Arbeitsprozess beschreiben. Keine [PFLICHTFELD]-Marker im Output.
5. Präsentiere den generierten Agent-Volltext an den Operator. Warte auf Freigabe ("ok", "weiter") oder Korrektur-Anforderung. Bei Korrektur: max. 3 Versuche, dann Agent als "Offen" markieren und Ursprungs-Anforderung für den nächsten Durchlauf notieren.
6. Abschluss-Zusammenfassung: Agent-Name, Status (Erstellt / Offen / Abgebrochen), Dateipfad (`agent/[name].md`), validierte Querverweise (Soul-Datei + Skills als Liste). Hinweis zum manuellen Speichern: "Agent wurde noch nicht gespeichert. Bitte kopiere den Inhalt in `agent/[name].md` und führe `git add agent/[name].md && git commit -m 'feat: agent [name]'` aus."

## Verifikation

- Approval-Gate eingehalten: Agent wurde erst nach expliziter Bestätigung in Schritt 3 generiert
- Format-Konformität: Agent hat genau 7 Sektionen mit den exakten Header-Namen aus `templates/agent-template.md` (Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills)
- D006-Konformität: Mission ist genau 1 Satz, Capabilities enthalten keine Persönlichkeitsmerkmale, Operating Loop beschreibt wiederholbare Schritte
- Querverweise validiert: Soul-Datei (`soul/*.md`) und alle Skills (`/elvis-*`) existieren im Ökosystem — keine Phantomreferenzen
- Abschluss-Zusammenfassung vorhanden mit Status, Dateipfad und Querverweisliste
- Failure-Indikator: Wenn Capabilities Persönlichkeitsbeschreibungen enthalten ("denkt logisch", "ist geduldig") statt ausführbarer Fähigkeiten — Output ist ungültig; Agent neu generieren. Wenn Soul-Querverweis auf nicht-existierende Datei zeigt — Output ist ungültig.
- Akzeptanzkriterium: 1 Agent generiert, alle Querverweise validiert, Mission ist aktionsorientiert, Capabilities sind ausführbar, Operator über jeden Schritt informiert

## Abhängigkeiten

- Input: Beschreibung des gewünschten Agenten (Aufgabenbereich, Soul-Zuordnung `soul/[name].md`, Skill-Liste `/elvis-*`)
- Empfohlene Vorgänger-Skills: `/elvis-soul-generator` (wenn ein neuer Soul für diesen Agent benötigt wird), `/elvis-identity-generator` (wenn eine neue Identity für diesen Agent benötigt wird)
- Hinweis: Output (`agent/[name].md`) wird von `/elvis-agent-creator` (Phase 2) konsumiert — dort werden Soul, Identity und Agent-Definition in einem vollständigen Workflow zusammengeführt. Die Querverweisvalidierung in diesem Skill ist Voraussetzung für eine fehlerfreie Zusammenführung in Phase 2.

## Output

Agent-Vorschau (vor Bestätigung: Name + 1-Satz-Mission + Soul-Zuordnung + Skill-Liste) + vollständige Agent-Definition im 7-Sektionen-Format nach `templates/agent-template.md` (nach Bestätigung) + Abschluss-Zusammenfassung mit Status, Dateipfad und validierter Querverweisliste. Alle Inhalte im Chat ausgegeben — kein automatisches Speichern.
