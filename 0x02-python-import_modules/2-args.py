#!/usr/bin/python3


def main():
    if len(sys.argv) == 1:
        print("0 arguments.")
        return
    if (len(sys.argv) - 1) == 1:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
        return
    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv)-1))

        for iterate in range(1, len(sys.argv)):
            print("{0}: {1}".format(iterate, sys.argv[iterate]))
        else:
            return

if __name__ == '__main__':
    import sys
    main()
