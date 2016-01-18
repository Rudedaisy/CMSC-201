# File:        proj1.py
# Written by:  Edward Hanson
# Date:        11/3/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Allows the user to play "Conway's Game of Life". Information
#              on the game's rules can be found here:
#              https://en.wikipedia.org/wiki/Conway's_Game_of_Life


def main():
    board = makeBoard()
    setBoard(board)
    iterations = input("How many iterations should I run? ")
    while checkInput(iterations, 0, "none") == False:
        print("Please enter a value greater than 0")
        iterations = input("How many iterations should I run? ")
    print("Starting Board:\n")
    printBoard(board)
    for iterationNum in range(0, int(iterations)):
        print("Iteration", (iterationNum+1), ":\n")
        board = nextIteration(board)
        printBoard(board)

# creates the board through user input
def makeBoard():
    board = []
    lineNum = 0
    elemNum = 0
    rows = input("Please enter number of rows: ")
    while checkInput(rows, 1, "none") == False:
        print("\tPlease enter a number greater or equal to 1")
        rows = input("Please enter number of rows: ")
    columns = input("Please enter number of columns: ")
    while checkInput(columns, 1, "none") == False:
        print("\tPlease enter a number greater or equal to 1")
        columns = input("Please enter number of columns: ")
    for j in range(0, int(rows)+2):
        board.append([])
        for i in range(0, int(columns)+2):
            # boarders the board with spaces to be compared against later
            if lineNum == 0 or lineNum == (int(rows)+1):
                if elemNum == (int(columns)+1):
                    elemNum = 0
                    lineNum += 1
                    board[j].append(" ")
                else:
                    board[j].append(" ")
                    elemNum += 1
            else:
                if elemNum == 0:
                    board[j].append(" ")
                    elemNum += 1
                elif elemNum == (int(columns)+1):
                    board[j].append(" ")
                    elemNum = 0
                    lineNum += 1
                else:
                    board[j].append(".")
                    elemNum += 1
    return board

# prints out the board's contents 
def printBoard(board):
    for row in board:
        for column in row:
            print(column + " ", end = "")
        print()

# initializes which cells are alive or not
def setBoard(board):
    row = ""
    column = ""
    SHIFT = -3
    while row != "q":
        row = input("Please enter the row of a cell to turn on (or 'q' to exit): ")
        if row != "q":
            while checkInput(row, 0, len(board)+SHIFT) == False:
                print("\tPlease enter a number between 0 and " + str(len(board)+SHIFT) + " inclusive...")
                row = input("Please enter the row of a cell to turn on (or 'q to exit): ")
            column = input("Please enter a column for the cell: ")
            while checkInput(column, 0, len(board[0])+SHIFT) == False:
                print("\tPlease enter a number between 0 and " + str(len(board[0])+SHIFT) + " inclusive...")
                column = input("Please enter a column for the cell: ")
            board[int(row)+1][int(column)+1] = "A"
    return board

# determines the next iteration of the board
def nextIteration(board):
    match = 0
    toLive = []
    toDie = []
    PERIMETER = [-1,0,1]
    MAX_TO_LIVE = 3
    MIN_TO_LIVE = 2
    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            if board[row][column] == ".":
                for line in PERIMETER:
                    for element in PERIMETER:
                        if board[row+line][column+element] == "A":
                            match += 1
                if match == MAX_TO_LIVE:
                    toLive.append([row, column])
                match = 0
            elif board[row][column] == "A":
                for line in PERIMETER:
                    for element in PERIMETER:
                        if board[row+line][column+element] == "A":
                            match += 1
                if (match-1) < MIN_TO_LIVE or (match-1) > MAX_TO_LIVE:
                    toDie.append([row, column])
                match = 0
    board = newBoard(board, toLive, toDie)
    return board

#creates a new board after next iteration
def newBoard(board, toLive, toDie):
    for row in toLive:
        board[row[0]][row[1]] = "A"
    for row in toDie:
        board[row[0]][row[1]] = "."
    return board

# checks if the user's input is correct
def checkInput(value, minimum, maximum):
    if minimum == "none":
        if float(value) > maximum:
            print("\tIncorrect input!")
            return False
    elif maximum == "none":
        if float(value) < minimum:
            print("\tIncorrect input!")
            return False
    else:
        if float(value) > maximum or float(value) < minimum:
            print("\tIncorrect input!")
            return False
    return True

main()
