#!/bin/bash
# Takes in a URL
# Sends a GET request to the URL
# Displays the body of the response (200 status code)
curl -sL "$1"