---
name: goal-manager
description: Creates a new goal folder and tracking files when a new discussion thread starts that doesn't belong to an existing goal.
---

# Goal Manager Skill

Use this skill when the user starts a new discussion thread that doesn't belong to any existing goal, or when instructed to initialize a new goal tracking structure.

## Context
The workspace uses a specific folder structure to track activities and goals:
- There is a central `Goals/` folder.
- Inside `Goals/`, there is a `Goals.md` file that lists all active, inactive, and archived goals.
- Each goal has its own subfolder inside `Goals/` (e.g., `Goals/[Goal Name]/`).
- Inside each goal's subfolder, there are standardized tracking files: `Progress.md`, `Knowledge.md` (featuring a `[Context Index]` at the top), and a `bin/` directory.

## Execution Steps
When invoked to create a new goal:
1. **PM Coach Interrogation**: Analyze the user's request. 
   - If the request is "Output-driven" (e.g., "build a script", "make a file"), you MUST push back. Ask: *"What is the specific Target Outcome we are trying to achieve? How will we measure its success (KPIs)?"*
   - Do NOT proceed with goal creation until the **Target Outcome**, **Success Metrics (KPIs)**, and **Definition of Done (DoD)** are clearly defined.
2. Identify the final name of the new goal.
3. Create a new folder in the `Goals/` directory with the goal name.
4. Inside the new folder, create:
   - A `Progress.md` file with a template to track high-level milestones.
   - A `Tasks.md` file with a markdown table for granular day-to-day behavioral tasks.
   - A `Knowledge.md` file using the **SGBM Outcome-Driven Template**:
     ```markdown
     # Knowledge: [Goal Name]

     ## Goal Snapshot
     > **Target Outcome:** [The specific result or change we are achieving]
     > **Success Metrics (KPIs):** [Measurable criteria]
     > **Definition of Done (DoD):** [Binary completion criteria]
     > **Key Decisions:** [Initial setup decisions]

     ## Context Map
     * - ## Goal Snapshot: (Line 3+)
     * - ## Context Map: (Line 9+)

     ---
     ## Initial Requirements
     ```
   - A `bin/` folder for supporting execution files.
5. Update the `Goals/Goals.md` file:
   - Add the new goal to the list and increment the counts.
   - **Mandatory**: Use the enriched metadata schema featuring the Target Outcome:
     ```markdown
     n. **[Goal Name]**: [Target Outcome Statement]
       - [Status: Active]
       - [Priority: P1]
       - [Due: None]
       - [Stakeholders: User]
       - [Blocked By: None]
       - [Last Review: YYYY-MM-DD]
       - [Tags: #tag1, #tag2]
     ```
6. Confirm with the user that the new goal has been set up with SGBM Outcome-Driven structures.
