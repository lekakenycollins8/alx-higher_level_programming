#!/usr/bin/python3
"""script that sends a request to URL and displays value of X-Request-Id"""


import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    header = 'X-Request-Id'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page = response.headers.get(header)
    print(page)
