#!/usr/bin/python3
for num in range(0, 100):
    a = num / 10
    b = num % 10

    if a < b and a != b and num != 89:
        print("{0:0=2d}, ".format(num), end='')
    if num == 89:
        print("{0}".format(num))
