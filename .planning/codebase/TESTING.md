# Testing Patterns

**Analysis Date:** 2026-03-14

## Test Framework

**Runner:**
- Bash shell scripts (`bash verify-s*.sh`)
- No traditional unit test framework (not applicable to Markdown-based system)

**Verification Approach:**
- Contract-driven verification: Each slice defines its own `verify-s*.sh` script
- Stopping-condition first: Verification script written BEFORE any content is created (D015)
- Exit code driven: `exit $ERRORS` where errors = count of failed checks

**Run Commands:**
```bash
bash scripts/verify-s02.sh     # Verify S02 — Souls and Identities (198 total checks)
bash scripts/verify-s03.sh     # Verify S03 — Agents (148 total checks)
bash scripts/verify-s04.sh     # Verify S04 — Skills (verification pattern TBD)
echo $?                         # Prints exit code (0 = all passed, N = N checks failed)
```

## Test File Organization

**Location:**
- Verification scripts live in `scripts/verify-[s-number].sh`
- One verification script per milestone slice
- Scripts are committed to repository alongside content files

**Naming:**
- Pattern: `verify-s02.sh`, `verify-s03.sh` (lowercase `s` + number)
- Scripts verify the slice number they correspond to
- No test fixtures — verification runs against actual content files

**Test Structure:**
```
scripts/
├── verify-s02.sh       # Tests Souls (10 files) + Identities (16 files)
├── verify-s03.sh       # Tests Agents (16 files)
├── verify-s04.sh       # Tests Skills (TBD count)
└── write_s03_plan.py   # Plan generator (not a test)
```

## Test Structure Pattern

All verification scripts follow this identical pattern:

```bash
#!/usr/bin/env bash
# scripts/verify-s0X.sh
# Description of what this slice verifies

ERRORS=0
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

pass() { echo "  ✓ $1"; }
fail() { echo "  ✗ $1"; ERRORS=$((ERRORS + 1)); }

echo ""
echo "══════════════════════════════════════════════════════"
echo " SXX Verifikation — OpenClaw Meta Maker"
echo "══════════════════════════════════════════════════════"

# ─────────────────────────────────────────────────────────
# [1/N] Group Name (X Checks)
# ─────────────────────────────────────────────────────────
echo ""
echo "[1/N] Group Name (X Checks)"

# Define arrays of files and sections
SOME_FILES=(...)
SOME_SECTIONS=(...)

# Run checks
for f in "${SOME_FILES[@]}"; do
  file_path="$ROOT/$f"
  file_name=$(basename "$f")
  if [ -f "$file_path" ]; then
    for section in "${SOME_SECTIONS[@]}"; do
      if grep -qF "$section" "$file_path"; then
        pass "$file_name: $section"
      else
        fail "$file_name: $section — Sektion fehlt"
      fi
    done
  fi
done

# Final summary
echo ""
echo "══════════════════════════════════════════════════════"
if [ "$ERRORS" -eq 0 ]; then
  echo " ✅ SXX Verifikation bestanden — alle N Checks grün"
else
  echo " ❌ SXX Verifikation fehlgeschlagen — $ERRORS Fehler gefunden"
fi
echo "══════════════════════════════════════════════════════"
echo ""

exit $ERRORS
```

## Verification Patterns

**S02 Verification (`scripts/verify-s02.sh`):**
- **Total checks:** 198 (26 file existence + 60 soul sections + 112 identity sections)
- **[1/3] File Existence (26 checks):**
  - 10 Soul files: `soul/strategist.md` through `soul/minimalist.md`
  - 16 Identity files: `identity/kirk.md` through `identity/uhura.md`
  - Check: `[ -f "$ROOT/$f" ]` — file exists

- **[2/3] Soul Sections (10 × 6 = 60 checks):**
  - For each soul file, verify 6 mandatory headers:
    - `## Name`
    - `## Philosophie`
    - `## Core Values`
    - `## Operating Principles`
    - `## Success Metrics`
    - `## Geeignet für`
  - Check: `grep -qF "$section" "$soul_path"` — exact header present

- **[3/3] Identity Sections (16 × 7 = 112 checks):**
  - For each identity file, verify 7 mandatory headers:
    - `## Name`
    - `## Charakter-Beschreibung`
    - `## Persönlichkeitsmerkmale`
    - `## Kommunikationsstil`
    - `## Stärken`
    - `## Schwächen`
    - `## Star Trek Referenz`
  - Check: `grep -qF "$section" "$id_path"` — exact header present

**S03 Verification (`scripts/verify-s03.sh`):**
- **Total checks:** 148 (16 file existence + 112 agent sections + 20 safeguard markers)
- **[1/3] File Existence (16 checks):**
  - 16 Agent files: `agent/kirk.md` through `agent/uhura.md`
  - Check: `[ -f "$ROOT/$f" ]`

- **[2/3] Agent Sections (16 × 7 = 112 checks):**
  - For each agent file, verify 7 mandatory headers:
    - `## Name`
    - `## Mission`
    - `## Capabilities`
    - `## Operating Loop`
    - `## Constraints`
    - `## Primärer Soul`
    - `## Primäre Skills`
  - Check: `grep -qF "$section" "$agent_path"`

