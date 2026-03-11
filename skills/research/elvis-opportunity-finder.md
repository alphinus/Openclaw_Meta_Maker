# Skill

## Name

/elvis-opportunity-finder

## Beschreibung

Analysiert einen Markt oder eine Nische auf ungenutzte Chancen aus 3 Quellentypen: Konkurrenz-Lücken, unerfüllte Zielgruppen-Wünsche und unbesetzte Nischen-Segmente. Bewertet identifizierte Gaps nach einem 3-Kriterien-Scoring und liefert eine priorisierte Liste von 5 validierten Marktlücken mit Handlungsempfehlung.

## Ziele

- 5 identifizierte Gaps — mindestens je 1 aus den 3 Quellentypen (Konkurrenz-Lücken, Zielgruppen-Wünsche, unbesetzte Nischen)
- Gap-Scoring für alle 5 Lücken: 3 Kriterien (Nachfrage, Wettbewerb, Erreichbarkeit) je 1–5 Punkte
- Priorisierte Rangliste der 5 Gaps nach Gesamtscore (max. 15 Punkte pro Gap)
- Konkrete Handlungsempfehlung für die Top-2 Gaps (je 2–3 Sätze)
- Validierungshinweis: welche 1–2 weiteren Schritte würden jeden Top-Gap weiter absichern

## Strategie

Die 3-Quellentypen-Methode verhindert blinde Flecken: Konkurrenz-Lücken zeigen was bestehende Player vergessen, Zielgruppen-Wünsche zeigen was Nutzer explizit fordern, unbesetzte Nischen zeigen strukturell freie Segmente. Das 3-Kriterien-Scoring (Nachfrage, Wettbewerb, Erreichbarkeit) bewertet Gaps nach realistischer Umsetzbarkeit — ein Gap mit hoher Nachfrage aber zu starkem Wettbewerb ist keine echte Lücke. Mindestens 5 validierte Gaps sichern eine ausreichende Auswahl für strategische Entscheidungen.

## Einschränkungen

- Genau 5 validierte Gaps im finalen Output — nicht weniger (dann Suche ausweiten), nicht mehr (dann priorisieren)
- Mindestens 1 Gap pro Quellentyp — rein konkurrenzbasierte Analyse ist unvollständig
- Scoring-Kriterien müssen mit Begründung (1–2 Sätze) dokumentiert sein — nackte Zahlen ohne Erklärung sind ungültig
- Keine Gaps ohne Quellenangabe (welches Signal aus welchem Quellentyp hat diesen Gap aufgezeigt?)
- Kein Gap darf als "validiert" gelten wenn er nur auf einer einzigen Beobachtung basiert

## Ausführungsschritte

