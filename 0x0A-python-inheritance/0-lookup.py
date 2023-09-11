#!/usr/bin/python3
"""
function that returns a list of attributes and methods of an object
"""


def lookup(obj):
    """
    returns a list of object attributes and methods
    """
    info = dir(obj)
    return info
