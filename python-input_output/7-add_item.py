#!/usr/bin/python3
"""
Module: add_item

This module contains a script that adds all
command-line arguments to a Python list
and saves them to a file as a JSON representation.

It uses the functions save_to_json_file
and load_from_json_file from
5-save_to_json_file.py and 6-load_from_json_file.py,
respectively.
"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

for i in range(1, len(argv)):
    items.append(argv[i])
save_to_json_file(filename, items)
