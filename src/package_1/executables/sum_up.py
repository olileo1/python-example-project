import argparse
from package_1.module_1 import my_sum

def cmdline_parse():
    parser = argparse.ArgumentParser(
        description="Sum to inputs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("x", help="The value for x", type=int)
    parser.add_argument("y", help="The value for y", type=int)
    args = parser.parse_args()
    return args

def main():
    args = cmdline_parse()
    if (args.x is not None) and (args.y is not None):
        print("x: " + str(args.x))
        print("y: " + str(args.y))
        out = my_sum(args.x, args.y)
        print("Result: " + str(out))
    else:
        print("No sum possible")

if __name__ == '__main__':
    main()