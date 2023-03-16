#!/usr/bin/python3
def best_score(a_dictionary):
    best = ""
    big = 0
    if a_dictionary is not None or a_dictionary != {}:
        for k, v in a_dictionary.items():
            if v > big:
                big = v
                best = k
        return (best)
    return (None)
