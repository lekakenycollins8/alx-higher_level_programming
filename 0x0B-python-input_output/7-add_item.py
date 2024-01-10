#!/usr/bin/python3
"""Module that adds all arguments to a Python list, then save them to a file"""


from sys import argv
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

if os.path.exists(filename):
    existing_list = load_from_json_file(filename)
else:
    existing_list = []
existing_list.extend(argv[1:])
save_to_json_file(existing_list, filename)
