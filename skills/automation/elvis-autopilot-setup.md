# Skill

## Name

/elvis-autopilot-setup

## Beschreibung

Richtet vollständige "Set & Forget"-Automatisierungs-Systeme ein: integriert mehrere Workflows zu einem autonomen System mit Monitoring, Alarm-Regeln und manuellen Override-Optionen. Ein Autopilot-System läuft kontinuierlich mit minimaler menschlicher Intervention (Ziel: <2 manuelle Eingriffe pro Woche) und meldet sich nur bei Problemen oder Entscheidungspunkten. Im Gegensatz zu Einzel-Workflows (z.B. `elvis-workflow-builder`, `elvis-batch-processor`) orchestriert dieser Skill End-to-End-Systeme über mehrere Tools und Prozesse hinweg.

## Ziele

- System-Architektur: Vollständige Beschreibung des Autopilot-Systems (Zweck, integrierte Workflows, involvierte Tools)
- Monitoring-Setup: mindestens 3 Health-Metriken (z.B. Verarbeitungszeit, Fehlerquote, Durchsatz) mit Schwellwerten definiert
- Alarm-Regeln: mindestens 2 kritische Alarm-Bedingungen (z.B. Fehlerquote >5%, System offline >10 Min) mit Eskalations-Kanälen (E-Mail/Slack/SMS)
- Override-Optionen: manuelle Eingriffs-Punkte definiert (z.B. Pause-Button, manuelle Freigabe für kritische Aktionen, Notfall-Rollback)
- Autonomie-Level: dokumentiert wie viele manuelle Eingriffe pro Woche erwartet werden (Ziel: <2)

## Strategie

Der Skill nutzt System-Orchestrierung statt Workflow-Ketten: Ein Autopilot-System ist mehr als die Summe seiner Workflows — es braucht Überwachung (Monitoring), Selbst-Korrektur (Retry-Logik, Fallback-Strategien) und kontrollierte Eskalation (Alarme nur bei echten Problemen, nicht bei normalen Schwankungen). Die Autonomie-Level-Metrik ist der Erfolgs-Indikator: Ein System das >2 manuelle Eingriffe/Woche benötigt ist kein echter Autopilot sondern ein überwachungsbedürftiges Automatisierungs-System. Manuelle Override-Optionen sind Sicherheits-Ventile — sie erlauben menschliches Eingreifen ohne das ganze System zu deaktivieren.

## Einschränkungen

- Nur für wiederkehrende, regelbasierte Prozesse geeignet — komplexe Entscheidungen oder kreative Aufgaben können nicht vollständig autopilotiert werden
- Mindestens 2 integrierte Workflows nötig — ein einzelner Workflow ist kein End-to-End-System sondern ein normaler Automatisierungs-Job
- Kritische Alarm-Bedingungen müssen actionable sein (z.B. "Fehlerquote >5%" ist actionable, "System läuft langsam" ist zu vage)
- Override-Optionen müssen erreichbar sein (z.B. Dashboard-Button, Admin-E-Mail-Adresse) — keine versteckten Notfall-Prozeduren
- Autonomie-Level <2 Eingriffe/Woche ist Ziel — manche Systeme benötigen mehr (z.B. finanzielle oder rechtliche Freigaben), dann Autopilot nicht geeignet

## Ausführungsschritte

