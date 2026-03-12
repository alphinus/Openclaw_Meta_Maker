# Skill

## Name

/elvis-batch-processor

## Beschreibung

Entwirft Batch-Verarbeitungs-Workflows für wiederkehrende Datenmengen: definiert optimale Batch-Größe (Einheiten pro Batch), Zeitfenster (Stunden für Verarbeitung), Fehlerquoten-Schwelle (%) und Retry-Strategie. Geeignet für Content-Erstellung, Daten-Analysen, Report-Generierung und andere Mengen-basierte Verarbeitungen. Im Gegensatz zu Event-basierten Triggern (z.B. `elvis-trigger-builder`) arbeitet dieser Skill mit geplanten Zeitfenstern und akkumulierten Datenmengen.

## Ziele

- Batch-Spezifikation: Batch-Größe (Anzahl Einheiten pro Verarbeitungs-Lauf), Zeitfenster (Stunden zwischen Läufen), erwartete Verarbeitungszeit pro Batch
- Fehler-Handling: Fehlerquoten-Schwelle (%), Retry-Strategie (Anzahl Wiederholungen, Backoff-Intervall), Eskalations-Regel (ab welcher Fehlerquote manuelle Intervention)
- Performance-Profil: Durchsatz (Einheiten pro Stunde), Ressourcen-Bedarf (CPU/Memory/Storage), Skalierungs-Strategie (was passiert bei doppelter Datenmenge)
- Testlauf-Ergebnisse: Minimale Validierung mit 1-2 Beispiel-Batches, dokumentierte Fehlerquote und Verarbeitungszeit

## Strategie

Der Skill nutzt Batch-basierte Verarbeitung statt Echtzeit-Processing: Daten werden akkumuliert bis eine Batch-Größe erreicht ist oder ein Zeitfenster abläuft, dann erfolgt die Verarbeitung in einem Durchlauf. Das reduziert Overhead (eine Verbindung statt hunderte), erlaubt Optimierungen (Bulk-APIs, parallele Verarbeitung innerhalb des Batches) und macht Fehler-Handling robuster (fehlgeschlagene Einheiten können isoliert wiederholt werden). Die Fehlerquoten-Schwelle ist kritisch: <5% ist normal (vereinzelte fehlerhafte Daten), 5-10% signalisiert Daten-Qualitätsprobleme, >10% bedeutet der Batch-Prozessor ist nicht produktionsbereit.

## Einschränkungen

- Nur für wiederkehrende Datenmengen verwenden — einmalige Massen-Verarbeitungen sind keine Batch-Workflows sondern Migrations-Skripte
- Batch-Größe muss messbar sein (z.B. "100 Artikel" oder "500 E-Mails") — keine abstrakten Einheiten wie "alle neuen Daten"
- Zeitfenster muss realistisch sein (Verarbeitungszeit < Zeitfenster) — sonst überlappen sich Batches und erzeugen Konflikte
- Fehlerquoten-Schwelle nur für transiente Fehler (z.B. API-Timeouts, Netzwerk-Probleme) — systematische Fehler (z.B. fehlerhafte Logik) müssen vor Produktiv-Einsatz behoben werden
- Keine Echtzeit-Anforderungen — wenn Daten sofort verarbeitet werden müssen, ist ein Event-basierter Workflow besser geeignet

## Ausführungsschritte

