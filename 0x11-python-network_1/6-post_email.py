#!/usr/bin/python3
"""
    - Takes in a URL and an email address
    - Sends a POST request to the passed URL with the email as a parameter
    - Displays the body of the response
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    res = requests.post(url, data={'email': email})
    print(res.text)
