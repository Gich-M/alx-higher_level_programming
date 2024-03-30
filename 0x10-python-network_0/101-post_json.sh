#!/bin/bash
# Sends a JSON POST request (with file contents) to a URL as 1st argument.
# Filename passed as 2nd argument.
# Displays the body of the response.
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "${1}"