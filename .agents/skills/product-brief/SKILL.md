# Skill: Product Briefing

This skill facilitates the creation of high-fidelity Product Specifications by acting as a "Thinking Partner" to the user.

## 📝 Workflow
1. **The Investigation Phase**: You MUST use the `codebase_investigator` sub-agent or targeted file reads to analyze the existing system before drafting. Do not guess constraints.
2. **The Discovery Phase**: Ask 3-5 high-signal questions to extract user intent, target audience, and core problem.
3. **Goal Initialization**: You MUST invoke the `goal-manager` skill to formally create the Goal directory structure before saving any documentation.
4. **Drafting the Spec**: Generate a structured markdown file (`Goals/[Goal]/Knowledge.md` or `SPEC.md` if initialized properly) containing:
    - **Problem Statement**: What are we solving?
    - **User Stories**: Who is it for and what do they want?
    - **Functional Requirements**: Core features and behaviors.
    - **Constraints & Risks**: Technical or business limitations (derived from Investigation).
    - **Success Metrics**: How do we know it works?
5. **Iteration Loop**: Present the draft and ask for specific feedback or "Counter-Intuitive" edge cases.

## 📜 Execution Rules
- Never accept a "one-line" requirement. Proactively seek depth.
- Link every Spec to a Strategic Pillar.
- **Strict Dependency**: You cannot write a Spec without first using `goal-manager`.
