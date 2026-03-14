# Skill

## Name

/elvis-soul-generator

## Beschreibung

Generiert eine neue Soul-Definition auf Basis einer Anforderungs-Beschreibung des Operators. Max. 1 Soul pro Durchlauf. Output im bindenden 6-Sektionen-Format (Name, Philosophie, Core Values, Operating Principles, Success Metrics, Geeignet für) gemäß `templates/soul-template.md`. Sichert Qualität durch Safeguards gegen unkontrollierte Generierung und Approval-Gate vor jeder Erstellung.

## Ziele

- 1 vollständige Soul-Datei pro Durchlauf, im verbindlichen 6-Sektionen-Format nach `templates/soul-template.md`
- Operator hat vor der Generierung explizit freigegeben — kein stiller Auto-Commit
- Soul erfüllt D006 in allen Ausführungsdetails: Philosophie beschreibt Weltbild (keine Aufgaben-Verben), Core Values haben konkrete Verhaltens-Ausprägung
- Reproduzierbares Ergebnis: Gleiche Anforderung → gleiches Soul-Format (keine kreativen Abweichungen)

## Strategie

Der Soul-Generator arbeitet nach dem Plan-Approve-Execute-Pattern: Erst eine kompakte Soul-Vorschau erstellen und vom Operator bestätigen lassen, dann die vollständige Soul Section-by-Section generieren. Die Trennung ist der zentrale Safeguard — der Operator sieht Name, Philosophie-Entwurf in 1 Satz und 3 Core-Value-Stichworte bevor eine einzige Zeile Soul-Text geschrieben wird. Das Template (`templates/soul-template.md`) ist die verbindliche Vorlage — der Generator darf keine Sektionen erfinden oder weglassen. Alle 6 Sektionen müssen befüllt sein, [PFLICHTFELD]-Platzhalter sind ein sofortiger Fehler. Kritisch: Philosophie beschreibt Weltbild, nie Aufgaben — "sieht jede Herausforderung als System" ist Philosophie, "plant Strategien" ist ein Fehler.

## Einschränkungen

- **Max-Limit:** Max. 1 Soul pro Durchlauf. Anforderungen für mehrere Souls werden sequentiell in separaten Durchläufen bearbeitet. Der Operator wird darauf hingewiesen bevor der erste Schritt beginnt.
- **Approval-Gate:** Vor der Erstellung zeigt der Generator die geplante Soul-Übersicht (Name, 1-Satz-Philosophie-Entwurf, 3 Core-Value-Stichworte) und wartet auf explizite Operator-Bestätigung ("bestätigt" oder "ok"). Keine Soul wird ohne Bestätigung erstellt.
- **Stop-Bedingung:** Der Prozess endet regulär wenn die Soul erstellt und vom Operator freigegeben wurde. Der Prozess endet vorzeitig wenn der Operator explizit abbricht ("stop", "abbrechen") oder wenn nach 3 Iterationen keine valide Anforderung formulierbar ist.
- **Rollback-Hinweis:** Wenn die generierte Soul nicht dem Template entspricht oder die Philosophie Aufgaben-Verben enthält, die Original-Anforderung erneut senden und komplett neu generieren — nicht iterativ korrigieren. Neu-Generierung mit präzisierter Anforderung ist schneller als schrittweise Anpassung.
- Kein automatisches Speichern oder Commiten — der Operator führt das manuelle Speichern durch

## Ausführungsschritte

1. Lies die Anforderung des Operators: Beschreibung des gewünschten Soul-Archetyps. Prüfe die Anzahl: Bei mehr als 1 Soul informiere den Operator sofort: "Anforderung enthält [N] Souls — max. 1 pro Durchlauf. Ich bearbeite den ersten jetzt und liste die restlichen am Ende für den nächsten Durchlauf."
2. **[APPROVAL-GATE]** Erstelle die Soul-Vorschau mit 3 Elementen: Name (Kleinbuchstaben, Substantiv oder Adjektiv, Archetyp-beschreibend), 1-Satz-Philosophie-Entwurf (Weltbild, keine Aufgaben-Verben), 3 Core-Value-Stichworte. Präsentiere die Vorschau an den Operator und warte auf explizite Bestätigung ("bestätigt" oder "ok"). Schritt endet hier — keine weiteren Aktionen ohne Bestätigung.
3. Nach Bestätigung: Generiere die Soul vollständig Section-by-Section nach `templates/soul-template.md`. Alle 6 Sektionen müssen befüllt sein: Name, Philosophie, Core Values, Operating Principles, Success Metrics, Geeignet für. D006-Konformität: Philosophie enthält 2–4 Sätze Fließtext zum Weltbild, Core Values haben je 1 Satz konkrete Verhaltens-Ausprägung, Operating Principles sind direkt umsetzbare Regeln (immer/nie-Formulierungen), Success Metrics sind nachvollziehbare Maßstäbe. Keine [PFLICHTFELD]-Marker im Output.
4. Präsentiere den generierten Soul-Volltext an den Operator. Warte auf Freigabe ("ok", "weiter") oder Korrektur-Anforderung. Bei Korrektur: max. 3 Versuche, dann Soul als "Offen" markieren und Ursprungs-Anforderung für den nächsten Durchlauf notieren.
5. Abschluss-Zusammenfassung: Soul-Name, Status (Erstellt / Offen / Abgebrochen), Dateipfad (`soul/[name].md`). Hinweis zum manuellen Speichern: "Soul wurde noch nicht gespeichert. Bitte kopiere den Inhalt in `soul/[name].md` und führe `git add soul/[name].md && git commit -m 'feat: soul [name]'` aus."

## Verifikation

- Approval-Gate eingehalten: Soul wurde erst nach expliziter Bestätigung in Schritt 2 generiert
- Format-Konformität: Soul hat genau 6 Sektionen mit den exakten Header-Namen aus `templates/soul-template.md` (Name, Philosophie, Core Values, Operating Principles, Success Metrics, Geeignet für)
- Inhaltliche Konformität: Philosophie enthält keine Aufgaben-Verben ("analysiert", "plant", "erstellt") — ausschließlich Weltbild-Beschreibung
- Core Values haben konkrete Verhaltens-Ausprägung, keine abstrakt-generischen Werte ohne Erklärung
- Abschluss-Zusammenfassung vorhanden mit Status und Dateipfad
- Failure-Indikator: Wenn Philosophie Aufgaben beschreibt statt Weltbild — Output ist ungültig; Soul neu generieren
- Akzeptanzkriterium: 1 Soul generiert oder mit Status "Offen" dokumentiert, Operator über jeden Schritt informiert, kein Output ohne Approval-Gate

## Abhängigkeiten

- Input: Beschreibung des gewünschten Soul-Archetyps (Charakterbeschreibung, Werte-Skizze, Einsatzgebiet-Hinweise)
- Empfohlene Vorgänger-Skills: keine (eigenständig einsetzbar — kein Vorgänger-Skill erforderlich)
- Hinweis: Output (`soul/[name].md`) wird von `/elvis-agent-generator` (Phase 1) als Referenz konsumiert und von `/elvis-agent-creator` (Phase 2) zur Zusammenführung in vollständige Agent-Definitionen genutzt

## Output

Soul-Vorschau (vor Bestätigung: Name + 1-Satz-Philosophie + 3 Core-Value-Stichworte) + vollständige Soul-Definition im 6-Sektionen-Format nach `templates/soul-template.md` (nach Bestätigung) + Abschluss-Zusammenfassung mit Status und Dateipfad. Alle Inhalte im Chat ausgegeben — kein automatisches Speichern.
