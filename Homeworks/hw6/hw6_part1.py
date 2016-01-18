# File:        hw6_part1.py
# Written by:  Edward Hanson
# Date:        10/17/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Adds names to a separate .txt file.


def main():
    # intialize variables
    nameList = []
    response = ""
    nameFile = open("names.txt", "a")

    # adds to name list depending on user input
    while response != "DONE":
        response = str(input("Please enter a name (or \"DONE\" to stop): "))
        if response != "DONE":
            nameList.append(response)

    # adds elements from name list to names.txt file
    for name in nameList:
        nameFile.write("Hello " + name + "!\n")

    # closes the opened file
    nameFile.close()

main()
