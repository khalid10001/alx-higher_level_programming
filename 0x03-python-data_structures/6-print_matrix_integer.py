#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for sub in matrix:
        if len(sub) == 0:
            print()
        for x in range(len(sub)):
            print("{:d}".format(sub[x]),
                    end="\n" if x is len(sub) - 1 else " "
