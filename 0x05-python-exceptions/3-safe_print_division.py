#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        r = a / b
    except:
        r = None
    finally:
        print("Inside result: {0}".format(r))
        return r
