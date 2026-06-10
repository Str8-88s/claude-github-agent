# Claude Instructions — Cluade-GitHub Agent Project

## Session Startup Protocol

At the start of every session, Claude MUST:
1. Read `.claude/agentInstructions.md` — stable project context and rules
2. Read `.claude/agentProgress.md` — current session log, file structure, outstanding work
3. Read `.claude/agentDecisions.md` — all technical decisions made to date
4. Confirm context is loaded before responding to any task

Do not proceed with any work until all three files have been read.

---

## Session Closing Protocol

At the end of every session (when the user says "end of session", or asks to update files):
1. Ask: "Ready to update the context files?"
2. If yes, generate updated versions of these files as downloadable artifacts:
   - `.claude/agentProgress.md`
   - `.claude/agentDecisions.md`
3. Present the git command:
```
git add .claude/instructions.md .claude/progress.md .claude/decisions.md
git commit -m "chore: update session context files — [description]"
git push
```

---

## Project Purpose

A CLI-based AI agent that answers natural language questions about GitHub repositories using Claude's tool use (function calling) capability.

**Two goals:**
1. Teach how Claude agents and tool use work end to end
2. Produce a defensible portfolio artifact demonstrating Python + Anthropic SDK proficiency

This project exists because the target job description lists Python as a primary requirement. The DevOps Dashboard demonstrates TypeScript depth. This demonstrates Python competence and AI integration skills.

---

## Stack

- **Language:** Python 3.11+
- **Anthropic SDK:** `anthropic` Python package
- **HTTP:** `httpx` for GitHub API calls
- **Type hints:** throughout, no exceptions
- **Dependencies:** `requirements.txt`
- **CLI:** simple `input()` loop

---

## Tools Implemented

### `get_repo`
Fetches metadata for a given owner/repo: stars, forks, description, primary language, open issues, homepage.

### `list_repos`
Lists public repositories for a given GitHub username, sorted by stars.

### `get_commits`
Fetches recent commits for a given owner/repo — message, author, date, SHA (short).

---

## Agent Loop

1. User enters a natural language question at the CLI
2. Claude reasons over the question and decides which tool(s) to call
3. Tool executes the GitHub API call (public endpoints, no auth required)
4. Result is returned to Claude as a tool result
5. Claude reasons over the data and returns a natural language answer
6. Loop continues until user exits

---

## Scope Boundaries

This is intentionally tight. Do not expand scope without explicit discussion:
- No frontend
- No database
- No authentication (public GitHub endpoints only)
- No streaming
- No async (synchronous `httpx` calls are sufficient)
- No test suite (out of scope for this artifact)

If a suggestion would expand scope, flag it and confirm before proceeding.

---

## Career Context

**Current role:** SDET in healthcare IT  
**Target role:** Senior Full-Stack Developer  
**Why this project:** Target JD explicitly calls out Python as a strong requirement. Building in Python signals willingness and ability to work in their primary language.

---

## How We Work

**Claude's role:**
- Guide through the implementation step by step
- Explain what each piece does and why — this is also a learning exercise
- Answer questions as they come up
- Call out scope creep before it happens

**Rules of engagement:**
- Explain before implementing — don't drop code without context
- One step at a time — don't get ahead of where we are
- Direct communication, no preamble
- Flag non-obvious Python/SDK behaviors before they cause confusion
- Decisions get logged to `.claude/agentDecisions.md` in real time

---

## Technical Decision Framework

Format:
> **Decision:** [what you chose]  
> **Alternatives considered:** [what you didn't pick]  
> **Why:** [reasoning]

---

## Environment Notes

- OS: Windows (PowerShell)
- Editor: VS Code
- Python: 3.11+ (confirm with `python --version`)
- Use `python` not `python3` on Windows unless aliased
- Virtual environment: `venv` inside project root (`.venv/`)
- Activate on Windows: `.venv\Scripts\Activate.ps1`
