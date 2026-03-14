# Skill

## Name

/elvis-command-router

## Beschreibung

Routet eingehende Anfragen an den richtigen Agent und Skill-Chain anhand einer statischen Routing-Tabelle. Kein NLP, kein intelligentes Matching — explizite Keyword-Zuordnung. Kein Generator: erstellt keine Dateien, trifft keine Inhalts-Entscheidungen. Jede Anfrage wird einem von drei Fällen zugeordnet: eindeutig (direkte Route), mehrdeutig (Operator wählt), unbekannt (vollständige Tabelle als Hilfe). Der Operator sieht die Tabelle und weiss was passiert.

## Ziele

- Jede Anfrage wird innerhalb von 1 Routing-Entscheidung dem richtigen Skill zugeordnet — max. 5 Routing-Entscheidungen pro Durchlauf
- Mehrdeutigkeiten werden dem Operator transparent gemacht — kein automatisches Raten
- Unbekannte Anfragen zeigen die vollständige Routing-Tabelle als Hilfe — keine stillen Fehler
- Routing-Tabelle ist die einzige Quelle der Wahrheit — konsistent, statisch, erweiterbar

## Strategie

Der Command-Router arbeitet nach dem Match-Clarify-Route-Pattern: Erst Anfrage gegen Routing-Tabelle matchen, bei eindeutigem Match direkt routen, bei Mehrdeutigkeit Operator wählen lassen, bei Unbekannt vollständige Tabelle zeigen. Der Router entscheidet nicht — er spiegelt. Die Routing-Tabelle steht direkt im Skill-Body und ist die einzige Quelle der Wahrheit.

**Routing-Tabelle (Phase 1 — aktuelle Skills):**

| Keyword / Anfrage-Typ | Agent | Skill-Chain |
|---|---|---|
| Soul erstellen, neue Soul, Soul generieren | Picard | /elvis-soul-generator |
| Identity erstellen, neue Identity, Identity generieren | Picard | /elvis-identity-generator |
| Agent erstellen, neuer Agent, Agent generieren | Picard | /elvis-agent-generator |
| Skills generieren, neue Skills, Skill erstellen | Elvis | /elvis-skill-generator |

Hinweis: Diese Tabelle wird in Phase 2 um weitere Meta-Skills erweitert (Agent-Creator, Skill-Expander, System-Analyzer, Library-Manager). Aktuell nur Phase-1-Skills + bestehender Skill-Generator enthalten.

## Einschränkungen

- **Max-Limit:** Max. 5 Routing-Entscheidungen pro Durchlauf. Einzelne Anfragen die mehr als 5 Routen berühren werden aufgeteilt und sequentiell abgearbeitet. Der Operator wird darauf hingewiesen bevor die erste Entscheidung getroffen wird.
- **Approval-Gate:** Bei mehrdeutigen Anfragen präsentiert der Router 2–3 Kandidaten-Routen (mit Agent und Skill-Chain) und wartet auf explizite Operator-Auswahl. Kein automatisches Raten bei Mehrdeutigkeit — warte auf Auswahl des Operators.
- **Stop-Bedingung:** Der Prozess endet regulär wenn alle Anfragen geroutet oder als "unbekannt" markiert sind. Der Prozess endet vorzeitig wenn der Operator explizit abbricht ("stop", "abbrechen") oder wenn nach 3 Klärungsversuchen bei einer mehrdeutigen Anfrage keine Auswahl getroffen wird.
- **Rollback-Hinweis:** Wenn eine falsche Route gewählt wurde, den Router erneut mit präzisierter Anfrage aufrufen — der Router hat keinen Zustand und kann jederzeit neu gestartet werden. Kein Rollback-Prozess nötig.
- Routing-Tabelle zeigt auf Skills (`/elvis-*`), niemals auf Phase-3-Commands (`/build-agent`, `/create-soul` etc.) — Commands sind formale Deklarationen, die den Router aufrufen, nicht umgekehrt

## Ausführungsschritte

