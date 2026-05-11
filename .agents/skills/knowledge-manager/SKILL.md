---
name: knowledge-manager
description: Use this skill whenever you or the user identify important context, architectural decisions, discovery research, requirements, user rules, or key constraints that should be preserved for a Goal. Trigger this skill proactively during natural conversation pauses, when a specific sub-topic concludes, when significant decisions are made, or when dense information needs synthesizing. Do not wait for the conversation to literally 'end'—trigger it whenever enough critical information has accumulated that it shouldn't be lost. It extracts key info and structures it flexibly into Knowledge.md.
---

# Knowledge Manager Skill

Use this skill whenever there is new important context, architectural decisions, discovery research, or key constraints identified during a conversation that should be preserved for future discussions within a specific Goal.

## Trigger Instructions
- **When to use**: When you or the user identifies information that needs to be persisted in a Goal's `Knowledge.md` file or when granular tasks in `Tasks.md` lead to significant decisions. Examples: finalizing a system architecture, discovering a new constraint, summarizing research findings, handling multi-turn discussions packed with dense information, or making a significant process decision. DO NOT WAIT for the "end of the conversation"—conversations rarely have definitive ends. Instead, trigger it proactively when a sub-topic concludes, when transitioning to a new subject, or when enough important context has been established that it would be detrimental to lose it.
- **Input**: The specific information to be added, and the relevant Goal name. Include lengthy discussion transcripts or dense data as input so the skill can synthesize it.

## Process: The "Bubble Up" Protocol
1. **Identify the Goal**: Ensure you know which Goal this knowledge belongs to. If unsure, refer to `Goals/Goals.md`.
2. **Mandatory Triage**: Classify each piece of incoming information:
   - **Knowledge Only (Decisions, Constraints, Context)**: Route to `Knowledge.md`.
   - **Action Only (Tasks, To-Dos, Follow-ups)**: Route to `Tasks.md`. Draft a new task following the Layer 2 schema.
   - **Both (Decision implying a Task)**: Route context to `Knowledge.md` AND draft a task in `Tasks.md`.
   - **Rule**: NEVER persist an action item solely in `Knowledge.md`. It must be promoted to the task tracking system.
3. **Locate & Read Files**: 
   - For Knowledge: Read ONLY the `## Goal Snapshot` and `## Context Map` of `Knowledge.md` first.
   - For Actions: Read the current `Tasks.md` to ensure no duplicate tasks.
4. **Format & Synthesize**: Structure the information logically. Extract key facts/decisions for Knowledge and define actionable, prioritized tasks for Actions.
5. **Update with User Gate**:
   - **User Confirmation (Mandatory)**: Present the proposed triage results and file updates (Knowledge.md changes + new Tasks.md drafts) to the user. Do NOT write to files until explicit approval is given.
   - **Atomicity**: Once approved, update the files in sequence:
     - Log activity via `.agents/bin/sgbm-logger.py`.
     - Update `Knowledge.md` (Body -> Context Map -> Snapshot via `sgbm-syncer.py`).
     - Update `Tasks.md` with new tasks.
     - Ensure `sgbm-validator.py` confirms structural integrity.
6. **Cross-Goal Tagging**: If new domains are introduced, sync tags with `Goals/Goals.md` via `sgbm-loader.py`.
7. **Confirm**: Briefly confirm that both knowledge and actions have been synced and the SGBM front-matter updated.

## Format Guidelines for `Knowledge.md` (SGBM Standard)
When updating the file, strictly adhere to the SGBM Intra-Goal Structure:

```markdown
# Knowledge Repository: [Goal Name]

## Goal Snapshot
- **Bottom Line**: [High-level summary of current state/intent]
- **Key Decisions**:
    - [Decision 1]
    - [Decision 2]

## Context Map
- [Header Name] (Line XX): [Brief 1-sentence context]

## [Context Index]
- [Detailed index of sections for legacy compatibility]

## [Adaptable Category 1]
...
```

Adapt and create the headings as necessary based on the information being added. Always prioritize fluidity, clarity, scannability, and preserving key information from lengthy discussions.
