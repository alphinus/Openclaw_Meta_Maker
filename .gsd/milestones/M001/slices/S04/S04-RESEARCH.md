# S04 Research — Growth + Content Skills (~30 Skills)

**Slice:** S04
**Milestone:** M001
**Datum:** 2026-03-11
**Status:** Research abgeschlossen — bereit zur Planung

---

## 1. Scope und Ziele

S04 produziert die beiden größten Skill-Kategorien des Ökosystems:

- **~15 Growth Skills** in `skills/growth/` — X/Twitter-Wachstumsstrategien, Analytics, Zielgruppenaufbau
- **~15 Content Skills** in `skills/content/` — X-Posts, Threads, Copywriting, Content-Planung

**Bereits aus S01 vorhanden (dürfen nicht dupliziert werden):**
- `skills/growth/elvis-growth-audit.md`
- `skills/content/elvis-x-hook-writer.md`

S04 muss also **~14 Growth Skills** und **~14 Content Skills** neu erstellen — insgesamt 28 neue Dateien.

---

## 2. Requirement Coverage

| Requirement | Relevanz für S04 | Status |
|-------------|-----------------|--------|
| R001 — ~100 Skills | S04 liefert ~28 der ~60 Nicht-Meta/Automation-Skills | primary owner |
| R002 — Erweitertes Skill-Format | Alle 28 Skills müssen alle 9 Sektionen haben | bindend |
| R003 — Konkrete Execution Steps | D006-Konformität: Mengen, Formate, Zeitangaben in jedem Step | primary owner |
| R006 — /elvis-* Prefix | Alle Skills im `## Name`-Block | bindend |
| R011 — Deutsch | Alle Inhalte auf Deutsch | bindend |

**R003 ist der kritische Qualitäts-Proof für S04** — die Benchmark-Skills aus S01 (`elvis-growth-audit.md`, `elvis-x-hook-writer.md`) definieren den Qualitäts-Mindeststandard. Kein S04-Skill darf abstrakter sein.

---

## 3. Technologien / Externe Abhängigkeiten

**Keine.** S04 ist reine Markdown-Generierung — kein Code, keine APIs, keine Bibliotheken.

Skill-Discover-Suche nicht erforderlich: Keine Frameworks oder Laufzeit-Technologien involviert.

---

## 4. Analyse der Benchmark-Skills (Qualitäts-Benchmark)

### elvis-growth-audit.md (Growth-Benchmark)

Qualitäts-Merkmale die alle Growth-Skills erfüllen müssen:
- **Mengen**: "Top-20 Posts", "die letzten 14 Kalendertage", "10 Hypothesen", "5 Muster"
- **Format**: "Markdown-Report mit 5 Abschnitten", "Tabelle mit 5 Spalten"
- **Formate für Hypothesen**: "Wenn…dann…weil…"-Format
- **Failure-Indikator** explizit: "< 5 Posts → Skill bricht ab mit Meldung"
- **Akzeptanzkriterium**: klar messbar ("genau 5 Muster und genau 10 Hypothesen")
- **Einschränkungen**: harte Zahlen ("Max. 20 Posts"), keine weichen Formulierungen

### elvis-x-hook-writer.md (Content-Benchmark)

Qualitäts-Merkmale die alle Content-Skills erfüllen müssen:
- **Mengen**: "genau 5 Varianten", "max. 280 Zeichen", "min. 80 Zeichen", "max. 2 Hashtags"
- **Schritt-Granularität**: jeder Schritt erzeugt genau ein abgrenzbares Artefakt
- **Selbst-Verifikation**: "Zeichenanzahl für jede Variante dokumentiert" direkt im Schritt-Format
- **Hook-Typen explizit benannt** — kein Interpretationsspielraum
- **Empfehlung begründet**: "in max. 3 Sätzen, basierend auf Hook-Typ, Thema-Typ, Tonfall"

---

## 5. Vollständige Skill-Listen für S04

### 5.1 Growth Skills (14 neu + 1 aus S01 = 15 total)

