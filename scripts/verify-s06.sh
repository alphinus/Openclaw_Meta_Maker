#!/usr/bin/env bash
# scripts/verify-s06.sh
# Objektive Stopping-Condition für Slice S06 — Automation + Analysis Skills (~20 Skills)
# Ausführen aus dem Projekt-Root: bash scripts/verify-s06.sh

set -euo pipefail

ERRORS=0
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

pass() { echo "  ✓ $1"; }
fail() { echo "  ✗ $1"; ERRORS=$((ERRORS + 1)); }

echo ""
echo "══════════════════════════════════════════════════════"
echo " S06 Verifikation — Automation + Analysis Skills"
echo "══════════════════════════════════════════════════════"

# ─────────────────────────────────────────────────────────
# CHECK-GRUPPE [1/4] — Datei-Existenz (19 neue Skills)
# ─────────────────────────────────────────────────────────
echo ""
echo "[1/4] Datei-Existenz — 19 neue Skill-Dateien (9 Automation + 10 Analysis)"

AUTOMATION_SKILLS=(
  "skills/automation/elvis-automation-audit.md"
  "skills/automation/elvis-task-automator.md"
  "skills/automation/elvis-content-scheduler.md"
  "skills/automation/elvis-trigger-builder.md"
  "skills/automation/elvis-data-pipeline.md"
  "skills/automation/elvis-integration-mapper.md"
  "skills/automation/elvis-system-optimizer.md"
  "skills/automation/elvis-batch-processor.md"
  "skills/automation/elvis-autopilot-setup.md"
)

ANALYSIS_SKILLS=(
  "skills/analysis/elvis-performance-tracker.md"
  "skills/analysis/elvis-kpi-dashboard.md"
  "skills/analysis/elvis-funnel-analyzer.md"
  "skills/analysis/elvis-content-analyzer.md"
  "skills/analysis/elvis-ab-tester.md"
  "skills/analysis/elvis-reporting-system.md"
  "skills/analysis/elvis-growth-tracker.md"
  "skills/analysis/elvis-conversion-analyzer.md"
  "skills/analysis/elvis-competitor-monitor.md"
  "skills/analysis/elvis-revenue-tracker.md"
)

ALL_S06_SKILLS=("${AUTOMATION_SKILLS[@]}" "${ANALYSIS_SKILLS[@]}")

for skill in "${ALL_S06_SKILLS[@]}"; do
  if [ -f "$ROOT/$skill" ]; then
    pass "$skill"
  else
    fail "$skill — Datei fehlt"
  fi
done

# ─────────────────────────────────────────────────────────
# CHECK-GRUPPE [2/4] — Sektions-Vollständigkeit (19 × 9 = 171 Checks)
# ─────────────────────────────────────────────────────────
echo ""
echo "[2/4] Sektions-Vollständigkeit — 171 Checks (19 Dateien × 9 Pflichtfelder)"

REQUIRED_SECTIONS=(
  "## Name"
  "## Beschreibung"
  "## Ziele"
  "## Strategie"
  "## Einschränkungen"
  "## Ausführungsschritte"
  "## Verifikation"
  "## Abhängigkeiten"
  "## Output"
)

for skill in "${ALL_S06_SKILLS[@]}"; do
  skill_path="$ROOT/$skill"
  skill_name=$(basename "$skill")
  if [ -f "$skill_path" ]; then
    for section in "${REQUIRED_SECTIONS[@]}"; do
      if grep -qF "$section" "$skill_path"; then
        pass "$skill_name: $section"
      else
        fail "$skill_name: $section — Sektion fehlt"
      fi
    done
  else
    for section in "${REQUIRED_SECTIONS[@]}"; do
      fail "$skill_name: $section — Datei fehlt"
    done
  fi
done

# ─────────────────────────────────────────────────────────
# CHECK-GRUPPE [3/4] — /elvis-Prefix im ## Name Block (19 Checks)
# ─────────────────────────────────────────────────────────
echo ""
echo "[3/4] /elvis-* Prefix — 19 Checks (je 1 pro Datei)"

for skill in "${ALL_S06_SKILLS[@]}"; do
  skill_path="$ROOT/$skill"
  skill_name=$(basename "$skill")
  if [ -f "$skill_path" ]; then
    if grep -A5 "^## Name" "$skill_path" | grep -q "/elvis-"; then
      pass "$skill_name: enthält /elvis-* im ## Name Block"
    else
      fail "$skill_name: kein /elvis-* Prefix im ## Name Block gefunden"
    fi
  else
    fail "$skill_name: Datei fehlt — /elvis-* Prüfung übersprungen"
  fi
done

# ─────────────────────────────────────────────────────────
# CHECK-GRUPPE [4/4] — Phantomreferenz-Check
# Alle in ## Abhängigkeiten genannten elvis-[a-z-]+ müssen als .md existieren
# ─────────────────────────────────────────────────────────
echo ""
echo "[4/4] Phantomreferenz-Check — alle referenzierten Skills müssen existieren"

for skill in "${ALL_S06_SKILLS[@]}"; do
  skill_path="$ROOT/$skill"
  skill_name=$(basename "$skill")
  if [ -f "$skill_path" ]; then
    # Abhängigkeiten-Block extrahieren und elvis-[a-z-]+ Referenzen herausfiltern
    deps_block=$(awk '/^## Abhängigkeiten/,/^## /' "$skill_path" | grep -oE 'elvis-[a-z-]+' || true)
    if [ -z "$deps_block" ]; then
      pass "$skill_name: Abhängigkeiten-Block — keine Referenzen (ok)"
    else
      while IFS= read -r dep; do
        # Suche die referenzierte Datei in allen skills/-Unterordnern
        found=0
        for subdir in growth content research strategy automation meta analysis; do
          if [ -f "$ROOT/skills/$subdir/$dep.md" ]; then
            found=1
            break
          fi
        done
        if [ "$found" -eq 1 ]; then
          pass "$skill_name: Abhängigkeit '$dep' existiert als Datei"
        else
          fail "$skill_name: Abhängigkeit '$dep' — Phantomreferenz! Datei nicht gefunden"
        fi
      done <<< "$deps_block"
    fi
  fi
done

# ─────────────────────────────────────────────────────────
# ZUSAMMENFASSUNG
# ─────────────────────────────────────────────────────────
echo ""
echo "══════════════════════════════════════════════════════"
if [ "$ERRORS" -eq 0 ]; then
  echo " ✅ S06 Verifikation bestanden — alle Checks grün"
  echo "    19 Skills × 9 Sektionen × Prefix + Phantom = vollständig"
else
  echo " ❌ S06 Verifikation fehlgeschlagen — $ERRORS Fehler gefunden"
  echo "    Erstelle fehlende Skill-Dateien und starte das Skript erneut."
fi
echo "══════════════════════════════════════════════════════"
echo ""

# D014: Fehlerzähler als Exit-Code
exit $ERRORS
