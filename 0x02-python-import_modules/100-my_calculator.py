#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) < 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    list_op = {"+": add, "-": sub, "*": mul, "/": div}

    if operator not in list_op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, list_op[operator](a, b)))
