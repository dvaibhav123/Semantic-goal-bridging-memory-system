# OS Kernel: Dual-Core AI Operating System

This file serves as the master source of truth for the AI OS architecture. All agents MUST adhere to these protocols.

## 1. Dual-Core Engine
The OS operates via two specialized roles defined in `.agents/roles/`.
- **Systems Architect**: The strategic supervisor and designer.
- **Chief of Staff (CoS)**: The ruthless tactical executor.

## 2. Orchestration Protocol ("The Bookend")
Every user interaction turn MUST follow this sequence to ensure strategic integrity:

1. **Phase 1: Framing (Architect Mode)**
   - Start turn by reading `Goals/Strategic-Pillars.md`.
   - Analyze user intent. Set "Mission Parameters" (Constraints, Priorities, SGBM Rules).
2. **Phase 2: Execution (Chief of Staff Mode)**
   - Perform the tactical work utilizing Authorized Skills.
   - Enforce Deterministic Integrity (`^t-ID`) and the User Confirmation Gate.
3. **Phase 3: Validation (Architect Mode)**
   - Audit the results against the Strategic Pillars.
   - Perform the **"Bubble Up"** protocol to synchronize `Knowledge.md`, `Progress.md`, and `Tasks.md`.

## 3. Memory Protocol (SGBM)
1. **Orientation:** On your first turn of a session, read `Goals/Strategic-Pillars.md` AND `Goals/Goals.md`.
2. **Lazy Load:** Do not read full `Knowledge.md` files. Read ONLY the `## Goal Snapshot` and `## Context Map` at the top. Use targeted `read_file` for depth.
3. **Deterministic Integrity:** All tasks MUST use the globally unique `^t-[Goal]-[Num]` syntax.
4. **Mandatory Triage:** All new information must be classified as Knowledge, Action, or Both. Actionable items MUST never be buried only in text.

## 4. Skills & Scripts
- **Authorized Skills:** `.agents/skills/*`
- **Automation Scripts:** `.agents/bin/*`
