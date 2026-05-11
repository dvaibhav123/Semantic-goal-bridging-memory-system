# Goal Knowledge Base: AI-Operating-System-for-PMs

## Goal Snapshot
> **Target Outcome:** Transform the repository into a self-improving AI Operating System for Product Managers that autonomously manages work prioritization and context.
> **Success Metrics (KPIs):** 100% of meeting action items mapped to goals; < 5 mins for daily focus list generation; no manual context drift.
> **Definition of Done (DoD):** Core skills (Meeting, Task, Knowledge) implemented; Goal schema metadata-rich; Outcome-driven templates active.
> **Key Decisions:**
> - Adopt SGBM (Semantic Goal-Bridging Memory) as the core memory architecture.
> - **Architecture Layer 1 (Goal Schema):** Enhance `Goals.md` to track metadata and Target Outcomes.
> - **Architecture Layer 2 (Task Schema):** Implement granular, behavioral task tracking in `Tasks.md`.
> - **Meeting Processor:** Autonomously map meeting notes to action items and goals.
> - **Task Prioritizer:** Auto-rank tasks via a P0-P3 priority matrix.
> - **Knowledge Triage:** Mandatory classification of info as Knowledge, Action, or Both.
> - **Outcome-Driven Goals:** Shift from output to outcome-focused goal definitions via a "PM Coach" gate.

## Context Map
- ## Goal Snapshot (Line 3): Target outcomes, KPIs, and DoD.
- ## Context Map (Line 14): Index for targeted extraction.
- ## Initial Requirements (Line 23): User-defined goals for PM workflow.
- ## Architecture - Goal Schema (Line 29): Defined metadata fields for goals.
- ## Architecture - Task Schema (Line 39): Implementation of granular task management.
- ## Meeting Note Analysis (Line 47): Strategy for processing meetings.
- ## Task Prioritization (Line 55): Strategy for autonomous task ranking.
- ## Knowledge Triage Protocol (Line 63): Strategy for routing info to knowledge vs. actions.
- ## Outcome-Driven Goals (Line 71): Strategy for enforcing outcome-focused definitions.

---

## Initial Requirements
- Managing day-to-day tasks.
- Prioritizing and managing work.
- Analyzing meeting notes for action items.
- Self-improving capabilities (learning from PM interactions).

## Architecture - Goal Schema
To prevent `Goals.md` from becoming just a list, each goal entry will track:
- **Target Outcome Statement**: Replaces the generic description in the index.
- **Status:** (Active, Paused, Completed, Archived)
- **Priority:** (P0, P1, P2, P3)
- **Stakeholders:** People involved or impacted (default: User).
- **Due Date:** Target completion date.
- **Blocked By:** Dependencies on other goals/tasks.
- **Tags:** Semantic tags (auto-populated if relevant).
- **Last Review Date:** For proactive PM review prompts.

## Architecture - Task Schema
Granular tasks are stored in `Tasks.md` using a structured table for behavioral tracking:
- **ID:** Unique identifier (e.g., T1, T2).
- **Status:** (Todo, In Progress, Blocked, Done, Dropped).
- **Priority:** (High, Med, Low).
- **Description:** Actionable task definition.
- **Dependencies:** Blockers or prerequisite tasks.

## Meeting Note Analysis
The system processes meeting notes via the `meeting-processor` skill:
- **Extraction:** Identifies Owner, Action, Due Date, and Related Goal context.
- **Semantic Mapping:** Maps tasks to existing goals in `Goals.md` via tags, or triggers `goal-manager` for new goals.
- **Agent Autonomy:** The skill formulates the entire update plan (new tasks, status updates) independently.
- **User Gate:** Explicit user confirmation is strictly required before the agent writes changes to `Tasks.md` or `Goals.md`.

## Task Prioritization
The system prioritizes work autonomously via the `task-prioritizer` skill:
- **Unified Backlog:** Scans all active goals and aggregates `Tasks.md` files.
- **Priority Matrix:** Auto-ranks tasks (P0: Overdue & Blocking, P1: Due this week, P2: Due next week, P3: Backlog).
- **Conflict Resolution:** Identifies circular or stale blockers, requesting user input when ambiguous.
- **Outputs:** Generates daily/weekly focus lists and updates the `Last Review` date on goals.

## Knowledge Triage Protocol
The `knowledge-manager` enforces a strict triage during the "Bubble Up" process:
- **Classification**: All incoming data is classified as Knowledge (Context/Decisions), Action (Tasks), or Both.
- **Routing**: Actions are promoted to `Tasks.md` and never stored only in `Knowledge.md`.
- **User Confirmation**: All proposed Knowledge and Task updates are presented for approval before commit.

## Outcome-Driven Goals
The `goal-manager` ensures all goals are outcome-focused:
- **PM Coach Gate**: The agent pushes back on output-focused requests (e.g., "build X") to extract the "Why" (Target Outcome) and "How" (KPIs).
- **Snapshot Schema**: `Knowledge.md` must contain Target Outcome, Success Metrics (KPIs), and Definition of Done (DoD).
- **Index Anchors**: The `Goals.md` index uses the Target Outcome statement as the primary identifier.
