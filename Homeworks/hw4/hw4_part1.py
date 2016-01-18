# File:        hw4_part1.py
# Written by:  Edward Hanson
# Date:        10/1/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Draws a right triangle using an inputted character and height.


def main():
    print("Welcome to Right-Triangle Producer!")
    height = int(input("Please enter a whole number for the height: "))
    symbol = str(input("Please enter a symbol to make the triangle out of: "))
    for lineNumber in range(1, (height + 1), 1):
        print(symbol*lineNumber)

main()
