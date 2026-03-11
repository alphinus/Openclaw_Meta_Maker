# M001: OpenClaw Meta Maker — Context

**Gathered:** 2026-03-11
**Status:** Bereit zur Planung

## Projektbeschreibung

OpenClaw Meta Maker generiert ein vollständiges, modulares Markdown-basiertes Agent-Ökosystem für OpenClaw. Ziel ist eine Agent-Factory: neue Agenten entstehen in unter 2 Minuten durch Kombination von vorgefertigten Souls, Identities, Agents und Skills.

## Warum dieser Milestone

Das gesamte Projekt ist ein einziger Milestone — reine Datei-Generierung ohne Runtime-Code. Der Output sind ~200 Markdown-Dateien die direkt in OpenClaw importiert oder verwendet werden können.

## Nutzer-sichtbares Ergebnis

### Wenn dieser Milestone abgeschlossen ist, kann der Nutzer:
- Alle Dateien direkt in OpenClaw importieren
- Einen neuen Agenten in < 2 Minuten durch Soul + Identity + Agent + 10 Skills zusammenstellen
- Bestehende Skills mit `/elvis-*` Commands aufrufen
- Das Autonomous System über `/build-agent`, `/generate-skills` etc. steuern
- Jede Datei als Vorlage für eigene Erweiterungen nutzen

### Entry Point / Umgebung
- Entry point: Dateisystem — Markdown-Dateien direkt in OpenClaw importieren
- Environment: OpenClaw (beliebige Plattform)
- Live Dependencies: keine

## Agenten-Mapping (Star Trek → Funktion)

| Star Trek Name | Funktion | Begründung |
|---------------|----------|------------|
| **Kirk** | Haupt-Agent (Elvis/Master) | Anführer, entscheidet, handelt |
| **Picard** | Orchestrator | Koordiniert, delegiert, strategisch |
| **Riker** | Growth Agent | Ambitioniert, expansiv |
| **Spock** | Research Agent | Logik, Analyse, Fakten |
| **Worf** | Strategy Agent | Taktik, Planung, Disziplin |
| **Data** | Content Agent | Präzise Produktion, unermüdlich |
| **Scotty** | Automation Agent | Systeme bauen, alles am Laufen halten |
| **LaForge** | Builder Agent | Engineering, konstruiert Lösungen |
| **Seven** | Analysis Agent | Datenverarbeitung, Effizienz |
| **Sulu** | Operator Agent | Steuert, navigiert, ausführend |
| **Tuvok** | System Agent | Sicherheit, Struktur, Logik |
| **McCoy** | Execution Agent | Hands-on, direkt, ergebnisorientiert |
| **Q** | Agent Creator (Meta) | Erschafft neue Entitäten |
| **Borg** | Skill Expander | Assimiliert, erweitert, wächst |
| **Troi** | System Analyzer | Erkennt Schwächen, analysiert Zustand |
| **Uhura** | Library Manager | Kommunikation, Organisation, Ordnung |

## Finales Skill-Format (bindend für alle Skills)

```markdown
# Skill

## Name
/elvis-[skill-name]

## Beschreibung
Kurze Beschreibung des Skills.

## Ziele
- Ziel 1
- Ziel 2
- Ziel 3

## Strategie
Wie der Skill an die Aufgabe herangeht.

## Einschränkungen
- Max. X Elemente pro Durchlauf
- Keine externen API-Aufrufe ohne Operator-Freigabe
- [weitere Sicherheitsgrenzen]

## Ausführungsschritte
1. Konkreter, spezifischer Schritt (nicht abstrakt)
2. Konkreter, spezifischer Schritt
3. Konkreter, spezifischer Schritt

## Verifikation
- Prüfkriterium 1: Was muss im Output vorhanden sein?
- Prüfkriterium 2: Was ist ein Zeichen für schlechten Output?
- Akzeptanzkriterium: Wann gilt der Skill als erfolgreich abgeschlossen?

## Abhängigkeiten
- Input: Was wird benötigt (Daten, vorheriger Skill-Output)?
- Empfohlene Vorgänger-Skills: [/elvis-skill-name oder "keine"]

## Output
Beschreibung des erwarteten Ergebnisses.
```

