#!/bin/bash
# Sends a request to URL and displays the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
