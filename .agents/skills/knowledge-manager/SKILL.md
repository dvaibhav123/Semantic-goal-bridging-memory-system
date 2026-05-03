---
name: knowledge-manager
description: Use this skill whenever you or the user identify important context, architectural decisions, discovery research, requirements, user rules, or key constraints that should be preserved for a Goal. Trigger this skill proactively during natural conversation pauses, when a specific sub-topic concludes, when significant decisions are made, or when dense information needs synthesizing. Do not wait for the conversation to literally 'end'—trigger it whenever enough critical information has accumulated that it shouldn't be lost. It extracts key info and structures it flexibly into Knowledge.md.
---

# Knowledge Manager Skill

Use this skill whenever there is new important context, architectural decisions, discovery research, or key constraints identified during a conversation that should be preserved for future discussions within a specific Goal.

## Trigger Instructions
- **When to use**: When you or the user identifies information that needs to be persisted in a Goal's `Knowledge.md` file. Examples: finalizing a system architecture, discovering a new constraint, summarizing research findings, handling multi-turn discussions packed with dense information, or making a significant process decision. DO NOT WAIT for the "end of the conversation"—conversations rarely have definitive ends. Instead, trigger it proactively when a sub-topic concludes, when transitioning to a new subject, or when enough important context has been established that it would be detrimental to lose it.
- **Input**: The specific information to be added, and the relevant Goal name. Include lengthy discussion transcripts or dense data as input so the skill can synthesize it.

## Process: The "Bubble Up" Protocol
1. **Identify the Goal**: Ensure you know which Goal this knowledge belongs to. If unsure, refer to `Goals/Goals.md`.
2. **Locate & Read Front-Matter**: Find the `Knowledge.md` file. **Read ONLY the `## Goal Snapshot` and `## Context Map` first** to determine where the new information fits.
3. **Format & Synthesize**: Structure the new knowledge logically.
   - **Synthesis**: Extract *key facts, constraints, and decisions*. Use Markdown tables for structured data.
   - **Fluid Schema**: Use descriptive, context-dependent headers.
4. **Update with Atomicity**: You MUST update the file using the following "Bubble Up" sequence:
   - **Log Activity**: Ensure all relevant tool calls and intents from the session have been logged via `.agents/bin/sgbm-logger.py`.
   - **Body**: Append or integrate the new structured information.
   - **Context Map**: Update the `## Context Map` with the new/modified headers and their line locations.
   - **Goal Snapshot**: Invoke `.agents/bin/sgbm-syncer.py` to synthesize the session log. Update the `## Goal Snapshot` with the resulting "Bottom Line" or "Key Decision".
   - **Flush**: Once the Snapshot is successfully updated, ensure the session log is flushed (either via `sgbm-syncer.py` or manually).
   - **Rule**: NEVER append to the body without concurrently updating the Context Map and Snapshot. Use the script `.agents/bin/sgbm-validator.py` to ensure the structure remains valid after edits.
5. **Cross-Goal Tagging**: If the new knowledge introduces a new domain, invoke `.agents/bin/sgbm-loader.py` to check existing tags and append new ones to `Goals/Goals.md`.
6. **Confirm**: Briefly confirm that the knowledge has been synced and the SGBM front-matter updated.

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
