#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 2, 2021
# This file adds two numbers entered by the user


def main():
    # Function that calculates the sum of both numbers
    number1 = int(input("Input your first number: "))
    number2 = int(input("Input your second number: "))
    # User input
    sum = number1 + number2
    # Process
    print("The sum of your two numbers is: {}".format(sum))


if __name__ == "__main__":
    main()
