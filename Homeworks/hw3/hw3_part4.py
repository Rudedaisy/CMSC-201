# File:        hw3_part4.py
# Written by:  Edward Hanson
# Date:        9/19/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Determines the state of a generator through two switches.


def main():
     print("Please enter 'y' for yes and 'n' for no.")
     firstSwitch = str(input("Is the first switch on? (y/n) "))
     secondSwitch = str(input("Is the second switch on? (y/n) "))

     if firstSwitch == secondSwitch:
          print("The generator is off.")
     else:
          print("The generator is on.")

main()
