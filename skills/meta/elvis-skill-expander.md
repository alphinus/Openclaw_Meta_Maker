# Skill

## Name

/elvis-skill-expander

## Beschreibung

Leitet neue Skill-Varianten von einem bestehenden Skill ab und generiert diese als vollständige 9-Sektionen-Skill-Definitionen gemäß `templates/skill-template.md`. Ausgehend von einem Basis-Skill analysiert der Expander Kernfunktion, Kategorie und Ausführungslogik und produziert bis zu 5 eigenständige Varianten mit expliziter Abgrenzung vom Ausgangsskill. Jede Variante ist sofort einsatzbereit — keine Beschreibungs-Liste, sondern eine vollständige Skill-Definition.

## Ziele

- Bis zu 5 neue Skill-Varianten als vollständige 9-Sektionen-Definitionen, direkt aus einem Basis-Skill abgeleitet
- Operator hat die Varianten-Übersicht explizit bestätigt bevor eine einzige Variante vollständig ausgearbeitet wird
- Jede Variante benennt die Abgrenzung zum Basis-Skill explizit in Beschreibung und Strategie
- Alle generierten Varianten erfüllen D006 (konkrete Mengen, Formate, Zeitangaben in Ausführungsschritten)
- Reproduzierbare Ergebnisse: gleicher Basis-Skill → konsistentes Varianten-Set ohne kreative Abweichungen vom Template

## Strategie

Der Skill-Expander arbeitet nach dem Plan-Approve-Execute-Pattern: zuerst eine Varianten-Übersicht planen und bestätigen lassen, dann jede Variante einzeln vollständig ausarbeiten. Die Trennung zwischen Planung (Übersichts-Tabelle) und Ausführung (vollständige 9-Sektionen-Definitionen) ist der zentrale Safeguard — der Operator entscheidet welche Richtungen sinnvoll sind, bevor Aufwand investiert wird. Der Basis-Skill ist nicht eine Vorlage die kopiert wird, sondern ein Ausgangspunkt der systematisch in benachbarte Domänen oder spezialisierte Anwendungsfälle erweitert wird. `templates/skill-template.md` ist die verbindliche Vorlage für jede generierte Variante.

## Einschränkungen

- **Max-Limit:** Max. 5 neue Skill-Varianten pro Durchlauf. Konsistent mit Borg's Agent-Definition (`agent/borg.md` Constraints). Anforderungen über 5 Varianten werden in mehrere Durchläufe aufgeteilt.
- **Approval-Gate:** Varianten-Übersichts-Tabelle (Schritt 3) muss vom Operator explizit bestätigt werden — kein Ausarbeiten ohne "bestätigt" oder "ok".
- **Stop-Bedingung:** Regulär wenn alle Varianten generiert und freigegeben. Vorzeitig wenn Operator abbricht ("stop", "abbrechen") oder wenn nach 3 Iterationen auf einer Variante keine Einigung erzielt wird (Variante wird als "Offen" markiert).
- **Rollback-Hinweis:** Fehlerhafte Variante vollständig neu generieren — nicht iterativ korrigieren. Eine neue Variante auf Basis von "fast richtigem" Output verschlechtert die Qualität. Operator sendet präzisierte Anforderung für die betroffene Variante.
- Keine Varianten außerhalb der 6 definierten Skill-Kategorien (growth, content, research, strategy, automation, meta) ohne explizite Operator-Genehmigung
- Kein automatisches Speichern oder Committen — der Operator kopiert den Output und führt `git add` / `git commit` manuell aus

## Ausführungsschritte

