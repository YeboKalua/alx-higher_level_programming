#!/usr/bin/python3
"""writes to file"""


def write_file(filename="", text=""):
    """writes text to a file"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)