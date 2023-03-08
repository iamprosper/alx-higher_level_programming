#!/usr/bin/python3
def remove_char_at(string, n):
    if not(n >= len(string) or n < 0):
        string = f"{string[:n]}{string[(n+1):]}"
    return string

# print(remove_char_at("Best School", 3))
