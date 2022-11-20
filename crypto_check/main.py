#!/usr/bin/python
import argparse
from price import check
from add import add
from display import display

parser = argparse.ArgumentParser(description="Script checks value of crypto curencie.")
parser.add_argument('--display', help='Display all your crypto', action='store_true')
parser.add_argument('--add', help='Add new crypto. Usage --add Symbol Amount', nargs=2)
parser.add_argument('--update', help='Update amount of owned crypt. Usage --update Symbol Amount', nargs=2)
parser.add_argument('--price', help='Check crypto price. All prices are checked against USDT Usage --price Symbol')
args = parser.parse_args()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if args.display:
        display()
    elif args.add is not None:
        add(args.add[0], args.add[1])
    elif args.update is not None:
        print(args.update)
    elif args.price is not None:
        data = check(args.price)
        print(data)

