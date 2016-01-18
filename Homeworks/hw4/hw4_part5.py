# File:        hw4_part5.py
# Written by:  Edward Hanson
# Date:        10/3/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Counts the number of times a character appears in a string.


def main():
    string = str(input("Please enter a string: "))
    character = str(input("Please enter a character: "))
    lowerString = string.lower()
    lowerCharacter = character.lower()
    characterCount = 0
    for segment in lowerString:
        if segment == lowerCharacter:
            characterCount += 1
    print("The character '" + character + "' appears " + str(characterCount) + " times in the string:\n\t" + string)

main()
