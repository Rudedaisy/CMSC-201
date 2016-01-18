# File:        hw5_part4.py
# Written by:  Edward Hanson
# Date:        10/13/2015
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Takes two user inputted lists and finds a pairwise sum.


def main():
    list1 = []
    list2 = []
    combList = []
    response = ""
    while response != "end":
        response = input("Please enter a number (or \"end\" to stop): ")
        if response != "end":
            list1.append(int(response))
    response = "" # restarts "respose" to be used for the next loop
    print("Thank you for completing the first list.")
    while response != "end":
        response = input("Please enter a number (or \"end\" to stop): ")
        if response != "end":
            list2.append(int(response))
    print("Thank you for completing the second list.\nPairwise sum:", end="")
    for element in range(0, len(list1)):
        combList.append(list1[element] + list2[element])
    print(combList)

main()
