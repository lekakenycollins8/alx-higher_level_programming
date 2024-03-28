#!/usr/bin/python3
"""Script that sends a POST request to passed URL with email as parameter"""


from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    email_value = {'email': email}
    data = urllib.parse.urlencode(email_value)
    data = data.encode('utf8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        page = response.read().decode('utf8')
    print(page)
