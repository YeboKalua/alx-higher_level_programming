#!/usr/bin/python3
"""reads text file and prints to std output"""


def read_file(filename=""):
    """reads and print text file"""
    with open(filename) as a_file:
        a_file.read()
        print(a_file)
        