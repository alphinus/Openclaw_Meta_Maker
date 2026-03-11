# Skill

## Name

/elvis-insight-extractor

## Beschreibung

Wandelt Rohdaten in priorisierte Erkenntnisse um: Muster-Erkennung aus mindestens 3 Datenpunkten pro Muster, Priorisierungs-Matrix (2×2: Konfidenz × Auswirkung) und Top-5 Erkenntnisse mit Handlungsrelevanz-Einschätzung. Dieser Skill schließt die Lücke zwischen Datenmasse und strategischer Entscheidungsgrundlage — aus Rohdaten werden belastbare, priorisierte Erkenntnisse.

## Ziele

- Mindestens 8 identifizierte Muster (je aus ≥ 3 Datenpunkten)
- Priorisierungs-Matrix (2×2): Alle Muster nach Konfidenz (Hoch/Niedrig) × Auswirkung (Groß/Klein) eingeordnet
- Top-5 Erkenntnisse: aus dem Quadrant "Hohe Konfidenz × Große Auswirkung" priorisiert
- Handlungsrelevanz-Einschätzung: Pro Top-5-Erkenntnis 1 konkreter nächster Schritt
- Datenpunkte-Audit: Liste aller verwendeten Datenpunkte mit Muster-Zuordnung

## Strategie

Rohdaten sind Rauschen ohne Muster-Erkennung. Muster sind Hypothesen ohne Konfidenz-Bewertung. Erkenntnisse sind wertlos ohne Handlungsrelevanz. Dieser Skill arbeitet in drei Phasen: Zuerst Muster-Erkennung durch Datenpunkt-Gruppierung (was co-variiert, was wiederholt sich, was widerspricht Erwartungen?), dann Konfidenz-Bewertung (wie viele Datenpunkte belegen das Muster? Wie diversifiziert sind die Quellen?), dann Auswirkungs-Einschätzung (wenn dieses Muster stimmt — was folgt daraus für Entscheidungen?). Die 2×2-Matrix trennt Aktions-Erkenntnisse (Hohe Konfidenz × Große Auswirkung) von interessanten aber nicht-prioritären Mustern.

## Einschränkungen

- Jedes Muster muss durch mindestens 3 Datenpunkte belegt sein — kein Muster aus 1–2 Datenpunkten
- Datenpunkte müssen aus der übergebenen Datenbasis stammen — keine neuen Daten innerhalb des Skill-Ablaufs erheben
- Konfidenz-Bewertung folgt fester Logik: Hoch = ≥ 5 Datenpunkte aus ≥ 2 verschiedenen Quelltypen, Niedrig = 3–4 Datenpunkte oder nur 1 Quelltyp
- Auswirkungs-Einschätzung: Groß = beeinflusst eine Kernentscheidung (Content-Strategie, Zielgruppe, Format, Timing), Klein = interessant aber nicht entscheidungsrelevant
- Top-5 Erkenntnisse kommen prioritär aus dem Quadrant "Hohe Konfidenz × Große Auswirkung" — falls weniger als 5 Muster in diesem Quadrant: auffüllen aus "Niedrige Konfidenz × Große Auswirkung" mit Kennzeichnung

## Ausführungsschritte

