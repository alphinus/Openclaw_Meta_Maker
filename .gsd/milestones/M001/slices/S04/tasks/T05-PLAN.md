---
estimated_steps: 7
estimated_files: 7
---

# T05: Content Skills 8–14 erstellen

**Slice:** S04 — Growth + Content Skills (~30 Skills)
**Milestone:** M001

## Description

Die zweite Hälfte der Content Skills — von Opinion-Post bis Content-Brief. Diese 7 Skills schließen die Content-Kette ab und enthalten die wichtigsten cross-kategorie Abhängigkeiten:
- `elvis-content-ideas` referenziert `elvis-x-trend-scanner` (aus T02) — Trends als Content-Input
- `elvis-content-brief` referenziert `elvis-audience-builder` (aus T02) — Zielgruppe als Briefing

Nach T05 sind alle 28 neuen Skills erstellt — `bash scripts/verify-s04.sh` sollte mit Exit-Code 0 enden.

**Erlaubte Vorgänger in `## Abhängigkeiten`:**
- Alle Growth Skills (T02/T03)
- Alle Content Skills (T04 + diese T05-Skills, wenn zuvor in dieser Aufgabe erstellt)
- S01-Skills: `elvis-x-hook-writer`, `elvis-growth-audit`, `elvis-market-scan`, `elvis-execution-plan`
- `"keine (Einstiegs-Skill)"` wenn zutreffend

## Steps

1. **elvis-opinion-post.md** — Erstellt Meinungsbeitrag nach Struktur: Stance (1 Satz, klar positioniert, max. 100 Zeichen) → Begründung (2–3 Sätze, Datenpunkt oder Erfahrung) → Konsequenz (1 Satz, was folgt daraus) → 2 Gegenargumente (je 1 Satz) → Widerlegung (je 1 Satz). Ausführungsschritte: (1) Stance formulieren (kein Weichspülen: kein "es kommt drauf an"), (2) 3 Begründungspunkte sammeln (je mit Datenpunkt/Erfahrung), (3) Konsequenz ableiten, (4) 2 Stärkste Gegenargumente benennen, (5) Widerlegung je Gegenargument. Gesamtlänge: max. 500 Zeichen für Single-Post, oder als Thread 5 Tweets à max. 280 Zeichen. Failure: Stance enthält Weichmacher ("vielleicht", "könnte") → neu formulieren. Abhängigkeiten: keine (Einstiegs-Skill).

2. **elvis-how-to-writer.md** — Schreibt How-To-Anleitung als X-Thread oder Single-Post. Single-Post-Format: Titel-Tweet ("So [Ergebnis] in [Zeitraum/Schritten]:", max. 100 Zeichen) + max. 4 Schritte als nummerierte Liste (je max. 60 Zeichen pro Schritt-Zeile) = Gesamt max. 280 Zeichen. Thread-Format: Hook-Tweet + 5 Schritt-Tweets (je Schritt: Aktion + Ergebnis, max. 200 Zeichen) + CTA-Tweet = 7 Tweets. Ausführungsschritte: (1) Ziel-Ergebnis in 1 Satz, (2) Max. 5 Schritte identifizieren (nicht mehr), (3) Format wählen (Single-Post wenn ≤4 Schritte, Thread wenn 5), (4) Schritte mit Verben beginnen (Imperativ), (5) Zeichenzahl prüfen. Abhängigkeiten: keine (Einstiegs-Skill).

3. **elvis-content-ideas.md** — Generiert 20 Content-Ideen zu einem Thema in 4 Kategorien. Kategorien und Anteil: (A) Bildung = 8 Ideen (How-To, Erklärt, Fakten), (B) Unterhaltung = 5 Ideen (Story, Humor, Behind-the-Scenes), (C) Inspiration = 4 Ideen (Erfahrung, Quote, Transformation), (D) Konversion = 3 Ideen (Produkt, Angebot, Social Proof). Ausführungsschritte: (1) Thema in 3 Unter-Themen aufteilen, (2) Je Unter-Thema 7 Ideen brainstormen (≥21 Roh-Ideen), (3) 20 stärkste auswählen (Kriterium: Relevanz für Zielgruppe), (4) Kategorien zuweisen, (5) Output als Liste: Kategorie — Idee — Format (Single/Thread/Poll) — Dringlichkeit (Evergreen/Trend). Failure: Weniger als 3 Ideen in einer Kategorie → fehlende Kategorie explizit auffüllen. Abhängigkeiten: elvis-x-trend-scanner (empfohlen — Trends als Themen-Input).

