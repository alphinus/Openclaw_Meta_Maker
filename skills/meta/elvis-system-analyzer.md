# Skill

## Name

/elvis-system-analyzer

## Beschreibung

Analysiert das gesamte OpenClaw-Ökosystem qualitativ und liefert einen strukturierten Gesundheitsbericht mit benannten Lücken, Schweregrad-Einstufung (kritisch/mittel/niedrig) und konkreten Handlungsempfehlungen. Troi's primärer Analyse-Skill — read-only, keine Dateiänderungen. Kein Score, keine Zahlen 0–100 (das ist Aufgabe von /elvis-ecosystem-health). Dieser Skill liefert Tiefe, Kontext und Empfehlungen.

## Ziele

- Vollständiges Inventar aller Entities im Ökosystem (Soul, Identity, Agent, Skill) mit Typ, Kategorie und Pfad
- Identifizierte Lücken gegliedert nach Schweregrad: kritisch (blockiert Betrieb), mittel (beeinträchtigt Qualität), niedrig (kosmetisch/optional)
- Konkrete Handlungsempfehlungen pro Issue mit Verweis auf den zuständigen Meta-Skill (/elvis-*)
- Zusammenfassung mit Gesamt-Befund (Anzahl Issues pro Schweregrad) und Top-3-Prioritäten

## Strategie

System-Analyzer ist die qualitative Tiefenanalyse des Ökosystems — nicht zu verwechseln mit /elvis-ecosystem-health, der einen schnellen quantitativen Score liefert. Dieser Skill analysiert Kontext und Zusammenhänge: Warum fehlt ein Querverweis? Was bedeutet eine unterbesetzte Kategorie strategisch? Welche Agents sind ohne Soul einsatzbereit? Die Analyse folgt einem klaren Trichter: Inventar → Lücken → Schwächen → Balance → Report. Das Approval-Gate nach dem Befund-Report (Schritt 5) stellt sicher, dass der Operator entscheidet ob Empfehlungen als Aktions-Liste konkretisiert werden — die Analyse erzwingt keine Folge-Aktionen.

## Einschränkungen

- **Max-Limit:** Max. 1 vollständige System-Analyse pro Durchlauf. Konsistent mit Troi's Agent-Constraints (agent/troi.md: "Maximal 1 vollständige System-Analyse pro Durchlauf").
- **Approval-Gate:** Nach dem Befund-Report (Schritt 5) — "Warte auf explizite Bestätigung bevor Empfehlungen als priorisierte Aktions-Liste ausgegeben werden." Schritt 5 endet mit einem expliziten Halt. Kein weiterer Output ohne Operator-Bestätigung.
- **Stop-Bedingung:** Regulär wenn vollständiger Befund-Report ausgegeben und (nach Bestätigung) Handlungsempfehlungen mit Abschluss-Zusammenfassung geliefert wurden. Vorzeitig wenn Ökosystem-Dateien nicht zugänglich sind — fehlende Inputs dokumentieren und Analyse stoppen.
- **Rollback-Hinweis:** Analyse und Report sind read-only — keine direkten Systemänderungen durch diesen Skill. Rollback nicht anwendbar. Bei fehlerhafter Analyse (z.B. falsches Inventar): komplette Analyse neu starten, nicht iterativ korrigieren.
- Kein Schreiben von Dateien — alle Ergebnisse werden im Chat ausgegeben
- Kein quantitativer Score (0–100) — das ist ausschließlich Aufgabe von /elvis-ecosystem-health
- Keine automatischen Korrekturen oder Änderungen am Ökosystem

## Ausführungsschritte

1. Ökosystem-Scan starten: Alle Dateien in `soul/`, `identity/`, `agent/`, `skills/` inventarisieren. Für jede Datei erfassen: Dateiname, Entity-Typ (Soul/Identity/Agent/Skill), Kategorie (bei Skills: growth/content/research/strategy/automation/meta), Dateipfad. Ergebnis als Inventar-Tabelle mit 4 Spalten (Name, Typ, Kategorie, Pfad) zusammenfassen. Max. 1 Analyse pro Durchlauf — bei erneutem Aufruf im selben Durchlauf: "Bereits eine Analyse in diesem Durchlauf abgeschlossen — neuen Durchlauf starten."

