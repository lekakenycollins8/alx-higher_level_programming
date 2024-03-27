#!/bin/bash
# sends a JSON POST and displays body of response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
