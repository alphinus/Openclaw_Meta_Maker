# Skill

## Name

/elvis-skill-generator

## Beschreibung

Generiert neue Skills für das OpenClaw-System auf Basis einer Anforderungs-Beschreibung des Operators. Erstellt strukturierte Skill-Dateien im verbindlichen 9-Sektionen-Format, höchstens 10 neue Skills pro Durchlauf, immer mit Operator-Bestätigung vor der Erstellung. Sichert Qualität durch Safeguards gegen unkontrollierte Generierung.

## Ziele

- Maximal 10 neue Skill-Dateien pro Durchlauf, alle im verbindlichen 9-Sektionen-Format
- Operator hat jeden Skill vor der Erstellung explizit freigegeben (kein stiller Auto-Commit)
- Jeder generierte Skill erfüllt D006 (konkrete Mengen, Formate, Zeitangaben in Ausführungsschritten)
- Reproduzierbares Ergebnis: Gleiche Anforderung → gleiches Skill-Format (keine kreativen Abweichungen)

## Strategie

Der Skill-Generator arbeitet in zwei Phasen: zuerst eine Skill-Übersicht erstellen und bestätigen lassen, dann jeden Skill einzeln generieren. Die Trennung zwischen Planung (Phase 1) und Ausführung (Phase 2) ist der zentrale Safeguard: Der Operator sieht alle geplanten Skills bevor ein einziger geschrieben wird. Das Template (`templates/skill-template.md`) ist die verbindliche Vorlage — der Generator darf keine neuen Sektionen erfinden, keine bestehenden weglassen. Alle 9 Sektionen müssen befüllt sein, [PFLICHTFELD]-Platzhalter sind ein sofortiger Fehler.

## Einschränkungen

- **Max-Limit:** Max. 10 neue Skills pro Durchlauf. Anforderungen über 10 Skills werden in mehrere Durchläufe aufgeteilt. Der Operator wird darauf hingewiesen bevor der erste Skill generiert wird.
- **Approval-Gate:** Vor der Erstellung eines jeden Skills zeigt der Generator die geplante Skill-Übersicht (Name, Kategorie, 1-Satz-Beschreibung) und wartet auf explizite Operator-Bestätigung ("bestätigt" oder "ok"). Kein Skill wird ohne Bestätigung erstellt.
- **Stop-Bedingung:** Der Prozess endet regulär wenn alle angeforderten Skills erstellt und vom Operator bestätigt wurden. Der Prozess endet vorzeitig wenn der Operator explizit abbricht ("stop", "abbrechen") oder wenn nach 3 Iterationen auf einem Skill keine valide Anforderung formulierbar ist.
- **Rollback-Hinweis:** Wenn ein generierter Skill nicht den Anforderungen entspricht, die Original-Anforderung erneut senden — den fehlerhaften Skill nicht weiter anpassen. Korrekturen auf Basis von "fast richtigem" Output verschlechtern die Qualität. Neu-Generierung mit präzisierter Anforderung ist schneller.
- Keine Skills für Kategorien außerhalb der definierten 6 Kategorien (growth, content, research, strategy, automation, meta) ohne explizite Operator-Genehmigung für eine neue Kategorie
- Kein automatisches Speichern oder Commiten — der Operator führt `git add` und `git commit` manuell aus

## Ausführungsschritte

1. Lies die Anforderung des Operators: Liste von Skill-Namen oder Beschreibungen. Prüfe die Anzahl: Wenn mehr als 10 Skills angefordert, informiere den Operator sofort: "Anforderung enthält [N] Skills — max. 10 pro Durchlauf. Ich bearbeite Skills 1–10 jetzt und liste die restlichen am Ende für den nächsten Durchlauf."
2. Erstelle für jeden angeforderten Skill (max. 10) einen Übersichts-Eintrag: Skill-Name im `/elvis-*`-Format, Kategorie (growth / content / research / strategy / automation / meta), 1-Satz-Beschreibung des Zwecks. Präsentiere die vollständige Übersichts-Tabelle an den Operator und warte auf explizite Bestätigung.
3. Nach Operator-Bestätigung: Generiere Skill 1 vollständig im 9-Sektionen-Format gemäß `templates/skill-template.md`. Alle 9 Sektionen müssen befüllt sein: Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output. Ausführungsschritte müssen D006 erfüllen: jeder Schritt enthält Menge, Format und Zeitangabe wo sinnvoll.
4. Präsentiere den generierten Skill im Volltext an den Operator. Warte auf Freigabe ("ok", "weiter") oder Korrektur-Anforderung. Bei Korrektur: Wenn die Anforderung präzisierbar ist, präzisiere und generiere neu. Wenn nach 3 Versuchen keine Einigung: Markiere diesen Skill als "Offen" und fahre mit dem nächsten fort.
5. Wiederhole Schritt 3–4 für jeden weiteren Skill (Skill 2, Skill 3, … Skill N, max. 10). Zähle jeden abgeschlossenen Skill explizit: "Skill [N/Gesamt] abgeschlossen."
6. Nach dem letzten Skill: Erstelle eine Abschluss-Zusammenfassung mit 3 Spalten: Skill-Name, Status (Erstellt / Offen / Abgebrochen), Dateipfad (z.B. `skills/growth/elvis-new-skill.md`). Wenn Skills offen geblieben sind: füge die Original-Anforderung für den nächsten Durchlauf an.
7. Gib dem Operator die Anweisung zum manuellen Speichern: "Dateien wurden noch nicht gespeichert. Bitte kopiere den Skill-Inhalt in die entsprechende Datei und führe `git add -A && git commit -m 'feat: [Skill-Namen]'` aus."

## Verifikation

- Approval-Gate eingehalten: Kein Skill wurde ohne Übersichts-Bestätigung in Schritt 2 generiert
- Format-Konformität: Jeder generierte Skill hat genau 9 Sektionen mit den exakten Header-Namen aus dem Template
- D006-Konformität: Keine Ausführungsschritte ohne Mengenangabe, Format oder Zeitangabe — abstrakte Schritte wie "Analysiere den Markt" sind ein Fehler
- Abschluss-Zusammenfassung vorhanden: Mit Status pro Skill und ggf. offenen Anforderungen für nächsten Durchlauf
- Failure-Indikator: Wenn der Operator keine klare Anforderung formulieren kann (nach 2 Rückfragen) → Skill bricht ab mit "Anforderung nicht ausreichend präzisiert — empfehle: Ein Beispiel-Skill nennen der als Vorlage dient."
- Akzeptanzkriterium: Alle angeforderten Skills (max. 10) generiert oder mit Status "Offen" dokumentiert, Operator über jeden Schritt informiert, keine Skills ohne Freigabe

## Abhängigkeiten

- Input: Liste von Skill-Anforderungen (Name oder Beschreibung) und Ziel-Kategorie pro Skill
- Empfohlene Vorgänger-Skills: keine (Meta-Skill, unabhängig einsetzbar)

## Output

Übersichts-Tabelle der geplanten Skills (vor Bestätigung) + vollständig generierte Skill-Texte im 9-Sektionen-Format (nach Bestätigung) + Abschluss-Zusammenfassung mit Status und Dateipfaden. Alle Inhalte im Chat ausgegeben — kein automatisches Speichern.
