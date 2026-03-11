# Skill

## Name

/elvis-trend-analyzer

## Beschreibung

Analysiert 3 relevante Trends einer Nische tiefgehend entlang 5 Analyse-Dimensionen: Ursache, Reifegrad, Plattformverteilung, Zielgruppen-Relevanz und 6-Monate-Prognose. Im Unterschied zu oberflächlichen X-only-Trend-Scannern kombiniert dieser Skill Multi-Plattform-Daten, Kausalanalyse und belastbare Prognosen auf Basis mindestens 2 unabhängiger Datenquellen pro Trend.

## Ziele

- 3 analysierte Trends mit je 5 vollständig ausgefüllten Analyse-Dimensionen
- Mindestens 2 belegte Datenquellen pro Trend (plattformübergreifend) — oder Failure-Abbruch
- Kausal-Erklärung pro Trend (warum entsteht dieser Trend jetzt?) mit Beleg
- Reifegrad-Einstufung (Emerging / Growing / Peak / Declining) mit quantitativem Indikator
- 6-Monate-Prognose pro Trend: 3 mögliche Szenarien (Best Case, Base Case, Decline Case)

## Strategie

Wo /elvis-x-trend-scanner einen Trend auf X identifiziert und benennt, analysiert dieser Skill das Warum, das Wo und das Wohin. Die 5-Dimensionen-Struktur erzwingt kausalische Tiefe (Ursache), zeitliche Verortung (Reifegrad), räumliche Breite (Plattformverteilung), Zielgruppen-Relevanz (wer ist wirklich betroffen?) und prädiktive Nutzbarkeit (6-Monate-Prognose). Mindestens 2 unabhängige Quellen pro Trend verhindern Einzel-Signal-Fehlinterpretation — ein Trend der nur auf einer Plattform oder einer Quelle sichtbar ist, gilt als unbestätigt.

## Einschränkungen

- Genau 3 Trends pro Durchlauf — nicht weniger (dann Suchwinkel erweitern), nicht mehr (dann priorisieren)
- Mindestens 2 verschiedene Plattformen oder Quellen-Typen pro Trend (nicht nur X-Daten)
- Prognosen müssen als Szenarien formuliert sein — keine einzige deterministische Vorhersage ohne Konfidenzangabe
- Kein Trend ohne Kausal-Erklärung — "weil er gerade viel diskutiert wird" ist keine Ursache
- Unterscheidung von /elvis-x-trend-scanner muss explizit dokumentiert sein (Scope-Abgrenzung im Output)

## Ausführungsschritte

