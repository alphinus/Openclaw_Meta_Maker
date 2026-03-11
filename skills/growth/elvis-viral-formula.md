# Skill

## Name

/elvis-viral-formula

## Beschreibung

Identifiziert Viral-Muster aus den Top-5-Posts der letzten 30 Tage eines X/Twitter-Accounts. Extrahiert strukturelle Merkmale, emotionale Trigger und dokumentiert die 3 häufigsten Viral-Muster als wiederverwendbare Replikations-Vorlagen mit Platzhaltern.

## Ziele

- Top-5-Posts der letzten 30 Tage nach absoluten Impressionen identifiziert
- Strukturelle Merkmale jedes Posts extrahiert (Hook-Typ, Länge, Format)
- Bis zu 5 emotionale Trigger-Kategorien identifiziert und gewichtet
- 3 häufigste Viral-Muster dokumentiert mit Häufigkeitsangabe
- 3 Replikations-Vorlagen erstellt (Template mit [PLATZHALTER]-Syntax)

## Strategie

Der Skill geht induktiv vor: erst Beobachten (was sind die Top-5?), dann Strukturieren (welche Merkmale teilen sie?), dann Abstrahieren (welches Muster steckt dahinter?). Impressionen werden Engagement-Rate vorgezogen, weil Reichweite den Viral-Effekt besser abbildet als relative Engagement-Tiefe. Replikations-Vorlagen müssen so generisch sein, dass sie in neuen Kontexten wiederverwendbar sind — aber so konkret, dass ein neuer Post daraus in 5 Minuten erstellt werden kann.

## Einschränkungen

- Analyse exakt 5 Top-Posts (nach absoluten Impressionen, nicht Engagement-Rate)
- Zeitraum: strikt die letzten 30 Tage — keine älteren Posts
- Max. 5 emotionale Trigger-Kategorien (mehr verwässert das Muster)
- Genau 3 Viral-Muster dokumentieren — nicht mehr
- Replikations-Vorlagen: max. 280 Zeichen pro Template (X-Zeichenlimit)

## Ausführungsschritte

1. Rufe die Top-5-Posts der letzten 30 Tage nach absoluten Impressionen ab. Für jeden Post erfasse: Post-Text (vollständig), Datum/Uhrzeit, Impressionen (absolut), Likes, Reposts, Replies, Format (Text/Bild/Thread/Video/Poll). Dokumentiere die 5 Posts nummeriert mit allen Kennzahlen als Ausgangsdatensatz.
2. Extrahiere strukturelle Merkmale jedes der 5 Posts. Pro Post analysiere: (a) Hook-Typ (Frage, These, Zahl, Story-Opener, Kontrast, Liste), (b) Post-Länge in Zeichen, (c) Format (Text-Only, Bild, Thread-Start, Poll), (d) Vorhandensein von Hashtags (Anzahl), (e) Call-to-Action am Ende (Ja/Nein + Art). Trage Ergebnisse in eine 5-Zeilen × 5-Spalten-Tabelle ein.
3. Identifiziere emotionale Trigger in den 5 Posts. Analysiere jeden Post auf diese Trigger-Kategorien: Neugier, Überraschung/Kontra-Intuition, Aspiration/Neid, Empörung/Kontroverse, Identifikation/Zugehörigkeit. Pro Post: markiere welche Trigger aktiv sind (max. 2 pro Post). Zähle die Häufigkeit jedes Triggers über alle 5 Posts — dokumentiere als sortierte Liste (häufigster zuerst).
4. Identifiziere die 3 häufigsten Viral-Muster aus den Schritten 2 und 3: Ein Muster ist eine Kombination aus Hook-Typ + emotionalem Trigger + Format, die in mindestens 2 der 5 Posts vorkommt. Dokumentiere jedes Muster: Muster-Name (3–5 Wörter), Häufigkeit (X von 5 Posts), beteiligte Posts (Nummer), Durchschnitts-Impressionen der Muster-Posts.
5. Erstelle eine Replikations-Vorlage für jedes der 3 Muster. Format: Post-Template mit [PLATZHALTER] für variable Elemente. Beispiel-Struktur: "[ZAHL] Dinge über [THEMA] die [ZIELGRUPPE] kaum kennt: [LISTE]". Ergänze pro Vorlage: Anwendungs-Hinweis (1 Satz wann dieses Muster passt), Variationsmöglichkeiten (2 Alternativen für den Hook-Teil).

## Verifikation

- Top-5-Datensatz: Alle 5 Posts mit Impressionen, Likes, Reposts, Replies und Format dokumentiert
- Merkmal-Tabelle: 5 Zeilen × 5 Spalten vollständig befüllt (kein leeres Feld)
- Trigger-Analyse: Mindestens 3 verschiedene Trigger-Kategorien in den 5 Posts identifiziert
- Failure-Indikator: Weniger als 2 Posts teilen ein Merkmal-Muster → Meldung: "Kein klares Viral-Muster erkennbar — Posts zu divers. Analyse auf 90 Tage ausweiten oder Benchmark-Accounts hinzuziehen."
- Akzeptanzkriterium: Genau 3 Muster mit Häufigkeit, 3 Replikations-Vorlagen mit [PLATZHALTER]-Syntax, alle Templates ≤280 Zeichen

## Abhängigkeiten

- Input: Zugang zu X/Twitter-Account-Analytics (Post-Impressionen der letzten 30 Tage, sortierbar nach Impressionen)
- Empfohlene Vorgänger-Skills: elvis-growth-audit (liefert den Analytics-Datensatz als Ausgangsbasis)

## Output

Viral-Analyse-Report im Markdown-Format: Ausgangsdatensatz (Top-5-Posts tabellarisch), Merkmal-Tabelle (5 × 5), Trigger-Ranking (Liste), 3 Muster-Beschreibungen mit Häufigkeit, 3 Replikations-Vorlagen mit Platzhaltern und Anwendungs-Hinweisen. Gesamtlänge: max. 600 Wörter.
