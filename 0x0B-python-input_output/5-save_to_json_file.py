#!/usr/bin/python3
"""json module"""
import json


def save_to_json_file(my_obj, filename):
    """saves object to filename"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))