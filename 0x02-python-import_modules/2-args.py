#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        arg = "argument:"
    elif len(argv) == 1:
        print("0 arguments.")
        exit(0)
    else:
        arg = "arguments:"
    print("{} {}".format(len(argv) - 1, arg,))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))