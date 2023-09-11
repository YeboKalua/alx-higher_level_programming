#!/usr/bin/python3
def lookup(obj):
    """
    returns a list of object attributes and methods
    """
    info = dir(obj)
    return info
    
    