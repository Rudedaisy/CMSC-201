# File:        hw4_part2.py
# Written by:  Edward Hanson
# Date:        10/1/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Draws an empty box using an inputted width, height, and symbol.


def main():
    print("Welcome to Empty Box Producer!")
    width = int(input("Please enter a whole number for the width: "))
    height = int(input("Please enter a whole number for the height: "))
    symbol = str(input("Please enter a symbol to make the box out of: "))
    for lineNumber in range(1, (height + 1), 1):
        if lineNumber == 1 or lineNumber == height:
            print(symbol*width)
        else:
            print(symbol + " "*(width - 2) + symbol)

main()
