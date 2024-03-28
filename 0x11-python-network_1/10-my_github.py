#!/usr/bin/python3
"""takes your GitHub(username and password) and uses the GitHub API to display id"""


from sys import argv
import requests


if __name__ == "__main__":
    username = argv[1]
    token = argv[2]
    url = "https://api.github.com/user"
    headers = {
            'Authorization': "Bearer {}".format(token),
            'Accept': 'application/vnd.github+json'
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        print("Failed to retrieve user ID. Status code: {}".format(response.status_code))
