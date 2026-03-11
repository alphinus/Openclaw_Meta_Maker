# Skill

## Name

/elvis-follower-analysis

## Beschreibung

Analysiert die 50 aktivsten Follower eines X/Twitter-Accounts (definiert als: höchste Reply/Repost-Frequenz in den letzten 30 Tagen). Pro Follower werden Berufsfeld-Kategorie, primäre Themen (max. 3), Account-Alter in Jahren und Engagement-Typ erfasst. Output: Follower-Segment-Report mit 3 Haupt-Segmenten, je Segment Name, Größe, Top-3-Themen und Content-Empfehlung.

## Ziele

- 50 aktivste Follower nach Reply/Repost-Frequenz identifiziert und in einer Rohdaten-Tabelle dokumentiert
- Pro Follower: Berufsfeld-Kategorie, max. 3 primäre Themen, Account-Alter, Engagement-Typ (Replyer/Reposter/Liker) erfasst
- 3 Follower-Segmente aus den Rohdaten gebildet mit je Name, Größe (Anzahl von 50) und Top-3-Themen
- Content-Empfehlung pro Segment formuliert (je 2 Sätze)
- Segment-Report als strukturierte Grundlage für Kollaborations- und Content-Strategie

## Strategie

Die 50 aktivsten Follower repräsentieren den engagiertesten Kern der Zielgruppe — sie zeigen durch ihr Verhalten (nicht durch Selbstauskunft), welche Inhalte wirklich resonieren. Die Segmentierung nach Berufsfeld und Themen-Präferenzen liefert handlungsrelevante Cluster, nicht statistische Abstraktionen. Jedes Segment erhält eine direkte Content-Empfehlung — so wird die Analyse sofort in Posting-Entscheidungen überführt.

## Einschränkungen

- Genau 50 Follower analysieren — nicht mehr, nicht weniger (Reproduzierbarkeit)
- Aktivitäts-Definition strikt: Reply/Repost-Frequenz in den letzten 30 Tagen (kein Like-Counting)
- Max. 3 primäre Themen pro Follower (Fokus, kein Auffächern)
- Genau 3 Segmente im Output — weniger verliert Detail, mehr verliert Klarheit
- Content-Empfehlung pro Segment: max. 2 Sätze (actionable, kein Essay)

## Ausführungsschritte

1. Identifiziere die 50 aktivsten Follower: Exportiere alle Follower, sortiere nach Anzahl der Replies und Reposts auf eigene Posts in den letzten 30 Tagen (absteigend). Bei Gleichstand: Account mit höherem Account-Alter bevorzugen. Erstelle eine nummerierte Liste mit @Handle und Aktivitäts-Score (Replies × 2 + Reposts × 1 = gewichteter Score). Minimaler Aktivitäts-Score für Aufnahme: ≥1.
2. Erfasse pro Follower 4 Attribute in einer Rohdaten-Tabelle (50 Zeilen, 5 Spalten): @Handle, Berufsfeld-Kategorie (aus 6 Kategorien: Tech, Marketing, Kreativ, Business, Bildung, Sonstiges), primäre Themen (max. 3 Keywords), Account-Alter in Jahren (aufgerundet), Engagement-Typ (Replyer = >50% Replies, Reposter = >50% Reposts, Liker = Mix aus beiden). Dokumentiere die vollständige Tabelle.
3. Bilde 3 Follower-Segmente durch Cluster-Analyse der Rohdaten: Gruppiere nach dominanter Berufsfeld-Kategorie und Themen-Überschneidungen. Regel: Jedes Segment enthält mindestens 10 Follower von 50. Benenne jedes Segment mit einem prägnanten Label (2–4 Wörter, z.B. "Aufstrebende Tech-Gründer"). Dokumentiere Segment-Name, Größe (Anzahl), prozentuale Verteilung, Haupt-Engagement-Typ.
4. Leite für jedes Segment die Top-3-Themen ab: Zähle Themen-Nennungen je Segment und ranke nach Häufigkeit. Top-3 sind die 3 meistgenannten Keywords. Falls Gleichstand bei Platz 3: Thema mit höherem Replyer-Anteil bevorzugen. Dokumentiere pro Segment: Top-3-Themen mit Nennungs-Häufigkeit (z.B. "SaaS-Tools: 12 Nennungen").
5. Formuliere pro Segment eine Content-Empfehlung (je genau 2 Sätze): Satz 1 benennt das primäre Content-Format (Thread/Single-Post/Poll/Story), das dieses Segment bevorzugt (Basis: Engagement-Typ). Satz 2 gibt ein konkretes Themen-Beispiel für den nächsten Post, der dieses Segment anspricht. Erstelle abschließend den Follower-Segment-Report als 3-Block-Übersicht (Segment-Name, Größe, Top-3-Themen, Content-Empfehlung).

## Verifikation

- Rohdaten-Tabelle: Genau 50 Zeilen mit allen 5 Spalten befüllt
- Segmente: Genau 3 Segmente, je mindestens 10 Follower (≥ 10 von 50), Summe = 50
- Top-3-Themen: Pro Segment genau 3 Themen mit Häufigkeits-Angabe
- Failure-Indikator: Weniger als 20 Follower zeigen in 30 Tagen ≥1 Engagement (< 20 aktive Follower aus Top-50-Liste) → Meldung: "Engagement-Basis zu dünn — weniger als 20 aktive Follower identifiziert. Engagement-Booster-Aktionen vor dieser Analyse durchführen."
- Akzeptanzkriterium: 50-Follower-Rohdaten vollständig, 3 Segmente mit Name + Größe + Top-3-Themen + Content-Empfehlung (2 Sätze), Report-Gesamtlänge max. 600 Wörter

## Abhängigkeiten

- Input: Follower-Liste mit Aktivitätsdaten (Reply- und Repost-Counts pro Follower der letzten 30 Tage)
- Empfohlene Vorgänger-Skills: elvis-audience-builder (für Nischen-Kontext und Berufsfeld-Kategorisierung)

## Output

Follower-Segment-Report mit 3 Abschnitten: (1) 50-Follower-Rohdaten-Tabelle (50 Zeilen, 5 Spalten), (2) Segment-Übersicht (3 Blöcke mit Name, Größe, Top-3-Themen, Engagement-Typ), (3) Content-Empfehlungen (3 × 2 Sätze). Gesamtlänge: max. 600 Wörter. Dient als Eingabe für elvis-collab-strategy.
