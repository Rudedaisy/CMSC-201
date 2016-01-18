# File:        hw4_part4.py
# Written by:  Edward Hanson
# Date:        10/2/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Prints numbers 1-100 and displays messages at multiples of 3
#              and 5.


def main():
    for num in range(1, 101, 1):
        if (num % 3) == 0 and not ((num % 5) == 0):
            print("Better three hours too soon than a minute too late.")
        elif (num % 5) == 0 and not ((num % 3) == 0):
            print("Where do you see yourself in five years?")
        elif (num % 5) == 0 and ((num % 3) == 0):
            print("In the future, everyone will be world-famous for 15 minutes.")
        else:
            print(num)

main()
