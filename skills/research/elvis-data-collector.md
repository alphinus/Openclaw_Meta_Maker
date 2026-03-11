# Skill

## Name

/elvis-data-collector

## Beschreibung

Erhebt strukturierte Daten aus 5 Quelltypen: (1) öffentliche Statistiken und Reports, (2) Plattform-Metriken, (3) Nutzer-Aussagen, (4) Konkurrenz-Beobachtungen, (5) Eigene Tests und Experimente. Format: Tabelle mit Spalten (Quelle, Typ, Datum, Datenpunkt, Relevanz 1–3). Vollständigkeits-Check: mindestens 3 Einträge pro Quelltyp für eine belastbare Datenbasis.

## Ziele

- Daten-Tabelle mit mindestens 15 Einträgen (mindestens 3 pro Quelltyp × 5 Typen)
- Vollständigkeits-Check: Dokumentiert ob jeder der 5 Quelltypen ≥ 3 Einträge hat
- Relevanz-Verteilung: Mindestens 5 Einträge mit Relevanz-Score 3 (direkt anwendbar)
- Datenlücken-Report: Quelltypen mit < 3 Einträgen plus Erklärung und Ersatz-Strategie
- Rohdaten-Zusammenfassung: 5 auffälligste Datenpunkte (höchste Relevanz + aktuellstes Datum)

## Strategie

Daten-Erhebung scheitert oft an zwei Extremen: zu wenige Quelltypen (Monokultur) oder zu viele un-priorisierte Datenpunkte (Datenmüll). Die 5-Quelltypen-Struktur erzwingt Diversität: Statistiken geben Makro-Kontext, Plattform-Metriken geben Echtzeit-Performance, Nutzer-Aussagen geben qualitative Belege, Konkurrenz-Beobachtungen geben Benchmarks, eigene Tests geben kontrollierte Evidenz. Der Relevanz-Score 1–3 filtert Datenmüll (Score 1: kontextuell nützlich) von direkt anwendbaren Belegen (Score 3: direkt entscheidungsrelevant). Diese Kombination liefert eine Datenbasis die sowohl Breite (5 Typen) als auch Nutzbarkeit (Relevanz-Filter) sicherstellt.

## Einschränkungen

- Mindestens 2 Quelltypen mit jeweils ≥ 3 Einträgen erforderlich (sonst Failure-Abbruch)
- Datenpunkte müssen konkret und verifizierbar sein: nicht "viele Nutzer mögen das" sondern "87% der Befragten in [Studie] nannten X als Top-3-Priorität"
- Datum-Pflicht: Jeder Eintrag muss ein Erhebungs- oder Publikationsdatum haben (oder explizit "undatiert" mit Begründung)
- Keine Doppeleinträge: Dieselbe Information aus derselben Quelle zählt nur einmal
- Relevanz-Score-Vergabe: 1 = kontextuell nützlich (Hintergrundwissen), 2 = unterstützend (stärkt eine Hypothese), 3 = direkt entscheidungsrelevant (ändert oder bestätigt eine Kernentscheidung)

## Ausführungsschritte

