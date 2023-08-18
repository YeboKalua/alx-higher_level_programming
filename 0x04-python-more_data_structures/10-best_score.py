#!/usr/bin/python3
def best_score(a_dictionary):
    max_v = max(a_dictionary.values())
    max_key = [k for k, v in a_dictionary.items() if v == max_v]
    return max_key
