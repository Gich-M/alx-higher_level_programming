#!/usr/bin/python3
"""
    - Takes GitHub credentials (username and password)
            and uses the GitHub API to display your id
    - Use Basic Authentication with a personal access token
            as password to access information
            (only read:user permission is needed)
    Args:
        - username (str): GitHub username
        - password (str): personal access token
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
