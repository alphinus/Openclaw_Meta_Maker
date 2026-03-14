---
phase: 2
slug: composition-autonomous
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-03-14
---

# Phase 2 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Manual — reines Markdown-Projekt ohne ausführbaren Code |
| **Config file** | none |
| **Quick run command** | Manuelle Checkliste: Safeguard-Quartet + 9 Sektionen + D006 |
| **Full suite command** | Manuelle Vollprüfung aller 7 Skill-Dateien gegen Templates + Querverweise |
| **Estimated runtime** | ~10 minutes (manual review) |

---

## Sampling Rate

- **After every task commit:** Manuelle Checkliste: 4 Safeguards vorhanden? 9 Sektionen vorhanden? D006-Konformität?
- **After every plan wave:** Alle Skills vollständig + Querverweise geprüft
- **Before `/gsd:verify-work`:** Smoke-Test — jeden Skill mit Beispiel-Anforderung aufrufen, Output gegen Template validieren
- **Max feedback latency:** ~5 minutes per skill

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 2-01-01 | 01 | 1 | META-04 | manual | Prüfe: Agent-Creator hat Single-Approval, orchestriert Soul+Identity+Agent, <2min Flow | N/A | ⬜ pending |
| 2-01-02 | 01 | 1 | META-05 | manual | Prüfe: Skill-Expander generiert vollständige 9-Sektionen-Varianten, nicht nur Listen | N/A | ⬜ pending |
| 2-01-03 | 01 | 1 | META-12 | manual | Prüfe: Concept-Design liefert Blaupause mit Mission, Soul, Skill-Bedarf | N/A | ⬜ pending |
| 2-02-01 | 02 | 1 | META-06 | manual | Prüfe: System-Analyzer liefert detaillierten Report mit Schweregrad | N/A | ⬜ pending |
| 2-02-02 | 02 | 1 | META-09 | manual | Prüfe: Ecosystem-Health liefert Score 0-100, klar abgegrenzt von Analyzer | N/A | ⬜ pending |
| 2-03-01 | 03 | 2 | META-07 | manual | Prüfe: Library-Manager produziert kategorisierten Katalog | N/A | ⬜ pending |
| 2-03-02 | 03 | 2 | META-10 | manual | Prüfe: Agent-Optimizer identifiziert Schwächen + generiert optimierte Version | N/A | ⬜ pending |
| 2-ALL | ALL | ALL | SAFE-01..04 | manual | Prüfe: Alle 7 Skills haben vollständiges Safeguard-Quartet mit Approval-Gate als Schritt | N/A | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

*Existing infrastructure covers all phase requirements. No test framework setup needed — pure Markdown project with manual checklist verification.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Agent-Creator Single-Approval Flow | META-04 | Workflow-Logik-Prüfung | Ausführungsschritte lesen: genau 1 Approval-Gate nach Konzeptphase? |
| Skill-Expander vollständige Varianten | META-05 | Semantische Prüfung | Output-Beschreibung: 9-Sektionen pro Variante, nicht nur Namensliste? |
| Health vs. Analyzer Abgrenzung | META-06/09 | Scope-Prüfung | Beide Skills vergleichen: Score vs. Report klar getrennt? |
| Safeguard-Quartet in jedem Skill | SAFE-01..04 | Pattern-Matching | Einschränkungen-Block gegen Gold-Standard prüfen |

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