4. **elvis-headline-writer.md** — Schreibt 7 Headline-Varianten für denselben Inhalt — je eine pro Formel. Formeln: (1) Zahl ("7 Wege, um..."), (2) Frage ("Warum [Problem]?"), (3) How-To ("So [Ergebnis] in [Zeitraum]"), (4) Secret ("Das [Gruppe] nicht über [Thema] sagt"), (5) Warning ("Stopp: Bevor du [Aktion]..."), (6) Result ("Ich habe [X] getan. Das ist passiert."), (7) Contrast ("Die meisten [Aktion]. Ich nicht."). Zeichenlimit: jede Variante max. 100 Zeichen. Ausführungsschritte: (1) Kern-Aussage des Inhalts in 1 Satz, (2) Für jede Formel: Template ausfüllen, (3) Zeichenzahl prüfen, (4) Stärkste Variante empfehlen (Begründung: welche Emotion, welche Zielgruppe), (5) A/B-Test-Empfehlung (welche 2 Varianten testen). Abgrenzung zu elvis-x-hook-writer: Headline-Writer ist format-neutral (nicht X-spezifisch), Hook-Writer erzeugt fertige Tweet-Varianten. Abhängigkeiten: keine (Einstiegs-Skill).

5. **elvis-reply-writer.md** — Schreibt 5 strategische Antworten auf einen viralen Post. Ziele: (1) Sichtbarkeit (kontroverser Standpunkt, max. 100 Zeichen), (2) Expertise (Daten oder Erfahrung, max. 200 Zeichen), (3) Netzwerk (Lob + eigene Perspektive, max. 150 Zeichen), (4) Humor (witzige Erweiterung, max. 120 Zeichen), (5) CTA (Folgefrage die Kommentare generiert, max. 100 Zeichen). Ausführungsschritte: (1) Original-Post-Kernaussage identifizieren, (2) Je Ziel eine Antwort-Strategie wählen, (3) Je Antwort Variante schreiben, (4) Zeichenzahl prüfen, (5) Beste Antwort für sofortige Nutzung empfehlen + Begründung (Warum das Ziel "Sichtbarkeit" für Wachstum prioritär ist). Failure: Antwort > erlaubtes Zeichenlimit → kürzen. Abhängigkeiten: keine (Einstiegs-Skill).

6. **elvis-dm-writer.md** — Schreibt Cold-DM-Sequenz: 3 Nachrichten. Nachricht 1 — Opener (max. 150 Zeichen): persönliche Beobachtung zum Empfänger + konkrete Gemeinsamkeit, kein "Ich habe Ihre Arbeit verfolgt". Nachricht 2 — Mehrwert (max. 200 Zeichen): konkreter Mehrwert (Ressource, Insight, Idee) ohne Gegenleistung. Nachricht 3 — Follow-Up (max. 100 Zeichen): weiche CTA ("Falls relevant — [Angebot in 1 Satz]"). Timing: Nachricht 2 frühestens 24h nach Opener, Nachricht 3 frühestens 48h nach Nachricht 2. Ausführungsschritte: (1) Empfänger-Profil studieren (letzter Post, Bio, Thema), (2) Opener schreiben (spezifisch, kein Template-Feeling), (3) Mehrwert-Nachricht schreiben (was kann der Empfänger sofort nutzen?), (4) Follow-Up schreiben (Einladung, nicht Druck), (5) Timing-Plan dokumentieren. Failure: Nachricht enthält Preis oder Verkaufsangebot in Opener → neu schreiben. Abhängigkeiten: keine (Einstiegs-Skill).