## Integrierte Ordnerstruktur (bindend)

```
openclaw-meta-maker/
├── soul/                    (10 Souls)
├── identity/                (16 Identities — Star Trek Namen)
├── agent/                   (16 Agent-Definitionen — Star Trek Namen)
├── skills/
│   ├── growth/              (~15 Skills)
│   ├── content/             (~15 Skills)
│   ├── research/            (~15 Skills)
│   ├── strategy/            (~15 Skills)
│   ├── automation/          (~15 Skills)
│   └── meta/                (~15 Skills: Generators + System + Commands)
├── commands/                (Command-Definitionen als Markdown)
└── templates/               (Soul-, Identity-, Agent-, Skill-Templates)
```

## Skill-Kategorien und Deduplizierung

Aus der Spec wurden folgende Duplikate zusammengeführt:
- `elvis-x-hook-writer` + `elvis-hook-writer` → `/elvis-x-hook-writer`
- `elvis-x-thread-writer` + `elvis-thread-writer` → `/elvis-x-thread-writer`
- `elvis-x-trend-scanner` + `elvis-trend-scanner` → `/elvis-x-trend-scanner`
- `elvis-x-audience` + `elvis-audience-builder` → `/elvis-audience-builder`
- `elvis-execution` + `elvis-execution-plan` → `/elvis-execution-plan`

Ziel: ~90-100 einzigartige Skills total.

## Safeguard-Anforderungen für Autonome Agenten

Alle Meta/Autonomous Skills (Borg, Q, Picard, Troi, Uhura) müssen explizit enthalten:
1. **Max-Limit**: Maximal X Aktionen/Generierungen pro Durchlauf (z.B. max. 10 Skills)
2. **Approval-Gate**: Operator muss Ergebnis bestätigen bevor nächster Schritt ausgeführt wird
3. **Stop-Bedingung**: Klare Definition wann der Prozess endet
4. **Rollback-Hinweis**: Was zu tun ist wenn ein Schritt fehlschlägt

## Risiken und Unbekannte

- **Inhaltsqualität** — Skills müssen konkret genug sein für echte Ausführung ohne zu eng zu sein für verschiedene Kontexte
- **Konsistenz über 100 Dateien** — Format-Abweichungen über so viele Dateien möglich → Template in S01 muss robust sein
- **Deutsche Sprache + Fachbegriffe** — Einige OpenClaw-Konzepte haben keine guten deutschen Übersetzungen → Fachbegriffe bleiben englisch (z.B. "Skill", "Soul", "Agent")

## Relevant Requirements

- R001 — ~100 Skills über 6 Domänen
- R002 — Erweitertes Skill-Format (Constraints, Verification, Dependencies)
- R003 — Konkrete Execution Steps
- R004 — Safeguards für autonome Agenten
- R005 — Star Trek Agenten-Namen
- R006 — /elvis-* Naming Convention
- R007 — Integrierte Ordnerstruktur
- R008 — 10 Souls
- R009 — Command System
- R010 — Templates
- R011 — Deutsch

## In Scope

- ~200 Markdown-Dateien: 10 Souls, 16 Identities, 16 Agents, ~90-100 Skills, 10 Commands, 4 Templates, README
- Vollständiger Inhalt für jede Datei (nicht nur Struktur)
- Alle 6 Layer: Starter Kit, Skill Library, Operator Pack, Meta-Agent System, Autonomous System, Command System

## Out of Scope

- Ausführbarer Code jeglicher Art
- API-Verbindungen zu externen Diensten
- Pixel Agents Visualisierung
- Echte Social-Media-Automation
