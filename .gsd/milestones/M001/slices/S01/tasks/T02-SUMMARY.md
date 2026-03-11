---
id: T02
parent: S01
milestone: M001
provides:
  - templates/skill-template.md — zweistufiges Template (Anweisungs-Block + vollständiges /elvis-x-growth Beispiel) mit allen 9 Sektionen
key_files:
  - templates/skill-template.md
key_decisions:
  - Zweistufige Struktur: Anweisungs-Block mit HTML-Kommentaren oben, Beispiel-Skill unten — klar getrennt durch visuelle Trennlinie + Kommentar-Marker
  - Beispiel-Skill /elvis-x-growth (X/Twitter Growth Analysis) demonstriert D006-Konformität mit konkreten Mengen (30 Posts, Top-10, 7 Tage), Zeitangaben (5 Minuten, 10 Minuten) und Formaten (Markdown-Bericht, 4 Abschnitte, 5-Spalten-Tabelle)
patterns_established:
  - Template-Kommentare enthalten: Was gehört in die Sektion + Pflicht-Format + häufiger Fehler — minimiert Autoren-Fehler bei S04–S07
  - "[PFLICHTFELD]" Marker bei Name, Beschreibung, Ausführungsschritte, Verifikation, Output — maschinell auswertbar durch elvis-skill-generator in S07
observability_surfaces:
  - grep "^## " templates/skill-template.md — listet alle 9 Sektions-Header
  - bash scripts/verify-s01.sh — Check [3/7] prüft alle 9 Header und läuft jetzt durch (✓)
duration: ~20min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T02: Skill-Template mit vollständigem Beispiel schreiben

**`templates/skill-template.md` erstellt: zweistufiges Template mit allen 9 Sektionen und vollständig ausgearbeitetem Beispiel-Skill `/elvis-x-growth`.**

## What Happened

`templates/skill-template.md` wurde als einzige Datei dieses Tasks geschrieben. Die Datei hat zwei klar getrennte Teile:

**Teil 1 — Anweisungs-Block:** Jede der 9 Sektionen enthält einen HTML-Kommentar mit drei Informationen: (1) ob Pflichtfeld, (2) erwartetes Format und Inhalt, (3) häufiger Fehler. `[PFLICHTFELD]` ist bei Name, Beschreibung, Ausführungsschritte, Verifikation und Output gesetzt.

**Visuelle Trennlinie:** `---` + Kommentar `<!-- BEISPIEL BEGINS BELOW — KEIN TEMPLATE-INHALT -->` trennt die beiden Teile eindeutig.

**Teil 2 — Beispiel-Skill `/elvis-x-growth`:** Vollständig ausgearbeiteter X/Twitter Growth Analysis Skill. Ausführungsschritte erfüllen D006: spezifische Mengen ("letzten 30 Posts", "Top-10", "3 stärksten Muster"), Zeitangaben ("letzten 30 Kalendertage", "innerhalb von 5 Minuten", "7 Tage"), konkrete Formate ("Markdown-Format mit 4 Abschnitten", "Top-10-Tabelle mit 5 Spalten", "max. 800 Wörter"). Verifikation enthält sowohl Erfolgs- als auch Failure-Kriterien.

## Verification

```
bash scripts/verify-s01.sh
```

Check [3/7] (`skill-template.md — 9 Sektions-Header`) läuft vollständig durch — alle 9 Header grün:
- ✓ ## Name
- ✓ ## Beschreibung
- ✓ ## Ziele
- ✓ ## Strategie
- ✓ ## Einschränkungen
- ✓ ## Ausführungsschritte
- ✓ ## Verifikation
- ✓ ## Abhängigkeiten
- ✓ ## Output

Manueller Check `## Ausführungsschritte` im Beispiel: Schritt 1 enthält "30 Posts" + "letzten 30 Kalendertage"; Schritt 3 enthält "innerhalb von 5 Minuten"; Schritt 5 enthält "nächsten 7 Tage". ✓

Restliche Fehler im verify-Skript (checks 2/4/5/6/7) sind erwartungsgemäß — werden in T03/T04 behoben.

## Diagnostics

- `grep "^## " templates/skill-template.md` — listet alle 9 Sektions-Header (Template-Teil) + alle 9 Sektions-Header (Beispiel-Teil), also 18 Zeilen gesamt — Normal für zweistufige Struktur
- `bash scripts/verify-s01.sh` — Check [3/7] zeigt den Status aller 9 Template-Header; `grep -q` findet beide Vorkommen (Template + Beispiel), Check ist robust
- `grep "\[PFLICHTFELD\]" templates/skill-template.md` — listet alle 5 Pflichtfeld-Marker

## Deviations

Keine. Template exakt nach Plan in 4 Schritten erstellt.

## Known Issues

Keine.

## Files Created/Modified

- `templates/skill-template.md` — zweistufiges Template: Anweisungs-Block mit HTML-Kommentaren (9 Sektionen, 5 Pflichtfelder) + vollständiges Beispiel `/elvis-x-growth` mit konkreten D006-konformen Ausführungsschritten