2. Lücken-Analyse durchführen: Fehlende Querverweise identifizieren — jeder Agent (agent/*.md) referenziert einen Soul (soul/*.md, Feld "Primärer Soul") und eine Liste von Skills (/elvis-*). Prüfe: (a) Referenziert ein Agent einen Soul der nicht in soul/ existiert? → "Gebrochener Soul-Verweis". (b) Referenziert ein Agent Skills die nicht in skills/meta/ existieren? → "Gebrochener Skill-Verweis". (c) Existiert ein Soul der von keinem Agent referenziert wird? → "Nicht referenzierter Soul". (d) Existiert ein Skill der von keinem Agent in seiner Primäre-Skills-Liste aufgeführt wird? → "Nicht referenzierter Skill". Alle gefundenen Issues als Liste dokumentieren.

3. Schwächen-Analyse durchführen: (a) Unvollständige Definitionen — prüfe alle Entities gegen die vorgeschriebene Sektionen-Anzahl: Souls müssen 6 Sektionen haben, Identities 7, Agents 7, Skills 9. Fehlende Sektionen als Issues dokumentieren. (b) Fehlende Safeguards in Meta-Skills — prüfe alle Dateien in `skills/meta/*.md` auf Vorhandensein der 4 Safeguard-Elemente: Max-Limit, Approval-Gate (als nummerierter Schritt mit "warte auf"), Stop-Bedingung (regulär + vorzeitig), Rollback-Hinweis. Fehlende Elemente als Issues dokumentieren. (c) D006-Verstöße — prüfe Ausführungsschritte auf abstrakte Formulierungen ohne konkrete Mengen oder Formate. Schritte wie "Analysiere das System" ohne Mengenangabe als Issues dokumentieren.

4. Kategorie-Balance prüfen: Zähle die Anzahl Skills pro Kategorie (growth, content, research, strategy, automation, meta). Berechne den Durchschnitt (Gesamt-Skills / 6 Kategorien). Identifiziere Kategorien die mehr als doppelt so viele Skills haben wie der Durchschnitt → "überbesetzt". Identifiziere Kategorien die 0 Skills haben oder weniger als halb so viele wie der Durchschnitt → "unterbesetzt". Dokumentiere als Issues mit konkreten Zahlenwerten.

5. [APPROVAL-GATE] Befunde als strukturierten Report präsentieren, gegliedert nach Schweregrad:

   **Befund-Report — OpenClaw Ökosystem**

   | Schweregrad | Anzahl Issues |
   |-------------|---------------|
   | Kritisch    | [N] |
   | Mittel      | [N] |
   | Niedrig     | [N] |

   Kritische Issues (blockieren Betrieb): [Liste mit Issue-Typ und betroffener Datei]
   Mittlere Issues (beeinträchtigen Qualität): [Liste]
   Niedrige Issues (kosmetisch/optional): [Liste]

   "Analyse abgeschlossen. Warte auf explizite Bestätigung ("ok", "weiter") um Handlungsempfehlungen als priorisierte Aktions-Liste auszugeben." Schritt endet hier — kein weiterer Output ohne Operator-Bestätigung.

6. Nach Bestätigung: Konkrete Handlungsempfehlungen pro Issue ausgeben — jeweils mit Verweis auf den zuständigen Meta-Skill. Beispiel-Format:
   - "Gebrochener Soul-Verweis in agent/borg.md (soul/builder.md fehlt) → Empfehlung: /elvis-soul-generator aufrufen um soul/builder.md zu erstellen."
   - "Fehlende Safeguards in skills/meta/elvis-example.md (Max-Limit fehlt) → Empfehlung: Skill manuell ergänzen oder /elvis-skill-generator mit korrektem Safeguard-Quartet neu generieren."
   Issues in Reihenfolge der Schweregrade ausgeben: zuerst kritisch, dann mittel, dann niedrig.

7. Abschluss-Zusammenfassung ausgeben: Gesamt-Befund in 3 Zeilen (Anzahl kritisch/mittel/niedrig), Top-3-Prioritäten als priorisierte Handlungsliste, Hinweis "Für schnellen quantitativen Score: /elvis-ecosystem-health aufrufen."

## Verifikation

- Report enthält Schweregrad-Einstufung (kritisch/mittel/niedrig) mit expliziten Zahlenwerten — ein Report ohne Schweregrade ist ein Fehler
- Approval-Gate eingehalten: Handlungsempfehlungen wurden erst nach Operator-Bestätigung in Schritt 5 ausgegeben
- Read-only bestätigt: Kein Schreiben von Dateien während der Analyse — alle Ergebnisse im Chat
- Kein Score (0–100) im Output — Zahl 0–100 wäre Überschneidung mit /elvis-ecosystem-health
- Handlungsempfehlungen (Schritt 6) enthalten konkrete Skill-Verweise (/elvis-*) für jedes Issue
- Failure-Indikator: Wenn kein Verzeichnis (soul/, identity/, agent/, skills/) zugänglich ist → "Ökosystem-Dateien nicht zugänglich — fehlende Inputs: [Liste]. Analyse gestoppt."
- Akzeptanzkriterium: Vollständiger Befund-Report (alle 4 Analyse-Bereiche) + Handlungsempfehlungen ausgegeben, Abschluss-Zusammenfassung mit Top-3-Prioritäten vorhanden

## Abhängigkeiten

- Input: Lesezugang zu den Verzeichnissen `soul/`, `identity/`, `agent/`, `skills/` im OpenClaw-Ökosystem
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Analyse-Skill, unabhängig einsetzbar)
- Ergänzender Skill: /elvis-ecosystem-health (quantitativer Score als schneller Vorcheck vor dieser Tiefenanalyse empfohlen)

## Output

Strukturierter Gesundheitsbericht im Chat mit 4 Teilen: (1) Inventar-Tabelle aller Entities (Soul/Identity/Agent/Skill), (2) Befund-Report nach Schweregrad (kritisch/mittel/niedrig) mit Anzahl Issues, (3) Handlungsempfehlungen pro Issue mit Skill-Verweis (/elvis-*), (4) Abschluss-Zusammenfassung mit Top-3-Prioritäten. Kein automatisches Speichern — alle Inhalte im Chat ausgegeben.
