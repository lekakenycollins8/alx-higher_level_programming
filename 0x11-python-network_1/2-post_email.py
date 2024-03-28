#!/usr/bin/python3
"""Script that sends a POST request to passed URL with email as parameter"""


from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = argv[1]
    email_value = {'email': argv[2]}
    data = urllib.parse.urlencode(email_value)
    data = data.encode('utf8')
    header = {"Content-Type": 'application/x-www-form-urlencoded'}
    req = urllib.request.Request(url, data, header)
    with urllib.request.urlopen(req) as response:
        page = response.read().decode('utf8')
    print("Your email is: {}".format(page))
