# File:        lab4_part2.py
# Author:      Edward Hanson
# Date:        9/22/15
# Section:     18
# E-mail:      ehanson1@umbc.edu
# Description: Determines whether or not the input is a pet.


def main():
    animal = str(input("Please input an animal: "))
    animal = animal.lower()
    if animal == "cat" or animal == "dog":
        print("This is a pet.")
    else:
        print("This is not a pet.")

main()
