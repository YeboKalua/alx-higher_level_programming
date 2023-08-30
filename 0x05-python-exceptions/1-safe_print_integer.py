#!/usr/bin/python3

def safe_print_integer(value):
    """
    Function that checks for integer and prints it
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
