# File:        hw6_part2.py
# Written by:  Edward Hanson
# Date:        10/17/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Calculates a weighted grade from data contained in another file.


def main():
    # asks user to input name of file to open
    fileName = str(input("Please enter the name of the file that contains the grades: "))

    # initialzes the variables
    gradesFile = open(fileName, "r")
    grades = []
    percentsEarned = []
    rowWorth = 0
    rowGrade = 0
    rowPoints = 0
    lineNumber = 0
    columnNumber = 0
    finalGrade = 0

    # creates 2-D list based off of file
    for line in gradesFile:
        grades.append([])
        line.strip()
        grades[lineNumber] = line.split()
        lineNumber += 1
    
    # calculates percentage of grade earned per line
    for row in grades:
        for column in row:
            if columnNumber == 0:
                rowWorth = float(column)
            else:
                rowPoints += float(column)
            columnNumber += 1
        rowGrade = rowWorth * (rowPoints / (columnNumber - 1))
        percentsEarned.append(rowGrade)
        # resets counters to be used for upcoming row
        columnNumber = 0
        rowWorth = 0
        rowGrade = 0
        rowPoints = 0

    # sums up all percentages of grade earned
    for percent in percentsEarned:
        finalGrade += percent
    print("Your final weighted score is " + str(finalGrade) + "%.")

    # closes the opened file
    gradesFile.close()

main()
