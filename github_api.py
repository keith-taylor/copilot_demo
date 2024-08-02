# github_api_client.py

import requests
import os
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Fetch GitHub repositories for a user")
parser.add_argument("username", help="GitHub username")
args = parser.parse_args()
username = args.username


def get_repos(username):
    """
    Fetch the list of repositories for a given GitHub username.

    Parameters:
    username (str): GitHub username

    Returns:
    list: List of repository names
    """
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    repos = response.json()
    repo_names = [repo["name"] for repo in repos]
    return repo_names


if __name__ == "__main__":
    repo_names = get_repos(username)
    print(f"Repositories for user {username}: {repo_names}")
