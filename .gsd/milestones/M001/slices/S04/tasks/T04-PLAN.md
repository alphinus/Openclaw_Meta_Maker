---
estimated_steps: 7
estimated_files: 7
---

# T04: Content Skills 1–7 erstellen

**Slice:** S04 — Growth + Content Skills (~30 Skills)
**Milestone:** M001

## Description

Die erste Hälfte der Content Skills erstellen — von Thread-Writer bis CTA-Writer. Qualitäts-Benchmark ist `skills/content/elvis-x-hook-writer.md` aus S01: genau 5 Varianten, explizite Zeichenzahlen (min. 80 / max. 280), je Schritt ein abgrenzbares Artefakt, Zeichenanzahl direkt im Schritt-Format dokumentiert.

Diese 7 Skills decken die Kern-Formate für X/Twitter-Content ab: Threads, Kalender, Copywriting, Repurposing, Stories, Bio und CTAs. Alle Zeichenlimits sind explizit und pro Schritt dokumentiert.

**Erlaubte Vorgänger in `## Abhängigkeiten`:**
- elvis-x-hook-writer (S01)
- Alle Growth Skills aus T02/T03
- Andere Content Skills aus T04 (falls bereits erstellt in dieser Aufgabe)
- `"keine (Einstiegs-Skill)"` wenn zutreffend

## Steps

1. **elvis-x-thread-writer.md** — Schreibt X-Thread mit 8–12 Tweets. Ausführungsschritte: (1) Hook-Tweet (max. 280 Zeichen, Frage oder Aussage, kein Doppelpunkt am Ende), (2) Entwicklungs-Tweets 2–7 (je max. 280 Zeichen, je ein Punkt/Argument, Nummerierung im Tweet), (3) Beweis-Tweet (Daten, Beispiel, Story, max. 280 Zeichen), (4) Übergangs-Tweet ("Hier ist das Wichtigste:", max. 100 Zeichen), (5) CTA-Tweet (1 klare Handlungsaufforderung, max. 280 Zeichen). Gesamt: min. 8, max. 12 Tweets. Failure: Hook-Tweet > 280 Zeichen oder < 60 Zeichen → neu schreiben. Abhängigkeiten: elvis-x-hook-writer, elvis-viral-formula.

2. **elvis-content-calendar.md** — Erstellt 30-Tage-Content-Kalender. 5 Kategorien: (A) Bildung (How-To, Erklärt), (B) Unterhaltung (Story, Humor), (C) Inspiration (Quote, Erfolg), (D) Konversion (Angebot, CTA), (E) Engagement (Frage, Poll). Verteilung: A=40%, B=20%, C=20%, D=10%, E=10% → ergibt: 12A + 6B + 6C + 3D + 3E = 30 Posts. Ausführungsschritte: (1) Kategorie-Verteilung berechnen, (2) Themen-Pool je Kategorie (min. 5 Ideen), (3) Kalender-Tabelle (Spalten: Tag, Datum, Kategorie, Thema, Format, Zeit), (4) Lückenprüfung (kein Tag ohne Eintrag), (5) Export-Format (Markdown-Tabelle 30 Zeilen). Abhängigkeiten: elvis-content-ideas (aus T05, aber content-calendar kann auch standalone starten — `elvis-content-ideas optional`).

   **Hinweis:** Da elvis-content-ideas aus T05 kommt, formuliere Abhängigkeit als "Empfohlener Vorgänger: elvis-content-ideas — kann aber auch eigenständig genutzt werden."

3. **elvis-copywriting.md** — Schreibt verkaufsfördernden Text nach PAS-Prinzip für 3 Formate. PAS = Problem → Agitation → Solution. Format 1: Produkt-Post (max. 280 Zeichen, P=1 Satz, A=1 Satz, S=1 Satz + Preis). Format 2: Angebot-Tweet (max. 240 Zeichen, direkte Nutzen-Sprache, 1 CTA am Ende). Format 3: DM-Pitch (max. 150 Zeichen Opener + max. 200 Zeichen Angebot + max. 100 Zeichen CTA = 3 Nachrichten). Ausführungsschritte: 5 Schritte. Failure: Text enthält "günstig", "billig" oder "kostenlos" ohne konkreten Wert → markieren. Abhängigkeiten: elvis-x-hook-writer.

4. **elvis-content-repurpose.md** — Wandelt einen Langform-Inhalt in 5 X-Posts + 1 Thread um. Input-Typen: Artikel (min. 800 Wörter) oder Video-Transkript (min. 5 Min). Ausführungsschritte: (1) Langform-Inhalt auf 5 Kern-Aussagen verdichten (je max. 1 Satz), (2) Jede Kern-Aussage zu X-Post expandieren (max. 280 Zeichen, je anderer Stil: Fakt, Quote, Frage, Kontrast, Liste), (3) Thread-Hook aus der stärksten Kern-Aussage (max. 280 Zeichen), (4) Thread-Body (6 Tweets à max. 280 Zeichen, je eine Kern-Aussage + Kontext), (5) Thread-CTA (max. 140 Zeichen). Output: 5 Posts + 8-Tweet-Thread. Failure: Langform-Inhalt < 800 Wörter / < 5 Min → Hinweis "zu kurz für Repurposing". Abhängigkeiten: elvis-x-thread-writer, elvis-x-hook-writer.

