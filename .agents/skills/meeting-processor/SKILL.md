---
name: meeting-processor
description: Processes structured or unstructured meeting notes to extract action items, map them to goals, and manage tasks. Requires explicit user confirmation before modifying tracking files.
---

# Meeting Processor Skill

Use this skill when the user provides meeting notes (structured or unstructured) and needs to extract action items and integrate them into the AI OS goal and task tracking system.

## Input
- Structured or unstructured meeting notes.

## Execution Steps

1. **Analyze and Extract**: Analyze the provided meeting notes to extract all action items. For each action item, determine:
   - **Owner**: Who is responsible (default to User if unstated).
   - **Action**: What needs to be done.
   - **Due Date**: When it needs to be completed (if mentioned).
   - **Context**: Any relevant context to help map the action to a goal.

2. **Goal Mapping**: 
   - For each action item, find a matching goal in the central index (`Goals/Goals.md`) by comparing the context of the action item with the **semantic tags** of the active goals.
   - Ensure the task doesn't already exist in the matched goal's `Tasks.md` file.

3. **Drafting Strategy**:
   - **Existing Goal**: If a matching goal is found and the task is new, prepare to add the action item as a new task in that goal's `Tasks.md` file.
   - **New Goal**: If no matching goal exists, prepare to invoke the `goal-manager` skill to create a new goal based on the action item's context.
   - **Updates**: If a task already exists but the meeting notes indicate a status change or update, prepare to update the existing task.

4. **User Confirmation (Mandatory)**: 
   - Present a clear summary to the user detailing the proposed changes:
     - New tasks to be added to specific existing goals.
     - Existing tasks to be updated (e.g., status changes).
     - New goals to be created.
   - **CRITICAL**: The agent is empowered to decide the mapping, but MUST obtain explicit user confirmation before applying any changes to `Goals.md`, any `Tasks.md`, or creating new goals.

5. **Execution & Notification**: 
   - Upon user confirmation, apply the changes to the respective files.
   - Provide a final confirmation to the user stating clearly that "New tasks have been added/updated" or "Task statuses have been changed".