1. Definiere System-Zweck und Scope: Bitte den Operator den Autopilot-Use-Case zu beschreiben: Welches End-to-End-Ziel wird verfolgt (z.B. "vollautomatischer Social-Media-Content-Cycle von Recherche bis Veröffentlichung"), welche Teil-Workflows sind involviert (z.B. "Content-Recherche → Artikel-Generierung → Bild-Auswahl → Post-Scheduling → Performance-Tracking"), welche Tools sind beteiligt. Dokumentiere: System-Zweck (1-2 Sätze), integrierte Workflows (nummerierte Liste mit je 1-2 Sätzen), involvierte Tools (kommaseparierte Liste).
2. Spezifiziere integrierte Workflows: Für jeden Teil-Workflow dokumentiere: Workflow-Name, Input (was triggert den Workflow), Output (was wird produziert), Verbindung zum nächsten Workflow (wie fließen Daten weiter). Erstelle eine Workflow-Kette als nummerierte Liste: "1. Workflow A → Output X → 2. Workflow B → Output Y → 3. Workflow C → Endzustand". Mindestens 2 Workflows, besser 3-5 für echtes End-to-End-System.
3. Definiere Monitoring-Metriken: Identifiziere mindestens 3 Health-Metriken die kontinuierlich überwacht werden: Verarbeitungszeit (z.B. "durchschnittliche Zeit von Input bis Endzustand" in Minuten/Stunden), Fehlerquote (z.B. "% fehlgeschlagener Workflow-Durchläufe"), Durchsatz (z.B. "Einheiten pro Tag/Woche"). Für jede Metrik definiere: Normaler Bereich (z.B. "Verarbeitungszeit 30-60 Min"), Warn-Schwelle (z.B. ">90 Min"), kritische Schwelle (z.B. ">120 Min oder System hängt").
4. Konfiguriere Alarm-Regeln: Definiere mindestens 2 kritische Alarm-Bedingungen die sofortige Aufmerksamkeit benötigen (z.B. "Fehlerquote >5% über 1 Stunde", "System offline >10 Minuten", "kein Output seit >24 Stunden"). Für jede Alarm-Bedingung dokumentiere: Bedingung (konkrete Schwelle), Eskalations-Kanal (E-Mail/Slack/SMS), Empfänger (wer wird alarmiert), erwartete Reaktionszeit (z.B. "innerhalb 2 Stunden"). Vermeide Alarm-Spam — nur echte Probleme alarmieren, nicht normale Schwankungen.
5. Spezifiziere Override-Optionen: Definiere manuelle Eingriffs-Punkte für Notfälle oder Sonderfälle: Pause-Button (stoppt alle Workflows temporär ohne Daten zu verlieren), manuelle Freigabe für kritische Aktionen (z.B. "Veröffentlichung wartet auf OK-Button bevor Post live geht"), Notfall-Rollback (z.B. "letzten verarbeiteten Batch rückgängig machen"). Dokumentiere für jede Override-Option: Name, Zweck (wann wird sie gebraucht), Zugriffs-Methode (z.B. "Dashboard-Button unter /admin/autopilot"), erwartete Nutzungs-Häufigkeit (z.B. "1-2× pro Monat für Sonderfälle").
6. Schätze Autonomie-Level: Basierend auf den definierten Alarm-Regeln und Override-Optionen schätze: Wie viele manuelle Eingriffe pro Woche sind realistisch (Ziel: <2). Zähle: Erwartete Alarme (basierend auf historischer Fehlerquote oder Schätzung), geplante manuelle Freigaben (falls vorhanden), Notfall-Overrides (sehr selten, <1× pro Monat). Dokumentiere: erwartete Eingriffe/Woche, Begründung (1-2 Sätze), ob Ziel <2 erreicht wird.

## Verifikation

- System-Architektur: Zweck, integrierte Workflows (≥2) und involvierte Tools dokumentiert
- Workflow-Kette: alle Teil-Workflows mit Input/Output/Verbindung dokumentiert, klare End-to-End-Abfolge erkennbar
- Monitoring-Metriken: mindestens 3 Metriken mit Normaler Bereich, Warn-Schwelle, kritischer Schwelle definiert
- Alarm-Regeln: mindestens 2 kritische Bedingungen mit Eskalations-Kanal und Reaktionszeit definiert
- Override-Optionen: mindestens 2 manuelle Eingriffs-Punkte (z.B. Pause, manuelle Freigabe) mit Zugriffs-Methode dokumentiert
- Autonomie-Level: erwartete Eingriffe/Woche geschätzt und dokumentiert
- Failure-Indikator: Wenn Autonomie-Level >2 manuelle Eingriffe/Woche → Meldung "Kein echter Autopilot — System benötigt [X] Eingriffe/Woche (Ziel: <2). Empfehle entweder mehr Automatisierung (z.B. automatische Freigaben statt manueller), robustere Fehler-Behandlung (weniger Alarme) oder akzeptieren dass dieser Prozess überwachungsbedürftig ist."
- Akzeptanzkriterium: System-Architektur mit ≥2 Workflows, ≥3 Monitoring-Metriken, ≥2 Alarm-Regeln, ≥2 Override-Optionen, Autonomie-Level geschätzt ≤2 Eingriffe/Woche

## Abhängigkeiten

- Input: Beschreibung des End-to-End-Use-Cases (Ziel, Teil-Workflows, involvierte Tools)
- Empfohlene Vorgänger-Skills: `elvis-workflow-builder` (baut Einzel-Workflows die hier integriert werden), `elvis-trigger-builder` (definiert Auslöser für automatische Workflow-Starts), `elvis-batch-processor` (definiert Batch-Verarbeitungs-Workflows die in das Autopilot-System eingebettet werden können), `elvis-integration-mapper` (zeigt welche Tool-Integrationen bereits existieren und für das Autopilot-System genutzt werden können)

## Output

Markdown-Dokument mit 6 Abschnitten: (1) System-Architektur (Zweck, integrierte Workflows, involvierte Tools), (2) Workflow-Kette (End-to-End-Abfolge mit Input/Output/Verbindungen), (3) Monitoring-Setup (≥3 Metriken mit Schwellwerten), (4) Alarm-Regeln (≥2 kritische Bedingungen mit Eskalations-Kanal), (5) Override-Optionen (≥2 manuelle Eingriffs-Punkte mit Zugriffs-Methode), (6) Autonomie-Level (erwartete Eingriffe/Woche und Bewertung ob Ziel <2 erreicht). Einsatzbereit als Spezifikation für vollautomatisches "Set & Forget"-System.
