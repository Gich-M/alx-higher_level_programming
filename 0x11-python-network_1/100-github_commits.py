#!/usr/bin/python3
"""
    - List 10 commits (from the most recent to oldest):
                        repository “rails” by the user “rails”
    - Use the GitHub API, https://developer.github.com/v3/repos/commits/
    - Print all commits by: `<sha>: <author name>` (one by line)
    Args:
        - repository name: The name of the repository
        - owner name: The name of the owner
"""
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    res = requests.get(url)

    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
