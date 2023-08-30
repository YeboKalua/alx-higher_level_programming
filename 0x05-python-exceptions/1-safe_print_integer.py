#!/usr/bin/python3
"""
Function that checks for integer and prints it
"""
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False