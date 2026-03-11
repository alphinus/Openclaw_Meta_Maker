---
id: T05
parent: S04
milestone: M001
provides:
  - skills/content/elvis-opinion-post.md — Stance-first Meinungsbeitrag, Single-Post (max. 500 Zeichen) oder 5-Tweet-Thread, Weichmacher-Failure-Check
  - skills/content/elvis-how-to-writer.md — How-To Single-Post (≤4 Schritte, max. 280 Zeichen) oder 7-Tweet-Thread (5 Schritte), Imperativ-Verben-Zwang
  - skills/content/elvis-content-ideas.md — 20 Ideen in 4 Kategorien (8A+5B+4C+3D), 3 Unter-Themen, Evergreen/Trend-Tags, Cross-Referenz zu elvis-x-trend-scanner
  - skills/content/elvis-headline-writer.md — 7 Headline-Varianten nach 7 Formeln (Zahl/Frage/How-To/Secret/Warning/Result/Contrast), je max. 100 Zeichen, A/B-Test-Empfehlung
  - skills/content/elvis-reply-writer.md — 5 strategische Antworten (Sichtbarkeit/Expertise/Netzwerk/Humor/CTA) mit je eigenem Zeichenlimit, Sichtbarkeit-Priorität-Begründung
  - skills/content/elvis-dm-writer.md — 3-Nachrichten Cold-DM-Sequenz (Opener/Mehrwert/Follow-Up) + Timing-Plan Tag 0/1+/3+, kein Verkaufsangebot in Nachrichten 1–2
  - skills/content/elvis-content-brief.md — 7-Felder-Briefing-Template (Ziel/Zielgruppe/Kernbotschaft/Format/Tonfall/CTA/Tabu-Liste), Cross-Referenz zu elvis-audience-builder
key_files:
  - skills/content/elvis-opinion-post.md
  - skills/content/elvis-how-to-writer.md
  - skills/content/elvis-content-ideas.md
  - skills/content/elvis-headline-writer.md
  - skills/content/elvis-reply-writer.md
  - skills/content/elvis-dm-writer.md
  - skills/content/elvis-content-brief.md
key_decisions:
  - elvis-content-ideas verwendet 8/5/4/3-Kategorie-Aufteilung (Bildung/Unterhaltung/Inspiration/Konversion = 20 Ideen) mit Failure-Check wenn Kategorie < Soll-Anzahl — erzwingt vollständige Verteilung
  - elvis-how-to-writer wählt Format automatisch nach Schrittzahl (≤4 Schritte → Single-Post, genau 5 → Thread) — Format-Entscheidung ist deterministisch nicht manuell
  - elvis-dm-writer Timing-Plan ist hart (frühestens 24h / frühestens 48h) nicht "circa" — erzwingt explizite Staffelung über mindestens 3 Tage
  - elvis-opinion-post Weichmacher-Liste ist explizit (vielleicht/könnte/es kommt drauf an) — Failure-Check ist pattern-basiert nicht semantisch
patterns_established:
  - Failure-Indikatoren als Muster-Match auf konkrete Begriffe (Weichmacher-Liste) statt semantischer Bewertung — reproduzierbar und prüfbar
  - Timing-Regeln als Minimum-Abstände (frühestens X) statt exakter Zeitpunkte — gibt Flexibilität ohne Beliebigkeit
  - Cross-kategorie Abhängigkeiten explizit in Beschreibung UND Abhängigkeiten-Sektion genannt — doppelte Sichtbarkeit
observability_surfaces:
  - bash scripts/verify-s04.sh — 252 Sektions-Checks (28 × 9), 28 Prefix-Checks, Phantom-Referenz-Check; Exit-Code 0 = alles vollständig
duration: ~25min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T05: Content Skills 8–14 erstellen

**7 Content-Skill-Dateien erstellt (elvis-opinion-post bis elvis-content-brief) — alle 9 Pflichtsektion-Header vorhanden, alle Zeichenlimits explizit, verify-s04.sh zeigt Exit-Code 0 für alle 28 Skills.**

## What Happened

Erstellt wurden 7 Content Skills als zweite Hälfte der Content-Kette (S04):

1. **elvis-opinion-post.md** — Stance-first-Struktur (Stance → Begründung → Konsequenz → 2 Gegenargumente → Widerlegung). Single-Post max. 500 Zeichen oder 5-Tweet-Thread. Failure-Check auf explizite Weichmacher-Begriffe ("vielleicht", "könnte", "es kommt drauf an").

