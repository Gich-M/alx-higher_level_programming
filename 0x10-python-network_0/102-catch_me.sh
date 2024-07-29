#!/bin/bash
# Makes a request to `0.0.0.0:5000/catch_me that causes server to respond with body response message 'You got me!'.
curl -s -X GET 0.0.0.0:5000/catch_me -w "\nYou got me!"