| # | Dateiname | Skill-Name | Kurzbeschreibung |
|---|-----------|-----------|-----------------|
| 1 | `elvis-growth-audit.md` | `/elvis-growth-audit` | ✅ Aus S01 — Benchmark |
| 2 | `elvis-x-trend-scanner.md` | `/elvis-x-trend-scanner` | Scannt aktuelle Trends in einer Nische auf X/Twitter — die Top-10 Trend-Themen der letzten 48 Stunden mit Relevanz-Score |
| 3 | `elvis-audience-builder.md` | `/elvis-audience-builder` | Definiert die Zielgruppe in 5 Dimensionen und identifiziert 10 Accounts die diese Zielgruppe bereits erreichen |
| 4 | `elvis-competitor-analysis.md` | `/elvis-competitor-analysis` | Analysiert 5 Konkurrenz-Accounts: Posting-Frequenz, Content-Mix, Top-Posts, Follower-Wachstum pro Woche |
| 5 | `elvis-posting-schedule.md` | `/elvis-posting-schedule` | Erstellt einen 4-Wochen-Posting-Plan mit optimalen Uhrzeiten, Content-Typen und Themen-Rotation |
| 6 | `elvis-profile-optimizer.md` | `/elvis-profile-optimizer` | Optimiert alle 7 Profil-Elemente (Name, Bio, Profilbild, Header, Pinned Post, Location, Website) nach einem 20-Punkte-Scoring |
| 7 | `elvis-viral-formula.md` | `/elvis-viral-formula` | Identifiziert die 3 häufigsten Viral-Muster aus den Top-5-Posts der letzten 30 Tage und erstellt eine Replikations-Vorlage |
| 8 | `elvis-engagement-booster.md` | `/elvis-engagement-booster` | Definiert 5 tägliche Engagement-Aktionen (Kommentare, Reposts, Replies) mit Zeitbudget max. 20 Min/Tag |
| 9 | `elvis-follower-analysis.md` | `/elvis-follower-analysis` | Analysiert die 50 aktivsten Follower: wer sie sind, was sie teilen, welche Themen sie engagieren |
| 10 | `elvis-niche-finder.md` | `/elvis-niche-finder` | Bewertet 5 potenzielle Nischen nach 4 Kriterien (Größe, Wettbewerb, Monetarisierbarkeit, Expertise-Fit) mit Scoring 1–5 |
| 11 | `elvis-collab-strategy.md` | `/elvis-collab-strategy` | Identifiziert 10 Kollaborations-Partner und erstellt 3 Kollaborations-Formate mit konkretem Outreach-Skript |
| 12 | `elvis-monetization-planner.md` | `/elvis-monetization-planner` | Bewertet 5 Monetarisierungs-Wege nach Aufwand und Ertragspotenzial und erstellt einen 90-Tage-Monetarisierungs-Plan |
| 13 | `elvis-growth-sprint.md` | `/elvis-growth-sprint` | 7-Tage-Intensivplan mit täglichen Aktionen, Zeitbudget und erwarteten Metriken pro Tag |
| 14 | `elvis-growth-loop.md` | `/elvis-growth-loop` | Definiert einen wiederkehrenden 7-Tage-Wachstumszyklus (Analyse → Produktion → Distribution → Optimierung) |
| 15 | `elvis-x-analytics.md` | `/elvis-x-analytics` | Wertet 90-Tage-Analytics aus: Follower-Wachstumskurve, beste Wochen, Engagement-Entwicklung, Top-Content-Kategorien |

### 5.2 Content Skills (14 neu + 1 aus S01 = 15 total)

