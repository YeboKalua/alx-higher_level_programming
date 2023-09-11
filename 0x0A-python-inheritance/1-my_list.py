#!/usr/bin/python3
"""
prints numbers in sorted order
"""


class MyList(list):
    '''Custom MyList class.'''
    def print_sorted(self):
        '''Method for printing sorted list.'''
        print(sorted(self))
