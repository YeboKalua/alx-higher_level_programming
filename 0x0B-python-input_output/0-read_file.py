#!/usr/bin/python3
"""reads text file and prints to std output"""


def read_file(filename=""):
    """reads and print text file"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        for line in a_file:
            print(line, end='')
        