| # | Dateiname | Skill-Name | Kurzbeschreibung |
|---|-----------|-----------|-----------------|
| 1 | `elvis-x-hook-writer.md` | `/elvis-x-hook-writer` | ✅ Aus S01 — Benchmark |
| 2 | `elvis-x-thread-writer.md` | `/elvis-x-thread-writer` | Schreibt einen X-Thread mit 8–12 Tweets zu einem Thema — jeder Tweet maximal 280 Zeichen, mit Hook, Entwicklung und CTA |
| 3 | `elvis-content-calendar.md` | `/elvis-content-calendar` | Erstellt einen 30-Tage-Content-Kalender mit 30 Post-Ideen, Content-Typen und Themen-Rotation in 5 Kategorien |
| 4 | `elvis-copywriting.md` | `/elvis-copywriting` | Schreibt verkaufsfördernden Text für 3 Formate (Produkt-Post, Angebot-Tweet, DM-Pitch) nach dem PAS-Prinzip |
| 5 | `elvis-content-repurpose.md` | `/elvis-content-repurpose` | Wandelt einen Langform-Inhalt (Artikel/Video) in 5 X-Posts und einen Thread um |
| 6 | `elvis-story-writer.md` | `/elvis-story-writer` | Schreibt eine Personal-Story nach dem 3-Akt-Prinzip (Problem → Wendepunkt → Lösung) in maximal 280 Zeichen pro Teil |
| 7 | `elvis-bio-writer.md` | `/elvis-bio-writer` | Generiert 3 Bio-Varianten (sachlich, provokativ, storytelling) für das X-Profil — max. 160 Zeichen je Variante |
| 8 | `elvis-cta-writer.md` | `/elvis-cta-writer` | Schreibt 5 Call-to-Action-Varianten für einen Post — Follow, Repost, Kommentar, Link-Klick, DM-Aktion |
| 9 | `elvis-opinion-post.md` | `/elvis-opinion-post` | Erstellt einen klaren Meinungsbeitrag (Stance → Begründung → Konsequenz) mit 2 Gegenargumenten und Widerlegung |
| 10 | `elvis-how-to-writer.md` | `/elvis-how-to-writer` | Schreibt eine How-To-Anleitung als X-Thread oder Single-Post mit maximal 5 konkreten Schritten |
| 11 | `elvis-content-ideas.md` | `/elvis-content-ideas` | Generiert 20 Content-Ideen zu einem Thema in 4 Kategorien (Bildung, Unterhaltung, Inspiration, Konversion) |
| 12 | `elvis-headline-writer.md` | `/elvis-headline-writer` | Schreibt 7 Headline-Varianten für denselben Inhalt — je eine pro Formel (Zahl, Frage, How-To, Secret, Warning, Result, Contrast) |
| 13 | `elvis-reply-writer.md` | `/elvis-reply-writer` | Schreibt 5 strategische Antworten auf einen viralen Post — jede mit unterschiedlichem Ziel (Sichtbarkeit, Expertise, Netzwerk, Humor, CTA) |
| 14 | `elvis-dm-writer.md` | `/elvis-dm-writer` | Schreibt eine Cold-DM-Sequenz: Opener, Mehrwert-Nachricht und Follow-Up — zusammen max. 3 Nachrichten, je max. 150 Zeichen |
| 15 | `elvis-content-brief.md` | `/elvis-content-brief` | Erstellt ein vollständiges Content-Brief für einen Post oder Thread: Ziel, Zielgruppe, Kernbotschaft, Format, Tonfall, CTA |

---

## 6. Abhängigkeits-Kette (Skill-zu-Skill)

Abhängigkeiten sind für die `## Abhängigkeiten`-Sektion jedes Skills relevant. Identifizierte natürliche Ketten:

**Growth-Kette (typischer Workflow):**
```
elvis-niche-finder → elvis-audience-builder → elvis-competitor-analysis
                                            ↓
                         elvis-profile-optimizer → elvis-posting-schedule
                                                              ↓
                                            elvis-growth-sprint → elvis-growth-loop
                                                          ↓
                                              elvis-growth-audit → elvis-x-analytics
```

**Content-Kette (typischer Workflow):**
```
elvis-content-ideas → elvis-content-brief → elvis-x-hook-writer
                                          → elvis-x-thread-writer
                                          → elvis-story-writer
                                          → elvis-how-to-writer
                                          → elvis-opinion-post
                                                    ↓
                                      elvis-content-calendar (plant alle obigen)
                                                    ↓
                                      elvis-content-repurpose (verwertet Output)
```

