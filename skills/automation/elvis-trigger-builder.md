# Skill

## Name

/elvis-trigger-builder

## Beschreibung

Definiert Event-basierte If/Then-Trigger-Ketten für komplexe Automatisierungen: Spezifikation von 5 Trigger-Typen (Zeit, Event, Daten-Schwelle, Nutzer-Aktion, System-Status), Bedingungs-Logik mit AND/OR-Verknüpfungen, Fehlerfall-Routing. Liefert eine strukturierte Trigger-Spezifikation als Baustein für Workflow-Automatisierungen — keine Code-Implementierung.

## Ziele

- Dokumentierte Trigger-Kette für min. 1 Automatisierungs-Szenario mit min. 3, max. 10 Trigger-Bedingungen
- Alle 5 Trigger-Typen mit jeweils min. 1 konkretem Beispiel dokumentiert (Zeit, Event, Daten-Schwelle, Nutzer-Aktion, System-Status)
- Bedingungs-Logik: min. 2 AND-Verknüpfungen und min. 1 OR-Verknüpfung in der Trigger-Kette
- Fehlerfall-Routing: Definition was passiert wenn Trigger nicht eindeutig auswertbar ist (min. 2 Fehler-Szenarien)

## Strategie

Der Skill ist der **Baustein für komplexe Automatisierungen**: Während /elvis-workflow-builder Workflows beschreibt und /elvis-task-automator einzelne Aufgaben spezifiziert, definiert dieser Skill die **auslösenden Bedingungen**. Die 5 Trigger-Typen decken alle relevanten Automatisierungs-Szenarien ab: Zeit (periodisch), Event (Reaktion auf Ereignis), Daten-Schwelle (Schwellenwert überschritten), Nutzer-Aktion (User hat etwas getan), System-Status (System-Zustand hat sich geändert). Die Bedingungs-Logik mit AND/OR erlaubt präzise Trigger-Definition statt "immer wenn X". Fehlerfall-Routing verhindert dass unklare Trigger-Zustände die Automatisierung blockieren.

## Einschränkungen

- Min. 3 Trigger-Bedingungen pro Kette — weniger ist trivial (einfaches If/Then ohne Skill machbar)
- Max. 10 Trigger-Bedingungen pro Kette — mehr wird unübersichtlich und fehleranfällig (besser in Teil-Ketten aufteilen)
- Trigger-Bedingung muss eindeutig auswertbar sein (Boolean True/False) — keine vagen Bedingungen wie "wenn es sinnvoll erscheint"
- Keine Code-Implementierung — nur Trigger-Spezifikation in strukturierter natürlicher Sprache
- Trigger mit rechtlichen/finanziellen Konsequenzen müssen expliziten Freigabe-Schritt haben (z.B. "AND Operator-Freigabe erteilt")

## Ausführungsschritte

