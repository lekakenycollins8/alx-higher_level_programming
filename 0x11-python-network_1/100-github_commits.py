#!/usr/bin/python3
"""Lists 10 commits from repository "rails" by user: rails"""


from sys import argv
import requests


if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner_name, repo_name)
    response = requests.get(url)
    user_commit = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(user_commit[i].get('sha'), \ 
                    user_commit[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
