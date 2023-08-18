#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    key_list = list(a_dictionary)
    if key in key_list:
        del a_dictionary[key]
    return a_dictionary
