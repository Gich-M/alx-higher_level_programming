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
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get(
        "https://api.github.com/repos/{}/commits".format(sys.argv[3]),
        auth=auth)
    for commit in res.json():
        print(
            "{:s}: {:s}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")))
