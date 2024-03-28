#!/usr/bin/python3
"""sends request to url and displays body"""


from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