5. **elvis-story-writer.md** — Schreibt Personal-Story nach 3-Akt-Prinzip. Akt 1: Problem (max. 280 Zeichen — Ausgangssituation + Schmerzpunkt). Akt 2: Wendepunkt (max. 280 Zeichen — der Moment der Veränderung + konkretes Erlebnis). Akt 3: Lösung/Erkenntnis (max. 280 Zeichen — was sich verändert hat + implizite Botschaft). Ausführungsschritte: (1) Kern-Erfahrung in 1 Satz fassen, (2) Akt 1 schreiben (Problem konkret, kein Jammern), (3) Akt 2 schreiben (eine spezifische Szene, kein Allgemeinplatz), (4) Akt 3 schreiben (Erkenntnis ohne direkte Moral-Aussage), (5) Zeichenanzahl je Akt prüfen. Failure: Ein Akt > 280 Zeichen → kürzen. Abhängigkeiten: keine (Einstiegs-Skill).

6. **elvis-bio-writer.md** — Generiert 3 Bio-Varianten: (A) Sachlich (Berufsrolle + Expertise + Ergebnis, max. 120 Zeichen), (B) Provokativ (Kontra-These + Differenzierung + CTA, max. 150 Zeichen), (C) Storytelling (Transformation + Identität + Einladung, max. 160 Zeichen). Ausführungsschritte: (1) Kernkompetenz in 3 Keywords, (2) Variante A schreiben (Formel: [Rolle] der [Tätigkeit] für [Zielgruppe]), (3) Variante B schreiben (Formel: Nicht [Klischee]. [Differenzierung]. [CTA].), (4) Variante C schreiben (Formel: Von [X] zu [Y]. Jetzt [Aktivität].), (5) Zeichenzahl je Variante dokumentieren. Failure: Variante A > 120 Zeichen → kürzen. Abhängigkeiten: keine (Einstiegs-Skill).

7. **elvis-cta-writer.md** — Schreibt 5 CTA-Varianten für einen Post. Variante 1: Follow-CTA (Warum folgen? 1 konkreter Nutzen, max. 60 Zeichen). Variante 2: Repost-CTA (Wer profitiert? 1 Zielgruppe, max. 80 Zeichen). Variante 3: Kommentar-CTA (offene Frage, max. 100 Zeichen). Variante 4: Link-Klick-CTA (Nutzen + Dringlichkeit, max. 100 Zeichen). Variante 5: DM-CTA (Trigger-Wort + Handlung, max. 80 Zeichen). Ausführungsschritte: 5 Schritte (je eine Variante mit Formel und Beispiel). Failure: Mehr als 1 CTA im gleichen Post → Warnmeldung "Zu viele CTAs — max. 1 pro Post". Abhängigkeiten: keine (Einstiegs-Skill, passt zu jedem Content-Skill).

## Must-Haves

- [ ] Alle 7 Dateien enthalten alle 9 Pflichtsektion-Header
- [ ] Alle Zeichenlimits explizit benannt (min/max als Zahlen)
- [ ] Jeder Skill hat ≥4 nummerierte Ausführungsschritte mit ≥1 Mengenangabe
- [ ] elvis-x-thread-writer.md enthält min. 8 / max. 12 Tweets-Spezifikation
- [ ] elvis-bio-writer.md enthält alle 3 Varianten-Formeln
- [ ] elvis-cta-writer.md enthält alle 5 CTA-Typen
- [ ] Alle Inhalte auf Deutsch

## Verification

- `bash scripts/verify-s04.sh 2>&1 | grep "✗" | grep -E "thread-writer|content-calendar|copywriting|content-repurpose|story-writer|bio-writer|cta-writer"` → keine ✗-Zeilen
- `grep -c "Zeichen" skills/content/elvis-x-thread-writer.md` → Wert ≥ 3 (Zeichenlimits erwähnt)
- `grep "280" skills/content/elvis-x-thread-writer.md` → vorhanden

## Observability Impact

- Signals added/changed: 7 Content Skills erscheinen in `bash scripts/verify-s04.sh` als ✓
- How a future agent inspects this: `bash scripts/verify-s04.sh` — nach T04 fehlen nur noch 7 Content Skills aus T05
- Failure state exposed: Fehlende Sektion = ✗ im Output

## Inputs

- `skills/content/elvis-x-hook-writer.md` — Qualitäts-Benchmark: Varianten-Format, Zeichenzahl-Dokumentation
- `skills/growth/elvis-viral-formula.md` (aus T02) — Abhängigkeit für thread-writer
- `skills/growth/elvis-audience-builder.md` (aus T02) — Kontext für content-calendar
- `templates/skill-template.md` — 9-Sektionen-Struktur
- S04-RESEARCH.md Abschnitt 5.2

## Expected Output

- `skills/content/elvis-x-thread-writer.md` — 8–12 Tweets, Hook + Entwicklung + CTA
- `skills/content/elvis-content-calendar.md` — 30-Tage-Kalender, 5 Kategorien, 30 Einträge
- `skills/content/elvis-copywriting.md` — PAS-Prinzip, 3 Formate
- `skills/content/elvis-content-repurpose.md` — 5 Posts + 8-Tweet-Thread aus Langform
- `skills/content/elvis-story-writer.md` — 3-Akt-Struktur, je max. 280 Zeichen
- `skills/content/elvis-bio-writer.md` — 3 Varianten (sachlich/provokativ/storytelling)
- `skills/content/elvis-cta-writer.md` — 5 CTA-Typen mit Formeln