1. Erfasse das Automatisierungs-Szenario: Erfrage vom Operator: Szenario-Name (max. 50 Zeichen), Szenario-Beschreibung (2-3 Sätze was automatisiert werden soll), gewünschtes Ergebnis (was passiert wenn alle Trigger erfüllt sind?). Dokumentiere auch Nicht-Trigger: Wann soll die Automatisierung NICHT laufen? (z.B. "Nicht am Wochenende", "Nicht wenn System-Status = Wartung"). Erstelle Szenario-Übersicht mit 4 Feldern: Name, Beschreibung, Ergebnis, Nicht-Trigger.
2. Definiere Trigger-Bedingungen für alle 5 Trigger-Typen: Für jeden der 5 Typen erstelle min. 1 konkrete Trigger-Bedingung für das Szenario. Zeit-Trigger: Zeitpunkt oder Intervall (z.B. "Jeden Montag 09:00 Uhr" oder "Alle 4 Stunden"). Event-Trigger: Ereignis in System (z.B. "Neue E-Mail empfangen" oder "Datei in Ordner X hochgeladen"). Daten-Schwelle-Trigger: Schwellenwert überschritten (z.B. "Bestellungen heute >50" oder "Speicherplatz <10%"). Nutzer-Aktion-Trigger: User-Interaktion (z.B. "Formular ausgefüllt" oder "Button 'Senden' geklickt"). System-Status-Trigger: System-Zustand (z.B. "Server-Status = Online" oder "Datenbank-Sync abgeschlossen"). Format je Trigger: "Typ: [Trigger-Typ] | Bedingung: [auswertbare Bedingung] | Erwarteter Wert: [True/False-Kriterium]".
3. Erstelle die Bedingungs-Logik mit AND/OR-Verknüpfungen: Kombiniere die definierten Trigger-Bedingungen zu einer Trigger-Kette. Dokumentiere die Logik in Pseudo-Code-Format (kein echter Code, sondern strukturierte natürliche Sprache): "IF (Bedingung A) AND (Bedingung B) THEN [Aktion]; ELSE IF (Bedingung C) OR (Bedingung D) THEN [Alternative Aktion]; ELSE [Standard-Aktion]". Min. 2 AND-Verknüpfungen (beide Bedingungen müssen erfüllt sein) und min. 1 OR-Verknüpfung (eine von mehreren Bedingungen reicht). Erstelle Trigger-Ketten-Diagramm als Text: "Start → [Bedingung 1: True?] → [Bedingung 2: True?] → [Aktion ausführen] / [False → Fehlerfall-Routing]".
4. Spezifiziere Fehlerfall-Routing für min. 2 Fehler-Szenarien: Definiere was passiert wenn Trigger-Bedingungen nicht eindeutig auswertbar sind. Fehler-Szenario 1: Datenquelle für Trigger nicht verfügbar (z.B. "API für Event-Trigger antwortet nicht" → Aktion: "Retry nach 5 Minuten, max. 3 Versuche, dann Slack-Benachrichtigung"). Fehler-Szenario 2: Trigger-Bedingung mehrdeutig (z.B. "System-Status = unbekannt" → Aktion: "Workflow pausieren, E-Mail an Operator, manuelle Prüfung erforderlich"). Format je Fehler: "Fehler: [Szenario] | Erkennungs-Bedingung: [Wie wird der Fehler erkannt?] | Aktion: [Was passiert?] | Escalation: [Wann muss ein Mensch eingreifen?]".
5. Dokumentiere Trigger-Verifikation und Test-Fälle: Erstelle min. 3 Test-Fälle um die Trigger-Kette zu verifizieren. Test-Fall-Format: "Test 1: [Bedingung A = True, B = True, C = False] → Erwartetes Ergebnis: [Aktion X ausgeführt]". Dokumentiere für jeden Test-Fall: Input-Werte (welche Trigger-Bedingungen sind True/False?), erwartetes Ergebnis (welche Aktion wird ausgeführt?), Verifikations-Methode (wie wird geprüft dass es funktioniert hat? z.B. "Log-Eintrag vorhanden", "E-Mail versendet", "Datei erstellt"). Erstelle Test-Tabelle mit 4 Spalten: Test-Fall-Nr, Input-Werte, Erwartetes Ergebnis, Verifikations-Methode.

## Verifikation

- Trigger-Typen: Alle 5 Typen (Zeit, Event, Daten-Schwelle, Nutzer-Aktion, System-Status) mit min. 1 Beispiel dokumentiert
- Bedingungs-Logik: Min. 2 AND-Verknüpfungen und min. 1 OR-Verknüpfung in Trigger-Kette vorhanden
- Trigger-Ketten-Diagramm: Vollständiger Flow von Start bis Aktion/Fehlerfall dokumentiert
- Fehlerfall-Routing: Min. 2 Fehler-Szenarien mit Erkennungs-Bedingung, Aktion und Escalation
- Test-Fälle: Min. 3 Test-Fälle mit Input, erwarteter Output und Verifikations-Methode
- Failure-Indikator: Wenn Trigger-Bedingung nicht eindeutig formulierbar ist (keine klare True/False-Auswertung möglich) → Meldung "Trigger nicht automatisierbar — Bedingung [X] erfordert menschliches Ermessen. Empfehle Regel-Definition oder manuelle Freigabe als zusätzliche Trigger-Bedingung."
- Akzeptanzkriterium: Alle 5 Trigger-Typen dokumentiert, Bedingungs-Logik mit AND/OR, Trigger-Ketten-Diagramm, min. 2 Fehlerfall-Routings, min. 3 Test-Fälle

## Abhängigkeiten

- Input: Automatisierungs-Szenario (Name, Beschreibung, gewünschtes Ergebnis) — kann auch unstrukturiert sein, der Skill strukturiert es
- Empfohlene Vorgänger-Skills: /elvis-workflow-builder — liefert Workflow-Kontext für komplexe Trigger-Ketten; /elvis-task-automator — liefert Aufgaben-Spezifikation an die Trigger gebunden werden können

## Output

Markdown-Dokument mit 6 Abschnitten: (1) Szenario-Übersicht (Name, Beschreibung, Ergebnis, Nicht-Trigger), (2) Trigger-Definitionen (alle 5 Typen mit konkreten Bedingungen), (3) Bedingungs-Logik (Pseudo-Code-Format mit AND/OR-Verknüpfungen), (4) Trigger-Ketten-Diagramm (Text-basierter Flow), (5) Fehlerfall-Routing (min. 2 Szenarien mit Erkennungs-/Aktions-/Escalation-Regeln), (6) Test-Fälle (min. 3 mit Input/Output/Verifikation). Einsatzbereit als Trigger-Spezifikation für No-Code-Tools oder Custom-Entwicklung.
