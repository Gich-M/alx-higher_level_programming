#!/usr/bin/python3
"""
    - Takes in URL
    - Sends a request to the URL
    - Displays the body of the response (decoded in utf-8)
    - Manage urllib.error.HTTPError exceptions
    - Print: Error code: followed by the HTTP status code
"""
from urllib import request, error
import sys

if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
