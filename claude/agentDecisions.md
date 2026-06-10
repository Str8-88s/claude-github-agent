# Decisions — GitHub Agent

Technical decisions made during development. Logged in real time during sessions.

Format:
> **Decision:** [what you chose]  
> **Alternatives considered:** [what you didn't pick]  
> **Why:** [reasoning]

---

**Decision:** Language  
**Choice:** Python 3.11+  
**Alternatives considered:** Node.js + TypeScript (original plan)  
**Why:** Target JD explicitly lists Python as a primary requirement. Building in Python sends the right signal. TypeScript depth is already demonstrated by the DevOps Dashboard.

---

**Decision:** HTTP client  
**Choice:** `httpx`  
**Alternatives considered:** `requests`, `urllib`  
**Why:** Modern Python HTTP client with a clean API and first-class type hint support. Standard choice in async Python contexts; familiar to any Python engineer reviewing the code.

---

**Decision:** GitHub API access  
**Choice:** Public endpoints, no auth  
**Alternatives considered:** Personal access token for higher rate limits  
**Why:** Keeps setup friction at zero — no token required to run the demo. Public endpoints allow 60 requests/hour unauthenticated, which is sufficient for a CLI demo. Can add optional token support later if needed.

---

**Decision:** CLI interface  
**Choice:** Simple `input()` loop  
**Alternatives considered:** `argparse` (single query per invocation), `click` (richer CLI)  
**Why:** Conversational loop is more compelling as a demo — shows the agent handling multiple questions in sequence. `argparse` would require re-running the script for every question. `click` adds a dependency with no meaningful benefit here.

---

**Decision:** Scope  
**Choice:** Three tools only — `get_repo`, `list_repos`, `get_commits`  
**Alternatives considered:** Additional tools (issues, pull requests, releases)  
**Why:** Tight scope produces a finished, defensible artifact. Three tools are enough to demonstrate the full agent loop and tool selection logic. More tools add surface area without adding interview value.

---

**Decision:** Model  
**Choice:** `claude-sonnet-4-6`  
**Alternatives considered:** `claude-sonnet-4-20250514` (outdated string)  
**Why:** Current model string as of June 2026. Older string returned 404 from the API.
