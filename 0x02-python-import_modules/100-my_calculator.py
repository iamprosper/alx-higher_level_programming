#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    result = 0
    if (operator == "+"):
        result = add(a, b)
    elif (operator == "-"):
        result = sub(a, b)
    elif (operator == "*"):
        result = mul(a, b)
    elif (operator == "/"):
        result = div(a, b)
    else:
        print("Unknown operator. Available operator: +, -, * and /")
        sys.exit(1)
    print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
