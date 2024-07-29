#!/usr/bin/python3
"""
    - Takes a letter: must be sent in variable q
            If no argument is given, set q=""
    - Sends POST request to 'http://0.0.0.0:5000/search_user'
        with the letter as a parameter.
    - If the response body is properly JSON formatted and not empty,
            display the id and name like this: [<id>] <name>
    - Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
"""
import requests
import sys

if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        user = res.json()
        if res.json():
            print("[{}] {}".format(user.get("id"), user.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
