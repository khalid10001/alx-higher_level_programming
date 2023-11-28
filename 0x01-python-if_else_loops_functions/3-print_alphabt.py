#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    if alpha != 'q' and alpha != 'e':
        print("{:c}".format(alpha), end="")
