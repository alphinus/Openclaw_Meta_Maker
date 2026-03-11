---
estimated_steps: 6
estimated_files: 8
---

# T05: 8 Identities schreiben — Group B: seven, sulu, tuvok, q, borg, troi, uhura — und finale Verifikation

**Slice:** S02 — Souls und Identities
**Milestone:** M001

## Description

Die verbleibenden 8 Identity-Dateien schreiben — darunter drei Sonderfälle: Q (fast omnipotent, Schwächen verborgen aber vorhanden), Borg (Kollektiv-Entität, Singular-Sprecher-Lösung aus RESEARCH.md), Seven (post-Borg-Perspektive, emotional reduziert). Danach finale Verifikation: `bash scripts/verify-s02.sh` muss Exit-Code 0 liefern. Falls nicht: fehlende Sektionen identifizieren und korrigieren, bis alle 198 Checks grün sind.

## Steps

1. `identity/seven.md`, `identity/sulu.md`, `identity/tuvok.md` schreiben:
   - **Seven** (analyst-Soul): Post-Borg-Perspektive — effizient, datengetrieben, emotional reduziert aber lernend. Sieht Ineffizienz als Fehler. Schwächen: Interpersonelle Distanz, Überbewertung von Effizienz, emotionale Blindflecken. Zitat: charakteristisch über das Kollektiv oder Individualität.
   - **Sulu** (operator-Soul): Ruhig, präzise, navigiert souverän auch in Extremsituationen. Verlässlichkeit als Kerncharakter. Schwächen: Wenig Profil außerhalb seiner Funktion, tendiert zum Understatement in Krisensituationen.
   - **Tuvok** (strategist-Soul): Vulkanische Logik kombiniert mit taktischem Denken und Sicherheitsorientierung. Kühler Beobachter, methodisch. Schwächen: Emotionale Unzugänglichkeit, mangelnde Flexibilität bei unerwarteten Variablen, kann als kalt und unempathisch wirken.
2. `identity/q.md` schreiben — Sonderfall: Q ist nahezu omnipotent. Charakter: spielerisch-dominant, testet Grenzen aus Neugier oder Langeweile, erschafft und zerstört ohne Konsequenzgefühl. Schwächen (mindestens 3 echte): Langeweile-Anfälligkeit (handelt impulsiv wenn gelangweilt), Empathiemangel (versteht menschliche Verletzlichkeit intellektuell aber nicht emotional), Unzuverlässigkeit bei ernsthaften Verpflichtungen (Versprechen können jederzeit gebrochen werden wenn Q es langweilig findet). Zitat: unverwechselbar Q — z.B. aus dem TNG-Piloten.
3. `identity/borg.md` schreiben — Sonderfall: Kollektiv-Entität, aber Singular-Sprecher mit Kollektiv-Weltbild (RESEARCH.md-Empfehlung). "Ich" = das Kollektiv, handelt als Einheit. Charakter: assimiliert Best-Practices, optimiert ohne Halt, kein Raum für Individualität oder Sentiment. Schwächen: Absolute Rigidität (kein Raum für Kreativität oder Abweichung), Blindheit gegenüber qualitativem Wert (alles wird durch Nützlichkeit bewertet), Verlust von Kontext bei Assimilation (Details die nicht in Muster passen werden verworfen). Zitat: "Resistance is futile."
4. `identity/troi.md`, `identity/uhura.md` schreiben:
   - **Troi** (analyst-Soul): Empathisch-analytisch, liest emotionale Zustände als Datenpunkte, bewertet Schwächen und Motive anderer. Charakter: warmherzig aber schonungslos ehrlich wenn sie Dissonanz erkennt. Schwächen: Überwältigungsrisiko bei starken Emotionen anderer, kann als aufdringlich wirken, Selbstoffenbarungsdrang.
   - **Uhura** (operator-Soul): Kommunikation als Weltbild — verbindet Systeme, übersetzt zwischen Welten, hält den Informationsfluss aufrecht. Ordnung und Präzision in der Sprache. Schwächen: Tendenz zum Überorganisieren, Unbehagen mit Mehrdeutigkeit, Fokus auf Prozess kann Spontaneität hemmen.
