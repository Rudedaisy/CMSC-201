# File:        hw7.py
# Written by:  Edward Hanson
# Date:        10/25/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Uses separate functions to manipulate an inputted list and 
#              output the results.


def main():
    response = ""
    userList = getList()
    while response != "0":
        printMenu()
        response = str(input("Please enter your choice, or '0' to exit: "))
        if response == "1":
            getMin(userList)
        elif response == "2":
            getMax(userList)
        elif response == "3":
            getMean(userList)
        elif response == "4":
            getMedian(userList)
        elif response == "5":
            userList = emptyList(userList)
        elif response == "0":
            break
        else:
            print("Incorrect input!")

# creates the list of numbers through user's input
def getList():
    userList = []
    response = ""
    print("Enter a list of integers or 'q' to end the list!")
    while response != "q":
        response = input("Enter an integer: ")
        if response != "q": 
            userList.append(int(response))
    return userList

# creates a menu of options for the user to choose from
def printMenu():
    response = ""
    print("Please choose the statistic you would like to calculate!")
    print("1. Min\n2. Max\n3. Mean\n4. Median\n5. Clear List")

# finds the minimum value of the user's list
def getMin(userList):
    minimum = 0
    skip = False
    for number in userList:
        if skip == False:
            minimum = number
            skip = True
        if number < minimum:
            minimum = number
    print("The minimum value is:", minimum)

# finds the maximum value of the user's list
def getMax(userList):
    maximum = 0
    skip = False
    for number in userList:
        if skip == False:
            maximum = number
            skip = True
        if number > maximum:
            maximum = number
    print("The maximum value is:", maximum)

# calculates the mean of the user's list
def getMean(userList):
    total = 0
    numCount = 0
    mean = 0
    for number in userList:
        total += number
        numCount += 1
    mean = total / numCount
    print("The mean value is:", mean)

# finds the median of the user's list
def getMedian(userList):
    userList.sort()
    numCount = len(userList)
    median = 0
    if numCount % 2 == 0:
        median = (userList[int(numCount/2)-1] + userList[int(numCount/2)]) / 2
    else:
        median = userList[int(numCount//2)]
    print("The median value is:", median)

# empties the current list and allows the user to make another list
def emptyList(userList):
    userList = []
    userList = getList()
    return userList
    
main()