**Cross-Kategorie (Growth → Content):**
- `elvis-growth-audit` → `elvis-x-hook-writer` (Muster als Briefing)
- `elvis-x-trend-scanner` → `elvis-content-ideas` (Trends als Content-Input)
- `elvis-viral-formula` → `elvis-x-thread-writer` (Formel anwenden)
- `elvis-audience-builder` → `elvis-content-brief` (Zielgruppe als Briefing)

**Alle Skills müssen tatsächlich existierende Skills in `## Abhängigkeiten` referenzieren** — keine Phantomreferenzen. Cross-Referenzen auf S05-Skills (Research/Strategy) sind in S04 noch nicht erlaubt, da S05 noch nicht abgeschlossen ist. Ausnahme: `elvis-execution-plan` und `elvis-market-scan` existieren bereits aus S01.

---

## 7. Risiken und Entscheidungen

### Risiko 1: Skill-Überlappung (mittel)
**Problem:** Zwischen `elvis-x-hook-writer` (S01) und `elvis-headline-writer` (S04) besteht inhaltliche Ähnlichkeit.  
**Lösung:** Klare Abgrenzung durch Scope: `elvis-x-hook-writer` = Tweet-Varianten (fertige Posts, verschiedene Strukturen), `elvis-headline-writer` = Headline-Formeln für denselben Inhalt (copywriting-fokussiert, nicht X-spezifisch). Beide haben distinkte `## Strategie`-Sektionen die die Abgrenzung explizit machen.

### Risiko 2: Konkretheitsgrad (mittel, per ROADMAP identifiziert)
**Problem:** Growth-Skills neigen zu abstrakten Schritten ("analysiere Trends"), Content-Skills zu generischen Varianten ("schreibe verschiedene Stile").  
**Mitigation:** D006-Pflicht-Checkliste vor Abschluss jedes Skills:
- [ ] Jeder Schritt enthält mindestens eine konkrete Zahl (Anzahl, Zeitraum, Zeichenlimit)
- [ ] Jeder Schritt enthält das erwartete Output-Format (Tabelle, Bullet-List, Markdown-Abschnitt)
- [ ] Failure-Indikator in `## Verifikation` benannt
- [ ] Akzeptanzkriterium messbar formuliert

### Risiko 3: Dateinamen-Konsistenz (niedrig)
**Problem:** S01 hatte Abweichungen zwischen Plan-Dateinamen und verify-Skript-Dateinamen.  
**Mitigation:** Dateinamen in dieser Research-Datei sind autoritativ für S04. Das S04-Verify-Skript wird diese Namen als Stopping-Condition verwenden.

### Risiko 4: Cross-Referenz auf nicht-existierende Skills (niedrig)
**Problem:** `## Abhängigkeiten` könnte auf S05/S06/S07-Skills verweisen die in S04 noch nicht existieren.  
**Regel:** In S04-Skills sind nur folgende Skills als Vorgänger erlaubt:
- Alle anderen S04-Skills (die in dieser Liste aufgeführt sind)
- S01-Skills: `elvis-growth-audit`, `elvis-x-hook-writer`, `elvis-market-scan`, `elvis-execution-plan`, `elvis-workflow-builder`, `elvis-skill-generator`
- Bei keiner echten Abhängigkeit: `"keine (Einstiegs-Skill)"`

---

## 8. Verifikations-Strategie für S04

### Verifikations-Skript: `scripts/verify-s04.sh`

Das S04-Verifikations-Skript soll prüfen:

1. **Datei-Existenz**: Alle 28 neuen Skill-Dateien (14 Growth + 14 Content) vorhanden
2. **Sektions-Vollständigkeit**: Alle 9 Pflicht-Sektionen in jeder der 28 Dateien (252 Checks)
3. **/elvis-* Prefix**: Alle 28 Skills enthalten `/elvis-` im `## Name`-Block
4. **Keine Phantomreferenzen**: Alle in `## Abhängigkeiten` genannten Vorgänger-Skills existieren als Dateien

**Exit-Code:** Fehlerzähler (0 = vollständig grün), konsistent mit D014 und verify-s01.sh.

