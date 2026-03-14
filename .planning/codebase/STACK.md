# Technology Stack

**Analysis Date:** 2026-03-14

## Languages

**Primary:**
- Markdown - All content and configuration (100% of deliverable)
- German - All documentation, skill descriptions, agent definitions, soul philosophies

**Secondary:**
- Python - Utility scripts for file generation and planning
- Bash - Verification and automation scripts

## Runtime

**Environment:**
- No runtime engine required
- File-based system (Markdown files only)
- Platform-agnostic (any OS with file storage)

**Package Manager:**
- None — project generates static Markdown files for import into OpenClaw
- Lockfile: Not applicable

## Frameworks

**Content Generation:**
- Pure Markdown with no external framework dependencies
- Template-based generation (`templates/` directory)

**Build/Dev:**
- Bash verification scripts (`scripts/verify-*.sh`)
- Python scripts for automated planning (`scripts/write_*.py`)

## Key Dependencies

**External:**
- None detected — this is a self-contained Markdown generation project

**Infrastructure:**
- Git — Version control (`.git` directory, `.gitignore` present)
- GSD workflow system — Planning and execution framework (`.gsd/` directory)

## Configuration

**Environment:**
- No environment variables required for core functionality
- No `.env` file detected (commented out in `.gitignore`)

**Build:**
- Bash scripts in `scripts/` directory for verification and generation
- Python scripts for planning and task generation (`write_s03_plan.py`, `write_s03_tasks.py`)

## Platform Requirements

**Development:**
- Text editor (any — pure Markdown)
- Bash shell for verification scripts
- Python 3 for automation scripts
- Git for version control

**Production:**
- Target platform: OpenClaw (proprietary agent system)
- Delivery method: Direct Markdown file import
- No server, API, or runtime required

---

*Stack analysis: 2026-03-14*