2. **elvis-how-to-writer.md** — Format-Wahl deterministisch nach Schrittzahl: ≤4 Schritte → Single-Post (max. 280 Zeichen), genau 5 Schritte → 7-Tweet-Thread. Alle Schritte beginnen mit Imperativ-Verb.

3. **elvis-content-ideas.md** — 20 Ideen in fixer 8/5/4/3-Verteilung (Bildung/Unterhaltung/Inspiration/Konversion). Brainstorming über 3 Unter-Themen mit ≥21 Roh-Ideen. Evergreen/Trend-Tags je Idee. Cross-Referenz zu `elvis-x-trend-scanner` (T02).

4. **elvis-headline-writer.md** — 7 Headline-Varianten, je eine pro Formel: Zahl, Frage, How-To, Secret, Warning, Result, Contrast. Jede ≤100 Zeichen. Stärken-Empfehlung mit Emotion-Label + A/B-Test-Empfehlung für 2 psychologisch verschiedene Varianten.

5. **elvis-reply-writer.md** — 5 strategische Antworten (Sichtbarkeit ≤100, Expertise ≤200, Netzwerk ≤150, Humor ≤120, CTA ≤100 Zeichen). Empfehlung mit Begründung warum Sichtbarkeit (kontroverser Standpunkt = mehr Replies = Algorithmus-Reichweite) prioritär ist.

6. **elvis-dm-writer.md** — 3-Nachrichten Cold-DM-Sequenz mit harten Timing-Regeln: Nachricht 2 frühestens 24h nach Opener, Nachricht 3 frühestens 48h nach Nachricht 2. Kein Verkaufsangebot in Nachrichten 1–2. Failure-Check erkennt Preis/Angebot im Opener.

7. **elvis-content-brief.md** — 7-Felder-Template: Ziel (exakt 1 aus 3), Zielgruppe (elvis-audience-builder, max. 2 Sätze), Kernbotschaft (1 Satz), Format, Tonfall, CTA (elvis-cta-writer), Tabu-Liste (max. 3 Punkte). Max. 300 Wörter Gesamt-Output. Cross-Referenz zu `elvis-audience-builder` (T02).

## Verification

```
bash scripts/verify-s04.sh
# Exit-Code 0
# [1/4] 28 Datei-Existenz-Checks ✓
# [2/4] 252 Sektions-Checks (28 × 9) ✓
# [3/4] 28 /elvis-* Prefix-Checks ✓
# [4/4] Phantom-Referenz-Check ✓
# ✅ S04 Verifikation bestanden — alle Checks grün

grep "elvis-x-trend-scanner" skills/content/elvis-content-ideas.md  # vorhanden ✓
grep "elvis-audience-builder" skills/content/elvis-content-brief.md  # vorhanden ✓
```

Alle 4 Must-Haves explizit verifiziert:
- elvis-content-ideas.md enthält 4-Kategorien mit Anzahl (8+5+4+3=20) ✓
- elvis-headline-writer.md enthält alle 7 Formeln explizit benannt ✓
- elvis-dm-writer.md enthält Timing-Plan (24h/48h-Regeln) ✓
- elvis-content-brief.md enthält 7 Briefing-Sektionen ✓

## Diagnostics

- `bash scripts/verify-s04.sh` — vollständige Inspektion aller 28 Skills, Exit-Code = Fehleranzahl (0 = alles ok)
- Jede ✗-Zeile zeigt genau Datei + fehlende Sektion — direkter Reparatur-Hinweis

## Deviations

Keine. Alle 7 Skills exakt nach T05-PLAN.md erstellt.

## Known Issues

Keine.

## Files Created/Modified

- `skills/content/elvis-opinion-post.md` — Stance-first Meinungsbeitrag, Weichmacher-Failure-Check
- `skills/content/elvis-how-to-writer.md` — How-To Single-Post oder 7-Tweet-Thread, Format-Wahl nach Schrittzahl
- `skills/content/elvis-content-ideas.md` — 20 Ideen in 4 Kategorien (8+5+4+3), Cross-Referenz zu elvis-x-trend-scanner
- `skills/content/elvis-headline-writer.md` — 7 Headline-Formeln, A/B-Test-Empfehlung
- `skills/content/elvis-reply-writer.md` — 5 strategische Antworten × 5 Ziele, je Zeichenlimit
- `skills/content/elvis-dm-writer.md` — 3-Nachrichten-Sequenz, Timing-Plan Tag 0/1+/3+
- `skills/content/elvis-content-brief.md` — 7-Felder-Brief-Template, Cross-Referenz zu elvis-audience-builder
