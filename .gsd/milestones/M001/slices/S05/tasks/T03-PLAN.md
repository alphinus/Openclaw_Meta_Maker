---
estimated_steps: 7
estimated_files: 7
---

# T03: Strategy Skills S01–S07 erstellen

**Slice:** S05 — Research + Strategy Skills (~30 Skills)
**Milestone:** M001

## Description

Erstellt die ersten 7 Strategy Skills (S01–S07): Growth Strategy, Positioning Strategy, Content Strategy, Go-to-Market, Platform Strategy, Risk Assessment und Competitive Strategy. Diese Skills decken die meta-strategische Ebene ab — sie stehen über den taktischen Growth-Skills aus S04 und definieren Langzeit-Richtung statt kurzfristige Maßnahmen.

Qualitäts-Benchmark: `skills/strategy/elvis-execution-plan.md` (SMART-Ziele, Impact/Aufwand-Matrix, 30-Tage-Plan) — alle Strategy Skills müssen mindestens diesen Konkretisierungsgrad erreichen.

## Steps

1. Lies `skills/strategy/elvis-execution-plan.md` als Qualitäts-Benchmark — merke Format: SMART-Ziele, 2×2 Matrizen, konkrete Zeiträume (30/90/365 Tage). Lies auch `skills/growth/elvis-monetization-planner.md` um die Grenze zu S04-Growth-Skills zu verstehen.
2. Erstelle `skills/strategy/elvis-growth-strategy.md` — Meta-Wachstumsstrategie: 3 Wachstums-Horizonte (30 / 90 / 365 Tage) mit je 3 SMART-Zielen, 1 Haupt-Kanal + 2 Neben-Kanäle mit Ressourcen-Aufteilung (%), Milestone-Checkpoints alle 30 Tage. Differenzierung von `elvis-growth-audit` (Ist-Analyse) durch Soll-Definition und Strategie. Abhängigkeit: `elvis-growth-audit` als empfohlener Vorgänger.
3. Erstelle `skills/strategy/elvis-positioning-strategy.md` — Differenzierung in der Nische: 5-Dimensionen-Map (Zielgruppe, Problem, Lösung, Differenzierung, Tonalität) × Selbst vs. 3 Konkurrenten, 1-Satz USP im Format "Für [Zielgruppe], die [Problem haben], biete ich [Lösung] im Gegensatz zu [Alternativ]". Failure-Indikator bei < 3 Konkurrenten in der Map.
4. Erstelle `skills/strategy/elvis-content-strategy.md` — Langfristige Content-Strategie (90 Tage): 3 Content-Säulen mit je 40%/40%/20% Gewichtung, Themen-Cluster pro Säule (mindestens 5 Themen je), Publikations-Rhythmus (Formate × Frequenz × Plattform). Differenzierung von `elvis-content-calendar` (taktischer Wochenplan) durch strategische Ausrichtung. Abhängigkeit: `elvis-content-calendar` als empfohlener Vorgänger.
5. Erstelle `skills/strategy/elvis-go-to-market.md` — GTM-Strategie für neues Produkt/Angebot: Zielgruppen-Segment (1 primäres), Kanal-Auswahl (3 priorisierte Kanäle), Botschafts-Framework (Problem → Lösung → Beweis → CTA), Launch-Phasen (Pre-Launch 2 Wochen / Launch-Woche / Post-Launch 4 Wochen). Failure-Indikator bei nicht definierten Erfolgsmetriken für jede Phase.
6. Erstelle `skills/strategy/elvis-platform-strategy.md` — Multi-Plattform-Strategie: Plattform-Portfolio-Matrix (2×2: Aufwand × Reichweite) für mindestens 5 Plattformen, Haupt-Plattform mit 60%-Ressourcen, 3 Neben-Plattformen mit je 10–15%, Migrations-Trigger (Wann wird Haupt-Plattform gewechselt?). Failure-Indikator bei fehlender Ressourcen-%-Aufteilung.
7. Erstelle `skills/strategy/elvis-risk-assessment.md` — Risikobewertung: 10 identifizierte Risiken × 3 Dimensionen (Eintrittswahrscheinlichkeit 1–5, Auswirkung 1–5, Erkennbarkeit 1–5), Risiko-Priorisierungs-Matrix (Top-3 kritische Risiken), 1 Mitigation-Maßnahme pro Top-3-Risiko. Failure-Indikator bei < 5 Risiken mit vollständiger Bewertung.
8. Erstelle `skills/strategy/elvis-competitive-strategy.md` — Wettbewerbsstrategie: 3 Basis-Strategien (Differenzierung / Kostenführerschaft / Fokus) — eine auswählen und begründen, 5 konkrete Differenzierungs-Punkte vs. Top-3-Konkurrenten, Verteidigungs-Maßnahmen gegen Imitation (3 Maßnahmen). Abhängigkeit: `elvis-competitor-deep-dive` oder `elvis-competitor-analysis` als empfohlener Vorgänger. Failure-Indikator bei fehlender Strategie-Auswahl.