1. Definiere den Erhebungs-Fokus: Thema, Ziel-Frage (Was sollen die Daten beantworten?) und Erhebungszeitraum (Daten aus den letzten [X] Monaten). Erstelle einen Erhebungsplan für alle 5 Quelltypen: Für jeden Typ eine konkrete Quelle benennen (z.B. "Typ 1 — Statistiken: Statista + Google Trends für Nischen-Keywords", "Typ 5 — Eigene Tests: A/B-Test aus den letzten 4 Wochen oder falls nicht verfügbar: Pilot-Experiment als nächster Schritt"). Ziel: 5 Quellen-Angaben als Plan vor der Erhebung.
2. Erhebe Daten aus **Quelltyp 1 — Öffentliche Statistiken und Reports**: Suche in mindestens 3 verschiedenen Quellen (z.B. Statista, Branchenreporte, Akademische Paper, Regierungsstatistiken). Ziel: ≥ 5 Datenpunkte. Für jeden Datenpunkt: exakte Zahl oder Aussage aus der Quelle übernehmen (nicht paraphrasieren), Quelle + URL, Publikationsdatum, Relevanz-Score 1–3. Füge alle Einträge in die Daten-Tabelle ein.
3. Erhebe Daten aus **Quelltyp 2 — Plattform-Metriken**: Eigene oder öffentlich einsehbare Metriken von Plattformen (YouTube Analytics, Social-Media-Insights, Newsletter-Statistiken, Website-Analytics). Falls keine eigenen Daten verfügbar: nutze öffentliche Benchmarks (z.B. "durchschnittliche Email-Open-Rate in [Branche]: 24%"). Ziel: ≥ 5 Datenpunkte. Erhebe Daten aus **Quelltyp 3 — Nutzer-Aussagen**: Direkte Zitate aus Foren, Reviews, Kommentaren oder Direktgesprächen. Ziel: ≥ 5 authentische Aussagen mit Quellenangabe. Füge alle Einträge in die Tabelle.
4. Erhebe Daten aus **Quelltyp 4 — Konkurrenz-Beobachtungen**: Beobachtbare Daten über Konkurrenten (Posting-Frequenz, Content-Formate, sichtbare Engagement-Raten, Produktpreise, Positionierung). Ziel: ≥ 5 Datenpunkte aus mindestens 3 verschiedenen Konkurrenten. Erhebe Daten aus **Quelltyp 5 — Eigene Tests und Experimente**: Dokumentierte Ergebnisse eigener Aktivitäten (z.B. "Post A mit Bild: 120 Likes, Post B ohne Bild: 45 Likes — Bild-Format +167%"). Falls keine Tests vorliegen: dokumentiere "kein eigener Test verfügbar" und markiere Typ 5 als Datenlücke. Füge alle Einträge in die Tabelle.
5. Konsolidiere die vollständige Daten-Tabelle: Format | Nr. | Quelle | Typ (1–5) | Datum | Datenpunkt (exakt) | Relevanz (1–3) |. Sortiere nach Typ, dann nach Relevanz absteigend. Zähle Einträge pro Quelltyp und erstelle den Vollständigkeits-Check: | Typ | Anzahl Einträge | Status (✓ ≥ 3 / ✗ < 3) |.
6. Führe den Datenlücken-Report durch: Identifiziere alle Quelltypen mit < 3 Einträgen. Für jeden Lücken-Typ: Erkläre warum wenig Daten verfügbar sind (Nische zu eng? Daten hinter Paywall? Kein eigener Test?) und empfehle eine Ersatz-Strategie (welche alternative Quelle könnte diese Lücke schließen?). Format: "Datenlücke Typ [X]: [Erklärung]. Ersatz-Strategie: [Konkreter Vorschlag]."
7. Identifiziere die 5 auffälligsten Datenpunkte für die Rohdaten-Zusammenfassung: Auswahlkriterien — Relevanz-Score 3 hat Priorität, bei Gleichstand: aktuellstes Datum. Format pro Eintrag: "Datenpunkt [Nr.]: [Exakter Datenpunkt]. Quelle: [Typ + Quelle]. Warum auffällig: [1 Satz warum dieser Datenpunkt besonders relevant oder überraschend ist]."

## Verifikation

- Tabellen-Vollständigkeit: Alle Einträge haben alle 6 Spalten ausgefüllt (Nr., Quelle, Typ, Datum, Datenpunkt, Relevanz)
- Vollständigkeits-Check: Tabelle mit 5 Zeilen (eine pro Typ) und Status ✓/✗ vorhanden
- Relevanz-Verteilung: Mindestens 5 Einträge mit Relevanz-Score 3 in der Gesamttabelle
- Datenlücken-Report: Für alle Typen mit < 3 Einträgen vorhanden mit Ersatz-Strategie
- Rohdaten-Zusammenfassung: Genau 5 Einträge mit Begründung "warum auffällig"
- Failure-Indikator: Weniger als 2 Quelltypen mit ≥ 3 Einträgen nach vollständiger Erhebung → Skill bricht ab mit "Datenbasis unzureichend: Weniger als 2 Quelltypen mit ausreichend Daten (≥ 3 Einträge) — Daten-Diversität für verlässliche Analyse nicht gegeben"
- Akzeptanzkriterium: ≥ 15 Einträge in der Tabelle, Vollständigkeits-Check vorhanden, ≥ 5 Relevanz-3-Einträge, Datenlücken-Report, Rohdaten-Zusammenfassung

## Abhängigkeiten

- Input: Erhebungs-Fokus (Thema + Ziel-Frage + Zeitraum) und optional: Liste bekannter Quellen die geprüft werden sollen
- Empfohlene Vorgänger-Skills: /elvis-market-scan (Marktdaten als Basis für Quelltyp 1), /elvis-competitor-deep-dive (Konkurrenz-Daten als Basis für Quelltyp 4)

## Output

Daten-Kollektion mit 4 Teilen: (1) Erhebungs-Plan (5 Quelltypen mit je Quelle + Ziel), (2) Vollständige Daten-Tabelle (≥ 15 Einträge × 6 Spalten), (3) Vollständigkeits-Check + Datenlücken-Report, (4) Rohdaten-Zusammenfassung (Top-5 auffälligste Datenpunkte). Gesamtlänge: max. 1.200 Wörter (ohne Tabelle).
