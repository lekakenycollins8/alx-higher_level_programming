#!/usr/bin/python3
"""sends a request to URL and displays the value of X-Request-Id"""


import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    header_value = req.headers.get('X-Request-Id')
    print(header_value)
