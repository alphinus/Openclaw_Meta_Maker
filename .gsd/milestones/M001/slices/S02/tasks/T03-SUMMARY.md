---
id: T03
parent: S02
milestone: M001
provides:
  - soul/operator.md — 6 Sektionen, Weltbild "Erhält laufende Systeme", Sulu + Uhura als primäre Agenten, explizite Abgrenzung zu execution
  - soul/analyst.md — 6 Sektionen, Weltbild "Was bedeutet das?", Seven + Troi als primäre Agenten, explizite researcher-Abgrenzung in Philosophie
  - soul/creator.md — 6 Sektionen, Weltbild "Erschafft Neues", Data + Q als primäre Agenten, explizite builder-Abgrenzung in Philosophie
  - soul/minimalist.md — 6 Sektionen, Lens-Soul ohne primären Agenten, konkrete messbare Success Metrics
key_files:
  - soul/operator.md
  - soul/analyst.md
  - soul/creator.md
  - soul/minimalist.md
key_decisions:
  - none
patterns_established:
  - Abgrenzung analyst vs. researcher explizit in Philosophie-Sektion ("Was bedeutet das?" vs. "Was ist wahr?") — Leser erkennt sofort welcher Soul für welche Aufgabe geeignet ist
  - Abgrenzung creator vs. builder explizit in Philosophie-Sektion (erschafft neue Entitäten vs. konstruiert mit bekannten Materialien nach bekannten Prinzipien)
  - Lens-Soul-Pattern für minimalist: kein primärer Agent, expliziter sekundärer Charakter für alle Agenten in Geeignet-für-Sektion dokumentiert
  - Success Metrics bei minimalist konkret und messbar formuliert ("braucht keine Dokumentation", "drei Iterationen weniger", "Kollege versteht ohne Einführung")
observability_surfaces:
  - bash scripts/verify-s02.sh — Soul-Block (60 Checks) vollständig grün; Fehleranzahl 120 (nur noch Identity-Fehler für T04+T05)
duration: ~30min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T03: 4 Souls schreiben — operator, analyst, creator, minimalist

**4 nuancierte Soul-Archetypes mit klaren Abgrenzungen geschrieben — verify-s02.sh sinkt von 148 auf 120 Fehler (−28); Soul-Block vollständig grün (60/60).**

## What Happened

Alle 4 Soul-Dateien mit je 6 Sektionen geschrieben. Die kritischen Abgrenzungen wurden als erste Priorität behandelt:

**operator.md**: Weltbild "navigiert und erhält laufende Systeme". Stabilitätsfokus explizit gegen execution abgegrenzt (Execution = Ergebnisse unter Druck; Operator = Chaos vermeiden als Grundprinzip). Primäre Agenten Sulu (Operator Agent) und Uhura (Library Manager) zugeordnet.

**analyst.md**: Kernabgrenzung zu researcher in der Philosophie-Sektion: "Die Kernfrage des Analysts lautet nicht 'Was ist wahr?' (das ist die Frage des Researchers), sondern 'Was bedeutet das?'" — Die Arbeit des Analysts beginnt, wo die des Researchers endet. Primäre Agenten Seven (Analysis Agent) und Troi (System Analyzer).

**creator.md**: Kernabgrenzung zu builder in der Philosophie-Sektion: "Ein Builder konstruiert mit bekannten Materialien nach verstandenen Prinzipien. Ein Creator erschafft neue Entitäten: neue Konzepte, neue Formate, neue Frameworks." Beide Ausprägungen (Data = präzise; Q = spielerisch provokativ) als gültig markiert.

**minimalist.md**: Als Lens-Soul implementiert. Philosophie erklärt explizit warum kein primärer Agent diesen Soul alleine trägt. Success Metrics konkret: "Die Lösung braucht keine Dokumentation, weil sie sich selbst erklärt", "Kollege versteht das Ergebnis ohne Einführungsgespräch", "Drei Iterationen weniger als ursprünglich geplant".

## Verification

```
bash scripts/verify-s02.sh
→ Soul-Block [2/3]: alle 60 Soul-Sektions-Checks ✓ (grün)
→ 120 Fehler verbleiben (nur noch Identity-Fehler für T04+T05)

grep -c "^## " soul/operator.md soul/analyst.md soul/creator.md soul/minimalist.md
→ operator.md:6 / analyst.md:6 / creator.md:6 / minimalist.md:6 ✓

grep "Was bedeutet" soul/analyst.md
→ 2 Treffer (Philosophie + Geeignet-für-Sektion) ✓

grep "Lens-Soul\|sekundärer Soul\|kein primärer" soul/minimalist.md
→ 3 Treffer ✓

grep "## Geeignet für" soul/*.md | wc -l
→ 10 (alle 10 Souls haben die Sektion) ✓
```

## Diagnostics

`bash scripts/verify-s02.sh` — Soul-Block [2/3] vollständig grün. Fortschrittsindikator: 198→183→148→120. Verbleibende 120 Fehler sind ausschließlich Identity-Fehler (15 fehlende identity/*.md Dateien × 7 Sektionen = 105, plus 15 Datei-Existenz-Fehler).

## Deviations

none

## Known Issues

none

## Files Created/Modified

- `soul/operator.md` — Weltbild "Erhält laufende Systeme", Sulu + Uhura, explizite execution-Abgrenzung
- `soul/analyst.md` — Weltbild "Was bedeutet das?", Seven + Troi, explizite researcher-Abgrenzung
- `soul/creator.md` — Weltbild "Erschafft Neues", Data + Q, explizite builder-Abgrenzung
- `soul/minimalist.md` — Lens-Soul, kein primärer Agent, konkrete Success Metrics