1. Nimm die Rohdaten entgegen und erstelle einen Datenpunkte-Überblick: Zähle alle verfügbaren Datenpunkte, kategorisiere sie nach Typ (Statistik, Zitat, Metrik, Beobachtung, Test-Ergebnis) und notiere die Quelltypen-Verteilung. Format: "Datenpunkte gesamt: [N]. Typen: [Statistiken: X, Zitate: Y, Metriken: Z, ...]. Quelltypen: [Typ 1: X%, Typ 2: Y%, ...]." Empfohlene Vorgänger-Inputs: /elvis-data-collector liefert das Format (Tabelle mit Quelltypen) das direkt weiterverarbeitet werden kann.
2. Gruppiere Datenpunkte nach thematischer Ähnlichkeit zu Mustern: Scanne alle Datenpunkte nach Mustern — was wiederholt sich, was co-variiert, was steht im Widerspruch zur Erwartung? Erstelle Rohgruppen: jede Gruppe = potentielles Muster. Ziel: 10–15 Rohgruppen. Füge jeden Datenpunkt genau 1 Rohgruppe zu (keine Doppelzuordnung). Falls ein Datenpunkt zu keiner Gruppe passt: erstelle Gruppe "Isolierte Datenpunkte" für spätere Prüfung.
3. Validiere die Muster-Gruppen: Prüfe für jede Rohgruppe ob ≥ 3 Datenpunkte vorhanden sind. Gruppen mit < 3 Datenpunkten: verschmelze mit ähnlicher Gruppe falls möglich, sonst verschiebe in "Isolierte Datenpunkte". Formuliere für jedes validierte Muster (≥ 3 Datenpunkte) eine Muster-Aussage in 1 Satz: "Muster [Nr.]: [Aussage was das Muster beschreibt]. Belege: [Datenpunkt A], [Datenpunkt B], [Datenpunkt C] (+ weitere)." Ziel: mindestens 8 validierte Muster.
4. Bewerte alle validierten Muster für die Priorisierungs-Matrix: Für jedes Muster: **Konfidenz** (Hoch = ≥ 5 Datenpunkte aus ≥ 2 Quelltypen; Niedrig = 3–4 Datenpunkte oder nur 1 Quelltyp) und **Auswirkung** (Groß = beeinflusst Kernentscheidung; Klein = interessant aber nicht entscheidungsrelevant). Erstelle die 2×2-Matrix: | Quadrant | Muster-Liste | Anzahl Muster |. Quadranten: (1) Hohe Konfidenz × Große Auswirkung = "Handeln", (2) Niedrige Konfidenz × Große Auswirkung = "Validieren", (3) Hohe Konfidenz × Kleine Auswirkung = "Beobachten", (4) Niedrige Konfidenz × Kleine Auswirkung = "Ignorieren".
5. Identifiziere die Top-5 Erkenntnisse: Priorisiere aus Quadrant "Handeln" (Hohe Konfidenz × Große Auswirkung). Falls < 5 Muster im "Handeln"-Quadrant: ergänze aus "Validieren"-Quadrant mit Kennzeichnung "[Niedrige Konfidenz — erst validieren]". Format pro Erkenntnis: "Erkenntnis [Nr.]: [Aussage in 1–2 Sätzen]. Konfidenz: [Hoch/Niedrig]. Auswirkung: [Groß/Klein]. Belegt durch: [X] Datenpunkte aus [Y] Quelltypen."
6. Entwickle die Handlungsrelevanz-Einschätzung für jede Top-5-Erkenntnis: Format: "Handlungsrelevanz für Erkenntnis [Nr.]: Wenn diese Erkenntnis stimmt, dann [Konsequenz für Strategie/Content/Produkt]. Nächster Schritt: [Konkreter umsetzbarer Handlungsschritt]. Zeitrahmen: [Sofort / Kurzfristig (< 4 Wochen) / Mittelfristig (1–3 Monate)]."
7. Erstelle das Datenpunkte-Audit: Liste alle verwendeten Datenpunkte mit ihrer Muster-Zuordnung. Format: Tabelle | Datenpunkt (kurz) | Typ | Quelle | Muster-Nr. | Quadrant |. Ergänze die Isolierten Datenpunkte-Liste: Datenpunkte die keinem Muster zugeordnet wurden — Begründung warum und ob sie für zukünftige Muster-Erkennung relevant bleiben.

## Verifikation

- Muster-Validierung: Mindestens 8 Muster mit je ≥ 3 Datenpunkten und Muster-Aussage in der validierten Liste
- 2×2-Matrix: Alle validierten Muster einem der 4 Quadranten zugeordnet, Matrix-Tabelle vorhanden
- Top-5-Erkenntnisse: Genau 5 Erkenntnisse mit Konfidenz, Auswirkung und Datenpunkt-Anzahl
- Handlungsrelevanz: Für alle 5 Erkenntnisse vorhanden mit Konsequenz, Schritt und Zeitrahmen
- Datenpunkte-Audit: Tabelle mit vollständiger Zuordnung aller Datenpunkte
- Failure-Indikator: Weniger als 3 Datenpunkte für ein behauptetes Muster → Skill bricht ab mit "Muster-Konfidenz unzureichend: Mindestens 1 Muster mit weniger als 3 Datenpunkten belegt — Erkenntnisqualität nicht gewährleistet"
- Akzeptanzkriterium: ≥ 8 validierte Muster, 2×2-Matrix vollständig, Top-5 mit Konfidenz und Auswirkung, Handlungsrelevanz-Einschätzungen, Datenpunkte-Audit

## Abhängigkeiten

- Input: Rohdaten-Kollektion (als Tabelle, Liste oder Markdown) mit mindestens 15 Datenpunkten aus mindestens 2 verschiedenen Quelltypen
- Empfohlene Vorgänger-Skills: /elvis-data-collector (liefert strukturierte Daten-Tabelle mit Quelltypen-Angaben direkt weiterverarbeitbar für Muster-Gruppierung)

## Output

Insight-Report mit 5 Teilen: (1) Datenpunkte-Überblick (Statistik + Typen-Verteilung), (2) Validierte Muster-Liste (≥ 8 Muster mit Aussage + Datenpunkt-Anzahl), (3) 2×2-Priorisierungs-Matrix (4 Quadranten mit Muster-Zuordnung), (4) Top-5 Erkenntnisse mit Handlungsrelevanz-Einschätzung, (5) Datenpunkte-Audit (Tabelle). Gesamtlänge: max. 1.400 Wörter (ohne Tabellen).
