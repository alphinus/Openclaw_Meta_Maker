# Skill

## Name

/elvis-agent-optimizer

## Beschreibung

Analysiert eine bestehende Agent-Definition (`agent/*.md`) auf Schwächen und produziert eine optimierte Version nach `templates/agent-template.md`. Identifiziert konkrete Probleme (fehlende Skills, schwache Constraints, veraltete Soul-Referenzen, Format-Abweichungen) und präsentiert einen Schwächen-Report zur Bestätigung bevor die optimierte Version generiert wird. Scope ist ausschließlich auf `agent/*.md` beschränkt — kein Zugriff auf `soul/`, `identity/` oder `skills/`.

## Ziele

- Schwächen-Report mit konkreten, benannten Issues (Typ, Schwere, Empfehlung) als Approval-Gate-Inhalt ausgegeben
- Optimierte Agent-Definition vollständig im 7-Sektionen-Format nach `templates/agent-template.md` generiert
- Vorher/Nachher-Vergleich als Diff-Tabelle (Spalten: Sektion, Vorher, Nachher, Änderungsgrund) präsentiert
- Scope-Disziplin eingehalten: Soul- und Skill-Probleme benannt aber nicht behoben (Verweis auf zuständige Skills)
- Max. 1 Agent-Optimierung pro Durchlauf vollständig abgeschlossen

## Strategie

Der Agent-Optimizer folgt dem Analyse-vor-Generierung-Prinzip: Erst alle Schwächen diagnostizieren und als Report präsentieren, dann auf Bestätigung warten, dann optimierte Version generieren. Diese Trennung ist kritisch — der Operator muss die Diagnose kennen und bestätigen, bevor eine neue Version entsteht. Die Scope-Beschränkung auf `agent/*.md` ist hart: Soul- und Skill-Schwächen werden im Report benannt, aber die Optimierung adressiert nur was in der Agent-Datei selbst korrigierbar ist. Für Soul- und Skill-Korrekturen verweist der Optimizer auf die zuständigen Skills (`/elvis-soul-generator`, `/elvis-skill-generator`). Die Original-Datei bleibt immer unverändert — die Optimierung ist ein neuer Output, keine Überschreibung.

## Einschränkungen

- **Max-Limit:** Max. 1 Agent-Optimierung pro Durchlauf. Tiefe Schwächen-Analyse erfordert Einzelbehandlung — Batching würde oberflächliche Diagnosen produzieren
- **Approval-Gate:** Nach Schritt 3 (Schwächen-Report als Tabelle) — wartet auf explizite Operator-Bestätigung bevor Schritt 4 (Generierung der optimierten Version) beginnt. Kein Überspringen des Reports
- **Stop-Bedingung:** Regulär wenn optimierte Version generiert, Vorher/Nachher-Diff präsentiert und Operator die Freigabe erteilt. Vorzeitig wenn Operator abbricht ("stop", "abbrechen") oder die Agent-Datei nicht lesbar ist (Datei nicht gefunden, falsches Format)
- **Rollback-Hinweis:** Die Original-Agent-Datei bleibt unverändert — die Optimierung wird ausschließlich als neuer Chat-Output präsentiert, nicht als Dateiüberschreibung. Bei fehlerhafter Optimierung: Original beibehalten und mit präzisierten Schwächen-Prioritäten neu generieren (neu aufrufen, nicht iterativ korrigieren)
- **Scope-Beschränkung:** Ausschließlich `agent/*.md` — kein Lesen oder Modifizieren von `soul/*.md`, `identity/*.md` oder `skills/*`. Wenn Soul- oder Skill-Probleme identifiziert werden: im Report als Issue nennen und auf `/elvis-soul-generator` bzw. `/elvis-skill-generator` verweisen. Keine Korrekturen außerhalb der Agent-Datei
- Kein automatisches Speichern — der Operator kopiert die optimierte Version manuell in `agent/[name].md`

## Ausführungsschritte

