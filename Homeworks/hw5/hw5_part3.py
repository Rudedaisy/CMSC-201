# File:        hw5_part3.py
# Written By:  Edward Hanson
# Date:        10/13/2015
# Section:     18
# E-mail:      ehanson1@umbc.edu
# Description: Simulates the up and down movement of a hailstone in a storm.


def main():
    height = int(input("Please input the starting height of the hailstone: "))
    print("Hail is currently at height", height)
    while height != 1:
        if height % 2 == 0:
            height = height // 2
        else:
            height = (height * 3) + 1
        print("Hail is currently at height", height)

main()
