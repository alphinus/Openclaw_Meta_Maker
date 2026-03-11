# Skill

## Name

/elvis-audience-builder

## Beschreibung

Definiert die Zielgruppe eines X/Twitter-Accounts in 5 Dimensionen: demografisch, psychografisch, Content-Präferenzen, Plattform-Verhalten und Referenz-Accounts. Liefert ein vollständiges 5-Dimensionen-Profil plus eine Liste von 10 Accounts, die diese Zielgruppe bereits erfolgreich erreichen.

## Ziele

- 5-Dimensionen-Profil der Zielgruppe vollständig ausgefüllt (Demografie, Psychografie, Content, Verhalten, Referenzen)
- 10 Referenz-Accounts identifiziert, die die Zielgruppe bereits erreichen
- Schmerzpunkte und Wünsche der Zielgruppe in ≥5 konkreten Punkten dokumentiert
- Content-Präferenzen mit Formatangaben und bevorzugten Posting-Zeiten festgehalten
- Profil als wiederverwendbare Grundlage für alle nachgelagerten Growth-Skills

## Strategie

Das Profil wird schichtweise aufgebaut: erst harte Fakten (Demografie), dann weiche Motivationen (Psychografie), dann Verhaltensbeobachtungen (Plattform). Die 10 Referenz-Accounts sind das praktische Anchor-Objekt — sie machen abstrakte Profil-Annahmen konkret prüfbar. Wer diese Accounts erfolgreich beobachtet, kennt die Zielgruppe bereits in Aktion. Keine Empfehlung ohne Referenz-Anker.

## Einschränkungen

- Dimensionen-Beschreibungen: max. 100 Wörter pro Dimension
- Referenz-Account-Liste: genau 10 Accounts, keine Duplikate
- Schmerzpunkte-Liste: min. 3, max. 7 Punkte
- Keine persönlichen Daten realer Personen ohne Operator-Freigabe
- Profilbild-Analysen oder biometrische Auswertungen sind ausgeschlossen

## Ausführungsschritte

1. Erhebe die demografische Dimension der Zielgruppe: Altersrange (z.B. 25–40 Jahre), primäres Berufsfeld (1–3 Kategorien), geografischer Schwerpunkt (Land/Region), Einkommenssegment (falls relevant). Dokumentiere in einer 4-zeiligen Liste mit je einem Schlagwort + kurzer Erläuterung (max. 1 Satz pro Zeile).
2. Erhebe die psychografische Dimension: Kernwerte der Zielgruppe (3 Werte), Primärziele auf der Plattform (2–3 Ziele), Top-3 Schmerzpunkte (konkrete Probleme die Content lösen kann), Aspirationen (was sie in 12 Monaten erreichen wollen). Format: 4 nummerierte Unterabschnitte mit je max. 30 Wörtern.
3. Definiere Content-Präferenzen: bevorzugte Formate auf X (Text-Post / Thread / Bild / Poll — mit %-Schätzung), Top-5 Themen die die Zielgruppe anzieht (je 1 Keyword + 1 Satz Begründung), bevorzugte Posting-Zeitfenster (3 Zeitblöcke mit Wochentag-Angabe, z.B. Mo–Fr 08–10 Uhr).
4. Analysiere das Plattform-Verhalten: typische Like/Repost/Reply-Ratio (welche Interaktion dominiert), Account-Typen denen die Zielgruppe folgt (3 Typen z.B. Experten, Entertainer, Peers), durchschnittliche tägliche Nutzungsdauer (Schätzung in Minuten), Interaktionsbereitschaft (hoch/mittel/niedrig + 1-Satz-Begründung).
5. Identifiziere 10 Referenz-Accounts auf X, die diese Zielgruppe bereits erfolgreich erreichen. Pro Account: @Handle, Follower-Anzahl (Größenordnung), primärer Content-Typ (1–3 Wörter), warum dieser Account die Zielgruppe anspricht (1 Satz). Dokumentiere als Tabelle mit 4 Spalten: @Handle, Follower-Größe, Content-Typ, Relevanz-Begründung.

## Verifikation

- Vollständigkeit: Alle 5 Dimensionen ausgefüllt — Demografie, Psychografie, Content-Präferenzen, Plattform-Verhalten, Referenz-Accounts
- Referenz-Accounts: Genau 10 Accounts in der Tabelle mit allen 4 Spalten befüllt
- Schmerzpunkte: Mindestens 3 konkrete Schmerzpunkte in der psychografischen Dimension
- Failure-Indikator: Weniger als 5 Referenz-Accounts identifizierbar → Skill gibt Meldung aus: "Nische zu klein oder zu neu — weniger als 5 Referenz-Accounts gefunden. Nischendefinition prüfen oder auf benachbarte Nische ausweiten."
- Akzeptanzkriterium: Profil vollständig (5 Dimensionen), 10 Referenz-Accounts mit Tabelle, alle Angaben nischespezifisch (keine generischen Aussagen wie "interessiert sich für Content")

## Abhängigkeiten

- Input: Beschreibung des eigenen Accounts (Nische, bisheriger Content-Fokus, Ziel der Präsenz) als Operator-Eingabe
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill)

## Output

5-Dimensionen-Profil der Zielgruppe im Markdown-Format (5 nummerierte Abschnitte) plus Referenz-Account-Tabelle (10 Zeilen, 4 Spalten). Gesamtlänge: max. 600 Wörter. Dient als Eingabe für elvis-competitor-analysis, elvis-posting-schedule und elvis-engagement-booster.
