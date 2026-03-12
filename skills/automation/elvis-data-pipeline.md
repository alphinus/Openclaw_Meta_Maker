# Skill

## Name

/elvis-data-pipeline

## Beschreibung

Entwirft Daten-Fluss-Pipelines zwischen Tools: Spezifikation von min. 3 Datenquellen, Transformation-Schritte, min. 2 Ausgabe-Ziele, Validierungs-Checkpoints. Liefert eine vollständige Pipeline-Architektur-Spezifikation — keine Code-Implementierung, sondern strukturierte Dokumentation der Daten-Flüsse, Transformations-Regeln und Qualitäts-Checks.

## Ziele

- Vollständige Pipeline-Spezifikation: min. 3 Datenquellen → Transformations-Schritte → min. 2 Ausgabe-Ziele
- Definierte Transformations-Regeln: min. 4 Transformations-Schritte (Filtern, Aggregieren, Formatieren, Anreichern)
- Validierungs-Checkpoints: min. 3 Qualitäts-Checks an strategischen Punkten der Pipeline (Eingang, Mitte, Ausgang)
- Fehler-Handling: Spezifikation was bei Daten-Qualitäts-Problemen passiert (min. 2 Fehler-Szenarien)

## Strategie

Der Skill fokussiert auf die **Daten-Ebene der Automation**: Während /elvis-workflow-builder Aufgaben-Flows dokumentiert, spezifiziert dieser Skill **Daten-Flüsse**. Die Pipeline-Struktur folgt dem ETL-Prinzip (Extract-Transform-Load): Daten aus min. 3 Quellen extrahieren, in min. 4 Schritten transformieren, in min. 2 Ziele laden. Die Validierungs-Checkpoints sind kritisch: Ohne sie werden fehlerhafte Daten weitergereicht und kontaminieren Downstream-Systeme. Der Output ist keine Code-Implementierung, sondern eine Architektur-Spezifikation die ein Entwickler oder No-Code-Tool implementieren kann.

## Einschränkungen

- Min. 3 Datenquellen — weniger ist trivial (einfache 1:1-Sync ohne Skill machbar)
- Min. 2 Ausgabe-Ziele — Single-Target-Pipelines sind selten (meist braucht man Dashboard + Storage oder Report + Alert)
- Min. 4 Transformations-Schritte — weniger ist keine Pipeline sondern simpler Datentransfer
- Max. 10 Transformations-Schritte — mehr wird unübersichtlich (besser in Teil-Pipelines aufteilen)
- Keine Code-Implementierung — nur Pipeline-Spezifikation mit Tool-Empfehlungen und Transformations-Logik in natürlicher Sprache
- Datenquellen müssen API/Export-Funktion haben — manuelle Copy-Paste-Daten sind nicht Pipeline-fähig

## Ausführungsschritte

1. Erfasse alle Datenquellen und Ausgabe-Ziele: Erfrage vom Operator: Pipeline-Zweck (1-2 Sätze was erreicht werden soll), Datenquellen (min. 3 aus: CRM, E-Mail-Tool, Analytics-Tool, E-Commerce-System, Social-Media-Plattform, Datenbank, Google Sheets, etc.), Ausgabe-Ziele (min. 2 aus: Dashboard, Data-Warehouse, Google Sheets, BI-Tool, Reporting-System, Alert-System, etc.). Dokumentiere für jede Datenquelle: Name, Daten-Typ (z.B. "Kunden-Kontakte", "Verkaufs-Transaktionen", "Website-Traffic"), Update-Frequenz (Echtzeit/Stündlich/Täglich/Wöchentlich), Export-Methode (API/CSV-Export/Datenbank-Query/Webhook). Erstelle Quellen-Tabelle mit 5 Spalten: Quelle-Nr, Name, Daten-Typ, Update-Frequenz, Export-Methode.
2. Definiere Transformations-Schritte in 4 Kategorien: Spezifiziere min. 4 Transformations-Schritte die auf die Daten angewendet werden. Transformation 1 (Filtern): Welche Daten werden ausgeschlossen? (z.B. "Nur Kunden mit Status = Aktiv", "Nur Transaktionen der letzten 30 Tage"). Transformation 2 (Aggregieren): Wie werden Daten zusammengefasst? (z.B. "Umsatz pro Tag summieren", "Durchschnittliche Session-Dauer berechnen"). Transformation 3 (Formatieren): Wie werden Daten-Formate vereinheitlicht? (z.B. "Datumsformat YYYY-MM-DD", "Währung in EUR konvertieren", "Text trimmen und lowercase"). Transformation 4 (Anreichern): Welche zusätzlichen Daten werden hinzugefügt? (z.B. "Kundensegment aus CRM hinzufügen", "Geo-Location aus IP-Adresse ermitteln"). Format je Transformation: "Schritt N ([Kategorie]): [Regel] → [Ergebnis]".
3. Spezifiziere Validierungs-Checkpoints an 3 Punkten: Definiere Qualitäts-Checks die an strategischen Punkten der Pipeline laufen. Checkpoint 1 (Eingang): Prüfung nach Daten-Extraktion (z.B. "Min. 100 Einträge vorhanden?", "Keine Null-Werte in Pflichtfeldern?", "Alle Quellen haben Daten geliefert?"). Checkpoint 2 (Mitte): Prüfung nach Transformation (z.B. "Aggregations-Summen plausibel?", "Formatierung erfolgreich?", "Keine Duplikate?"). Checkpoint 3 (Ausgang): Prüfung vor Daten-Load (z.B. "Ziel-Schema erfüllt?", "Daten-Größe <Max-Limit?", "Zeitstempel aktuell?"). Format je Checkpoint: "Checkpoint [Position]: [Prüfung 1], [Prüfung 2], [Prüfung 3] → Bei Fehler: [Aktion]".
4. Definiere Fehler-Handling für min. 2 Fehler-Szenarien: Spezifiziere was bei Daten-Qualitäts-Problemen passiert. Fehler-Szenario 1: Datenquelle liefert keine/fehlerhafte Daten (z.B. "API antwortet nicht" oder "CSV-Datei leer") → Aktion: "Retry nach 10 Minuten, max. 3 Versuche, dann E-Mail an Operator + Pipeline pausieren". Fehler-Szenario 2: Validierungs-Checkpoint schlägt fehl (z.B. "Duplikate gefunden" oder "Pflichtfeld fehlt") → Aktion: "Fehlerhafte Einträge in Quarantäne-Tabelle schreiben + Rest der Pipeline fortsetzen + täglicher Fehler-Report". Format je Fehler: "Fehler: [Szenario] | Erkennungs-Bedingung: [Wie wird der Fehler erkannt?] | Aktion: [Was passiert?] | Daten-Behandlung: [Werden fehlerhafte Daten verworfen/behalten/quarantänisiert?]".
5. Erstelle Pipeline-Architektur-Diagramm und Tool-Empfehlungen: Dokumentiere den vollständigen Daten-Fluss als Text-basiertes Diagramm: "Quellen ([Q1], [Q2], [Q3]) → Extraktion → Checkpoint 1 → Transformation (4 Schritte) → Checkpoint 2 → Load → Checkpoint 3 → Ziele ([Z1], [Z2])". Ergänze Mengenangaben: "Erwartetes Daten-Volumen: [X] Einträge pro Tag, Pipeline-Laufzeit: [Y] Minuten, Update-Frequenz: [täglich/stündlich]". Empfehle Pipeline-Tool basierend auf Komplexität: Einfach (1-2h Setup): Zapier, Make.com; Mittel (1-2 Tage): n8n, Airbyte; Komplex (>3 Tage): Custom-ETL mit Python/SQL, dbt, Airflow. Nenne für gewähltes Tool: Name, Preis-Hinweis, Begründung (1 Satz).

