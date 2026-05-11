# Project Instructions: Semantic Goal-Bridging Memory (SGBM)

This project follows the **SGBM Architecture** for context management. All agents operating in this workspace MUST adhere to the following protocols.

## Memory Protocol (SGBM)
1. **Orientation:** On your first turn, read `Goals/Strategic-Pillars.md` AND `Goals/Goals.md`. Use the pillars to weight priorities and semantic tags to identify relevant past goals.
2. **Lazy Load:** Do not read full `Knowledge.md` files. Read ONLY the `## Goal Snapshot` and `## Context Map` at the top. Use the Context Map for targeted `read_file` operations.
3. **The Bubble Up Rule:** When you make a significant architectural decision or reach a milestone, you MUST append the details to `Knowledge.md`. You are strictly forbidden from doing so without concurrently updating the `## Context Map` and `## Goal Snapshot` headers.
4. **Skills First:** Use the `goal-manager` logic to create new goals and `knowledge-manager` logic to sync context.

## Available Scripts (.agents/bin/)
- `sgbm-loader.py`: Tag extraction.
- `sgbm-logger.py`: Session event logger.
- `sgbm-syncer.py`: Auto-documentation script.
- `sgbm-validator.py`: CI/CD Quality Gate.

## Goal Structure
- `Goals/Goals.md`: Master index.
- `Goals/[Goal_Name]/Progress.md`: Execution tracking.
- `Goals/[Goal_Name]/Knowledge.md`: Decisions and context (SGBM structured).