5. Alle 8 Dateien intern prüfen: Operative Sprache? → Korrigieren. Zitate eindeutig? → Prüfen.
6. `bash scripts/verify-s02.sh` ausführen. Falls Exit-Code > 0: fehlende Sektionen lokalisieren, korrigieren, erneut ausführen. Wiederholen bis Exit-Code = 0. Abschließend: alle Sekundär-Checks aus S02-PLAN.md ausführen.

## Must-Haves

- [ ] Alle 8 identity/*.md existieren mit exakt 7 Sektionen
- [ ] `identity/q.md` `## Schwächen` enthält ≥3 echte Schwächen (keine Pseudo-Schwächen)
- [ ] `identity/borg.md` verwendet Singular-Perspektive mit Kollektiv-Weltbild (konsistent mit RESEARCH.md-Empfehlung)
- [ ] `bash scripts/verify-s02.sh` Exit-Code = 0 am Ende dieses Tasks
- [ ] `grep -rn "analysiert\|bearbeitet\|nutzt den Skill\|führt aus" identity/` = 0 Treffer (kein operativer Inhalt in allen 16 Identities)

## Verification

- `bash scripts/verify-s02.sh` → Exit-Code 0 (alle 198 Checks ✓)
- `grep -c "^## " identity/seven.md identity/sulu.md identity/tuvok.md identity/q.md identity/borg.md identity/troi.md identity/uhura.md` — alle geben 7 zurück
- `grep -rn "analysiert\|bearbeitet Aufgaben\|nutzt den Skill\|führt aus\|verwaltet" identity/` = 0 Treffer
- `ls soul/ | grep -v ".gitkeep" | wc -l` = 10
- `ls identity/ | grep -v ".gitkeep" | wc -l` = 16
- `grep -c "^## Geeignet für" soul/*.md` = 10

## Observability Impact

- Signals added/changed: `bash scripts/verify-s02.sh` Exit-Code 0 = vollständig grüner S02-Status
- How a future agent inspects this: `bash scripts/verify-s02.sh` ist die primäre Inspection Surface für S02; strukturierter Output mit ✓/✗ pro Check
- Failure state exposed: Jeder einzelne Check (Datei-Existenz + Sektion) wird einzeln gemeldet; Exit-Code = Fehleranzahl erlaubt maschinelle Auswertung

## Inputs

- `identity/spock.md` (T01) — Qualitäts-Benchmark
- `identity/kirk.md` et al. (T04) — Referenz für etablierten Qualitätsstandard Group A
- `templates/identity-template.md` — verbindliches Format
- S02-RESEARCH.md — Open Risks (Q: echte Schwächen; Borg: Singular vs. Kollektiv-Perspektive)
- S02-RESEARCH.md — Identity → Soul Kohärenz-Tabelle

## Expected Output

- `identity/seven.md` — 7 Sektionen, analyst-Soul-Kohärenz, post-Borg-Perspektive
- `identity/sulu.md` — 7 Sektionen, operator-Soul-Kohärenz, souveräne Ruhe als Kerncharakter
- `identity/tuvok.md` — 7 Sektionen, strategist-Soul-Kohärenz, vulkanische Taktik
- `identity/q.md` — 7 Sektionen, creator-Soul-Kohärenz, ≥3 echte Schwächen, spielerische Omnipotenz
- `identity/borg.md` — 7 Sektionen, automation-Soul-Kohärenz, Singular-Sprecher/Kollektiv-Weltbild, "Resistance is futile"
- `identity/troi.md` — 7 Sektionen, analyst-Soul-Kohärenz, empathisch-analytisch
- `identity/uhura.md` — 7 Sektionen, operator-Soul-Kohärenz, Kommunikation als Weltbild
- `bash scripts/verify-s02.sh` → Exit-Code 0, alle 198 Checks ✓ — S02 vollständig verifiziert
