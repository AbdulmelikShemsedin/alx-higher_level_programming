#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    index = 0
    new = my_list[:]
    for i in new:
        if i % 2:
            new[index] = False
        else:
            new[index] = True
        index += 1
    return new
