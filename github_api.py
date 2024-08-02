# github_api_client.py

import requests
import os
import argparse

GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
filter_term = "3"

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
    headers = {"Authorization": f"token {GITHUB_API_TOKEN}"}
    response = requests.get(url)
    repos = response.json()
    repo_names = [repo["name"] for repo in repos]
    return repo_names


if __name__ == "__main__":
    repo_names = get_repos(username)
    print(f"\nRepositories for user `{username}` containing `{filter_term}`: \n")
    for repo_name in repo_names:
        if filter_term in repo_name.lower():
            print(repo_name)
