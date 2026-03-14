---
phase: 3
slug: command-layer
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-03-14
---

# Phase 3 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Manual — reines Markdown-Projekt ohne ausführbaren Code |
| **Config file** | none |
| **Quick run command** | Manuelle Prüfung: 5-Felder-Format + keine Ausführungslogik |
| **Full suite command** | Alle 10 Command-Dateien + Router-Tabelle gegen Requirements prüfen |
| **Estimated runtime** | ~5 minutes (manual review) |

---

## Sampling Rate

- **After every task commit:** Prüfe: Datei hat max 5 Felder, keine Ausführungsschritte, korrekte Agent/Skill-Zuordnung
- **After every plan wave:** Alle Commands + Router-Tabelle auf Konsistenz prüfen
- **Before `/gsd:verify-work`:** Jeden Command manuell aufrufen, prüfen ob Route korrekt ist
- **Max feedback latency:** ~3 minutes

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 3-01-01 | 01 | 1 | CMD-01..10 | manual | Prüfe: 10 Dateien in commands/, je max 5 Felder, keine Logik | N/A | ⬜ pending |
| 3-02-01 | 02 | 1 | Router-Update | manual | Prüfe: Routing-Tabelle hat 12+ Einträge, alle Phase-2-Skills enthalten | N/A | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

*Existing infrastructure covers all phase requirements. No test framework setup needed — pure Markdown project.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Commands enthalten keine Logik | CMD-01..10 | Semantische Prüfung | Jede Command-Datei öffnen: keine Ausführungsschritte, keine Verifikation, keine Safeguards |
| Routing-Zuordnungen korrekt | CMD-01..10 | Referenz-Prüfung | Agent + Skill-Chain gegen REQUIREMENTS.md matchen |
| Router-Tabelle vollständig | Router-Update | Vollständigkeits-Check | Tabelle hat alle 12 Skills, keine Duplikate |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 300s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
