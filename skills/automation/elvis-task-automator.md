# Skill

## Name

/elvis-task-automator

## Beschreibung

Wandelt eine einzelne repetitive Aufgabe in eine vollständige Automations-Sequenz mit Trigger-Definition, Aktions-Kette, Fehlerbehandlung und Monitoring-Spezifikation um. Liefert ein einsatzbereites Automatisierungs-Briefing für No-Code-Tools oder Entwickler — keine Code-Implementierung, sondern präzise Workflow-Spezifikation in 5 Schritten.

## Ziele

- Vollständige Automatisierungs-Spezifikation für genau eine Aufgabe: Trigger, Aktions-Sequenz (3-8 Schritte), Fehlerbehandlung, Monitoring
- Identifizierte alle Varianten und Ausnahmen der Aufgabe (min. 2, max. 5 Varianten) mit jeweils dokumentiertem Verzweigungs-Punkt
- Tool-Empfehlung mit 2 Optionen (No-Code + API/Custom) inkl. grober Aufwands-Schätzung (Stunden)
- Erfolgs-Kriterium: Klare Definition wann die Automatisierung als "erfolgreich abgeschlossen" gilt (messbare Bedingung)

## Strategie

Der Skill fokussiert auf **Vollständigkeit statt Schnelligkeit**: Eine einzelne Aufgabe wird vollständig durchdacht — alle Varianten, alle Fehlerfälle, alle Monitoring-Punkte. Das Ergebnis ist implementierbar ohne Rückfragen. Die 5-Schritte-Struktur (Aufgabe analysieren → Trigger → Aktions-Sequenz → Fehlerbehandlung → Monitoring) ist systematisch: Erst das WAS (Aufgabe verstehen), dann das WANN (Trigger), dann das WIE (Aktionen), dann das WENN-NICHT (Fehler), dann das PRÜFEN (Monitoring). Aufgaben die menschliche Entscheidungen ohne klare Regeln erfordern sind nicht automatisierbar.

## Einschränkungen

- Genau eine Aufgabe pro Durchlauf — keine Workflow-Ketten oder Multi-Aufgaben-Systeme (dafür ist /elvis-workflow-builder zuständig)
- Aufgabe muss regelbasiert sein — wenn >20% der Fälle menschliches Ermessen erfordern, ist die Aufgabe nicht geeignet
- Aktions-Sequenz: min. 3, max. 8 Schritte — längere Sequenzen in Teil-Aufgaben aufbrechen
- Keine Code-Implementierung — nur Spezifikation in natürlicher Sprache mit Tool-Empfehlungen
- Keine Automatisierung von Prozessen mit rechtlichen/finanziellen Konsequenzen ohne expliziten Freigabe-Schritt in der Aktions-Sequenz

## Ausführungsschritte

