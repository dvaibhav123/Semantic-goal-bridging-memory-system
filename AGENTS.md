# System Instructions

> **Purpose:** This file contains instructions for AI agents operating in this workspace.
> *Note: If you are integrating SGBM into an existing project, insert the `Memory Protocol (SGBM)` section below into your existing `AGENTS.md` or `.cursorrules` file.*

## Memory Protocol (SGBM)
1. **Orientation:** On your first turn, read `Goals/Goals.md`. Use semantic tags to identify relevant past goals.
2. **Lazy Load:** Do not read full `Knowledge.md` files. Read ONLY the `## Goal Snapshot` and `## Context Map` at the top. Use the Context Map for targeted `read_file` operations.
3. **The Bubble Up Rule:** When you make a significant architectural decision or reach a milestone, you MUST append the details to `Knowledge.md`. You are strictly forbidden from doing so without concurrently updating the `## Context Map` and `## Goal Snapshot` headers.
4. **Skills First:** Always trigger `goal-manager` when a new thread does not fit an existing goal, and trigger `knowledge-manager` continuously to sync deep context.

---
*(Add your workspace's specific agent rules, persona definitions, or workflows below this line)*
