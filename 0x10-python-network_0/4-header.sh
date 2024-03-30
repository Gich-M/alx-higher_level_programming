#!/bin/bash
# Takes in a URL as an argument
# Header variable `X-School-User-Id must be sent with the value 98
# Sends a GET request to the URL
# Displays the body of the response
curl -sH "X-School-User-Id: 98" "${1}"