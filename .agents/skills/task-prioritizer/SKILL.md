---
name: task-prioritizer
description: Scans all active goals and tasks, unifies the backlog, applies a strict priority matrix, flags dependency conflicts, and outputs a daily/weekly focus list while updating goal review dates.
---

# Task Prioritizer Skill

Use this skill when the user wants to prioritize their workload, generate a focus list, or resolve task dependencies across the OS.

## Execution Steps

1. **Scan and Unify**:
   - Read the master index (`Goals/Goals.md`) to identify all Active goals.
   - For each active goal, read its `Tasks.md` file.
   - Compile a unified list of all tasks including properties: Goal, ID (must follow `^t-[Goal-Acronym]-[Number]`), Task Description, Status, Priority, Due Date (if any), and Dependencies (using `^t-IDs`).

2. **Apply Priority Matrix**:
   Evaluate and automatically re-rank the tasks based on the following matrix:
   - **P0 (Critical)**: Overdue AND blocks downstream tasks (check `^t-ID` dependencies).
   - **P1 (High)**: Due this week AND has no blockers.
   - **P2 (Medium)**: Due next week.
   - **P3 (Backlog)**: All other tasks (no immediate due date, or blocked by non-stale tasks).

3. **Dependency Conflict Resolution**:
   Analyze the unified task list for dependency issues using `^t-IDs`:
   - **Circular Blockers**: Task ^t-A blocks Task ^t-B, and Task ^t-B blocks Task ^t-A.
   - **Stale Blockers**: A task is blocked by a `^t-ID` that hasn't seen progress recently or doesn't exist.
   - *Agent Autonomy & Confirmation*: Flag these conflicts. If the resolution is obvious, draft a proposed fix. If enough information is not available to resolve the conflict safely, you MUST present the conflict and ask the user for clarification.

4. **Output Generation**:
   - **Daily Focus List**: A ranked list of P0 and P1 tasks to tackle today.
   - **Weekly Focus List**: A broader view including P2 tasks.
   - **Conflict Report**: Summary of flagged circular or stale blockers needing attention.

5. **State Updates ("Bubble Up")**:
   - Draft updates to the `Priority` column in the respective `Tasks.md` files to match the new matrix rankings.
   - Draft updates to `Goals/Goals.md`: For each active goal processed, update the `[Last Review: YYYY-MM-DD]` field to today's date.
   - **MANDATORY GATE**: Present the focus lists, conflict report, and proposed file updates to the user. Obtain explicit user confirmation before writing changes to any `Tasks.md` or `Goals.md` file.

6. **Finalize**: 
   - Upon user approval, apply the confirmed changes to the files.
