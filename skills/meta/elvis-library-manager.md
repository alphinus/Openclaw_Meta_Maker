# Skill

## Name

/elvis-library-manager

## Beschreibung

Inventarisiert, kategorisiert und strukturiert den gesamten Skill-Katalog des OpenClaw-Ökosystems. Erstellt einen durchsuchbaren Markdown-Katalog aller Skills mit Kategorie, Pfad und Vollständigkeits-Status. Schlägt strukturelle Änderungen (Umkategorisierungen, Archivierungen, Duplikat-Zusammenführungen) vor und wartet auf explizite Operator-Bestätigung bevor eine einzige Änderungs-Anweisung ausgegeben wird.

## Ziele

- Vollständiger Skill-Katalog als Markdown-Tabelle mit Spalten Name, Kategorie, Pfad, Status — alle Skills im `skills/`-Verzeichnis erfasst
- Jeder Skill auf Vollständigkeit geprüft: alle 9 Sektionen vorhanden? Fehlende Sektionen dokumentiert
- Duplikate erkannt: funktional ähnliche Skills namentlich aufgeführt mit Zusammenführungs-Empfehlung
- Strukturelle Änderungen nur nach expliziter Operator-Bestätigung durchgeführt — max. 10 Änderungen pro Durchlauf
- Abschließender Katalog als verwertbares Nachschlagewerk ausgegeben

## Strategie

Der Library-Manager folgt dem Inventar-vor-Änderung-Prinzip: Erst den vollständigen Ist-Stand erfassen und als Katalog präsentieren, dann Änderungsvorschläge formulieren, dann auf Approval warten — erst danach Änderungs-Anweisungen ausgeben. Diese Reihenfolge ist nicht verhandelbar. Der Operator sieht immer zuerst was vorhanden ist, bevor irgendeine Reorganisation stattfindet. Duplikat-Erkennung basiert auf funktionaler Ähnlichkeit (nicht nur Namensähnlichkeit) — zwei Skills sind Duplikate wenn sie dasselbe Problem für denselben Anwendungsfall lösen. Vollständigkeits-Check nutzt das verbindliche 9-Sektionen-Format als Referenz: Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output.

## Einschränkungen

- **Max-Limit:** Max. 10 Library-Änderungen (Umkategorisierungen, Archivierungen, Zusammenführungen) pro Durchlauf. Bei mehr als 10 vorgeschlagenen Änderungen: die 10 wichtigsten priorisieren und die restlichen als "Nächster Durchlauf" dokumentieren
- **Approval-Gate:** Nach Schritt 4 (Änderungsvorschläge als Tabelle) — wartet auf explizite Operator-Bestätigung bevor Schritt 5 (Änderungs-Anweisungen ausgeben) beginnt. Kein vorzeitiges Ausgeben von Änderungs-Anweisungen
- **Stop-Bedingung:** Regulär wenn Katalog aktualisiert, Änderungen dokumentiert und Abschluss-Zusammenfassung ausgegeben. Vorzeitig wenn Operator keine Änderungen wünscht ("nur Katalog") — Skill endet nach Schritt 3 mit Katalog-Ausgabe ohne Schritt 4–6
- **Rollback-Hinweis:** Alle Änderungs-Anweisungen in Schritt 5 sind Operator-Aktionen (keine automatischen Datei-Verschiebungen). Bei Fehler die umgekehrte Aktion ausführen (z.B. Datei zurück in ursprüngliche Kategorie verschieben). Der Katalog selbst kann jederzeit durch erneuten Aufruf neu generiert werden
- Kein Zugriff auf `agent/`, `soul/`, `identity/` oder andere Verzeichnisse außerhalb von `skills/`
- Keine automatischen Dateioperationen — alle Änderungen werden als Anweisungen ausgegeben, der Operator führt sie aus

## Ausführungsschritte