1. Agent-Datei entgegennehmen: Operator gibt `agent/[name].md` als Input an. Max-Limit prüfen: wenn mehr als 1 Agent angefordert, informieren: "Max. 1 Agent pro Durchlauf — ich bearbeite `agent/[name].md` jetzt." Datei lesen und gegen `templates/agent-template.md` prüfen: Sind alle 7 Sektionen vorhanden (Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills)? Ist die Datei im `agent/`-Verzeichnis? Bei nicht lesbarer oder nicht gefundener Datei: Skill abbrechen mit "Agent-Datei nicht lesbar: `agent/[name].md` — bitte Pfad prüfen."
2. Schwächen-Analyse durchführen: 4 Kategorien prüfen — (a) Fehlende Skills: In Capabilities beschriebene Fähigkeiten, die keinen entsprechenden Eintrag in den Primären Skills haben (erkennbar an Verb-Objekt-Formulierungen ohne `/elvis-*`-Referenz); (b) Schwache Constraints: Vage Formulierungen ohne harte Grenzen (z.B. "möglichst wenig" statt "max. N", "wenn möglich" statt "nie ohne Freigabe"); (c) Veraltete Soul-Referenz: `soul/[name].md` aus Primärer Soul — Plausibilitätsprüfung ausschließlich per Namenskonvention (kein Dateizugriff auf soul/*.md gemäß Scope-Beschränkung). Prüfen: Folgt der Dateiname dem `soul/[archetyp].md`-Schema? Ist der Archetyp-Name ein sinnvoller Soul-Typ (z.B. strategist, guardian, explorer)?; (d) Format-Probleme: Capabilities die Persönlichkeit beschreiben ("denkt logisch", "ist geduldig") statt ausführbare Fähigkeiten — diese gehören in die Identity, nicht den Agent.
3. **[APPROVAL-GATE]** Schwächen-Report als Tabelle präsentieren mit 5 Spalten: `| # | Issue | Typ | Schwere | Empfehlung |`. Typen: `Fehlender-Skill`, `Schwacher-Constraint`, `Soul-Referenz`, `Format-Problem`, `Sektions-Lücke`. Schwere: `Kritisch` (verhindert korrekten Betrieb) / `Mittel` (reduziert Qualität) / `Niedrig` (kosmetisch). Bei Issues aus `soul/` oder `skills/`: Empfehlung enthält Verweis auf zuständigen Skill. Nach Ausgabe der Tabelle: "Warte auf explizite Bestätigung. Antworte mit 'bestätigt' um die optimierte Version zu generieren oder benenne spezifische Issues die priorisiert werden sollen." — Schritt endet hier.
4. Nach expliziter Operator-Bestätigung: Optimierte Agent-Definition vollständig generieren im 7-Sektionen-Format nach `templates/agent-template.md`. Alle identifizierten Schwächen aus dem Agent-Scope adressieren: Schwache Constraints durch harte Zahlen ersetzen, Fehlende Skills in Primäre Skills aufnehmen (nur bereits im Ökosystem existierende `/elvis-*`-Skills), Format-Probleme in den korrekten Sektionen platzieren. Keine [PFLICHTFELD]-Marker im Output. Soul-Änderungen nur wenn Benennung nachweislich falsch ist — keine Soul-Inhalte generieren.
5. Vorher/Nachher-Vergleich als Diff-Tabelle präsentieren mit 4 Spalten: `| Sektion | Vorher | Nachher | Änderungsgrund |`. Für jede geänderte Sektion eine Zeile. Unveränderte Sektionen als `— | unverändert | —` eintragen. Auf Freigabe oder Korrektur-Anforderung warten: "Freigabe mit 'ok' oder Korrekturbedarf benennen."
6. Abschluss: Dateipfad ausgeben (`agent/[name].md`) + Speicher-Hinweis: "Optimierte Version wurde noch nicht gespeichert. Bitte den Inhalt in `agent/[name].md` kopieren (Original vorher sichern) und `git add agent/[name].md && git commit -m 'refactor: optimize agent [name]'` ausführen." Zusammenfassung: Anzahl adressierter Issues, Anzahl verwiesener Issues (Soul/Skills), Verbleibende Empfehlungen.

## Verifikation

- Approval-Gate eingehalten: Optimierte Version wurde erst nach Schritt 3-Bestätigung generiert — kein vorzeitiges Generieren
- Scope-Disziplin: Keine Änderungen in `soul/`, `identity/` oder `skills/` vorgenommen oder vorgeschlagen — nur `agent/[name].md` als Output
- Schwächen-Report vollständig: Alle 4 Kategorien geprüft (Fehlende Skills, Schwache Constraints, Soul-Referenz, Format-Probleme), Ergebnis je Kategorie dokumentiert (auch wenn 0 Issues in einer Kategorie)
- Vorher/Nachher-Diff vorhanden: Jede geänderte Sektion mit Begründung — keine Änderungen ohne Erklärung
- Original unverändert: Kein automatisches Überschreiben der Quelldatei
- Failure-Indikator: Wenn Agent-Datei nicht dem 7-Sektionen-Format entspricht (weniger als 5 Sektionen vorhanden) — Skill abbrechen mit "Datei entspricht nicht dem Agent-Template — empfehle `/elvis-agent-generator` zur Neu-Erstellung"
- Akzeptanzkriterium: Schwächen-Report präsentiert, Approval eingeholt, optimierte Version im 7-Sektionen-Format generiert, Vorher/Nachher-Diff ausgegeben, Speicher-Hinweis erteilt

## Abhängigkeiten

- Input: Pfad zu einer bestehenden Agent-Definition (`agent/[name].md`) vom Operator
- Empfohlene Vorgänger-Skills: keine (direkt auf bestehende Agent-Datei anwendbar)
- Verwandte Skills: `/elvis-agent-generator` (Neu-Erstellung wenn Optimierung nicht ausreicht), `/elvis-soul-generator` (wenn Soul-Probleme adressiert werden sollen), `/elvis-skill-generator` (wenn fehlende Skills erstellt werden sollen)

## Output

Schwächen-Report als 5-spaltige Tabelle (#/Issue/Typ/Schwere/Empfehlung) als Approval-Gate-Inhalt + optimierte Agent-Definition im vollständigen 7-Sektionen-Format nach `templates/agent-template.md` + Vorher/Nachher-Diff als 4-spaltige Tabelle (Sektion/Vorher/Nachher/Änderungsgrund) + Speicher-Hinweis mit Dateipfad und Git-Befehl. Alle Inhalte im Chat ausgegeben — kein automatisches Speichern oder Überschreiben der Original-Datei.
