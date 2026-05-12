# Skill: Brainstorming & Analysis

This skill leverages the "Party Mode" philosophy to explore multiple solutions and challenge assumptions.

## 📝 Workflow
1. **Persona Mapping**: Identify which defined personas from `.agents/roles/` (e.g., Architect, CoS, PM) should weigh in. Do NOT hallucinate personas outside of the OS Kernel.
2. **Multi-Perspective Brainstorming**: Present the problem from 3 different viewpoints:
    - **The Optimist**: Focus on innovation and "Blue Sky" features.
    - **The Realist**: Focus on MVP, speed to market, and technical simplicity.
    - **The Critic**: Focus on edge cases, technical debt, and potential failures.
3. **Synthesis**: Combine the best ideas into a "Recommended Path".
4. **SGBM Handoff**: You MUST invoke the `knowledge-manager` skill to execute the "Bubble Up" protocol and save the Synthesis into the relevant `Knowledge.md`.

## 📜 Execution Rules
- Explicitly state which defined persona is speaking during the brainstorming phase.
- Use the "Pre-Mortem" technique: Ask "If this feature fails in 6 months, why did it happen?"
- **Strict Dependency**: NEVER write to `Knowledge.md` directly. Always delegate to `knowledge-manager`.