1. Lies die Anfrage des Operators: Freitext oder Keyword. Prüfe die Anzahl der enthaltenen Routing-Anfragen: Bei mehr als 5 informiere den Operator sofort: "Anfrage enthält [N] Routing-Entscheidungen — max. 5 pro Durchlauf. Ich bearbeite die ersten 5 jetzt und liste die restlichen am Ende."
2. Matche jede Anfrage gegen die Routing-Tabelle (siehe Strategie-Abschnitt). Bestimme für jede Anfrage genau einen der drei Fälle: (a) Eindeutig — exakter oder nahezu exakter Keyword-Treffer, (b) Mehrdeutig — Anfrage passt auf 2 oder mehr Einträge, (c) Unbekannt — kein Treffer in der Tabelle.
3. Eindeutiger Match: Gib Route, Agent und Skill-Chain aus mit konkretem Aufruf-Befehl, z.B.: "Route: `/elvis-soul-generator` — Agent: Picard. Rufe `/elvis-soul-generator` auf und teile Picard die Anforderung mit."
4. **[APPROVAL-GATE]** Mehrdeutiger Match: Liste 2–3 passendste Routen mit Agent und Skill-Chain auf. Formulierung: "Anfrage ist mehrdeutig — mögliche Routen: [Liste]. Bitte eine Route auswählen." Schritt endet hier — warte auf Auswahl des Operators, keine automatische Entscheidung.
5. Unbekannte Anfrage: Gib aus "Keine Route gefunden für: [Anfrage]" und zeige die vollständige Routing-Tabelle aus dem Strategie-Abschnitt als Hilfe an. Schluss-Hinweis: "Bitte Anfrage präzisieren oder eine Route manuell wählen. Falls ein neuer Skill-Typ benötigt wird, kann die Routing-Tabelle in Phase 2 erweitert werden."

## Verifikation

- Routing-Tabelle ist vollständig: Alle Phase-1-Skills enthalten (elvis-soul-generator, elvis-identity-generator, elvis-agent-generator, elvis-skill-generator)
- Routing-Tabelle zeigt auf `/elvis-*`-Skills — keine Phase-3-Commands in der Tabelle
- Mehrdeutigkeits-Handling dokumentiert: Klärungsschritt mit Kandidaten-Liste vorhanden
- Unbekannt-Fall dokumentiert: Vollständige Tabelle als Hilfe, keine stillen Fehler
- Approval-Gate eingehalten: Keine automatische Entscheidung bei mehrdeutigen Anfragen
- Failure-Indikator: Wenn Routing-Tabelle auf Phase-3-Commands (`/build-agent`, `/create-soul` etc.) zeigt statt auf Skills (`/elvis-*`) — Tabelle ist ungültig. Wenn bei Mehrdeutigkeit automatisch geroutet wird statt Operator zu fragen — Prozess ist ungültig.
- Akzeptanzkriterium: Jede Anfrage wird einem der drei Fälle zugeordnet (eindeutig/mehrdeutig/unbekannt), Routing-Tabelle enthält mindestens 4 Einträge, alle Routen zeigen auf `/elvis-*`-Skills

## Abhängigkeiten

- Input: Anfrage des Operators (Freitext oder Keyword — was soll erstellt oder generiert werden?)
- Empfohlene Vorgänger-Skills: keine (Einstiegspunkt des Systems — kein Vorgänger-Skill erforderlich)
- Hinweis: Der Router ist der zentrale Knotenpunkt des Ökosystems. Phase 2 erweitert die Routing-Tabelle um weitere Meta-Skills (Agent-Creator, Skill-Expander, System-Analyzer, Library-Manager). Phase-3-Commands sind formale Deklarationen die den Router aufrufen — nicht umgekehrt.

## Output

Routing-Entscheidung mit Agent + Skill-Chain + konkretem Aufruf-Befehl (bei eindeutigem Match). Bei Mehrdeutigkeit: Kandidaten-Liste mit 2–3 Routen zur Operator-Auswahl. Bei Unbekannt: "Keine Route gefunden" + vollständige Routing-Tabelle. Alle Inhalte im Chat ausgegeben — kein automatisches Speichern, keine Dateierstellung.
