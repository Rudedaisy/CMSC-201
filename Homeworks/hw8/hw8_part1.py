# File:        hw8_part1.py
# Written by:  Edward Hanson
# Date:        11/20/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: takes in a user generated list and prints it out in reverse order using a 
#              recursive function


def main():
    myList = []
    response = int(input("Enter a number to append to the list, or '-1' to stop: "))
    while response != -1:
        myList.append(response)
        response = int(input("Enter a number to append to the list, or '-1' to stop: "))
    print("The list you entered is:", myList)
    print("The reversed list is: ")
    rev(myList, len(myList))

# rev() is a recursive function that prints out a list of integers in reverse order
# Input: the list to be printed and an index value that approaches 1
# Output: printed numbers from the given list in reverse order
def rev(myList, iteration):
    print(myList[iteration - 1])
    if iteration == 1:
        return 1
    else:
        return rev(myList, iteration - 1)

main()
