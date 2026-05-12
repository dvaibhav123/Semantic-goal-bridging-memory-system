# Release Log

This file tracks all updates to the Semantic Goal Management (SGM) system. Use this to integrate updates into existing project folders.

## [1.1.1] - 2026-05-12
### Fixed
- **Architectural Violation**: Patched `product-brief` skill. It now strictly requires the use of `codebase_investigator` for context gathering and `goal-manager` to ensure proper SGBM folder initialization before spec drafting.
- **Memory Corruption Risk**: Patched `brainstormer` skill. It is now strictly forbidden from editing `Knowledge.md` directly and MUST delegate "Bubble Up" operations to the `knowledge-manager` skill.
- **Phantom Personas**: Constrained the "Party Mode" in `brainstormer` to only utilize personas explicitly defined in `.agents/roles/`.

### Added
- **Persona Visibility Rule**: Updated `GEMINI.md` to mandate that the agent identifies its active core (Architect, CoS, or PM) at the start of every chat response.

### Integration Instructions
To update your local system to v1.1.1:
1. Replace `.agents/skills/product-brief/SKILL.md` and `.agents/skills/brainstormer/SKILL.md` with updated versions.
2. Update your `GEMINI.md` with the "Persona Visibility Rule".

---

## [1.1.0] - 2026-05-12
### Added
- **Product Manager (PM) Persona**: Introduced `.agents/roles/Product-Manager.md` for requirement synthesis and strategic brainstorming.
- **Product Briefing Skill**: Added `.agents/skills/product-brief/` to facilitate high-fidelity SPEC generation (BMAD Method).
- **Brainstorming Skill**: Added `.agents/skills/brainstormer/` for multi-perspective "Party Mode" analysis.
- **Multi-Core OS Update**: Upgraded `GEMINI.md` to include PM Rituals in the Phase 1 Framing protocol.

### Integration Instructions
To update your local system to v1.1.0:
1. Copy `.agents/roles/Product-Manager.md` to your roles directory.
2. Copy `.agents/skills/product-brief/` and `.agents/skills/brainstormer/` to your skills directory.
3. Update your `GEMINI.md` to reflect the "Multi-Core Engine" and Phase 1 PM trigger logic.
4. Ensure your agent prompt references the PM role for all new feature requests.

---

## [1.0.0] - 2026-05-12
### Added
- **Release Documentation**: Established `RELEASES.md` for tracking system updates.
- **Agent Handover Protocol**: Integrated system health and handover instructions directly into the root `README.md`.
- **Release Protocol**: Updated `GEMINI.md` with instructions for managing releases and system health tracking.

### Integration Instructions
To update your local system to v1.0.0:
1. Copy `RELEASES.md` to your root directory.
2. Update your root `README.md` with the "Maintenance & Updates" and "Agent Handover" sections.
3. Update your `GEMINI.md` with the "Release & Integrity Protocol" section.
