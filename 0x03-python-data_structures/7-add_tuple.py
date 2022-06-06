#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_len = len(tuple_a)
    tuple_b_len = len(tuple_b)

    if(tuple_a_len > 0 and tuple_a_len < 2):
        tuple_a = (tuple_a[0], 0)
    elif(tuple_a_len == 0):
        tuple_a = (0, 0)
    elif(tuple_a_len > 2):
        tuple_a = (tuple_a[0], tuple_a[1])

    if(tuple_b_len > 0 and tuple_b_len < 2):
        tuple_b = (tuple_b[0], 0)
    elif(tuple_b_len == 0):
        tuple_b = (0, 0)
    elif(tuple_b_len > 2):
        tuple_b = (tuple_b[0], tuple_b[1])

    add_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (add_tuple)
