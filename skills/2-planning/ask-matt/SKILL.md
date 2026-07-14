---
name: ask-matt
description: Ask which skill, flow, or MCP fits your situation. The master router over all 36+ skills and MCPs in this repo.
disable-model-invocation: true
---

# Ask Matt (Master Router)

You don't remember every skill or MCP, so ask. Use this guide to navigate the 36+ available skills and MCP tools, mapped to their specific workflow phases.

## 1. The Main Flow: Idea → Ship
The route most work travels. You have an idea and want it built.
- **`/grill-with-docs`** / **`/grill-me`** / **`/grilling`**: Sharpen the idea by relentless interview. Start here to refine requirements before writing code.
- **`/to-spec`**: Synthesize the conversation into a concrete Spec document.
- **`/to-tickets`**: Break the Spec into independent tracer-bullet tickets.
- **`/wayfinder`**: For huge efforts too big for one session — chart a shared map of investigation tickets.
- **`/implement`**: Build each ticket using TDD internally.
- **`/tdd`**: Write tests first, then build the behavior.
- **`/code-review`**: Two-axis code review (Standards + Spec) before committing.
- **`/scrutinize`**: Deep, outsider-perspective review of the PR/plan.
- **`/resolving-merge-conflicts`**: Fix git merge conflicts safely.

## 2. Design & Architecture (Coupled with MCP)
- **`/codebase-design`**: Deep-module vocabulary for designing module boundaries and interfaces.
- **`/improve-codebase-architecture`**: Scan for and surface codebase deepening/refactoring opportunities.
- **`/domain-modeling`**: Sharpen project vocabulary (ubiquitous language) and write ADRs.
- **`/prototype`**: Build throwaway code to answer a design question visually or logically.
- **`draw.io` (MCP)**: Generate or read diagrams, flowcharts, and architecture maps.
- **`StitchMCP` (MCP)**: Generate and apply UI screens, design systems, and visual components automatically.

## 3. Incident Response
When things break, follow these steps strictly.
- **`/debug-mantra`**: Recite the 4-step debugging mantra to stop guessing and start falsifying hypotheses.
- **`/diagnosing-bugs`**: Deep diagnosis loop for hard bugs, performance issues, or regressions.
- **`/post-mortem`**: Write the canonical RCA (Root Cause Analysis) after landing a fix.

## 4. Enterprise & Delegation
- **`GG-Research` (NotebookLM MCP)**: Ask NotebookLM to run zero-token research over large company knowledge bases, synthesize findings, or generate podcasts.
- **`/research`**: Send a background agent to read API docs or primary sources while you continue working.
- **`/qwen-agent`**: Delegate menial, low-risk, high-volume tasks (like renames/formatting) to a cheap Qwen-backed subagent.
- **`/triage`**: Triage issues and manage your backlog.

## 5. Content, Writing & Teaching
- **`/management-talk`**: Translate engineering updates into executive summaries (VP/PM friendly).
- **`/edit-article`**: Refine and polish written articles.
- **`/writing-beats`**: Structure the flow and beats of a piece of writing.
- **`/writing-fragments`**: Structure short text snippets and transitions.
- **`/writing-shape`**: Organize paragraphs and layout for readability.
- **`/writing-great-skills`**: Guide on how to write new custom AI skills.
- **`/obsidian-vault`**: Search, read, and create notes in the Obsidian vault.
- **`/teach`**: Get 1-on-1 tutoring via guided codebase exercises.
- **`/scaffold-exercises`**: Create course structures and exercise directories for the team.
- **`/englishmania-manual`**: Router to the overarching English Mania workflow methodology.
- **`/wizard`**: Run an interactive onboarding wizard.

## 6. Context Management & Guardrails
- **`/claude-handoff`** / **`/handoff`**: Compact context into a handoff file so you can open a fresh session without losing memory.
- **`/loop-me`**: Break out of an AI circular thinking loop.
- **`/qwenchance`**: Prevent the agent from looping or exhausting context limits on long tasks.
- **`/git-guardrails-claude-code`**: Add safety hooks blocking dangerous git commands.
- **`/setup-pre-commit`**: Add husky/lint-staged hooks for code formatting.
- **`/setup-matt-pocock-skills`**: Setup issues/labels for a new repo.
- **`/setup-ts-deep-modules`**: Setup TS configs for deep modules.
- **`/migrate-to-shoehorn`**: Migrate `as` type assertions in test files.