### Qualitäts-Kriterien (manuell, nicht per Skript prüfbar)
- Jeder `## Ausführungsschritte`-Block hat mindestens 4 konkrete, nummerierte Schritte
- Jeder Schritt enthält mindestens eine Mengenangabe (Zahl, Zeitraum oder Zeichenlimit)
- Jede `## Verifikation`-Sektion benennt einen Failure-Indikator

---

## 9. Strukturüberblick Vorhandene Dateien

```
skills/
├── growth/
│   └── elvis-growth-audit.md          ← S01 Benchmark (vorhanden)
│   [14 neue Skills aus S04-Liste]
└── content/
    └── elvis-x-hook-writer.md         ← S01 Benchmark (vorhanden)
    [14 neue Skills aus S04-Liste]
```

Keine weiteren Dateien in `skills/growth/` oder `skills/content/` vor S04.

---

## 10. Empfohlene Implementierungs-Reihenfolge

**Task-Aufteilung für S04:**

**T01 — Verify-Skript für S04 erstellen** (~15 Min)  
- `scripts/verify-s04.sh` mit 4 Check-Gruppen schreiben
- Initial-Lauf (erwartete ~284 Fehler)

**T02 — Growth Skills 1–7** (~60 Min)  
- `elvis-x-trend-scanner`, `elvis-audience-builder`, `elvis-competitor-analysis`
- `elvis-posting-schedule`, `elvis-profile-optimizer`, `elvis-viral-formula`, `elvis-engagement-booster`
- Aufbauend auf `elvis-growth-audit` als Qualitäts-Benchmark

**T03 — Growth Skills 8–14** (~60 Min)  
- `elvis-follower-analysis`, `elvis-niche-finder`, `elvis-collab-strategy`
- `elvis-monetization-planner`, `elvis-growth-sprint`, `elvis-growth-loop`, `elvis-x-analytics`

**T04 — Content Skills 1–7** (~60 Min)  
- `elvis-x-thread-writer`, `elvis-content-calendar`, `elvis-copywriting`
- `elvis-content-repurpose`, `elvis-story-writer`, `elvis-bio-writer`, `elvis-cta-writer`
- Aufbauend auf `elvis-x-hook-writer` als Qualitäts-Benchmark

**T05 — Content Skills 8–14** (~60 Min)  
- `elvis-opinion-post`, `elvis-how-to-writer`, `elvis-content-ideas`
- `elvis-headline-writer`, `elvis-reply-writer`, `elvis-dm-writer`, `elvis-content-brief`

**T06 — Verifikation** (~20 Min)  
- `bash scripts/verify-s04.sh` → Exit-Code 0
- Manuelle Stichproben-Prüfung auf D006-Konformität (3 Growth + 3 Content)
- S04-SUMMARY.md schreiben

---

## 11. Forward Intelligence für den Planer

- **Keine externen Bibliotheken oder Frameworks** — reine Markdown-Arbeit, kein Code
- **Der kritischste Qualitäts-Risiko** ist D006-Verletzung in Ausführungsschritten — jeder abstrakte Schritt wie "Analysiere die Performance" ohne Mengangabe ist ein Defekt
- **Content-Skills sind tendenziell einfacher** zu konkretisieren (Zeichenzahlen, Varianten-Anzahl), Growth-Skills erfordern mehr Domänenwissen (Engagement-Formeln, Zeitangaben)
- **Die Growth-Kette hat natürliche Abhängigkeiten** — `elvis-niche-finder` kommt zuerst, `elvis-growth-loop` kommt zuletzt; Abhängigkeiten-Sektionen sollten diese Kette abbilden
- **Phantom-Referenzrisiko ist real**: Growth-Skills neigen dazu, Research-Skills zu referenzieren (z.B. "Vorgänger: /elvis-opportunity-finder") — solche S05-Skills existieren in S04 noch nicht und dürfen nicht referenziert werden
- **S04 liefert den Proof für R003** (konkrete Execution Steps) — dies ist die wichtigste Requirements-Validierung in diesem Slice
