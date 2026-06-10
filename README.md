# Claude GitHub Agent

A CLI-based AI agent that answers natural language questions about GitHub repositories using Claude's tool use (function calling) capability.

## What It Does

Ask the agent questions in plain English — it decides which GitHub API calls to make, fetches the data, and returns a natural language answer.

```
You: what repos does Str8-88s have?
[calling tool: list_repos]
Agent: Str8-88s has 3 public repositories...

You: show me the recent commits to Str8-88s/devops-dashboard
[calling tool: get_commits]
Agent: Here are the 10 most recent commits...
```

## How It Works

1. User enters a natural language question
2. Claude reasons over the question and decides which tool(s) to call
3. The tool executes a GitHub API call and returns the data
4. Claude reasons over the result and returns a natural language answer
5. Loop continues until the user exits

When a tool is needed, two API calls happen: one for Claude to decide what to call, and a second after the tool result is returned for Claude to form the final answer.

## Tools

| Tool | Description |
|------|-------------|
| `get_repo` | Fetch metadata for a repository — stars, forks, language, description, open issues |
| `list_repos` | List public repositories for a GitHub user, sorted by stars |
| `get_commits` | Fetch the 10 most recent commits for a repository |

GitHub public endpoints are used — no GitHub token required.

## Setup

**Prerequisites:** Python 3.11+, an [Anthropic API key](https://console.anthropic.com)

```bash
# Clone the repo
git clone https://github.com/Str8-88s/claude-github-agent.git
cd claude-github-agent

# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set your Anthropic API key
export ANTHROPIC_API_KEY=sk-ant-...   # macOS/Linux
$env:ANTHROPIC_API_KEY = "sk-ant-..." # Windows PowerShell
```

## Running the Agent

```bash
py agent.py       # Windows
python agent.py   # macOS/Linux
```

Type `exit` or `quit` to stop.

## Example Queries

```
how many stars does Str8-88s/devops-dashboard have?
what repos does Str8-88s have?
show me the recent commits to Str8-88s/devops-dashboard
what language is Str8-88s/devops-dashboard written in?
what is the most starred repo for Str8-88s?
```

## Project Structure

```
claude-github-agent/
├── agent.py           # Main agent loop — input, Claude API calls, tool dispatch
├── tools.py           # Anthropic tool definitions + tool execution dispatch
├── github_client.py   # httpx wrapper for GitHub REST API endpoints
└── requirements.txt
```

## Stack

- **Python 3.11+**
- **[anthropic](https://pypi.org/project/anthropic/)** — Anthropic Python SDK
- **[httpx](https://pypi.org/project/httpx/)** — HTTP client for GitHub API calls