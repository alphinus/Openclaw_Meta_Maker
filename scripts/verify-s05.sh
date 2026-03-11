#!/usr/bin/env bash
# scripts/verify-s05.sh
# Objektive Stopping-Condition für Slice S05 — Research + Strategy Skills (~30 Skills)
# Ausführen aus dem Projekt-Root: bash scripts/verify-s05.sh

set -euo pipefail

ERRORS=0
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

pass() { echo "  ✓ $1"; }
fail() { echo "  ✗ $1"; ERRORS=$((ERRORS + 1)); }

echo ""
echo "══════════════════════════════════════════════════════"
echo " S05 Verifikation — Research + Strategy Skills"
echo "══════════════════════════════════════════════════════"

# ─────────────────────────────────────────────────────────
# CHECK-GRUPPE [1/4] — Datei-Existenz (28 neue Skills)
# ─────────────────────────────────────────────────────────
echo ""
echo "[1/4] Datei-Existenz — 28 neue Skill-Dateien (14 Research + 14 Strategy)"

RESEARCH_SKILLS=(
  "skills/research/elvis-ai-research.md"
  "skills/research/elvis-opportunity-finder.md"
  "skills/research/elvis-trend-analyzer.md"
  "skills/research/elvis-source-validator.md"
  "skills/research/elvis-competitor-deep-dive.md"
  "skills/research/elvis-audience-research.md"
  "skills/research/elvis-keyword-researcher.md"
  "skills/research/elvis-pain-point-finder.md"
  "skills/research/elvis-research-synthesizer.md"
  "skills/research/elvis-expert-finder.md"
  "skills/research/elvis-case-study-analyzer.md"
  "skills/research/elvis-data-collector.md"
  "skills/research/elvis-problem-explorer.md"
  "skills/research/elvis-insight-extractor.md"
)

STRATEGY_SKILLS=(
  "skills/strategy/elvis-growth-strategy.md"
  "skills/strategy/elvis-positioning-strategy.md"
  "skills/strategy/elvis-content-strategy.md"
  "skills/strategy/elvis-go-to-market.md"
  "skills/strategy/elvis-platform-strategy.md"
  "skills/strategy/elvis-risk-assessment.md"
  "skills/strategy/elvis-competitive-strategy.md"
  "skills/strategy/elvis-decision-framework.md"
  "skills/strategy/elvis-prioritization-engine.md"
  "skills/strategy/elvis-scenario-planner.md"
  "skills/strategy/elvis-okr-planner.md"
  "skills/strategy/elvis-pivot-advisor.md"
  "skills/strategy/elvis-resource-allocator.md"
  "skills/strategy/elvis-monetization-strategy.md"
)

ALL_S05_SKILLS=("${RESEARCH_SKILLS[@]}" "${STRATEGY_SKILLS[@]}")

for skill in "${ALL_S05_SKILLS[@]}"; do
  if [ -f "$ROOT/$skill" ]; then
    pass "$skill"
  else
    fail "$skill — Datei fehlt"
  fi
done

# ─────────────────────────────────────────────────────────
# CHECK-GRUPPE [2/4] — Sektions-Vollständigkeit (28 × 9 = 252 Checks)
# ─────────────────────────────────────────────────────────
echo ""
echo "[2/4] Sektions-Vollständigkeit — 252 Checks (28 Dateien × 9 Pflichtfelder)"

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

for skill in "${ALL_S05_SKILLS[@]}"; do
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
# CHECK-GRUPPE [3/4] — /elvis-Prefix im ## Name Block (28 Checks)
# ─────────────────────────────────────────────────────────
echo ""
echo "[3/4] /elvis-* Prefix — 28 Checks (je 1 pro Datei)"

for skill in "${ALL_S05_SKILLS[@]}"; do
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

for skill in "${ALL_S05_SKILLS[@]}"; do
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
        for subdir in growth content research strategy automation meta; do
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
  echo " ✅ S05 Verifikation bestanden — alle Checks grün"
  echo "    28 Skills × 9 Sektionen × Prefix + Phantom = vollständig"
else
  echo " ❌ S05 Verifikation fehlgeschlagen — $ERRORS Fehler gefunden"
  echo "    Erstelle fehlende Skill-Dateien und starte das Skript erneut."
fi
echo "══════════════════════════════════════════════════════"
echo ""

# D014: Fehlerzähler als Exit-Code
exit $ERRORS
