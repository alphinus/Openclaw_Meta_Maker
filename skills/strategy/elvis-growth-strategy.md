# Skill

## Name

/elvis-growth-strategy

## Beschreibung

Entwickelt eine Meta-Wachstumsstrategie mit 3 Horizont-Ebenen (30 / 90 / 365 Tage), je 3 SMART-Zielen und einer priorisierten Kanal-Aufteilung mit Ressourcen-Prozenten. Unterscheidet sich von `/elvis-growth-audit` (Ist-Analyse: Was ist passiert?) durch den Fokus auf Soll-Definition: Wohin soll die Wachstumskurve gehen, auf welchem Weg, mit welchen Ressourcen?

## Ziele

- 3 Wachstums-Horizonte (30 / 90 / 365 Tage) mit je 3 SMART-Zielen im Format: Ist-Wert → Soll-Wert, Metrik, Datum, Messmethode
- Kanal-Portfolio: 1 Haupt-Kanal (≥50% Ressourcen) + 2 Neben-Kanäle mit expliziter Ressourcen-Aufteilung in %
- Milestone-Checkpoints alle 30 Tage mit je 1 Go/No-Go-Kriterium
- Strategische Leitlinie: 1 übergeordnetes Wachstumsprinzip das alle Entscheidungen filtert

## Strategie

Die Strategie arbeitet von außen nach innen: Zuerst die 365-Tage-Vision definieren, dann die 90-Tage-Meilensteine ableiten, dann die ersten 30 Tage konkretisieren. Dieser Top-down-Ansatz verhindert taktisches Umherirren ohne strategischen Anker. Die Kanal-Konzentration (ein dominanter Haupt-Kanal) erzeugt Tiefenwirkung statt Oberflächenpräsenz auf vielen Plattformen gleichzeitig.

## Einschränkungen

- Max. 3 SMART-Ziele pro Horizont (9 Ziele gesamt) — mehr führt zu Fokus-Verlust
- Ressourcen-Aufteilung muss in % angegeben werden und auf 100% aufgehen
- Kein Horizont ohne mindestens 1 messbares Ziel mit konkretem Zahlenwert
- Milestone-Checkpoints sind Go/No-Go-Entscheidungspunkte — kein "weiter wie bisher" ohne Datenbasis
- Keine Strategie-Definitionen ohne Grenzziehung: Was gehört explizit NICHT zur Strategie?

## Ausführungsschritte

1. Kläre den strategischen Ausgangspunkt in 3 Minuten: Aktuelle Follower-/Subscriber-Zahl (Haupt-Plattform), aktuelle monatliche Reichweite (Impressionen oder Unique Visitors), aktueller Umsatz/Leads pro Monat, stärkster Kanal (wo kommt der Großteil des Traffics her?). Falls Daten fehlen, /elvis-growth-audit zuerst ausführen.
2. Definiere die 365-Tage-Vision: 3 SMART-Ziele für 12 Monate, jedes im Format "Von [Ist-Wert] auf [Soll-Wert] in [Metrik] bis [konkretes Monat/Jahr], gemessen via [Messmethode]." Mindestens 1 Ziel auf Reichweite, 1 auf Monetarisierung, 1 auf Community/Engagement.
3. Leite aus der 365-Tage-Vision die 90-Tage-Meilensteine ab: 3 SMART-Ziele die, wenn erreicht, die 365-Tage-Ziele auf Kurs halten. Jedes 90-Tage-Ziel soll ≥25% des Jahres-Ziels abdecken. Format identisch mit Schritt 2.
4. Konkretisiere die 30-Tage-Startziele: 3 SMART-Ziele die in den ersten 30 Tagen erreichbar sind. Fokus auf Momentum-Aufbau und erste Datengewinnung. Jedes Ziel muss innerhalb von 30 Tagen messbar sein.
5. Definiere das Kanal-Portfolio: Haupt-Kanal mit 50–60% Ressourcen-Anteil, Neben-Kanal 1 mit 20–25%, Neben-Kanal 2 mit 15–20%, Rest (10%) für Experimente. Begründe jede Kanal-Wahl mit 1 Satz (warum dieser Kanal für diese Zielgruppe). Erstelle eine Tabelle: Kanal | Ressourcen-% | Primäres Ziel | Haupt-Format.
6. Erstelle 4 Milestone-Checkpoints (nach Tag 30 / 60 / 90 / 180): Für jeden Checkpoint 1 Go-Metrik (Ziel erreicht → weitermachen), 1 No-Go-Metrik (Ziel verfehlt → Strategie-Review), und 1 konkrete Anpassungsmaßnahme für den No-Go-Fall.
7. Formuliere die strategische Leitlinie als 1–2 Sätze: Das übergeordnete Wachstumsprinzip das bei Ressourcen-Konflikten priorisiert wird (z.B. "Tiefe vor Breite — wir gehen zuerst auf einem Kanal in die Tiefe, bevor wir expandieren"). Schreibe den vollständigen Strategie-Plan im Markdown-Format: Vision / 3-Horizonte-Tabelle / Kanal-Portfolio / Milestone-Checkpoints / Leitlinie. Max. 1.000 Wörter.

## Verifikation

- Ziele-Qualität: Alle 9 SMART-Ziele (3 × 3 Horizonte) enthalten Ist-Wert, Soll-Wert, Metrik, Datum und Messmethode
- Kanal-Arithmetik: Alle Ressourcen-% addieren sich auf 100%
- Milestone-Vollständigkeit: Alle 4 Checkpoints haben je 1 Go- und 1 No-Go-Metrik
- Failure-Indikator: Wenn kein einziger Ist-Wert bekannt ist (alle 5 Basis-Metriken unbekannt) → "Strategiebasis fehlt: Ohne Ist-Daten ist diese Strategie Spekulation. Empfehle: /elvis-growth-audit zuerst ausführen."
- Akzeptanzkriterium: 9 SMART-Ziele vollständig ausgefüllt, Kanal-Portfolio auf 100% normiert, 4 Checkpoints mit Go/No-Go-Metriken

## Abhängigkeiten

- Input: Aktuelle Wachstumsdaten (mind. Hauptkanal-Metriken) und übergeordnete Wachstums-Ambition (1–3 Sätze)
- Empfohlene Vorgänger-Skills: /elvis-growth-audit (liefert Ist-Metriken), /elvis-market-scan (liefert Marktkontext)

## Output

Markdown-Dokument (max. 1.000 Wörter) mit 5 Abschnitten: Strategische Leitlinie, 3-Horizonte-Tabelle (30/90/365 Tage × 3 SMART-Ziele), Kanal-Portfolio-Tabelle (4 Kanäle mit Ressourcen-%), Milestone-Checkpoints (4 × Go/No-Go), Grenzen der Strategie (Was ist explizit ausgeschlossen).
