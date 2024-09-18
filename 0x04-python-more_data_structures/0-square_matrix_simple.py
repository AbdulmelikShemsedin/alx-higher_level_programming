#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix[:][:]
    idx = 0
    for i in new:
        indx = 0
        for j in i:
            new[idx][indx] = j * j
            indx += 1
        idx += 1
    return new
