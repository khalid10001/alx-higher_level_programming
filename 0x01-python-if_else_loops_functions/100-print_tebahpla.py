#!/usr/bin/python3

for alpha in range(25, -1, -1):
    c = alpha + ord('A')
    if alpha % 2 == 1:
        c += 32
    print("{:c}".format(c), end="")
