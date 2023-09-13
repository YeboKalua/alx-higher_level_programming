#!/usr/bin/python3
"""json module"""
import json


def load_from_json_file(filename):
    """creates object from json text"""
    with open(filename, mode='r') as file:
        data = json.load(file)
    return data

        