## Verifikation

- Quellen-Tabelle: Min. 3 Datenquellen mit Daten-Typ, Update-Frequenz, Export-Methode dokumentiert
- Transformations-Schritte: Min. 4 Schritte in 4 Kategorien (Filtern, Aggregieren, Formatieren, Anreichern) spezifiziert
- Validierungs-Checkpoints: 3 Checkpoints (Eingang, Mitte, Ausgang) mit jeweils min. 2 Prüfungen pro Checkpoint
- Fehler-Handling: Min. 2 Fehler-Szenarien mit Erkennungs-Bedingung, Aktion und Daten-Behandlung
- Pipeline-Diagramm: Vollständiger Daten-Fluss von Quellen über Transformationen zu Zielen dokumentiert
- Mengenangaben: Erwartetes Daten-Volumen, Pipeline-Laufzeit und Update-Frequenz spezifiziert
- Failure-Indikator: Wenn mehr als 1 Datenquelle keine API/Export-Funktion hat → Meldung "Pipeline nicht automatisierbar — [N] von [M] Quellen haben keine API/Export. Benötigte Quellen: [Liste]. Empfehle manuelle Daten-Sammlung oder Tool-Wechsel zu API-fähigen Alternativen."
- Akzeptanzkriterium: Min. 3 Quellen + min. 2 Ziele dokumentiert, min. 4 Transformations-Schritte, 3 Validierungs-Checkpoints, min. 2 Fehler-Handlings, Pipeline-Diagramm, Tool-Empfehlung

## Abhängigkeiten

- Input: Pipeline-Zweck (1-2 Sätze), Liste der verfügbaren Datenquellen und gewünschten Ausgabe-Ziele — auch unstrukturiert, der Skill strukturiert sie
- Empfohlene Vorgänger-Skills: /elvis-automation-audit — identifiziert Daten-Integration-Bedarf als Automatisierungs-Kandidat; /elvis-kpi-dashboard (aus Analysis-Kategorie) — definiert welche Metriken das Ausgabe-Ziel braucht

## Output

Markdown-Dokument mit 6 Abschnitten: (1) Quellen-Tabelle (min. 3 Datenquellen mit Daten-Typ, Update-Frequenz, Export-Methode), (2) Transformations-Schritte (min. 4 in 4 Kategorien mit Regeln und Ergebnissen), (3) Validierungs-Checkpoints (3 Checkpoints mit jeweils 2-3 Prüfungen), (4) Fehler-Handling (min. 2 Szenarien mit Erkennungs-/Aktions-/Daten-Behandlungs-Regeln), (5) Pipeline-Architektur-Diagramm (Text-basierter Daten-Fluss mit Mengenangaben), (6) Tool-Empfehlungen (Pipeline-Tool mit Preis und Begründung). Einsatzbereit als ETL-Pipeline-Spezifikation für Entwickler oder No-Code-Implementierung.
