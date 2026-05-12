# Semantic Goal-Bridging Memory (SGBM) 🧠

[![Memory Architecture](https://img.shields.io/badge/Architecture-SGBM-blue.svg)](#)
[![Agent Compatible](https://img.shields.io/badge/Agent-Agnostic-success.svg)](#)

SGBM is a lightweight, tool-agnostic memory architecture designed to solve **Context Window Bloat** and **Context Drift** for LLM agents working on long-running, multi-goal projects. 

Instead of forcing your agent to read thousands of lines of past conversation history or dumping entire documentation folders into the prompt, SGBM uses a **"Lazy Load"** approach. It enables agents to semantically discover relevant past goals and surgically extract only the precise lines of context they need.

---

## 🎯 The Problem it Solves
When agents work on complex repositories over weeks or months:
1. **Context Window Bloat:** Feeding the agent the entire project history is expensive and leads to "lost in the middle" hallucination.
2. **Context Drift:** Agents make brilliant architectural decisions in Turn 5, but forget them by Turn 20 because the decision was never formally documented.
3. **Siloed Goals:** An agent working on "Feature B" doesn't realize it should reuse the auth logic established during "Feature A".

## ✨ How SGBM Works (The Dual-Layer Architecture)

SGBM organizes project memory into two optimized layers:

### 1. The Inter-Goal Bridge (Discovery)
* **File:** `Goals/Goals.md`
* **How it works:** This is the master index. Every active and completed goal is listed here with **Semantic Tags** (e.g., `[Tags: #auth, #react]`).
* **Agent Behavior:** On startup, the agent reads *only* this file. It scans the tags to instantly know which past goals might contain relevant context for the current task.

### 2. The Intra-Goal Navigator (Surgical Extraction)
* **File:** `Goals/<Goal_Name>/Knowledge.md`
* **How it works:** Instead of reading a massive knowledge file, every `Knowledge.md` is protected by a strict front-matter header:
  * **`## Goal Snapshot`**: A brief summary of the "Bottom Line" and "Key Decisions".
  * **`## Context Map`**: An index mapping the rest of the file's headers to specific line numbers (e.g., `- ## API Specs (Line 140+)`).
* **Agent Behavior:** The agent reads *only* the top portion. If the Snapshot looks relevant, it uses the Context Map to perform a targeted `read_file(start_line: 140)` to grab exactly what it needs.

---

## ⚙️ How it Tracks: The "Bubble Up" Protocol

To prevent "Context Drift", SGBM enforces a strict programmatic workflow for updating memory. Deep knowledge is useless if the front-matter index isn't updated.

1. **Logging (`sgbm-logger.py`)**: As the agent works, its actions and intents are quietly logged to a temporary `session_log.json`.
2. **Milestone Reached**: When a task is completed in `Progress.md`, a trigger fires.
3. **Synthesis (`sgbm-syncer.py`)**: The temporary session log is digested to extract the "Strategic Why".
4. **The Bubble Up**: The agent appends the detailed findings to the bottom of `Knowledge.md`, but it is **programmatically forced** to also update the `Context Map` and `Goal Snapshot` at the top. 
5. **Validation (`sgbm-validator.py`)**: A quality gate ensures that no task is marked complete unless the SGBM front-matter has been properly synced.

---

## 🚀 Porting SGBM to Your Project

SGBM is **Tool-Agnostic**. It works with Gemini CLI, Copilot, Cursor, or any agent that has file read/write capabilities.

### 1. Copy the Directory Skeleton
Replicate this folder structure in your project root:
```text
your-project/
├── Goals/
│   ├── Goals.md                <-- The Master Index
│   └── Template_Goal/          <-- Use this when starting new tasks
│       ├── Progress.md
│       └── Knowledge.md        <-- Must contain the SGBM Front-Matter
└── .agents/
    └── bin/
        ├── sgbm-loader.py      <-- Tag extraction script
        ├── sgbm-logger.py      <-- Session event logger
        ├── sgbm-syncer.py      <-- Auto-documentation script
        └── sgbm-validator.py   <-- CI/CD Quality Gate
```

### 2. Configure the Agent Skills
SGBM is driven by two critical agent skills that automate the tracking protocol. You must ensure these exist in your new workspace's `.agents/skills/` folder:
*   **`goal-manager`**: Automates the initialization of new goals, ensuring they are created with the correct SGBM Template (Snapshot and Context Map) and initialized with semantic tags in the master index.
*   **`knowledge-manager`**: The core engine of the "Bubble Up" protocol. It ensures that any new deep knowledge added to a goal is concurrently synthesized into the `Goal Snapshot` and mapped in the `Context Map`.

### 3. Instruct Your Agent (The "Soft Hook")
Add the following to your agent's system prompt (e.g., `.cursorrules`, `AGENTS.md`, or Custom Instructions):

> **Memory Protocol (SGBM):**
> 1. **Orientation:** On your first turn, read `Goals/Goals.md`. Use semantic tags to identify relevant past goals.
> 2. **Lazy Load:** Do not read full `Knowledge.md` files. Read ONLY the `## Goal Snapshot` and `## Context Map` at the top. Use the Context Map for targeted `read_file` operations.
> 3. **The Bubble Up Rule:** When you make a significant architectural decision or reach a milestone, you MUST append the details to `Knowledge.md`. You are strictly forbidden from doing so without concurrently updating the `## Context Map` and `## Goal Snapshot` headers.

### 3. Wire Up the Scripts (The "Hard Hooks" - Optional but Recommended)
To make the system bulletproof, bind the Python scripts to your environment's lifecycle events:
* **Pre-prompt Injection:** Run `sgbm-loader.py` to automatically inject the tag index into the agent's context window on startup.
* **Git Pre-Commit Hook:** Run `sgbm-validator.py` to physically block `git commit` if the agent updated code but forgot to "Bubble Up" the documentation.

---

## 🛠️ Usage Example

**User:** "We need to add OAuth to the new Dashboard goal."
**Agent (Internal Monologue):**
1. *Reads `Goals.md`. Sees `[Tags: #auth, #security]` under the old `Backend Revamp` goal.*
2. *Reads lines 1-30 of `Goals/Backend Revamp/Knowledge.md`.*
3. *Reads `Goal Snapshot`: "Decided on JWT tokens over session cookies due to scaling requirements."*
4. *Reads `Context Map`: `- ## JWT Implementation Details (Line 210)`*
5. *Reads lines 210-250 of the file to get the exact secret keys and token expiration logic.*
6. *Implements Dashboard Auth perfectly matching the legacy system, using only 500 tokens of context.*

---

## 🔄 Maintenance & Updates

To ensure the SGBM system stays healthy as your project grows, follow these maintenance protocols:

### 1. The Release Log (`RELEASES.md`)
When updating the SGBM core (scripts, skills, or protocols), document the changes in `RELEASES.md`. This allows other agents or collaborators to safely "patch" their local SGBM folders by following the **Integration Instructions** provided in each release entry.

### 2. Agent Handover & System Context
When a new agent (or a new session) initializes this workspace, it MUST verify the current system health:
- **Integration Checklist**:
    1. Check `.agents/bin/` for core scripts.
    2. Review `RELEASES.md` for the current protocol version.
    3. Verify `Goals/Goals.md` for active goal alignment.
- **Maintenance State**:
    - **Current Blocker**: [None]
    - **Planned Updates**: Logic for automated `sgbm-validator.py` cross-checks.
    - **Environment**: Python 3.x required for `.agents/bin/` scripts.

---
*Built for developers who want their AI agents to remember the 'Why', not just the 'What'.*
