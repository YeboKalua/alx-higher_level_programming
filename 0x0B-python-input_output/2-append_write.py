#!/usr/bin/python3
"""appends and writes to file"""


def append_write(filename="", text=""):
    """appends to file"""
    with open(filename, mode='a', encoding='utf-8') as file:
        count = file.write(text)
        return count