---
phase: 1
slug: generators-router
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-03-14
---

# Phase 1 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Manual — reines Markdown-Projekt ohne ausführbaren Code |
| **Config file** | none |
| **Quick run command** | Manuelle Checkliste: Safeguard-Quartet + 9 Sektionen + D006 |
| **Full suite command** | Manuelle Vollprüfung aller 4 Skill-Dateien gegen Templates + Querverweise |
| **Estimated runtime** | ~5 minutes (manual review) |

---

## Sampling Rate

- **After every task commit:** Manuelle Checkliste: 4 Safeguards vorhanden? 9 Sektionen vorhanden? D006-Konformität?
- **After every plan wave:** Alle Skills vollständig + Querverweise geprüft (Router referenziert alle Generatoren)
- **Before `/gsd:verify-work`:** Smoke-Test — jeden Skill mit Beispiel-Anforderung aufrufen, Output gegen Template validieren
- **Max feedback latency:** ~5 minutes per skill

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 1-01-01 | 01 | 1 | META-01 | manual | Prüfe: Soul hat 6 Sektionen, keine [PFLICHTFELD]-Marker, Philosophie ≠ Aufgabenbeschreibung | N/A | ⬜ pending |
| 1-01-02 | 01 | 1 | SAFE-01 | manual | Prüfe: Max-Limit "Max. 1" in Einschränkungen mit expliziter Zahl | N/A | ⬜ pending |
| 1-01-03 | 01 | 1 | SAFE-02 | manual | Prüfe: Ausführungsschritt mit "warte auf" + Bestätigungs-Keyword | N/A | ⬜ pending |
| 1-01-04 | 01 | 1 | SAFE-03 | manual | Prüfe: Zwei Stop-Bedingungen (regulär + vorzeitig) | N/A | ⬜ pending |
| 1-01-05 | 01 | 1 | SAFE-04 | manual | Prüfe: Rollback als Operator-Anweisung formuliert | N/A | ⬜ pending |
| 1-02-01 | 02 | 1 | META-02 | manual | Prüfe: Identity hat 7 Sektionen, Charakter-Beschreibung ohne Aufgaben-Verben | N/A | ⬜ pending |
| 1-02-02 | 02 | 1 | SAFE-01..04 | manual | Prüfe: Vollständiges Safeguard-Quartet wie Soul-Generator | N/A | ⬜ pending |
| 1-03-01 | 03 | 1 | META-03 | manual | Prüfe: Agent hat 7 Sektionen, Soul-/Skill-Querverweise valide | N/A | ⬜ pending |
| 1-03-02 | 03 | 1 | SAFE-01..04 | manual | Prüfe: Vollständiges Safeguard-Quartet + Querverweisvalidierung in Ausführungsschritten | N/A | ⬜ pending |
| 1-04-01 | 04 | 2 | META-08 | manual | Prüfe: Routing-Tabelle vollständig, Mehrdeutigkeits-/Unbekannt-Handling dokumentiert | N/A | ⬜ pending |
| 1-04-02 | 04 | 2 | SAFE-01..04 | manual | Prüfe: Max-Limit "Max. 5", Approval-Gate bei Mehrdeutigkeit, Stop + Rollback | N/A | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

*Existing infrastructure covers all phase requirements. No test framework setup needed — pure Markdown project with manual checklist verification.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Soul-Generator Output im 6-Sektionen-Format | META-01 | Kein Code — Markdown-Authoring | Skill aufrufen, Output gegen soul-template.md prüfen |
| Identity-Generator keine Aufgaben-Verben | META-02 | Semantische Prüfung | Charakter-Beschreibung lesen, auf "analysiert/erstellt/plant" scannen |
| Agent-Generator Querverweise valide | META-03 | Querverweisvalidierung | Prüfen ob referenzierte Souls/Skills im Ökosystem existieren |
| Router Mehrdeutigkeits-Handling | META-08 | Routing-Logik-Verifikation | Mehrdeutige Anfrage senden, prüfen ob 2-3 Kandidaten gelistet werden |
| Safeguard-Quartet vollständig | SAFE-01..04 | Pattern-Matching auf Markdown | Einschränkungen-Block jedes Skills gegen Gold-Standard prüfen |

*All phase behaviors require manual verification — pure Markdown project.*

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 300s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
