# Skill

## Name

/elvis-concept-design

## Beschreibung

Entwirft und validiert neue Agent-Konzepte als Vorstufe zum Agent-Creator. Liest die Anforderung des Operators, prüft das bestehende Ökosystem auf Überschneidungen (`agent/*.md`, `soul/*.md`), und liefert ein strukturiertes Konzept-Dokument mit Mission, empfohlenem Soul, Identity-Charakter, Skill-Bedarf und Machbarkeits-Einschätzung. Output ist immer ein validiertes Konzept-Dokument — kein fertiger Agent. Wer einen fertigen Agenten will, ruft anschließend `/elvis-agent-creator` auf.

## Ziele

- Konzept-Dokument mit allen 6 Elementen (Mission, Soul-Empfehlung, Identity-Charakter, Skill-Bedarf, Machbarkeits-Einschätzung, nächste Schritte) vollständig ausgefüllt
- Ökosystem-Prüfung abgeschlossen: kein Duplikat mit bestehendem Agenten in `agent/*.md`
- Machbarkeits-Einschätzung basiert auf verfügbaren Skills in `skills/meta/*.md` (existierend vs. fehlend markiert)
- Operator hat das Konzept explizit bestätigt bevor die finale Version formatiert wird
- Kein fertiger Agent im Output — klare Abgrenzung zur Agent-Erstellung

## Strategie

Der Concept-Designer arbeitet nach dem Plan-Approve-Execute-Pattern: zuerst das Ökosystem scannen und ein Konzept entwerfen, dann zur Bestätigung vorlegen, dann final formatieren. Die Ökosystem-Prüfung ist nicht optional — sie verhindert redundante Agenten und stellt sicher dass Skill-Bedarf gegen tatsächlich verfügbare Skills geprüft wird. Q's Stärke liegt in der konzeptuellen Validierung: Konzeptfehler (falscher Soul, fehlende Skills, Duplikat-Agent) kosten nichts wenn sie vor dem Agent-Creator erkannt werden — sie kosten viel wenn der Agent-Creator erst beim Bauen auf die Probleme stößt. Das Konzept-Dokument ist der Output, nicht ein Zwischenschritt.

## Einschränkungen

- **Max-Limit:** Max. 1 Konzept pro Durchlauf. Konzeptvalidierung braucht sorgfältige Prüfung gegen das bestehende Ökosystem — Batching würde Qualitätsverlust bedeuten.
- **Approval-Gate:** Konzept-Entwurf (Schritt 4) muss vom Operator explizit bestätigt werden — keine finale Formatierung ohne "bestätigt" oder "ok".
- **Stop-Bedingung:** Regulär wenn das Konzept-Dokument fertig und vom Operator freigegeben ist. Vorzeitig wenn Operator abbricht ("stop", "abbrechen") oder wenn nach 3 Revisionsversuchen keine Einigung auf ein Konzept erzielt wird.
- **Rollback-Hinweis:** Konzept-Entwurf komplett verwerfen und mit präzisierter Anforderung neu beginnen — kein iteratives Patchen eines unklaren Konzepts. Eine klare Anforderung liefert bessere Ergebnisse als 3 Korrekturrunden auf einem schwachen Entwurf.
- Output ist ausschließlich ein Konzept-Dokument — keine Agent-Definition, keine Soul-Datei, kein Identity-Dokument
- Kein automatisches Speichern oder Committen — der Operator entscheidet ob das Konzept archiviert wird

## Ausführungsschritte

