#!/usr/bin/python3


def main():
    tot = 0
    for iterate in range(1, len(sys.argv)):
        tot += int(sys.argv[iterate])
    else:
        return print("{}".format(tot))

if __name__ == '__main__':
    import sys
    main()