1. Analysiere die Aufgabe vollständig: Erfasse Aufgaben-Name (max. 50 Zeichen), detaillierte Beschreibung (3-5 Sätze was genau getan wird), aktueller Zeit-Aufwand pro Durchlauf (Minuten), Häufigkeit (täglich/wöchentlich/monatlich), Input-Daten (welche Informationen werden benötigt?), Output-Ziel (was ist das Ergebnis?). Identifiziere min. 2, max. 5 Varianten der Aufgabe (z.B. "Fall 1: Mit Anhang → speichern und weiterleiten; Fall 2: Ohne Anhang → nur weiterleiten").
2. Definiere den Trigger: Was löst die Automatisierung aus? Format: Trigger-Typ (Zeit / Event / Bedingung), konkrete Trigger-Spezifikation (z.B. "Jeden Werktag um 08:00 Uhr" oder "Neue E-Mail mit Betreff enthält 'Anfrage' eingeht"), Frequenz-Schätzung (wie oft wird der Trigger pro Tag/Woche erwartet?). Dokumentiere auch Nicht-Trigger: Wann soll die Automatisierung NICHT laufen? (z.B. "Nicht am Wochenende", "Nicht wenn Absender auf Blocklist").
3. Spezifiziere die Aktions-Sequenz in 3-8 Schritten: Jeder Schritt in Format "Schritt N: [Aktion] → [Ergebnis]". Beispiel: "Schritt 1: Daten aus System X abrufen (API-Call) → Liste mit 10-100 Einträgen; Schritt 2: Einträge filtern nach Bedingung Y → gefilterte Liste mit 5-30 Einträgen; Schritt 3: Gefilterte Liste in Google Sheet eintragen (Zeile anhängen) → Sheet aktualisiert". Für jeden Schritt dokumentiere: benötigte Tools/APIs, erwarteter Output, Zeitaufwand (Sekunden/Minuten). Markiere Verzweigungs-Punkte für Varianten (z.B. "Falls Liste leer → Schritt 5 überspringen").
4. Definiere Fehlerbehandlung für min. 3 Fehler-Szenarien: Identifiziere die 3 wahrscheinlichsten Fehler (z.B. "API nicht erreichbar", "Datei fehlt", "Validierung schlägt fehl"). Für jeden Fehler dokumentiere: Fehler-Erkennungs-Bedingung, Fehler-Aktion (Retry / Slack-Benachrichtigung / E-Mail an Operator / Workflow stoppen), Escalation-Regel (wann muss ein Mensch eingreifen?). Format: "Fehler 1: [Bedingung] → [Aktion] → [Escalation nach N Versuchen]".
5. Spezifiziere Monitoring und Erfolgs-Kriterium: Definiere welche Metriken getrackt werden sollen (z.B. "Anzahl erfolgreich verarbeiteter Einträge pro Tag", "Durchschnittliche Laufzeit pro Durchlauf", "Fehlerrate in %"). Definiere Erfolgs-Kriterium: Wann gilt ein Automatisierungs-Durchlauf als erfolgreich? (z.B. "Alle Einträge verarbeitet UND keine kritischen Fehler UND Laufzeit <5 Minuten"). Empfehle Monitoring-Tool (z.B. "Zapier History", "n8n Execution Log", "Custom Dashboard mit täglich E-Mail-Report").

## Verifikation

- Vollständigkeit: Alle 5 Schritte dokumentiert (Aufgaben-Analyse, Trigger, Aktions-Sequenz, Fehlerbehandlung, Monitoring)
- Aufgaben-Analyse: Min. 2 Varianten identifiziert mit Verzweigungs-Punkten in Aktions-Sequenz
- Aktions-Sequenz: 3-8 Schritte, jeder Schritt mit Tool/API und erwartetem Output
- Fehlerbehandlung: Min. 3 Fehler-Szenarien mit Erkennungs-Bedingung, Aktion und Escalation
- Erfolgs-Kriterium: Klare messbare Definition (nicht vage "läuft gut" sondern konkrete Bedingung)
- Failure-Indikator: Wenn Aufgabe menschliche Entscheidungen ohne klare Regeln erfordert (>20% der Fälle) → Meldung "Aufgabe nicht automatisierbar — zu viele Ermessensentscheidungen. Empfehle manuelle Bearbeitung mit Tool-Unterstützung."
- Akzeptanzkriterium: Vollständige 5-Schritte-Spezifikation, min. 2 Varianten, min. 3 Fehler-Szenarien, Erfolgs-Kriterium definiert, Tool-Empfehlungen mit Aufwands-Schätzung

## Abhängigkeiten

- Input: Beschreibung der zu automatisierenden Aufgabe (Name, grobe Beschreibung, Häufigkeit) — auch unstrukturiert, der Skill strukturiert sie
- Empfohlene Vorgänger-Skills: /elvis-automation-audit — liefert priorisierte Aufgaben-Liste als Kandidaten für Task-Automation; /elvis-workflow-builder — wenn mehrere Aufgaben als Workflow koordiniert werden sollen

## Output

Markdown-Dokument mit 6 Abschnitten: (1) Aufgaben-Analyse (Name, Beschreibung, Varianten, Zeit/Häufigkeit), (2) Trigger-Spezifikation (Typ, Bedingung, Frequenz, Nicht-Trigger), (3) Aktions-Sequenz (3-8 Schritte mit Tools und Outputs), (4) Fehlerbehandlung (3 Szenarien mit Erkennungs-/Aktions-/Escalation-Regeln), (5) Monitoring-Spezifikation (Metriken, Erfolgs-Kriterium, Tool-Empfehlung), (6) Tool-Empfehlungen (2 Optionen mit Aufwands-Schätzung). Einsatzbereit als Implementierungs-Briefing.