7. **elvis-content-brief.md** — Erstellt vollständiges Content-Brief für Post oder Thread. Briefing-Sektionen: (1) Ziel (Awareness/Engagement/Conversion — nur 1 auswählen), (2) Zielgruppe (Segment aus elvis-audience-builder, max. 2 Sätze), (3) Kernbotschaft (1 Satz, die zentrale Aussage), (4) Format (Single-Post/Thread/Poll — mit Begründung), (5) Tonfall (Sachlich/Provokativ/Persönlich — mit Begründung), (6) CTA (Typ aus elvis-cta-writer), (7) Tabu-Liste (max. 3 Punkte: was nicht gesagt werden soll). Ausführungsschritte: 5 Schritte. Output: Ausgefülltes Brief-Template (7 Felder, max. 300 Wörter). Failure: Mehr als 1 Ziel ausgewählt → auf 1 reduzieren. Abhängigkeiten: elvis-audience-builder, elvis-content-ideas, elvis-cta-writer.

## Must-Haves

- [ ] Alle 7 Dateien enthalten alle 9 Pflichtsektion-Header
- [ ] elvis-content-ideas.md enthält 4-Kategorien-Aufteilung mit Anzahl (8+5+4+3=20)
- [ ] elvis-headline-writer.md enthält alle 7 Formeln explizit benannt
- [ ] elvis-dm-writer.md enthält Timing-Plan (24h/48h-Regeln)
- [ ] elvis-content-brief.md enthält 7 Briefing-Sektionen
- [ ] Cross-kategorie Abhängigkeiten korrekt: content-ideas → x-trend-scanner, content-brief → audience-builder
- [ ] Alle Inhalte auf Deutsch

## Verification

- `bash scripts/verify-s04.sh` → Exit-Code 0 (alle 28 Skills vollständig)
- `bash scripts/verify-s04.sh 2>&1 | tail -5` → Abschluss-Banner mit "0 Fehler" oder äquivalent
- `grep "elvis-x-trend-scanner" skills/content/elvis-content-ideas.md` → vorhanden (cross-kategorie Link)
- `grep "elvis-audience-builder" skills/content/elvis-content-brief.md` → vorhanden

## Observability Impact

- Signals added/changed: Nach T05 → `bash scripts/verify-s04.sh` Exit-Code 0; alle 28 × 9 = 252 Sektions-Checks ✓
- How a future agent inspects this: `bash scripts/verify-s04.sh` als vollständige Inspektion
- Failure state exposed: Jede ✗-Zeile zeigt genau welche Datei/Sektion noch fehlt

## Inputs

- `skills/content/elvis-x-hook-writer.md` — Qualitäts-Benchmark
- `skills/growth/elvis-x-trend-scanner.md` (aus T02) — Cross-Referenz für content-ideas
- `skills/growth/elvis-audience-builder.md` (aus T02) — Cross-Referenz für content-brief
- `skills/content/elvis-cta-writer.md` (aus T04) — Abhängigkeit für content-brief
- `skills/content/elvis-content-ideas.md` (aus diesem Task, zuerst erstellt) — Abhängigkeit für content-brief

## Expected Output

- `skills/content/elvis-opinion-post.md` — Stance + Begründung + 2 Gegenargumente
- `skills/content/elvis-how-to-writer.md` — Single-Post (≤4 Schritte) oder Thread (5 Schritte)
- `skills/content/elvis-content-ideas.md` — 20 Ideen in 4 Kategorien (8+5+4+3)
- `skills/content/elvis-headline-writer.md` — 7 Varianten × 7 Formeln
- `skills/content/elvis-reply-writer.md` — 5 strategische Antworten × 5 Ziele
- `skills/content/elvis-dm-writer.md` — 3-Nachrichten-Sequenz + Timing-Plan
- `skills/content/elvis-content-brief.md` — 7-Felder-Briefing-Template
