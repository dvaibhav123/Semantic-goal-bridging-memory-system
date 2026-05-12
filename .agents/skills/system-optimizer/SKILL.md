---
name: system-optimizer
description: Exclusive to the Systems Architect. Synthesizes entries from the Friction Log to evolve OS skills and roles.
---

# System Optimizer Skill

Use this skill when performing a System Audit or when the Friction Log contains 'Pending' items.

## Execution Steps

1. **Review Friction**: Read `.agents/memory/Friction-Log.md` and filter for all entries with status `Pending`.
2. **Review Context**: Read `.agents/memory/Improvement-Log.md` to understand historical updates and prevent regression.
3. **Analyze Root Cause**: For each pending friction item, determine if the issue is due to:
   - Ambiguous Role instructions.
   - Missing or buggy Skill logic.
   - Vague SGBM templates.
4. **Draft Solution**: Formulate a technical update to the relevant `.agents/skills/*.md` or `.agents/roles/*.md` file to resolve the issue permanently.
5. **Draft Improvement Entry**: Prepare a new row for the `Improvement-Log.md` referencing the Friction IDs being resolved.
6. **User Confirmation (Mandatory)**: Present the proposed system changes and log updates to the user. Do NOT apply changes without explicit approval.
7. **Execute & Update**: 
   - Apply the approved file changes.
   - Append the new entry to `Improvement-Log.md`.
   - Update the status of processed Friction items to `Resolved`.
