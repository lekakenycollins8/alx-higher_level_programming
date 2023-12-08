#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_sc = None
    best_key = None
    for key, value in a_dictionary.items():
        if best_sc is None or value > best_sc:
            best_sc = value
            best_key = key
    return best_key
