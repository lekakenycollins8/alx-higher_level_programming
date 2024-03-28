#!/usr/bin/python3
"""takes your GitHub(username and pat) and uses the GitHub API to display id"""


from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = argv[1]
    token = argv[2]
    auth = HTTPBasicAuth(username, token)
    url = "https://api.github.com/user"
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        print("Failed to retrieve ID. code: {}".format(response.status_code))
