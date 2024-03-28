#!/usr/bin/python3
"""sends a POST request to URL with email as parameter"""


from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    email_value = {'email': email}
    response = requests.post(url, data=email_value)
    print(response.text)
