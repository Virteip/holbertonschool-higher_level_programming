#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for i in range(list_length):
        try:
            p = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            p = 0
        except TypeError:
            print("wrong type")
            p = 0
        except IndexError:
            print("out of range")
            p = 0
        finally:
            list_3.append(p)

    return my_list_3