1. Basis-Skill vom Operator entgegennehmen. Skill-Datei lesen und analysieren: Kategorie (growth / content / research / strategy / automation / meta), Kernfunktion (Was tut der Skill?), Ausführungslogik (Wie geht er vor?), Zielgruppe (Für wen ist er gedacht?). Max-Limit prüfen: wenn mehr als 5 Varianten angefordert, informiere den Operator sofort: "Anforderung enthält [N] Varianten — max. 5 pro Durchlauf. Ich bearbeite Varianten 1–5 jetzt."
2. Basis-Skill-Analyse im Chat ausgeben: Name, Kategorie, Kernfunktion in 1–2 Sätzen, 3 identifizierte Erweiterungsrichtungen (z.B. spezialisierte Zielgruppe, verwandter Anwendungsfall, erhöhte Tiefe/Breite).
3. Varianten-Übersicht erstellen: für jede Variante (max. 5) einen Tabellen-Eintrag mit 4 Spalten — Varianten-Name (im `/elvis-*`-Format), Kategorie, 1-Satz-Beschreibung des Zwecks, explizite Abgrenzung vom Basis-Skill in 1 Satz. Tabelle an Operator senden und auf explizite Bestätigung warten. **[APPROVAL-GATE — warte auf explizite Bestätigung des Operators bevor Schritt 4 beginnt.]**
4. Nach Operator-Bestätigung: Generiere Variante 1 vollständig im 9-Sektionen-Format gemäß `templates/skill-template.md`. Alle 9 Sektionen müssen befüllt sein: Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output. In Beschreibung und Strategie explizit benennen: "Abgrenzung zu /[Basis-Skill-Name]: [1 Satz]." Ausführungsschritte müssen D006 erfüllen: jeder Schritt enthält Menge, Format und Zeitangabe wo sinnvoll.
5. Variante 1 im Volltext an Operator präsentieren. Auf Freigabe ("ok", "weiter") oder Korrektur warten. Bei Korrektur: wenn die Anforderung präzisierbar ist, präzisiere und generiere die Variante neu (max. 2 Versuche). Nach 2 Versuchen ohne Einigung: Variante 1 als "Offen" markieren und mit Variante 2 fortfahren.
6. Schritte 4–5 für jede weitere Variante wiederholen (Variante 2, 3, … max. 5). Jede abgeschlossene Variante explizit zählen: "Variante [N/Gesamt] abgeschlossen."
7. Nach der letzten Variante: Abschluss-Zusammenfassung als Tabelle mit 3 Spalten — Varianten-Name, Status (Erstellt / Offen / Abgebrochen), empfohlener Dateipfad (z.B. `skills/growth/elvis-neue-variante.md`). Wenn offene Varianten existieren: Original-Anforderung für nächsten Durchlauf anfügen. Operator über manuelles Speichern informieren: "Dateien noch nicht gespeichert — Inhalt in entsprechende Datei kopieren und `git add skills/[pfad] && git commit -m 'feat: [Varianten-Name]'` ausführen."

## Verifikation

- Approval-Gate eingehalten: Keine Variante wurde ohne Übersichts-Bestätigung in Schritt 3 vollständig ausgearbeitet
- Format-Konformität: Jede generierte Variante hat genau 9 Sektionen mit den exakten Header-Namen aus `templates/skill-template.md`
- Abgrenzungs-Pflicht: Jede Variante benennt in Beschreibung oder Strategie die explizite Abgrenzung zum Basis-Skill
- D006-Konformität: Keine Ausführungsschritte ohne Mengenangabe, Format oder Zeitangabe — abstrakte Schritte wie "Analysiere den Skill" sind ein Fehler
- Vollständigkeit: Keine [PFLICHTFELD]-Platzhalter im generierten Output — vorhanden = sofortiger Fehler
- Abschluss-Zusammenfassung vorhanden: Status pro Variante und empfohlene Dateipfade
- Failure-Indikator: Wenn der Basis-Skill keine eindeutige Kernfunktion hat (nach 2 Rückfragen unklar) → Skill bricht ab mit "Basis-Skill nicht ausreichend definiert — empfehle: vollständige 9-Sektionen-Definition bereitstellen."
- Akzeptanzkriterium: Alle angeforderten Varianten (max. 5) als vollständige 9-Sektionen-Definitionen generiert oder mit Status "Offen" dokumentiert

## Abhängigkeiten

- Input: Bestehender Basis-Skill als vollständige Skill-Definition (Name + Inhalt) oder Dateipfad zu einer `skills/*.md` Datei; optional: gewünschte Erweiterungsrichtungen oder Zielkategorien für die Varianten
- Empfohlene Vorgänger-Skills: `/elvis-skill-generator` (wenn der Basis-Skill noch nicht existiert)

## Output

Varianten-Übersichts-Tabelle (4 Spalten: Name, Kategorie, Beschreibung, Abgrenzung) vor dem Approval-Gate + bis zu 5 vollständig ausgearbeitete Skill-Definitionen im 9-Sektionen-Format nach Bestätigung + Abschluss-Tabelle mit Status und Dateipfaden. Alle Inhalte im Chat ausgegeben — kein automatisches Speichern.
