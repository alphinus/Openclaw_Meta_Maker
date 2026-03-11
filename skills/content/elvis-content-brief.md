# Skill

## Name

/elvis-content-brief

## Beschreibung

Erstellt ein vollständiges Content-Brief für einen Post oder Thread mit 7 Briefing-Sektionen: Ziel, Zielgruppe, Kernbotschaft, Format, Tonfall, CTA, Tabu-Liste. Output ist ein ausgefülltes Brief-Template (7 Felder, max. 300 Wörter). Nutzt Zielgruppe aus elvis-audience-builder und Ideen aus elvis-content-ideas.

## Ziele

- Ausgefülltes Brief-Template mit allen 7 Sektionen: Ziel, Zielgruppe, Kernbotschaft, Format, Tonfall, CTA, Tabu-Liste
- Exakt 1 Ziel ausgewählt (Awareness, Engagement oder Conversion)
- Zielgruppe: 1 Segment aus elvis-audience-builder, max. 2 Sätze
- Kernbotschaft: 1 Satz, die zentrale Aussage des Content-Stücks
- Tabu-Liste: max. 3 Punkte — was explizit nicht gesagt werden soll

## Strategie

Ein Content-Brief verhindert das häufigste Problem beim Content-Erstellen: zu viele Ziele, zu breite Zielgruppe, unklar was der Content leisten soll. Das 7-Felder-Template erzwingt Entscheidungen vor dem Schreiben — das spart Überarbeitungsschleifen. Die Tabu-Liste ist besonders wertvoll: sie definiert Grenzen explizit statt implizit. Die Einzel-Ziel-Regel ("nur 1 auswählen") verhindert "alles auf einmal"-Content der nichts richtig macht.

## Einschränkungen

- Sektion 1 Ziel: exakt 1 aus 3 Optionen — Awareness (Reichweite), Engagement (Interaktion) oder Conversion (Handlung)
- Sektion 2 Zielgruppe: 1 Segment aus elvis-audience-builder, max. 2 Sätze
- Sektion 3 Kernbotschaft: exakt 1 Satz
- Sektion 4 Format: Single-Post, Thread oder Poll — mit Begründung (1 Satz)
- Sektion 5 Tonfall: Sachlich, Provokativ oder Persönlich — mit Begründung (1 Satz)
- Sektion 6 CTA: 1 CTA-Typ aus elvis-cta-writer (Follow, Repost, Kommentar, Link-Klick oder DM)
- Sektion 7 Tabu-Liste: max. 3 Punkte, je 1 Satz
- Gesamt-Output: max. 300 Wörter
- Kein automatisches Posten — Brief ist zur manuellen Freigabe bestimmt

## Ausführungsschritte

1. Kläre den Kontext: (a) Für welches Content-Stück wird das Brief erstellt? (Thema/Idee aus elvis-content-ideas oder freie Eingabe), (b) Was ist der Kanal (X/Twitter Post, Thread, Poll)? Dokumentiere Thema und Kanal als "Brief-Kontext" vor dem Template.
2. Fülle Sektionen 1–3 aus: (1) Wähle exakt 1 Ziel (Awareness/Engagement/Conversion) und begründe die Wahl in 1 Satz. (2) Bestimme die Zielgruppe: 1 Segment aus dem elvis-audience-builder 5-Dimensionen-Profil, max. 2 Sätze (Wer ist diese Person? Was braucht sie?). (3) Formuliere die Kernbotschaft: 1 Satz, die zentrale Aussage die der Leser nach dem Post kennen soll.
3. Fülle Sektionen 4–5 aus: (4) Wähle Format (Single-Post wenn 1 Gedanke, Thread wenn ≥3 Entwicklungsschritte, Poll wenn Meinungsabfrage) + 1 Satz Begründung. (5) Wähle Tonfall (Sachlich wenn Expertise-Ziel, Provokativ wenn Sichtbarkeits-Ziel, Persönlich wenn Vertrauens-Ziel) + 1 Satz Begründung.
4. Fülle Sektionen 6–7 aus: (6) Wähle CTA-Typ aus elvis-cta-writer (Follow, Repost, Kommentar, Link-Klick oder DM) — passend zum gewählten Ziel aus Sektion 1. (7) Erstelle Tabu-Liste: max. 3 Punkte — was explizit in diesem Content-Stück NICHT gesagt werden soll (z.B. kein Konkurrenz-Vergleich, kein Preis-Nennung, keine politische Aussage).
5. Prüfe Brief auf Konsistenz: Passt der CTA zum Ziel? (Awareness → Follow/Repost; Engagement → Kommentar; Conversion → Link-Klick/DM). Passt der Tonfall zur Zielgruppe? Überschreitet die Kernbotschaft 1 Satz? Dokumentiere das finale Brief als Template mit 7 nummerierten Feldern.

## Verifikation

- Brief-Kontext vorhanden (Thema + Kanal)
- Alle 7 Sektionen ausgefüllt: Ziel, Zielgruppe, Kernbotschaft, Format, Tonfall, CTA, Tabu-Liste
- Sektion 1: genau 1 Ziel ausgewählt (Awareness/Engagement/Conversion)
- Sektion 2: Zielgruppe ≤ 2 Sätze, Bezug zu elvis-audience-builder
- Sektion 3: Kernbotschaft = 1 Satz
- Sektion 7: Tabu-Liste ≤ 3 Punkte
- Gesamt-Output ≤ 300 Wörter
- Failure-Indikator: Mehr als 1 Ziel in Sektion 1 → Meldung "Zu viele Ziele — auf 1 reduzieren: Primäres Ziel [X] behalten, [Y] und [Z] entfernen"
- Akzeptanzkriterium: 7 Sektionen vollständig, exakt 1 Ziel, Kernbotschaft als 1 Satz, Tabu-Liste ≤ 3 Punkte

## Abhängigkeiten

- Input: Content-Thema oder -Idee (aus elvis-content-ideas oder freie Eingabe)
- Empfohlene Vorgänger-Skills: elvis-audience-builder (Zielgruppen-Segment für Sektion 2), elvis-content-ideas (Ideen-Input für Brief-Kontext), elvis-cta-writer (CTA-Typ für Sektion 6)

## Output

Brief-Kontext (Thema + Kanal) + ausgefülltes Brief-Template mit 7 Sektionen (Ziel / Zielgruppe / Kernbotschaft / Format / Tonfall / CTA / Tabu-Liste). Gesamtlänge: max. 300 Wörter, Markdown-Format.
