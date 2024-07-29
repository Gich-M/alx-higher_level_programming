#!/bin/bash
# Takes in a URL
# Sends a POST request to the passed URL
# email: test@gmail.com
# subject: I will always be here for PLD
# Displays the body of the response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}"