#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) > 0:
        max_k = max(a_dictionary, key=a_dictionary.get)
        return max_k
    else:
        return None
