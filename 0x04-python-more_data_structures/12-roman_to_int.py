#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {'I': 1, 'V': 5, 'X', 10, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if type(roman_string) == str:
        for ch in characters:
            result += values.get(ch)
    return (result)
