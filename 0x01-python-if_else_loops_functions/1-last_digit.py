#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    l = number % 10
else:
    l = number % -10

if l > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(number, l))
elif l == 0:
    print("Last digit of {0} is {1} and is 0".format(number, l))
elif l < 6 and number != 0:
    print("Last digit of {0} is {1}\
 and is less than 6 and not 0".format(number, l))