1. Erhebe Konkurrenz-Lücken aus den vorhandenen Wettbewerber-Daten: Analysiere die Top-5 Konkurrenz-Accounts (aus elvis-competitor-analysis Output oder direkter Beobachtung) auf **fehlende Themen** (Bereiche die sie nicht abdecken), **Qualitätslücken** (Themen die sie schlecht oder oberflächlich behandeln) und **Format-Lücken** (Formate die ihre Zielgruppe wünscht, die sie aber nicht liefern). Dokumentiere jeden Lücken-Befund im Format: "Lücke: [Beschreibung] — Quelle: [Account oder Beobachtung] — Typ: Thema/Qualität/Format".
2. Erhebe Zielgruppen-Wünsche aus 3 Quellen: (a) Kommentare und Antworten auf Konkurrenz-Posts (welche Fragen tauchen ≥ 3 Mal auf?), (b) Community-Foren oder Reddit-Threads zur Nische (Top-5 meistgefragten Themen), (c) Direkte Feedback-Signale aus eigenen Posts falls vorhanden. Dokumentiere je Quelle mindestens 3 unerfüllte Wünsche im Format: "Wunsch: [Beschreibung] — Beleg: [Quelle, Datum, Häufigkeit]".
3. Erhebe unbesetzte Nischen-Segmente durch strukturierte Marktkarte: Zeichne eine 2×2-Matrix (Achsen: Zielgruppen-Spezifität niedrig/hoch × Themen-Tiefe oberflächlich/tief) und ordne bekannte Angebote darin ein. Identifiziere mindestens 2 leere Felder oder dünn besetzte Quadranten als potenzielle Nischen-Segmente. Dokumentiere jedes Segment in 1 Satz: "Segment: [Beschreibung] — Marktlage: [wie viele Player, welche Größe]".
4. Wähle aus allen gesammelten Signalen die 5 vielversprechendsten Gaps aus (mindestens je 1 aus den 3 Quellentypen). Score jeden Gap nach 3 Kriterien, je 1–5 Punkte: **Nachfrage** (1 = keine Evidenz, 5 = vielfach belegt und messbar), **Wettbewerb** (1 = viele starke Player, 5 = kaum oder schwache Mitbewerber), **Erreichbarkeit** (1 = erfordert enorme Ressourcen, 5 = mit vorhandenen Mitteln umsetzbar in ≤ 4 Wochen). Dokumentiere Score + 1-Satz-Begründung pro Kriterium.
5. Erstelle die Gap-Scoring-Tabelle (5 Zeilen × 4 Spalten: Gap-Name, Nachfrage, Wettbewerb, Erreichbarkeit, Gesamtscore). Sortiere die 5 Gaps absteigend nach Gesamtscore. Schreibe für die Top-2 Gaps eine Handlungsempfehlung (je 2–3 Sätze: was konkret tun, in welchem Zeitraum, welches erste messbare Signal zeigt Erfolg). Füge pro Gap einen Validierungshinweis hinzu: 1–2 Schritte die diesen Gap weiter absichern würden (z.B. "10 Nutzer befragen ob [Wunsch] bestätigt wird").

## Verifikation

- Quellentyp-Abdeckung: Mindestens 1 validierter Gap pro Quellentyp (Konkurrenz-Lücken, Zielgruppen-Wünsche, unbesetzte Nischen)
- Scoring-Vollständigkeit: Alle 5 Gaps mit allen 3 Kriterien bewertet, je Kriterium eine Begründung (1–2 Sätze)
- Gesamtscores: korrekt summiert (max. 15 pro Gap), Tabelle vollständig (5 × 4 Felder)
- Handlungsempfehlungen: Top-2 Gaps haben je eine Empfehlung mit Zeitangabe und Erfolgs-Signal
- Failure-Indikator: Weniger als 3 validierte Gaps identifizierbar (alle Quellentypen durchsucht aber nicht genug Signal gefunden) → Skill bricht ab mit "Gap-Analyse unzureichend: Weniger als 3 validierte Gaps (< 3) — Nischendefinition erweitern oder Analysezeitraum auf 6 Monate ausweiten"
- Akzeptanzkriterium: 5 Gaps mit vollständigem 3-Kriterien-Scoring, mindestens je 1 Gap aus 3 Quellentypen, Top-2-Empfehlungen mit Zeitangabe

## Abhängigkeiten

- Input: Beschreibung der eigenen Nische (1–3 Sätze) sowie optional: Output von elvis-competitor-analysis (Konkurrenz-Daten) und/oder elvis-market-scan (Marktüberblick)
- Empfohlene Vorgänger-Skills: /elvis-market-scan (Marktüberblick), /elvis-competitor-analysis (Konkurrenz-Daten als Rohstoff für Quellentyp 1)

## Output

Gap-Analyse-Report mit 4 Abschnitten: (1) Rohdaten aus 3 Quellentypen (je min. 3 Signale pro Typ), (2) Gap-Scoring-Tabelle (5 × 4 Felder mit Begründungen), (3) Handlungsempfehlungen für Top-2 Gaps (je 2–3 Sätze + Validierungshinweis), (4) Ausgeschlossene Gaps (1–3 Kandidaten die nicht die Qualitätsschwelle erreicht haben, mit Begründung). Gesamtlänge: max. 1.000 Wörter.
