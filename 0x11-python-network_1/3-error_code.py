#!/usr/bin/python3
"""sends a request to URL and displays body decoded in utf8"""


import urllib.request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('ascii')
        print(body)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
