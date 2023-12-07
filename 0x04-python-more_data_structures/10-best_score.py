#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxvalue = 0
    maxkey = None
    for x, y in a_dictionary.items():
        if y > maxvalue:
            maxvalue = y
            maxkey = x
    return maxkey
