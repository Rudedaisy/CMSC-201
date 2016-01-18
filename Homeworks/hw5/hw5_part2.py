# File:        hw5_part2.py
# Written by:  Edward Hanson
# Date:        10/9/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Prints a box using increasing integers. The width and height
#              are determined by the user.


def main():
    print("Welcome to counting box creator!")
    width = int(input("Please enter a positive integer for the width: "))
    height = int(input("Please enter a positive integer for the height: "))
    area = width * height
    heightNum = 0
    numList = []
    for element in range(1, height+1):
        numList.append([])
    for number in range(1, area+1):
        if number % width != 0:
            numList[heightNum].append(str(number) + " ")
        else:
            numList[heightNum].append(str(number) + " ")
            heightNum += 1
    for row in numList:
        for column in row:
            print(column, end = "")
        print(end = "\n")

main()
