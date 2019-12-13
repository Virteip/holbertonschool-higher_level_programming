#!/usr/bin/python3


def main():
    iterate = 0
    for iterate in dir(hidden_4):
        if iterate[0:1] != '_':
            print("{}".format(iterate))
if __name__ == '__main__':
    import hidden_4
    main()
