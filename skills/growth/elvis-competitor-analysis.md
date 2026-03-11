# Skill

## Name

/elvis-competitor-analysis

## Beschreibung

Analysiert 5 direkte Konkurrenz-Accounts auf X/Twitter systematisch nach 5 Metriken. Liefert eine Vergleichstabelle (5 Accounts × 5 Metriken) plus 3 datenbasierte Handlungsempfehlungen — als Grundlage für die eigene Positionierung in der Nische.

## Ziele

- 5 Konkurrenz-Accounts ausgewählt und begründet (aus dem Zielgruppen-Profil abgeleitet)
- Vergleichstabelle 5 × 5 vollständig befüllt: Follower-Anzahl, Posting-Frequenz/Woche, Content-Mix (% Text/Bild/Thread), Top-3-Posts-Engagement-Rate, geschätztes Follower-Wachstum/Woche
- 3 konkrete Handlungsempfehlungen aus der Analyse abgeleitet
- Positionierungs-Lücke identifiziert: was machen Konkurrenten nicht, was die eigene Zielgruppe möchte

## Strategie

Die Analyse geht systematisch vor: erst Rohdaten erheben (Metriken), dann Muster erkennen (wer wächst warum?), dann Lücken identifizieren (was fehlt im Markt?). Fünf Accounts sind die Mindest-Datenbasis für verlässliche Muster — weniger führt zu Überinterpretation von Einzelfällen. Handlungsempfehlungen basieren ausschließlich auf beobachteten Daten, nicht auf Annahmen.

## Einschränkungen

- Genau 5 Konkurrenz-Accounts pro Analyse — nicht mehr, nicht weniger
- Nur öffentlich zugängliche Metriken erheben (keine API-Calls ohne Freigabe)
- Wachstumsschätzung basiert auf Vergleich aktueller Follower-Zahl vs. öffentlich sichtbarem Profil-Verlauf (Schätzung mit Unsicherheitsangabe)
- Keine Analyse privater Posts oder DMs
- Analyse-Zeitraum: die letzten 30 Tage für Posting-Frequenz und Content-Mix

## Ausführungsschritte

1. Wähle 5 Konkurrenz-Accounts aus dem Referenz-Account-Pool des Zielgruppen-Profils (elvis-audience-builder Output). Begründe jede Auswahl in 1 Satz: warum dieser Account als direkter Konkurrent gilt (gleiche Nische, ähnliche Follower-Zahl ±50 % oder klarer Aspirations-Account). Dokumentiere die 5 Accounts als Ausgangsliste.
2. Erhebe für jeden der 5 Accounts die Basis-Metriken: aktuelle Follower-Anzahl, Posting-Frequenz (Posts pro Woche, gemessen über die letzten 4 Wochen), Erstellungsdatum des Accounts (für Wachstums-Kontext). Trage die Werte in eine erste Tabellen-Version ein (5 Zeilen × 3 Spalten als Zwischenstand).
3. Analysiere den Content-Mix der letzten 30 Posts pro Account: zähle Text-Only-Posts, Bild-Posts und Thread-Posts separat. Berechne den Prozentsatz je Typ (% Text / % Bild / % Thread, Summe = 100 %). Trage die Werte in die Haupt-Tabelle ein (3 neue Spalten im Zwischenstand).
4. Identifiziere pro Account die Top-3 Posts der letzten 30 Tage nach Engagement (Likes + Reposts + Replies). Berechne die Engagement-Rate der Top-3 Posts (Likes + Reposts + Replies / Impressionen × 100). Berechne den Durchschnitt der Top-3-Rates und trage diesen als "Spitzen-Engagement-Rate" in die Haupt-Tabelle ein.
5. Schätze das wöchentliche Follower-Wachstum für jeden Account anhand öffentlich sichtbarer Hinweise (Profilbeschreibungen, ältere Posts mit Follower-Meilensteinen, Social-Blade-Daten falls verfügbar). Dokumentiere die Schätzung mit Unsicherheitsangabe (z.B. "+200–400/Woche, Konfidenz: mittel"). Erstelle die fertige Vergleichstabelle mit allen 5 Metriken.

## Verifikation

- Vollständigkeit: Tabelle hat genau 5 Zeilen (Accounts) × 5 Spalten (Follower, Posting-Frequenz, Content-Mix, Spitzen-Engagement-Rate, Wachstum/Woche)
- Content-Mix: Prozent-Angaben summieren sich auf 100 % pro Account
- Handlungsempfehlungen: Genau 3 Empfehlungen, jede verweist auf einen Datenpunkt aus der Tabelle
- Failure-Indikator: Weniger als 3 analysierbare Konkurrenz-Accounts gefunden (z.B. Nische zu klein) → Meldung: "Datenbasis unzureichend — weniger als 3 Konkurrenten analysierbar. Nischendefinition erweitern."
- Akzeptanzkriterium: Tabelle vollständig (alle 25 Felder befüllt), 3 Handlungsempfehlungen mit Datenbezug, eine Positionierungs-Lücke explizit benannt

## Abhängigkeiten

- Input: Ausgabe von elvis-audience-builder (Referenz-Account-Liste als Auswahlpool) sowie Zugang zu X/Twitter-Profil-Daten der 5 Accounts
- Empfohlene Vorgänger-Skills: elvis-audience-builder

## Output

Vergleichstabelle (5 Accounts × 5 Metriken) im Markdown-Format plus 3 nummerierte Handlungsempfehlungen (je max. 2 Sätze) plus eine Positionierungs-Lücken-Beschreibung (max. 3 Sätze). Gesamtlänge: max. 500 Wörter.
