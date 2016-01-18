# File:        hw4_part3.py
# Written by:  Edward Hanson
# Date:        10/1/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Determines whether a subject can be studied or not.


def main():
    subjects = []
    print("Please enter 10 different subjects: ")
    for subjectNum in range(1, 11, 1):
        subjects.append(input("Subject " + str(subjectNum) + ": "))
    for subjectNum in subjects:
        if subjectNum[-5: ] == "ology":
            print("You can study", subjectNum)
        else:
            print(subjectNum)
        

main()
