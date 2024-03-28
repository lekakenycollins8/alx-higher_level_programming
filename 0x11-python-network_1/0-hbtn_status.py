#!/usr/bin/python3
"""Module with script that feteches data from intranet"""


import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    page = response.read()
print("Body response:")
print("\t- type:", type(page))
print("\t- content:", page)
print("\t- utf8 content:", page)
