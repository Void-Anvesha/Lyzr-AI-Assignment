import requests
from urllib.parse import urlparse
import os

def parse_pr_url(url):
    """
    Parses a GitHub PR URL to extract owner, repo, and pull number.
    Example: https://github.com/owner/repo/pull/123
    Returns: (owner, repo, number)
    """
    parsed = urlparse(url)
    path_parts = parsed.path.strip('/').split('/')
    if len(path_parts) >= 4 and path_parts[2] == 'pull':
        return path_parts[0], path_parts[1], int(path_parts[3])
    return None, None, None

def get_pr_diff(owner, repo, number, token=None):
    """
    Fetches the raw diff of a PR.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}"
    headers = {
        "Accept": "application/vnd.github.v3.diff"
    }
    if token:
        headers["Authorization"] = f"token {token}"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch PR diff: {response.status_code} {response.text}")

def get_pr_details(owner, repo, number, token=None):
    """
    Fetches PR metadata (title, body, author, etc.).
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    if token:
        headers["Authorization"] = f"token {token}"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch PR details: {response.status_code} {response.text}")
