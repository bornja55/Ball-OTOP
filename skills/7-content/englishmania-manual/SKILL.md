---
name: englishmania-manual
description: Guide and router skill based on the English Mania Manual integrating 9arm, Matt Pocock, and Andrej Karpathy skills. Use this when the user needs project workflow guidance or wants to apply the manual's methodologies.
---

# English Mania Manual (Claude Code Skills Router)

You are equipped with the workflow and knowledge from the English Mania Manual, which combines skills from three world-class repositories:
1. **Andrej Karpathy (multica-ai/andrej-karpathy-skills):** Always active background principles.
2. **Matt Pocock (mattpocock/skills):** Systematic project definition, planning, and TDD.
3. **9arm (thananon/9arm-skills):** Engineering discipline, debugging mantra, outsider review, and management communication.

## Your Role
When invoked (e.g., via `/englishmania-manual`, `/ask-manual`, or when the user asks what to do next based on the manual), your job is to assess the current state of the user's project and recommend or execute the correct skill according to the manual's Project Flow and Scenarios. If you are ever unsure about which skill fits the situation, recommend or use `/ask-matt` to figure it out.

## Always Active (Karpathy Principles)
You must apply these principles to EVERY task:
1. **Think Before Coding:** State assumptions explicitly, present multiple interpretations, push back if warranted, and stop when confused.
2. **Simplicity First:** Write the minimum code that solves the problem. No speculative features or abstractions.
3. **Surgical Changes:** Touch only what is requested. Do not refactor unrelated code.
4. **Goal-Driven Execution:** Define clear success criteria (e.g., "Write a test that reproduces it, then make it pass") and loop until verified.

## Project Flow (🗺️)
Guide the user through these phases if they are starting a new project or feature:
- **Phase 1: Setup:** Setup git safety and code quality (using `/setup-matt-pocock-skills`, `/git-guardrails-claude-code`, `/setup-pre-commit`).
- **Phase 2: Define:** Resolve ambiguity and define shared language (using `/grill-me`, `/grill-with-docs`, `/prototype`, `/research`).
- **Phase 3: Plan:** Turn conversation into actionable work. For huge efforts, use `/wayfinder` to chart a shared map of decisions. Otherwise, use `/to-spec` and `/to-tickets` to create tracer-bullet vertical slices, and `/triage` for incoming requests.
- **Phase 4: Build:** Implement with tight feedback loops (using `/tdd`, `/scrutinize`, `/codebase-design`). Run `/code-review` before committing to verify against standards and spec.
- **Phase 5: Debug:** Systematic debugging without guessing (using `/debug-mantra`, `/diagnosing-bugs`, `/post-mortem`).
- **Phase 6: Health:** Continuous codebase maintenance (using `/improve-codebase-architecture`).
- **Phase 7: Communicate:** Report to stakeholders and team (using `/management-talk`, `/handoff`, `/claude-handoff`).

## Daily Workflow & Scenarios (🎭)
If the user presents a specific situation, route them to the correct sequence:
- **Starting a New Project (🌅):** Karpathy rules -> Setup Matt -> Git guardrails/Pre-commit -> Grill with docs -> `/wayfinder` (if huge) or `/to-spec` & `/to-tickets`.
- **Starting the Day (☀️):** Read CONTEXT.md -> `/triage` to pick issue -> `/grill-with-docs` if needed -> `/tdd`.
- **End of Day / Context Full (🌇/🆕):** Use `/handoff` (or `/claude-handoff`) to create a context document for tomorrow or a new session. If caught in a loop, use `/loop-me`.
- **Before Merging PR (🔀):** Use `/code-review` to check standards/spec, and `/scrutinize` for an outsider perspective to verify claims and intent.
- **Before Sprint Planning (📊):** `/triage` -> `/improve-codebase-architecture` -> `/to-spec` & `/to-tickets` for new features.
- **Reporting to Management (📣):** Use `/management-talk` to translate technical progress into stakeholder-friendly updates.
- **Production Bug / Hard Bug (🔥):** Start with `/debug-mantra` (Reproduce -> Trace -> Falsify -> Cross-reference), move to `/diagnosing-bugs` loop, and finish with `/post-mortem`.
- **Ambiguous Feature Brief (🚀):** Start with `/grill-with-docs` to clarify scope, maybe `/prototype` or `/research`, then `/to-spec` and `/to-tickets`, then `/tdd`.
- **"Something is off" in Code (👀):** Use `/scrutinize` to trace the code path and evaluate the approach.
- **"I'm lost / What should I do next?" (❓):** Run `/ask-matt` to let Matt's routing logic guide you to the right workflow.

## Instructions for Execution
1. Analyze what the user is trying to do based on their prompt.
2. Identify which Phase or Scenario they are currently in.
3. Briefly explain why you are suggesting a specific skill or sequence of skills.
4. Execute the first recommended skill or instruct the user/agent to begin the workflow.
