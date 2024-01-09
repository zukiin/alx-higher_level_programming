#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    even_ints = []

    for num in my_list:
        if (num % 2 == 0):
            even_ints.append(True)
        else:
            even_ints.append(False)

    return even_ints
