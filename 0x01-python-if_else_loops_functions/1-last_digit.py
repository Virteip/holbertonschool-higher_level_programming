#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if last > 5:
    print("The last digit of {0} is {1} and is greater than 5".format(number, last))
elif last == 0:
    print("The last digit of {0} is {1} and is 0".format(number, last))
elif last < 6 and number != 0:
    print("The last digit of {0} is {1} and is less than 6 and not 0".format(number, last))
