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
1. Identify the name of the new goal. If the user hasn't provided a clear name, ask them for one.
2. Create a new folder in the `Goals/` directory with the goal name.
3. Inside the new folder, create:
   - A `Progress.md` file with a template to track status, milestones, and daily execution notes.
   - A `Knowledge.md` file using the **SGBM Template**:
     ```markdown
     # Knowledge: [Goal Name]

     ## Goal Snapshot
     > **Bottom Line:** [Intent of the goal]
     > **Key Decisions:** [Initial setup decisions]
     > **Reusable Hooks:** []

     ## Context Map
     * - ## Goal Snapshot: (Line 3+)
     * - ## Context Map: (Line 10+)

     ---
     ## Detailed Knowledge
     ```
   - A `bin/` folder for supporting execution files.
4. Update the `Goals/Goals.md` file:
   - Add the new goal to the list and increment the counts.
   - **Mandatory**: Append semantic tags directly underneath the goal using the format: `  - [Tags: #tag1, #tag2]`.
5. Confirm with the user that the new goal has been set up with SGBM structures.
