# File:        lab8.py
# Written By:  Edward Hanson
# Date:        10/20/2015
# Section:     18
# E-mail:      ehanson1@umbc.edu
# Description: 


def main():
    # initializes all variables
    carFile = open("cars.txt", "r")
    matchFile = open("results.txt", "w")
    color = ""
    doors = ""
    cost = ""
    carList = []
    potentialList = []
    CAR_COLOR = "red"
    NUM_DOORS = 4
    CAR_COST = 30000
    
    # creates 2-D list with inputted file
    for line in carFile:
        line = line.strip()
        carList.append(line.split(","))
    
    # creates list of cars that match criterion
    for row in carList:
        if row[1] == CAR_COLOR and row[2] == str(NUM_DOORS) and int(row[4]) < CAR_COST:
            potentialList.append(row)

    # places list of matched cars into another text file
    matchFile.write("Here are cars that match your critereon:\n")
    for line in potentialList:
        matchFile.write(line[0] + " --- $" + line[4] + "\n")

main()