1. Library-Status prüfen: Alle Dateien in `skills/*` (rekursiv alle Unterverzeichnisse) inventarisieren. Für jede Skill-Datei erfassen: Dateiname, abgeleiteter Skill-Name (`/elvis-[name]`), Kategorie (aus Unterverzeichnis: growth, content, research, strategy, automation, meta), Dateipfad relativ zu `skills/`. Max-Limit prüfen: wenn mehr als 10 Änderungen in Schritt 3 absehbar sind, vorab informieren.
2. Vollständigkeits-Check: Für jeden inventarisierten Skill prüfen ob alle 9 Sektionen (`## Name`, `## Beschreibung`, `## Ziele`, `## Strategie`, `## Einschränkungen`, `## Ausführungsschritte`, `## Verifikation`, `## Abhängigkeiten`, `## Output`) vorhanden sind. Fehlende Sektionen pro Skill als Komma-getrennte Liste erfassen. Status setzen: `Vollständig` (alle 9) / `Lückenhaft` (1–8 Sektionen) / `Leer` (0 Sektionen).
3. Katalog erstellen: Markdown-Tabelle mit 4 Spalten ausgeben — `| Skill-Name | Kategorie | Pfad | Status |` — alle inventarisierten Skills alphabetisch nach Kategorie sortiert. Duplikat-Erkennung: Skills mit funktional gleichem Zweck (erkennbar an Name + Beschreibung) identifizieren und als `[DUPLIKAT-KANDIDAT]` in der Status-Spalte markieren. Kategorie-Zählung als Zusammenfassung unterhalb der Tabelle: `Kategorie: N Skills`.
4. **[APPROVAL-GATE]** Änderungsvorschläge als Tabelle präsentieren mit 4 Spalten: `| # | Aktion | Objekt | Begründung |`. Mögliche Aktionen: `Umkategorisieren`, `Archivieren`, `Zusammenführen`, `Vollständigkeit beheben`. Max. 10 Vorschläge, priorisiert nach Impact. Nach Ausgabe der Tabelle: "Warte auf explizite Bestätigung der vorgeschlagenen Änderungen. Antworte mit 'bestätigt' oder liste die gewünschten Aktions-Nummern (z.B. '1, 3, 5')." — Schritt endet hier, keine weiteren Aktionen ohne Bestätigung.
5. Nach expliziter Operator-Bestätigung: Bestätigte Änderungen als nummerierte Operator-Anweisungen ausgeben. Format pro Anweisung: "Aktion [N]: [Konkrete Anweisung, z.B. 'Verschiebe `skills/growth/elvis-x.md` nach `skills/content/elvis-x.md`']". Jede Anweisung ist eine einzelne, ausführbare Dateioperation. Zählung: "Änderung [N/Gesamt] ausgegeben."
6. Abschluss: Aktualisierten Katalog als vollständige Markdown-Tabelle (4 Spalten, nach Schritt 5-Änderungen aktualisiert) erneut ausgeben. Zusammenfassung: Anzahl durchgeführter Änderungen, Anzahl verbleibender Lückenhafter Skills, empfohlene nächste Schritte (z.B. "3 Skills mit fehlenden Sektionen — `/elvis-skill-generator` zur Vervollständigung empfohlen").

## Verifikation

- Approval-Gate eingehalten: Keine Änderungs-Anweisung wurde vor Schritt 4-Bestätigung ausgegeben
- Katalog vollständig: Alle Dateien aus `skills/` in der Tabelle erfasst, keine Auslassungen
- Vollständigkeits-Check durchgeführt: Jeder Skill hat einen Status-Eintrag (`Vollständig` / `Lückenhaft` / `Leer`)
- Duplikat-Erkennung aktiv: Skills mit gleichem Zweck als `[DUPLIKAT-KANDIDAT]` markiert — bei 0 Duplikaten explizit vermerkt "Keine Duplikate identifiziert"
- Änderungs-Anweisungen als Operator-Aktionen formuliert: Nie "ich verschiebe" sondern "Verschiebe `[pfad]` nach `[pfad]`"
- Failure-Indikator: Wenn `skills/`-Verzeichnis leer oder nicht erreichbar ist, Skill abbrechen mit "Library nicht erreichbar — bitte Verzeichnisstruktur prüfen"
- Akzeptanzkriterium: Vollständiger Katalog ausgegeben, alle Vollständigkeits-Status gesetzt, Änderungsvorschläge präsentiert und auf Approval gewartet, nach Bestätigung max. 10 Änderungs-Anweisungen ausgegeben

## Abhängigkeiten

- Input: Zugriff auf `skills/`-Verzeichnisstruktur mit allen Unterverzeichnissen
- Empfohlene Vorgänger-Skills: keine (Meta-Skill, eigenständig einsetzbar)
- Empfohlene Folge-Skills: `/elvis-skill-generator` (wenn lückenhafte Skills vervollständigt werden sollen)

## Output

Skill-Katalog als Markdown-Tabelle (4 Spalten: Name, Kategorie, Pfad, Status) mit Kategorie-Zählung + Änderungsvorschläge als Tabelle (4 Spalten: #, Aktion, Objekt, Begründung) nach Approval-Gate + nummerierte Operator-Anweisungen für bestätigte Änderungen + aktualisierter Abschluss-Katalog. Alle Inhalte im Chat ausgegeben — keine automatischen Dateioperationen.
