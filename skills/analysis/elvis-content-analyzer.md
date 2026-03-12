# Skill

## Name

/elvis-content-analyzer

## Beschreibung

Analysiert Content-Performance kanalübergreifend als monatliches Mess-System: Top-10 Posts über alle aktiven Plattformen hinweg, bewertet nach 5 Metriken je Post, vergleicht Content-Typen und leitet Format-Empfehlungen ab. Im Gegensatz zu `elvis-x-analytics` (ausschließlich X/Twitter-fokussiert) betrachtet dieser Skill alle Kanäle gleichzeitig — und wird monatlich wiederholt um Content-Strategie-Entscheidungen fortlaufend auf Datenbasis zu stellen.

## Ziele

- Identifizierte Top-10 Posts nach Engagement-Rate über alle Kanäle hinweg (letzter 30-Tage-Zeitraum)
- 5 Metriken pro Post erfasst und ausgewertet: Reichweite, Engagement-Rate, Klick-Rate, Saves/Bookmarks, Kommentar-Qualität
- Content-Typ-Vergleich: 4 Formate verglichen (Text, Bild, Video, Thread/Karussell) nach Durchschnitts-Performance
- 3 kanal-übergreifende Format-Empfehlungen basierend auf Performance-Mustern
- Identifizierte kanalspezifische Stärken: welcher Content-Typ pro Plattform am besten performt

## Strategie

Die Multi-Channel-Analyse priorisiert Engagement-Rate über absolute Zahlen — ein Post mit 500 Reichweite und 8 % Engagement schlägt einen mit 5.000 Reichweite und 0,5 % Engagement. Der Content-Typ-Vergleich ist die zentrale Erkenntnisquelle: Er zeigt ob ein Format konsequent besser performt und macht Format-Entscheidungen datenbasiert statt intuitiv. Die kanalspezifischen Stärken-Analyse verhindert den Fehler denselben Content unverändert auf alle Plattformen zu posten.

## Einschränkungen

- Max. 4 Plattformen gleichzeitig analysieren (mehr macht die Auswertung unübersichtlich)
- Top-10 Posts über alle Kanäle kombiniert — nicht Top-10 pro Kanal (Fokus auf absolute Top-Performer)
- Nur Metriken auswerten die tatsächlich in der Plattform-Analytics verfügbar sind (keine Schätzungen)
- Zeitraum fix auf 30 Tage — keine kürzeren oder längeren Perioden (Vergleichbarkeit zwischen Reviews)
- Keine Aussagen über Paid-Content-Performance machen wenn organischer und bezahlter Content gemischt sind

## Ausführungsschritte

1. Ermittle alle aktiven Plattformen des Operators (max. 4). Für jede Plattform: rufe die letzten 30 Tage Analytics ab und extrahiere alle Posts mit mehr als 100 Impressionen. Sammle für jeden Post: Plattform, Post-Datum, Post-Typ (Text / Bild / Video / Thread), Impressionen/Reichweite, Likes + Kommentare + Shares, Klicks/Link-Klicks, Saves/Bookmarks (falls verfügbar).
2. Berechne die Engagement-Rate für jeden Post: (Likes + Kommentare + Shares) / Impressionen × 100. Erstelle eine kombinierte Rangliste über alle Plattformen: sortiere alle Posts absteigend nach Engagement-Rate. Markiere die Top-10 in einer Tabelle mit 7 Spalten: Rang, Plattform, Datum, Post-Typ, Engagement-Rate, Reichweite, 50-Zeichen-Vorschau.
3. Erweitere die Top-10-Tabelle um die restlichen 5 Metriken (Klick-Rate, Saves, Kommentar-Qualität). Klick-Rate = Klicks / Impressionen × 100. Kommentar-Qualität = kategorisiere als "Positiv (Lob / Zustimmung)", "Frage (zeigt Interesse)", "Diskussion (tiefe Auseinandersetzung)" oder "Neutral/Negativ". Trage alle Werte in die Tabelle ein.
4. Berechne den Content-Typ-Vergleich über alle Posts (nicht nur Top-10): Für jeden der 4 Typen (Text, Bild, Video, Thread) berechne Durchschnitts-Engagement-Rate, Durchschnitts-Reichweite und Anzahl Posts im Zeitraum. Erstelle eine Vergleichstabelle mit 5 Spalten: Typ, Anzahl Posts, Ø Reichweite, Ø Engagement-Rate, Rang.
5. Identifiziere kanalspezifische Stärken: Welcher Content-Typ hat auf jeder Plattform die höchste Engagement-Rate? Erstelle eine Plattform-Stärken-Matrix mit 2 Spalten: Plattform, Bester Content-Typ (mit Ø Engagement-Rate). Füge einen Satz Begründung pro Plattform hinzu.
6. Leite 3 kanal-übergreifende Format-Empfehlungen ab. Kriterium: Empfehlungen basieren auf Mustern die in mindestens 6 der Top-10 Posts beobachtbar sind. Jede Empfehlung: Beobachtung (was wurde gemessen?), Empfehlung (was soll als nächstes gemacht werden?), erwartete Wirkung (welche Verbesserung ist realistisch?).
7. Schreibe eine Zusammenfassung (max. 200 Wörter): Was ist der #1 Befund aus der Multi-Channel-Analyse? Welcher Kanal performt am besten? Welcher Content-Typ sollte sofort häufiger eingesetzt werden? Was sollte sofort reduziert oder gestoppt werden?

## Verifikation

- Top-10 vollständig: Alle 10 Posts mit allen 5 Metriken ausgefüllt (keine leeren Felder)
- Content-Typ-Vergleich: Alle 4 Typen bewertet (auch wenn einer 0 Posts hat → "Nicht genutzt")
- Muster-Nachweis: Jede Format-Empfehlung benennt die Anzahl Posts auf denen sie basiert (min. 6/10)
- Multi-Channel-Check: Wenn nur 1 Plattform analysiert wurde, Hinweis ausgeben dass es sich um Single-Channel-Analyse handelt
- Failure-Indikator: Wenn weniger als 10 Posts mit vollständigen Metriken (alle 5) in den letzten 30 Tagen verfügbar sind → Skill gibt aus: "Zu wenige Posts mit vollständigen Metriken (< 10) — Multi-Channel-Analyse nicht aussagekräftig. Entweder Zeitraum auf 60 Tage ausdehnen oder fehlende Metriken manuell ergänzen."
- Akzeptanzkriterium: Top-10-Tabelle vollständig, Content-Typ-Vergleich erstellt, 3 begründete Format-Empfehlungen, Plattform-Stärken-Matrix

## Abhängigkeiten

- Input: Analytics-Zugang zu allen aktiven Plattformen (min. 1, max. 4) für die letzten 30 Tage; min. 10 Posts mit vollständigen Metriken
- Empfohlene Vorgänger-Skills: /elvis-performance-tracker (liefert Baseline-Metriken), /elvis-x-analytics (wenn X/Twitter-fokussierte Tiefen-Analyse gewünscht ist)

## Output

Markdown-Dokument mit 5 Abschnitten: (1) Top-10-Posts-Tabelle (7+5 Spalten, kanalübergreifend), (2) Content-Typ-Vergleichstabelle (4 Typen × 4 Kennzahlen), (3) Plattform-Stärken-Matrix, (4) 3 kanal-übergreifende Format-Empfehlungen mit Evidenz-Nachweis, (5) Zusammenfassung mit sofortigen Handlungsempfehlungen (max. 200 Wörter). Einsatzbereit als monatliches Content-Review-Dokument.
