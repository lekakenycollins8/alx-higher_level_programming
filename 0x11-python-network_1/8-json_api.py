#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request to URL"""


from sys import argv
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = "" if len(argv) == 1 else argv[1]
    value = {'q': letter}
    req = requests.post(url, data=value)
    try:
        json_data = req.json()
        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    except ValueError:
        print("Not a valid JSON")