1. Anforderung des Operators lesen: Welche Art Agent wird benötigt? Welches Problem soll er lösen? Für wen ist er gedacht? Max-Limit prüfen: wenn mehr als 1 Konzept angefordert, informiere den Operator: "Max. 1 Konzept pro Durchlauf — ich bearbeite Konzept 1 jetzt und liste die restlichen Anforderungen am Ende."
2. Ökosystem-Scan: Alle Dateien in `agent/*.md` durchgehen und prüfen ob ein bestehender Agent dieselbe Aufgabe bereits abdeckt. Ergebnis: entweder "Kein Duplikat gefunden — Anforderung ist neu" oder "Ähnlicher Agent existiert: [Name] — empfehle `/elvis-agent-optimizer` statt Neuerstellung." Bei Duplikat-Fund Skill abbrechen und Operator informieren.
3. Soul-Prüfung: Alle Dateien in `soul/*.md` durchgehen. Passenden Soul für den geplanten Agenten identifizieren: welcher Archetyp (z.B. automation, creator, analyst) passt zur Anforderung? Ergebnis: entweder "Empfohlener Soul: `soul/[name].md`" oder "Kein passender Soul — neuer Soul nötig: [Archetyp-Beschreibung]."
4. Konzept-Dokument entwerfen mit 6 Elementen: (1) Konzept-Name + Mission in 1 aktionsorientierten Satz ("Analysiert / Generiert / Verwaltet [Objekt] um [Ziel] zu erreichen"), (2) Empfohlener Soul (`soul/[name].md` Verweis oder "neuer Soul nötig: [Archetyp]"), (3) Empfohlener Identity-Charakter (Star Trek Referenz + 1-Satz-Skizze der Persönlichkeit), (4) Skill-Bedarf als Liste der benötigten `/elvis-*` Skills — für jeden Skill markieren: "existiert: `skills/[pfad]`" oder "fehlt: muss mit /elvis-skill-generator erstellt werden", (5) Machbarkeits-Einschätzung hoch / mittel / niedrig + 2–3 Satz-Begründung basierend auf verfügbaren Skills und Souls, (6) Empfohlene nächste Schritte (z.B. "Aufrufen: `/elvis-agent-creator`" oder "Zuerst fehlende Skills erstellen mit `/elvis-skill-generator`"). Konzept-Entwurf im Chat präsentieren. **[APPROVAL-GATE — warte auf explizite Bestätigung oder Korrektur des Operators bevor Schritt 5 beginnt.]**
5. Bei Operator-Bestätigung: finales Konzept-Dokument als strukturiertes Markdown formatieren mit Überschrift "# Agent-Konzept: [Konzept-Name]" und den 6 Elementen als nummerierte Abschnitte. Gesamtlänge: max. 400 Wörter. Bei Korrektur: Anforderung präzisieren und Entwurf neu erstellen (max. 3 Versuche). Nach 3 Versuchen ohne Einigung: Skill vorzeitig beenden mit "Konzept nach 3 Revisionen nicht konsolidierbar — empfehle: Anforderung neu formulieren mit konkretem Use Case."
6. Abschluss-Zusammenfassung: Konzept-Name, Machbarkeits-Einschätzung (hoch/mittel/niedrig), empfohlener nächster Schritt in 1 Satz. Operator informieren dass das Konzept-Dokument im Chat vorliegt und manuell gespeichert werden kann (z.B. als `concepts/[konzept-name].md`).

## Verifikation

- Approval-Gate eingehalten: Finales Konzept-Dokument wurde erst nach expliziter Bestätigung in Schritt 4 formatiert
- Ökosystem-Prüfung abgeschlossen: `agent/*.md` auf Duplikate geprüft (Schritt 2), `soul/*.md` auf passenden Soul geprüft (Schritt 3)
- Konzept-Vollständigkeit: Alle 6 Elemente vorhanden — Mission, Soul-Empfehlung, Identity-Charakter, Skill-Bedarf (mit existiert/fehlt-Markierung), Machbarkeits-Einschätzung, nächste Schritte
- Kein fertiger Agent im Output: keine Agent-Definition, keine Soul-Datei, kein Identity-Dokument — nur Konzept-Dokument
- Machbarkeits-Einschätzung belegt: Begründung bezieht sich auf konkret geprüfte Skills und Souls (keine abstrakten Aussagen)
- Failure-Indikator: Wenn die Anforderung nach 2 Rückfragen noch kein klares Problem beschreibt → Skill bricht ab mit "Anforderung zu vage — beschreibe das konkrete Problem das der Agent lösen soll (max. 3 Sätze)."
- Akzeptanzkriterium: Konzept-Dokument mit allen 6 Elementen fertig, Operator über `/elvis-agent-creator` als nächsten Schritt informiert

## Abhängigkeiten

- Input: Textuelle Anforderungs-Beschreibung des Operators (welche Art Agent, welches Problem, für wen); Lesezugriff auf `agent/*.md` und `soul/*.md` für die Ökosystem-Prüfung
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill für Agent-Konzeptionierung; optional `/elvis-skill-generator` wenn bekannt ist dass neue Skills benötigt werden)

## Output

Finales Konzept-Dokument als Markdown (max. 400 Wörter) mit Überschrift und 6 nummerierten Abschnitten: (1) Konzept-Name + Mission, (2) Empfohlener Soul, (3) Empfohlener Identity-Charakter, (4) Skill-Bedarf mit existiert/fehlt-Markierung, (5) Machbarkeits-Einschätzung mit Begründung, (6) Empfohlene nächste Schritte. Kein fertiger Agent — nur die validierte Konzept-Blaupause. Ausgabe im Chat — kein automatisches Speichern.
