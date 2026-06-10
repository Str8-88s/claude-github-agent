import json
from typing import Any
import github_client

# Tool definitions in the format the Anthropic API expects.
# Claude reads these to understand what tools are available,
# what arguments they take, and when to use them.
TOOL_DEFINITIONS: list[dict[str, Any]] = [
    {
        "name": "get_repo",
        "description": (
            "Fetch metadata for a specific GitHub repository. "
            "Use this when the user asks about a particular repo — "
            "stars, forks, language, description, open issues, or homepage."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "owner": {
                    "type": "string",
                    "description": "The GitHub username or organization that owns the repository.",
                },
                "repo": {
                    "type": "string",
                    "description": "The repository name (without the owner prefix).",
                },
            },
            "required": ["owner", "repo"],
        },
    },
    {
        "name": "list_repos",
        "description": (
            "List public repositories for a GitHub user, sorted by stars. "
            "Use this when the user asks what repos someone has, "
            "or wants to browse a user's work."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": "The GitHub username to list repositories for.",
                },
            },
            "required": ["username"],
        },
    },
    {
        "name": "get_commits",
        "description": (
            "Fetch the 10 most recent commits for a GitHub repository. "
            "Use this when the user asks about recent activity, commit history, "
            "or what changes have been made to a repo."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "owner": {
                    "type": "string",
                    "description": "The GitHub username or organization that owns the repository.",
                },
                "repo": {
                    "type": "string",
                    "description": "The repository name (without the owner prefix).",
                },
            },
            "required": ["owner", "repo"],
        },
    },
]


def execute_tool(name: str, inputs: dict[str, Any]) -> str:
    """
    Execute a tool by name with the given inputs.
    Returns the result as a JSON string to send back to Claude.
    """
    if name == "get_repo":
        result = github_client.get_repo(inputs["owner"], inputs["repo"])
    elif name == "list_repos":
        result = github_client.list_repos(inputs["username"])
    elif name == "get_commits":
        result = github_client.get_commits(inputs["owner"], inputs["repo"])
    else:
        result = {"error": f"Unknown tool: {name}"}

    return json.dumps(result)