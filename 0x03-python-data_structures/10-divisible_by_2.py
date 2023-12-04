#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ch_div = []

    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            ch_div.append(True)
        else:
            ch_div.append(False)

    return (ch_div)
