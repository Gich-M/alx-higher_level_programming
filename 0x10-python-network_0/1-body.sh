#!/bin/bash
# Takes in a URL sends a GET request, and Displays the body of the response (200 status code)
curl -sL "$1"
