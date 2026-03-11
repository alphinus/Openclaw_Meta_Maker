# Skill

## Name

/elvis-workflow-builder

## Beschreibung

Identifiziert repetitive Aufgaben die mehr als 30 Minuten pro Woche kosten und dokumentiert jeden Workflow in einem standardisierten 5-Schritte-Format (Trigger → Aktion → Output → Bedingung → Fehlerfall). Liefert eine priorisierte Automatisierungs-Roadmap mit Aufwand-Schätzung und Tool-Empfehlungen.

## Ziele

- Identifizierte repetitive Aufgaben die jeweils >30 Min/Woche kosten, mit Zeitschätzung pro Aufgabe
- Jeder Workflow in max. 5 Schritten dokumentiert (Trigger → Aktion → Output → Bedingung → Fehlerfall)
- Priorisierte Automatisierungs-Roadmap: Aufgaben sortiert nach Zeit-Ersparnis / Implementierungs-Aufwand
- Tool-Empfehlungen für die Top-3 priorisierten Workflows (mit kostenloser und kostenpflichtiger Option)

## Strategie

Der Skill priorisiert nach Zeitersparnis — nicht nach technischer Eleganz. Eine repetitive Aufgabe die 2 Stunden/Woche kostet und in einem Tag automatisierbar ist, schlägt einen komplexen Workflow der 20 Minuten/Woche spart. Das 5-Schritte-Format (Trigger → Aktion → Output → Bedingung → Fehlerfall) ist bewusst minimalistisch: Es reicht aus um einen Workflow zu beschreiben ohne technische Details festzulegen. Fehler-Fälle werden explizit dokumentiert weil unbeaufsichtigte Automatisierungen ohne Fehlerbehandlung mehr Schaden anrichten als helfen.

## Einschränkungen

- Max. 10 Workflows pro Durchlauf (mehr überfordert die Priorisierung und verwässert den Fokus)
- Nur Aufgaben erfassen die tatsächlich >30 Min/Woche kosten — Aufgaben darunter in "Parking Lot" auslagern
- Jeder Workflow darf max. 5 Schritte haben — komplexere Workflows in Teilworkflows aufteilen
- Keine spezifischen Code-Implementierungen liefern — nur Workflow-Dokumentation und Tool-Empfehlungen
- Keine Workflows automatisieren die eine menschliche Entscheidung erfordern (z.B. finanzielle Genehmigungen) ohne expliziten Approval-Schritt im Workflow

## Ausführungsschritte

1. Erfasse alle repetitiven Aufgaben des Operators: Bitte den Operator eine Liste von mindestens 5 Aufgaben zu nennen die er regelmäßig wiederholt (täglich, wöchentlich, monatlich). Für jede Aufgabe schätze: Häufigkeit (täglich / wöchentlich / monatlich), Dauer pro Durchführung in Minuten, Berechne wöchentliche Gesamt-Minuten (Häufigkeit × Dauer). Nimm nur Aufgaben auf die >30 Min/Woche kosten.
2. Sortiere die Aufgaben absteigend nach wöchentlicher Zeit-Kosten. Erstelle eine Tabelle mit 4 Spalten: Aufgabe, Häufigkeit, Min/Durchlauf, Min/Woche. Markiere die Top-3 mit "🎯 Priorität".
3. Dokumentiere jeden der Top-3 Workflows im 5-Schritte-Format: Schritt 1 (Trigger): Was löst den Workflow aus? (z.B. "Neue E-Mail mit Betreff 'Anfrage' eingeht"). Schritt 2 (Aktion): Was passiert? (max. 2 Sätze). Schritt 3 (Output): Was ist das Ergebnis? (z.B. "Antwortentwurf in Drafts-Ordner erstellt"). Schritt 4 (Bedingung): Wann läuft der Workflow nicht normal? (z.B. "Wenn E-Mail kein Anhang hat"). Schritt 5 (Fehlerfall): Was passiert wenn etwas schiefgeht? (z.B. "Slack-Benachrichtigung an Operator, Workflow stoppt").
4. Bewerte für jeden der Top-3 Workflows den Implementierungs-Aufwand in 3 Kategorien: Einfach (1–4 Stunden, No-Code-Tool reicht), Mittel (1–3 Tage, Low-Code oder einfache API), Komplex (>3 Tage, Custom-Entwicklung oder komplexe Integration). Berechne den ROI-Zeitraum: "Automatisierung amortisiert sich nach [Wochen] Wochen" (Implementierungs-Aufwand in Stunden / wöchentliche Zeitersparnis in Stunden = Wochen bis Break-Even).
5. Empfehle für jeden der Top-3 Workflows je 2 Tools: eine kostenlose Option (z.B. Make Free Plan, n8n Community) und eine kostenpflichtige Option (z.B. Zapier, Make Pro). Nenne für jedes Tool: Name, Preis-Hinweis, Begründung warum es für diesen Workflow passt (1 Satz).

## Verifikation

- Vollständigkeit: Alle Top-3 Workflows vollständig im 5-Schritte-Format (Trigger, Aktion, Output, Bedingung, Fehlerfall)
- Zeitschätzungen: Jede Aufgabe hat wöchentliche Min-Angabe und nur Aufgaben >30 Min/Woche sind in der Liste
- ROI-Berechnung: Alle 3 Workflows haben einen berechneten Break-Even-Zeitraum in Wochen
- Fehlerfall dokumentiert: Kein Workflow ohne Schritt 5 (Fehlerfall) — unvollständige Workflows werden nicht gelistet
- Failure-Indikator: Wenn der Operator weniger als 3 Aufgaben mit >30 Min/Woche nennt → Skill gibt aus: "Zu wenige relevante Aufgaben (< 3 mit >30 Min/Woche) — Automatisierungspotenzial gering. Empfehle erst Prozess-Analyse."
- Akzeptanzkriterium: Priorisierte Aufgaben-Tabelle, 3 vollständige Workflow-Dokumentationen im 5-Schritte-Format, ROI-Schätzungen, Tool-Empfehlungen mit je 2 Optionen

## Abhängigkeiten

- Input: Liste von mindestens 5 repetitiven Aufgaben (auch unstrukturiert, der Skill strukturiert sie), optional: verfügbares Budget für Automatisierungs-Tools
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill für Automation-Kategorie)

## Output

Markdown-Dokument mit 4 Abschnitten: (1) Aufgaben-Tabelle mit Zeit-Kosten (alle erfassten Aufgaben, Top-3 markiert), (2) Drei Workflow-Dokumentationen im 5-Schritte-Format, (3) ROI-Übersicht (Implementierungs-Aufwand und Break-Even pro Workflow), (4) Tool-Empfehlungen (je 2 pro Workflow). Einsatzbereit als Automatisierungs-Briefing für Entwickler oder No-Code-Spezialisten.