1. Definiere den Batch-Kontext: Bitte den Operator den Verarbeitungs-Use-Case zu beschreiben: Was wird verarbeitet (z.B. "neue Artikel für Social-Media-Posts generieren"), wie viele Einheiten fallen an (pro Tag/Woche), welche Verarbeitungs-Schritte sind nötig (z.B. "Artikel abrufen → KI-Text generieren → in Content-Kalender eintragen"). Dokumentiere: Use-Case (1-2 Sätze), erwartete Datenmenge (Einheiten pro Tag/Woche), Verarbeitungs-Schritte (nummerierte Liste).
2. Bestimme optimale Batch-Größe: Frage den Operator nach Constraints: Gibt es API-Limits (z.B. max. 100 Anfragen pro Batch), Verarbeitungszeit-Grenzen (z.B. Batch muss in <30 Min fertig sein), Kosten-Überlegungen (größere Batches = weniger API-Aufrufe = günstiger). Berechne Batch-Größe als Kompromiss zwischen Effizienz (größer ist besser) und Constraints (kleiner ist sicherer). Dokumentiere: empfohlene Batch-Größe (Anzahl Einheiten), Begründung (1-2 Sätze), erwartete Verarbeitungszeit pro Batch (Minuten).
3. Definiere Zeitfenster und Cadence: Basierend auf Datenmenge und Batch-Größe berechne: Wie oft muss der Batch laufen (z.B. bei 500 Einheiten/Tag und Batch-Größe 100 → 5 Batches/Tag → alle 4-5 Stunden). Definiere Zeitfenster (Stunden zwischen Batch-Läufen) und bevorzugte Laufzeit (z.B. nachts/zu festen Zeiten). Dokumentiere: Zeitfenster (Stunden), Batches pro Tag/Woche, bevorzugte Laufzeit (optional).
4. Spezifiziere Fehler-Handling: Definiere Fehlerquoten-Schwelle (empfohlen: 5% — darüber ist Eskalation nötig), Retry-Strategie (z.B. 3 Wiederholungen mit 1-Minute Backoff), Verhalten bei dauerhaft fehlenden Einheiten (z.B. in Fehler-Log schreiben und überspringen). Dokumentiere: Fehlerquoten-Schwelle (%), Retry-Anzahl, Backoff-Intervall (Sekunden/Minuten), Eskalations-Regel (z.B. "Fehlerquote >5% → E-Mail an Admin").
5. Führe Testlauf durch: Simuliere 1-2 Beispiel-Batches mit realistischen Daten (falls vorhanden) oder Dummy-Daten. Messe: tatsächliche Verarbeitungszeit, aufgetretene Fehler (Anzahl und Art), Ressourcen-Verbrauch (falls messbar). Berechne Fehlerquote = (fehlerhafte Einheiten / Gesamt-Einheiten) × 100%. Dokumentiere Testlauf-Ergebnisse: Batch-Größe, Verarbeitungszeit, Fehlerquote, beobachtete Probleme (falls vorhanden).

## Verifikation

- Batch-Spezifikation: Batch-Größe (Anzahl), Zeitfenster (Stunden) und Verarbeitungszeit dokumentiert
- Fehler-Handling: Fehlerquoten-Schwelle (%), Retry-Strategie (Anzahl, Backoff), Eskalations-Regel definiert
- Zeitfenster-Konsistenz: Verarbeitungszeit < Zeitfenster (sonst Batch-Überlappung möglich)
- Testlauf: mindestens 1 Testlauf dokumentiert mit Batch-Größe, Verarbeitungszeit und Fehlerquote
- Failure-Indikator: Wenn Fehlerquote im Testlauf >5% → Meldung "Batch-Prozessor nicht produktionsbereit — Fehlerquote [X]% überschreitet Schwelle von 5%. Empfehle Fehlerursachen zu analysieren und Daten-Qualität/Verarbeitungs-Logik zu verbessern bevor der Prozessor in Produktion geht."
- Akzeptanzkriterium: Batch-Größe, Zeitfenster und Fehlerquoten-Schwelle spezifiziert, Fehler-Handling definiert, mindestens 1 Testlauf mit dokumentierter Fehlerquote <5%

## Abhängigkeiten

- Input: Beschreibung des Verarbeitungs-Use-Cases (was wird verarbeitet, erwartete Datenmenge, Verarbeitungs-Schritte)
- Empfohlene Vorgänger-Skills: `elvis-data-pipeline` (kann die Daten-Quelle für den Batch-Prozessor liefern)
- Empfohlene Nachfolger-Skills: `elvis-autopilot-setup` (kann den Batch-Prozessor in ein autonomes System integrieren)

## Output

Markdown-Dokument mit 5 Abschnitten: (1) Batch-Kontext (Use-Case, Datenmenge, Verarbeitungs-Schritte), (2) Batch-Spezifikation (Batch-Größe, Zeitfenster, Verarbeitungszeit), (3) Fehler-Handling (Fehlerquoten-Schwelle, Retry-Strategie, Eskalations-Regel), (4) Performance-Profil (Durchsatz, Ressourcen-Bedarf, Skalierungs-Strategie), (5) Testlauf-Ergebnisse (Batch-Größe, Verarbeitungszeit, Fehlerquote). Einsatzbereit als Spezifikation für Batch-Workflow-Implementierung.
