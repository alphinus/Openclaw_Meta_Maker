#!/usr/bin/env bash
# scripts/verify-s02.sh
# Objektive Stopping-Condition für Slice S02 — Souls und Identities
# Ausführen aus dem Projekt-Root: bash scripts/verify-s02.sh

ERRORS=0
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

pass() { echo "  ✓ $1"; }
fail() { echo "  ✗ $1"; ERRORS=$((ERRORS + 1)); }

echo ""
echo "══════════════════════════════════════════════════════"
echo " S02 Verifikation — OpenClaw Meta Maker"
echo "══════════════════════════════════════════════════════"

# ─────────────────────────────────────────────────────────
# [1/3] Datei-Existenz (26 Dateien)
# ─────────────────────────────────────────────────────────
echo ""
echo "[1/3] Datei-Existenz (26 Dateien)"

SOUL_FILES=(
  "soul/strategist.md"
  "soul/researcher.md"
  "soul/execution.md"
  "soul/builder.md"
  "soul/growth.md"
  "soul/automation.md"
  "soul/operator.md"
  "soul/analyst.md"
  "soul/creator.md"
  "soul/minimalist.md"
)

IDENTITY_FILES=(
  "identity/spock.md"
  "identity/kirk.md"
  "identity/picard.md"
  "identity/riker.md"
  "identity/worf.md"
  "identity/data.md"
  "identity/scotty.md"
  "identity/laforge.md"
  "identity/mccoy.md"
  "identity/seven.md"
  "identity/sulu.md"
  "identity/tuvok.md"
  "identity/q.md"
  "identity/borg.md"
  "identity/troi.md"
  "identity/uhura.md"
)

for f in "${SOUL_FILES[@]}"; do
  if [ -f "$ROOT/$f" ]; then
    pass "$f"
  else
    fail "$f — Datei fehlt"
  fi
done

for f in "${IDENTITY_FILES[@]}"; do
  if [ -f "$ROOT/$f" ]; then
    pass "$f"
  else
    fail "$f — Datei fehlt"
  fi
done

# ─────────────────────────────────────────────────────────
# [2/3] Soul-Sektionen (10 × 6 = 60 Checks)
# ─────────────────────────────────────────────────────────
echo ""
echo "[2/3] Soul-Sektionen (10 × 6 = 60 Checks)"

SOUL_SECTIONS=(
  "## Name"
  "## Philosophie"
  "## Core Values"
  "## Operating Principles"
  "## Success Metrics"
  "## Geeignet für"
)

for f in "${SOUL_FILES[@]}"; do
  soul_path="$ROOT/$f"
  soul_name=$(basename "$f")
  if [ -f "$soul_path" ]; then
    for section in "${SOUL_SECTIONS[@]}"; do
      if grep -qF "$section" "$soul_path"; then
        pass "$soul_name: $section"
      else
        fail "$soul_name: $section — Sektion fehlt"
      fi
    done
  else
    for section in "${SOUL_SECTIONS[@]}"; do
      fail "$soul_name: $section — Datei fehlt"
    done
  fi
done

# ─────────────────────────────────────────────────────────
# [3/3] Identity-Sektionen (16 × 7 = 112 Checks)
# ─────────────────────────────────────────────────────────
echo ""
echo "[3/3] Identity-Sektionen (16 × 7 = 112 Checks)"

IDENTITY_SECTIONS=(
  "## Name"
  "## Charakter-Beschreibung"
  "## Persönlichkeitsmerkmale"
  "## Kommunikationsstil"
  "## Stärken"
  "## Schwächen"
  "## Star Trek Referenz"
)

for f in "${IDENTITY_FILES[@]}"; do
  id_path="$ROOT/$f"
  id_name=$(basename "$f")
  if [ -f "$id_path" ]; then
    for section in "${IDENTITY_SECTIONS[@]}"; do
      if grep -qF "$section" "$id_path"; then
        pass "$id_name: $section"
      else
        fail "$id_name: $section — Sektion fehlt"
      fi
    done
  else
    for section in "${IDENTITY_SECTIONS[@]}"; do
      fail "$id_name: $section — Datei fehlt"
    done
  fi
done

# ─────────────────────────────────────────────────────────
# ZUSAMMENFASSUNG
# ─────────────────────────────────────────────────────────
echo ""
echo "══════════════════════════════════════════════════════"
if [ "$ERRORS" -eq 0 ]; then
  echo " ✅ S02 Verifikation bestanden — alle 198 Checks grün"
else
  echo " ❌ S02 Verifikation fehlgeschlagen — $ERRORS Fehler gefunden"
  echo "    Führe die fehlenden Tasks aus und starte das Skript erneut."
fi
echo "══════════════════════════════════════════════════════"
echo ""

exit $ERRORS