1. Identifiziere 3 Kandidaten-Trends durch Signale aus mindestens 3 verschiedenen Quellen-Typen: (a) Plattform-Daten (X, TikTok, YouTube, Instagram — je nach Nische), (b) Suchanfragen-Tools (Google Trends, Exploding Topics oder vergleichbar), (c) Fach-Communities und Publikationen (Branchenblogs, Newsletter, Reddit-Subreddits). Dokumentiere pro Trend-Kandidat die identifizierenden Signale (Quelle, Datum, Indikator-Typ) als Auswahlbegründung in 2–3 Sätzen.
2. Analysiere **Dimension 1: Ursache** für jeden der 3 Trends — beantworte: Was hat diesen Trend ausgelöst oder beschleunigt? Nenne den primären Auslöser (technologisch / gesellschaftlich / regulatorisch / saisonal / viral-kumulativ) und mindestens 1 belegenden Datenpunkt (Artikel, Studie, Meilenstein-Ereignis mit Datum). Format pro Trend: "Ursache: [1–2 Sätze Erklärung]. Beleg: [Quelle + Datum]."
3. Analysiere **Dimension 2: Reifegrad** — stufe jeden Trend ein nach dem 4-Phasen-Modell: **Emerging** (< 6 Monate alt, exponentielles Wachstum, < 20 % Marktdurchdringung), **Growing** (6–18 Monate, stabile Wachstumsrate, 20–60 % Durchdringung), **Peak** (> 18 Monate, verlangsamtes Wachstum, > 60 % Durchdringung), **Declining** (Rückgang messbarer Metriken). Füge einen quantitativen Indikator hinzu (z.B. "Suchanfragen +340 % in 6 Monaten" oder "Posting-Frequenz auf X stagniert seit 8 Wochen").
4. Analysiere **Dimension 3: Plattformverteilung** und **Dimension 4: Zielgruppen-Relevanz** für jeden Trend: Für Plattformverteilung — auf welchen 2–4 Plattformen ist der Trend aktiv, mit welcher relativen Stärke (stark / mittel / schwach pro Plattform)? Für Zielgruppen-Relevanz — welche spezifische Zielgruppen-Segmente sind am stärksten betroffen oder interessiert, und welchen direkten Bezug hat der Trend zur eigenen Nische (hoch / mittel / gering + 1-Satz-Begründung)?
5. Analysiere **Dimension 5: 6-Monate-Prognose** für jeden Trend: Formuliere 3 Szenarien — **Best Case** (Trend verstärkt sich weiter, welche Bedingungen müssen eintreten), **Base Case** (Trend entwickelt sich moderat weiter oder stabilisiert sich, wahrscheinlichstes Szenario), **Decline Case** (Trend verliert an Bedeutung, welche Faktoren würden das auslösen). Je Szenario: 1–2 Sätze + 1 messbarer Indikator der das Eintreten dieses Szenarios anzeigen würde.
6. Erstelle den finalen Trend-Report als 3-Block-Struktur (je 1 Block pro Trend): Trend-Name, Kurzdiagnose (2 Sätze), 5-Dimensionen-Tabelle (Dimension | Befund | Quelle/Beleg), 6-Monate-Prognose (3 Szenarien), Handlungs-Empfehlung für die eigene Nische (1–2 Sätze: was jetzt konkret tun?). Füge am Ende eine 3-Zeilen-Abgrenzungsnotiz zu /elvis-x-trend-scanner an: was dieser Skill mehr liefert und wann /elvis-x-trend-scanner der richtige Einstieg wäre.

## Verifikation

- Dimensionen-Vollständigkeit: Alle 3 Trends haben alle 5 Dimensionen vollständig ausgefüllt (15 Dimensionen-Felder gesamt)
- Quellen-Mindestanforderung: Jeder Trend hat mindestens 2 verschiedene Datenquellen (Plattform-Typ oder Publikations-Typ müssen sich unterscheiden)
- Prognose-Format: Alle 3 × 3 = 9 Szenarien vorhanden, je mit messbarem Indikator
- Kausalität: Keine Ursachen-Analyse lautet nur "hohe Nachfrage" oder "viele Posts" — muss strukturelle Erklärung enthalten
- Failure-Indikator: Weniger als 2 belegte, unabhängige Datenquellen für mindestens einen Trend gefunden → Skill bricht ab mit "Datenbasis unzureichend: Trend [Name] hat weniger als 2 unabhängige Datenquellen — Trend-Analyse nicht belastbar"
- Akzeptanzkriterium: 3 Trends × 5 Dimensionen vollständig, 9 Szenarien formuliert, ≥ 2 Quellen pro Trend, Abgrenzungsnotiz zu /elvis-x-trend-scanner vorhanden

## Abhängigkeiten

- Input: Nische oder Themenbereich (1–2 Sätze) sowie optional: Output von /elvis-x-trend-scanner (Trend-Kandidaten auf X als Startpunkt) und bevorzugter Analyse-Zeitraum (Standard: letzte 6 Monate)
- Empfohlene Vorgänger-Skills: /elvis-market-scan (Marktkontext), /elvis-x-trend-scanner (X-spezifische Trend-Signale als Ausgangsmaterial, nicht obligatorisch)

## Output

Trend-Report mit 3 Trend-Blöcken (je Trend: Name, Kurzdiagnose, 5-Dimensionen-Tabelle, 6-Monate-Prognose mit 3 Szenarien, Handlungsempfehlung) plus 3-Zeilen-Abgrenzungsnotiz zu /elvis-x-trend-scanner. Gesamtlänge: max. 1.500 Wörter.
