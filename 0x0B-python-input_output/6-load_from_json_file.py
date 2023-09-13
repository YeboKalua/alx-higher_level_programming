#!/usr/bin/python3
"""json module"""
import json


def load_from_json_file(filename):
    """creates object from json text"""
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            file.read(json.loads(line))
        