## Must-Haves

- [ ] 7 Dateien existieren in `skills/strategy/`
- [ ] Jede Datei enthält genau 9 Sektionen (Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output)
- [ ] Jeder `## Name` Block enthält `/elvis-*` Prefix
- [ ] Jeder Ausführungsschritt enthält mindestens 1 konkrete Zahl, Zeitangabe oder Prozent-/Matrixformat (D006)
- [ ] Jeder `## Verifikation` Block enthält `Failure-Indikator:` mit Schwelle + Standard-Meldungstext
- [ ] Strategy Skills differenzieren sich explizit in `## Beschreibung` von taktisch ähnlichen S04-Skills
- [ ] Keine Phantom-Referenzen in `## Abhängigkeiten` — nur D021-Whitelist

## Verification

```bash
# Datei-Existenz (7 Checks)
for f in elvis-growth-strategy elvis-positioning-strategy elvis-content-strategy \
          elvis-go-to-market elvis-platform-strategy \
          elvis-risk-assessment elvis-competitive-strategy; do
  [ -f "skills/strategy/$f.md" ] && echo "✓ $f" || echo "✗ $f FEHLT"
done

# Sektions-Check (Stichprobe)
grep -c "^## " skills/strategy/elvis-growth-strategy.md  # erwartet: 9
grep -c "^## " skills/strategy/elvis-competitive-strategy.md  # erwartet: 9

# /elvis-* Prefix
grep -l "/elvis-" skills/strategy/elvis-growth-strategy.md \
     skills/strategy/elvis-positioning-strategy.md | wc -l  # erwartet: 2

# Failure-Indikator Vollständigkeit
grep -l "Failure-Indikator:" skills/strategy/elvis-growth-strategy.md \
     skills/strategy/elvis-positioning-strategy.md \
     skills/strategy/elvis-content-strategy.md \
     skills/strategy/elvis-go-to-market.md \
     skills/strategy/elvis-platform-strategy.md \
     skills/strategy/elvis-risk-assessment.md \
     skills/strategy/elvis-competitive-strategy.md | wc -l  # erwartet: 7

# Phantom-Referenz-Check für competitive-strategy
awk '/^## Abhängigkeiten/,/^## /' skills/strategy/elvis-competitive-strategy.md | grep "elvis-"
# Darf nur: elvis-competitor-deep-dive, elvis-competitor-analysis (beide existieren)
```

## Observability Impact

- Signals added/changed: None
- How a future agent inspects this: `bash scripts/verify-s05.sh` nach T05 prüft alle 28 Skills inkl. diese 7; `grep "Failure-Indikator:" skills/strategy/*.md` für schnellen Vollständigkeits-Check
- Failure state exposed: Fehlende Differenzierungs-Aussage in `## Beschreibung` ist manuell erkennbar; Phantom-Referenz wird in verify-s05.sh Check [4/4] angezeigt

## Inputs

- `templates/skill-template.md` — verbindliches 9-Sektionen-Format
- `skills/strategy/elvis-execution-plan.md` — Qualitäts-Benchmark für Strategy Skills
- `skills/growth/elvis-monetization-planner.md` — Grenzziehungs-Referenz (taktisch vs. strategisch)
- `skills/growth/elvis-growth-audit.md` — Grenzziehung für elvis-growth-strategy (Ist- vs. Soll-Analyse)
- `skills/content/elvis-content-calendar.md` — Grenzziehung für elvis-content-strategy
- Alle S04-Skills in `skills/growth/` und `skills/content/` — referenzierbar als Abhängigkeiten

## Expected Output

- `skills/strategy/elvis-growth-strategy.md` — 3-Horizonte-Wachstumsstrategie (30/90/365 Tage)
- `skills/strategy/elvis-positioning-strategy.md` — 5-Dimensionen-Map + USP-Statement
- `skills/strategy/elvis-content-strategy.md` — 90-Tage-Content-Strategie mit 3 Säulen
- `skills/strategy/elvis-go-to-market.md` — GTM mit 3 Phasen (Pre-Launch / Launch / Post)
- `skills/strategy/elvis-platform-strategy.md` — Plattform-Portfolio-Matrix + Ressourcen-Aufteilung
- `skills/strategy/elvis-risk-assessment.md` — 10 Risiken × 3 Dimensionen + Top-3-Mitigation
- `skills/strategy/elvis-competitive-strategy.md` — Basis-Strategie-Auswahl + 5 Differenzierungs-Punkte