- **[3/3] Safeguard Markers (5 × 4 = 20 checks):**
  - Only for 5 autonomous agents: picard, q, borg, troi, uhura
  - For each agent, verify 4 bold-formatted markers in Constraints section:
    - `**Max-Limit:**`
    - `**Approval-Gate:**`
    - `**Stop-Bedingung:**`
    - `**Rollback-Hinweis:**`
  - Check: `grep -qF "$marker" "$agent_path"`

## Mocking

**Not Applicable:** This system has no external dependencies, API calls, or state mutations to mock. Verification is purely structural — checking file existence and header presence.

**Test Data:**
- No fixtures needed — files ARE the test data
- Verification runs against actual deployed files
- No factory functions or test data generators

## Coverage Requirements

**Requirements:** Not enforced by default — no coverage tool
- Initial run: All checks fail (expected state per D015)
- Progressive run: Checks pass as content is written
- Final state: Exit code 0 (all checks green)

**Coverage Philosophy:**
- Coverage = percentage of mandatory sections present
- A file with 6/7 sections = 1 check failing
- Target: 100% — exit code 0

**View Verification Results:**
```bash
bash scripts/verify-s02.sh
# Output shows each check as ✓ (pass) or ✗ (fail)
# Exit code = count of failures
echo "Result: $?"
```

## Test Types

**Contract Verification (Structural Tests):**
- Verifies all mandatory files exist
- Verifies all mandatory sections present in each file
- Verifies special markers (safeguards) present in autonomous agents
- Runs via: `bash scripts/verify-s*.sh`

**Failure Modes Tested:**
- Missing file: Script outputs "`[filename] — Datei fehlt`"
- Missing section: Script outputs "`[filename]: [section] — Sektion fehlt`"
- Missing safeguard: Script outputs "`[filename]: [marker] — Safeguard fehlt`"

**No Unit Tests:** Individual skills, agents, or souls are not unit tested. They are verified for structural completeness only.

**No Integration Tests:** Cross-references (agent → soul, agent → skills) are not tested by verification scripts — only section presence.

## Acceptance Criteria Pattern

Each verification script defines exact acceptance criteria:

**S02 Acceptance Criteria:**
- `bash scripts/verify-s02.sh` runs without bash syntax errors
- Exit code = 0 (or expected number of failures for incomplete slices)
- Output shows 198 checks (26 + 60 + 112)
- All sections are checked with exact header matches

**S03 Acceptance Criteria:**
- `bash scripts/verify-s03.sh` runs without bash syntax errors
- Exit code = 0 when complete
- Output shows 148 checks (16 + 112 + 20)
- All 5 autonomous agents have all 4 safeguard markers

**Pattern:** Verification scripts print structured output with ✓/✗ symbols followed by check name, then exit with code = error count.

## Verification-First Principle (D015)

**Key Pattern:** Verification script is written BEFORE any content files.

**First Run State:**
- Script runs: ✅ (no bash errors)
- All checks fail: ✅ (expected — files don't exist yet)
- Exit code = max errors: ✅ (e.g., 198 for S02, 148 for S03)

**Example Progression:**
```bash
# Before any files created
$ bash scripts/verify-s03.sh
[1/3] Datei-Existenz
  ✗ agent/kirk.md — Datei fehlt
  ✗ agent/spock.md — Datei fehlt
  ... (16 failures)
[2/3] Agent-Sektionen
  ✗ agent/kirk.md: ## Name — Datei fehlt
  ... (112 failures)
[3/3] Safeguard-Marker
  ✗ agent/picard.md: **Max-Limit:** — Datei fehlt
  ... (20 failures)
❌ 148 Fehler
$ echo $?
148

# After some agents created (e.g., Kirk, Spock, Worf)
$ bash scripts/verify-s03.sh
[1/3] Datei-Existenz
  ✓ agent/kirk.md
  ✓ agent/spock.md
  ✗ agent/picard.md — Datei fehlt
  ...
[2/3] Agent-Sektionen
  ✓ agent/kirk.md: ## Name
  ✓ agent/kirk.md: ## Mission
  ...
  ✗ agent/picard.md: ## Name — Datei fehlt
  ...
$ echo $?
127  # Number of remaining failures

# All agents complete, all sections present, all safeguards added
$ bash scripts/verify-s03.sh
[1/3] Datei-Existenz
  ✓ agent/kirk.md
  ... (all 16 pass)
[2/3] Agent-Sektionen
  ✓ agent/kirk.md: ## Name
  ... (all 112 pass)
[3/3] Safeguard-Marker
  ✓ agent/picard.md: **Max-Limit:**
  ... (all 20 pass)
✅ Verifikation bestanden — alle 148 Checks grün
$ echo $?
0
```

## Test Execution Environment

**Prerequisites:**
- Bash shell available
- Working directory: Project root
- No external dependencies (no Python, Ruby, Node, Docker, etc. required for verification)

**Execution Context:**
- Scripts use `ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"` to find project root
- Can be run from any directory: `bash /path/to/project/scripts/verify-s03.sh`
- All file paths are absolute from `$ROOT`

**Error Handling:**
- Bash set options: None (standard bash, no `set -e` or similar)
- Individual checks use `if [ -f ... ]` conditionals
- Errors accumulate in `ERRORS` counter, no early exit

---

*Testing analysis: 2026-03-14*
