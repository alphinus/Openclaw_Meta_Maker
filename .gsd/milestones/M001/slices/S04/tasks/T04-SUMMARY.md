---
id: T04
parent: S04
milestone: M001
provides:
  - skills/content/elvis-x-thread-writer.md — 8–12 Tweets, Hook + Entwicklung + CTA, 5-Schritt-Ausführung
  - skills/content/elvis-content-calendar.md — 30-Tage-Kalender, 5 Kategorien 40/20/20/10/10, 30 Einträge
  - skills/content/elvis-copywriting.md — PAS-Prinzip, 3 Formate (Produkt-Post/Angebot-Tweet/DM-Pitch)
  - skills/content/elvis-content-repurpose.md — 5 Posts (5 Stile) + 8-Tweet-Thread aus Langform
  - skills/content/elvis-story-writer.md — 3-Akt-Prinzip, je max. 280 Zeichen pro Akt
  - skills/content/elvis-bio-writer.md — 3 Varianten mit Formeln (sachlich/provokativ/storytelling)
  - skills/content/elvis-cta-writer.md — 5 CTA-Typen mit Formeln und Zeichenlimits
key_files:
  - skills/content/elvis-x-thread-writer.md
  - skills/content/elvis-content-calendar.md
  - skills/content/elvis-copywriting.md
  - skills/content/elvis-content-repurpose.md
  - skills/content/elvis-story-writer.md
  - skills/content/elvis-bio-writer.md
  - skills/content/elvis-cta-writer.md
key_decisions:
  - elvis-content-calendar verwendet feste 40/20/20/10/10-Kategorie-Verteilung (12A+6B+6C+3D+3E=30) — keine Abweichung ohne Operator-Freigabe, Lückenprüfung als eigener Schritt 4
  - elvis-content-repurpose liefert exakt 5 Posts in 5 verschiedenen Stilen (Fakt/Quote/Frage/Kontrast/Liste) + exakt 8-Tweet-Thread — Stile erzwingen Nicht-Redundanz bei Serie
  - elvis-bio-writer definiert 3 verschiedene Zeichenlimits je Variante (A=120, B=150, C=160) — unterschiedliche Limits weil Stil unterschiedlich viel Volumen erfordert
  - elvis-content-calendar Abhängigkeit von elvis-content-ideas (T05) als optional formuliert: "Empfohlener Vorgänger: elvis-content-ideas — kann aber auch eigenständig genutzt werden"
patterns_established:
  - Alle 7 Skills enthalten Failure-Indikator mit konkreter Schwelle und Meldungstext im Verifikations-Block
  - Zeichenlimits immer als explizite Zahlen (min/max) direkt in Ausführungsschritten und Verifikation
  - Formeln für strukturierte Outputs direkt im Ausführungsschritt dokumentiert (z.B. "[Rolle] der [Tätigkeit] für [Zielgruppe]")
  - Einstiegs-Skills (story-writer, bio-writer, cta-writer) verzichten bewusst auf Abhängigkeiten
observability_surfaces:
  - bash scripts/verify-s04.sh — zeigt ✓ für alle 7 T04-Skills in allen 4 Check-Gruppen; 77 verbleibende ✗ betreffen ausschließlich T05-Content-Skills
duration: ~35min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T04: Content Skills 1–7 erstellen

**7 Content-Skill-Dateien erstellt (elvis-x-thread-writer bis elvis-cta-writer) — alle 9 Pflichtsektion-Header vorhanden, alle Zeichenlimits explizit, verify-s04.sh zeigt 0 ✗-Zeilen für diese 7 Skills.**

## What Happened

Alle 7 Content Skills wurden nach dem 9-Sektionen-Template erstellt, mit `skills/content/elvis-x-hook-writer.md` als Qualitäts-Benchmark:

- **elvis-x-thread-writer**: 8–12 Tweets, Hook (min. 60/max. 280 Zeichen), Entwicklungs-Tweets 2–7 mit "N/"-Nummerierung, Beweis-Tweet, Übergangs-Tweet (max. 100 Zeichen), CTA-Tweet. Failure: Hook außerhalb Zeichenlimit → Stopp.
- **elvis-content-calendar**: 30-Tage-Kalender mit fixer 40/20/20/10/10-Verteilung (12A+6B+6C+3D+3E=30). Themen-Pool min. 5 Ideen je Kategorie. Abhängigkeit zu elvis-content-ideas als optional formuliert.
- **elvis-copywriting**: PAS-Prinzip in 3 Formaten — Produkt-Post (max. 280), Angebot-Tweet (max. 240), DM-Pitch (3 Nachrichten: 150+200+100 Zeichen). Verbotene Wörter "günstig/billig/kostenlos" werden markiert.
- **elvis-content-repurpose**: Aus Langform (min. 800 Wörter / 5 Min.) → 5 Posts in 5 verschiedenen Stilen (Fakt/Quote/Frage/Kontrast/Liste) + 8-Tweet-Thread. Failure: zu kurzer Input → Stopp.
- **elvis-story-writer**: 3-Akt-Struktur (Problem/Wendepunkt/Erkenntnis), je max. 280 Zeichen. Akt 2 erzwingt konkrete Szene, Akt 3 verbietet explizite Moral. Einstiegs-Skill ohne Abhängigkeiten.
- **elvis-bio-writer**: 3 Varianten mit je eigener Formel und eigenem Zeichenlimit (A=120, B=150, C=160 Zeichen). Zusammenfassungs-Tabelle (Variante/Zeichen/Limit/Status). Einstiegs-Skill.
- **elvis-cta-writer**: 5 CTA-Typen mit Formeln und Zeichenlimits (Follow 60 / Repost 80 / Kommentar 100 / Link 100 / DM 80). Warnmeldung "Zu viele CTAs" bei Mehrfach-CTA im gleichen Post.

## Verification

```bash
# Kein ✗ für die 7 T04-Skills:
bash scripts/verify-s04.sh 2>&1 | grep "✗" | grep -E "thread-writer|content-calendar|copywriting|content-repurpose|story-writer|bio-writer|cta-writer"
# → keine Ausgabe (Exit-Code 1 = grep fand keine Matches)

# Zeichenlimit-Checks:
grep -c "Zeichen" skills/content/elvis-x-thread-writer.md
# → 17

grep "280" skills/content/elvis-x-thread-writer.md | head -3
# → Zeilen mit 280-Zeichen-Angaben vorhanden

# Verbleibende Fehler: 77 (7 fehlende T05-Skills × 11 Checks)
bash scripts/verify-s04.sh 2>&1 | tail -5
# → ❌ 77 Fehler — ausschließlich T05-Skills (opinion-post, how-to-writer, content-ideas, headline-writer, reply-writer, dm-writer, content-brief)
```

## Diagnostics

- `bash scripts/verify-s04.sh` — nach T04 zeigen alle 21 bisherigen Skills (14 Growth + 7 Content) ✓ in allen 4 Check-Gruppen
- Verbleibende ✗-Zeilen betreffen ausschließlich die 7 T05-Content-Skills
- Alle 7 T04-Dateien in `skills/content/` — alle mit ≥5 nummerierten Ausführungsschritten, alle mit ≥1 Mengenangabe pro Schritt

## Deviations

- **elvis-content-calendar**: Abhängigkeit zu elvis-content-ideas (kommt aus T05) als optional formuliert: "Empfohlener Vorgänger: elvis-content-ideas — kann aber auch eigenständig genutzt werden" — exakt wie im Task-Plan gefordert.
- **elvis-cta-writer Schritt 5**: Variante 4 und 5 in einem Schritt zusammengefasst (wie im Task-Plan "5 Schritte" angegeben) — beide Varianten vollständig mit Formel und Beispiel dokumentiert.

## Known Issues

none

## Files Created/Modified

- `skills/content/elvis-x-thread-writer.md` — 8–12 Tweets, Hook min. 60/max. 280 Zeichen, 7 Ausführungsschritte
- `skills/content/elvis-content-calendar.md` — 30-Tage-Kalender, 5 Kategorien 12+6+6+3+3=30, 5 Ausführungsschritte
- `skills/content/elvis-copywriting.md` — PAS-Prinzip, 3 Formate mit expliziten Zeichenlimits, 5 Ausführungsschritte
- `skills/content/elvis-content-repurpose.md` — 5 Posts + 8-Tweet-Thread aus Langform, 5 Ausführungsschritte
- `skills/content/elvis-story-writer.md` — 3-Akt-Prinzip je max. 280 Zeichen, 5 Ausführungsschritte
- `skills/content/elvis-bio-writer.md` — 3 Varianten mit Formeln (A=120/B=150/C=160 Zeichen), 5 Ausführungsschritte
- `skills/content/elvis-cta-writer.md` — 5 CTA-Typen mit Formeln (Follow 60/Repost 80/Kommentar 100/Link 100/DM 80 Zeichen), 5 Ausführungsschritte
