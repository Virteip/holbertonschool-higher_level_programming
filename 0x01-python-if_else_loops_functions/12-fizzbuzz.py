#!/usr/bin/python3


def fizzbuzz():

    for i in range(1, 101):
        mod5 = i % 5
        mod3 = i % 3

        if mod5 == 0 and mod3 != 0:
            print("Buzz", end='')

        if mod3 == 0 and mod5 != 0:
            print("Fizz", end='')

        if mod3 == 0 and mod5 == 0:
            print("FizzBuzz", end='')

        if mod3 != 0 and mod5 != 0:
            print("{}".format(i), end='')

        if i != 100:
            print(" ", end='')

    print(" ", end='')
