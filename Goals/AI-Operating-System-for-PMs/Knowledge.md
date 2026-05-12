# Goal Knowledge Base: AI-Operating-System-for-PMs

## Goal Snapshot
> **Target Outcome:** Transform the repository into a self-improving AI Operating System for Product Managers that autonomously manages work prioritization and context via a role-driven architecture.
> **Success Metrics (KPIs):** 100% of meeting action items mapped to goals; < 5 mins for daily focus list generation; no manual context drift; 100% of tasks assigned unique ^t-IDs.
> **Definition of Done (DoD):** Core skills (Meeting, Task, Knowledge) implemented; Role-driven architecture (CoS, Architect) defined; OS Kernel (GEMINI.md) unified and linked.
> **Key Decisions:**
> - Adopt SGBM (Semantic Goal-Bridging Memory) as the core memory architecture.
> - **Architecture Layer 1 (Goal Schema):** Enhance `Goals.md` to track metadata and Target Outcomes.
> - **Architecture Layer 2 (Task Schema):** Implement granular, behavioral task tracking in `Tasks.md` with unique `^t-IDs`.
> - **Meeting Processor:** Autonomously map meeting notes to action items and goals.
> - **Task Prioritizer:** Auto-rank tasks via a P0-P3 priority matrix.
> - **Knowledge Triage:** Mandatory classification of info as Knowledge, Action, or Both.
> - **Outcome-Driven Goals:** Shift from output to outcome-focused goal definitions via a "PM Coach" gate.
> - **Strategic Hook:** Enforced reading of `Strategic-Pillars.md` during Orientation to ensure high-level alignment.
> - **Deterministic Integrity:** Enforced use of persistent Task IDs (`^t-AIOS-1`) to prevent state drift.
> - **Role-Driven Architecture:** Split agent logic into specialized personas (Chief of Staff, Architect) to prevent context contamination.
> - **OS Kernel Linkage:** Consolidated all logic into `GEMINI.md` and enforced the "Bookend" orchestration protocol for turn-by-turn role switching.

## Context Map
- ## Goal Snapshot (Line 3): Target outcomes, KPIs, and DoD.
- ## Context Map (Line 16): Index for targeted extraction.
- ## Initial Requirements (Line 26): User-defined goals for PM workflow.
- ## Architecture - Goal Schema (Line 32): Defined metadata fields for goals.
- ## Architecture - Task Schema (Line 42): Implementation of granular task management.
- ## Meeting Note Analysis (Line 50): Strategy for processing meetings.
- ## Task Prioritization (Line 58): Strategy for autonomous task ranking.
- ## Knowledge Triage Protocol (Line 66): Strategy for routing info to knowledge vs. actions.
- ## Outcome-Driven Goals (Line 74): Strategy for enforcing outcome-focused definitions.
- ## Strategic Hook Pattern (Line 82): Strategy for always-on strategic alignment.
- ## Deterministic Integrity (Line 90): Strategy for unique, persistent task IDs.
- ## Role-Driven Architecture (Line 98): Strategy for specialized agent personas.
- ## OS Kernel Linkage (Line 106): Strategy for unified instruction and orchestration logic.

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
- **ID:** Unique identifier using the `^t-[Goal-Acronym]-[Number]` syntax (e.g., `^t-AIOS-1`).
- **Status:** (Todo, In Progress, Blocked, Done, Dropped).
- **Priority:** (High, Med, Low).
- **Description:** Actionable task definition.
- **Dependencies:** Blockers or prerequisite tasks (using `^t-IDs`).

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

## Strategic Hook Pattern
Inspired by DEX, the OS implements a "Strategic Hook" to prevent strategic drift:
- **Orientation Protocol**: The agent is programmatically forced to read `Goals/Strategic-Pillars.md` at the start of every session.
- **Always-On Context**: High-level pillars (e.g., Q2 objectives) are injected before any granular task analysis occurs.
- **Weighting**: The `task-prioritizer` uses these pillars to weight P0/P1 tasks based on their alignment with the long-term North Star.

## Deterministic Integrity
To ensure rock-solid state management, the OS enforces unique, persistent IDs:
- **ID Syntax**: `^t-[Goal-Acronym]-[Number]`.
- **Referential Integrity**: All task references in `Progress.md`, focus lists, and "Blocked By" columns must use the `^t-ID`.
- **State Persistence**: Task IDs never change, even if description or status is updated, ensuring the agent never "loses" a task.

## Role-Driven Architecture
The OS utilizes specialized agent personas to manage context and execution:
- **Chief of Staff (CoS)**: The ruthless executor. Manages tactical noise, enforces memory hygiene, and executes daily tasks within established domains.
- **Systems Architect**: The strategic designer. Optimizes the OS, implements new skills, audits performance logs for systemic friction, and ensures 100% alignment with `Strategic-Pillars.md`. Acts as the "PM Coach" and the mandatory orchestrator bookending every session turn.

## OS Kernel Linkage
To ensure programmatic consistency, all agent logic is unified in `GEMINI.md`:
- **Central Kernel**: `GEMINI.md` defines the Dual-Core engine and consolidated SGBM memory protocols.
- **Bookend Orchestration**: Mandates that every session turn starts in Architect Mode (Framing), executes in CoS Mode (Tactical), and ends in Architect Mode (Validation).
- **Role Enforcement**: Agents are programmatically directed to their respective role files in `.agents/roles/` for behavioral guardrails.
