#!/usr/bin/python3
"""module about json"""
import json


def from_json_string(my_str):
    """returning from string to data structure"""
    return json.loads(my_str)
    