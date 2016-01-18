# File:        hw3_part3.py
# Written by:  Edward Hanson
# Date:        9/19/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Diagnoses a patient through a series of questions.


def main():
     print("Please enter 'y' for yes and 'n' for no to these  questions.")
     hasFever = str(input("Do you have a fever? (y/n) "))
     if hasFever == "n":
          hasStuffyNose = str(input("Do you have a stuffy nose? (y/n) "))
          if hasStuffyNose == "n":
               print("I do not detect an illness! You seem hypochondriacal.")
          elif hasStuffyNose == "y":
               print("It seems that you have a Head Cold.")
     elif hasFever == "y":
          hasRash = str(input("Do you have a rash? (y/n) "))
          if hasRash == "n":
               hasEarHurts = str(input("Do your ears hurt? (y/n) "))
               if hasEarHurts == "n":
                    print("It seems that you have a Flu.")
               elif hasEarHurts == "y":
                    print("It seems that you have an Ear Infection.")
          elif hasRash == "y":
               print("It seems that you have Measles.")

main()
