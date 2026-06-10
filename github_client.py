import httpx
from typing import Any

BASE_URL = "https://api.github.com"

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def get_repo(owner: str, repo: str) -> dict[str, Any]:
    """Fetch metadata for a single repository."""
    url = f"{BASE_URL}/repos/{owner}/{repo}"
    response = httpx.get(url, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    return {
        "name": data["full_name"],
        "description": data.get("description"),
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "language": data.get("language"),
        "open_issues": data["open_issues_count"],
        "homepage": data.get("homepage"),
    }


def list_repos(username: str) -> list[dict[str, Any]]:
    """List public repositories for a GitHub user, sorted by stars."""
    url = f"{BASE_URL}/users/{username}/repos"
    response = httpx.get(url, headers=HEADERS, params={"per_page": 30, "sort": "updated"})
    response.raise_for_status()
    repos = response.json()
    sorted_repos = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)
    return [
        {
            "name": r["full_name"],
            "description": r.get("description"),
            "stars": r["stargazers_count"],
            "language": r.get("language"),
        }
        for r in sorted_repos
    ]


def get_commits(owner: str, repo: str) -> list[dict[str, Any]]:
    """Fetch the 10 most recent commits for a repository."""
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"
    response = httpx.get(url, headers=HEADERS, params={"per_page": 10})
    response.raise_for_status()
    commits = response.json()
    return [
        {
            "sha": c["sha"][:7],
            "message": c["commit"]["message"].split("\n")[0],
            "author": c["commit"]["author"]["name"],
            "date": c["commit"]["author"]["date"],
        }
        for c in commits
    ]