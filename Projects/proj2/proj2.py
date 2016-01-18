# File:        proj2.py
# Written by:  Edward Hanson
# Date:        11/26/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Inputs a file and fills in corresponding spaces depending on
#              user's instructions.

CLEAR = " "

def main():
    fileToOpen = checkInput("", "None", "None", "textFile", "a file name for input: ")
    boardFile = open(fileToOpen, "r")
    # creates a 2D list from the inputed file
    board = [[character for character in line.strip()] for line in boardFile.readlines()]
    printBoard(board)
    fillCoordinates(board)
    boardFile.close()

# fillCoordinates() allows the user to select which starting coordinates they prefer to use
# Input: the game board, the coordinates of user's choice, and whether or not the user wants to view every iteration
# Output: the board once it has been filled as per user's request
def fillCoordinates(board):
    rotateOrder = ["-1,0", "0,1", "1,0", "0,-1"]
    coordinates = checkInput("", len(board) - 1, len(board[0]) - 1, "coordinates", "the coordinates you would like to start\nfilling at in the form \"row,col\", or 'Q' to quit: ")
    if coordinates == "Q":
        print("Thank you for using the autofill program!")
        return board
    else:
        row, column = dissectCoordinates(coordinates)
        symbol = str(checkInput("", "None", "None", "symbol", "a symbol to fill with: "))
        print("Would you like to show each step of the recursion?")
        willStep = checkInput("", "None", "None", "yes/no", "\"yes\" or \"no\": ")
        if board[row][column] != CLEAR:
            # prevents the code from filling spaces if the initial coordinate is a border
            printBoard(board)
            return fillCoordinates(board)
        direction = 0
        board = autoFill(board, rotateOrder, direction, symbol, row, column, willStep)
        if willStep == "no": 
            printBoard(board)
        return fillCoordinates(board)

# autoFill takes the board and fills empty spaces depending on the initial coordinate inputed by the user
# Input: the board, the order of rotation when filling, the current direction to check if a fill is possible,
#        the current coordinate that will be rotated around, whether or not to print every iteration
# Output: the board once its spaces have been filled accordingly
def autoFill(board, rotateOrder, direction, symbol, baseRow, baseColumn, willStep):
    if direction == 4: 
        return board
    if board[baseRow][baseColumn] == CLEAR:
        board[baseRow][baseColumn] = symbol
        if willStep == "yes": 
            printBoard(board)
        autoFill(board, rotateOrder, direction, symbol, baseRow, baseColumn, willStep)
        return autoFill(board, rotateOrder, direction + 1, symbol, baseRow, baseColumn, willStep)
    row, column = dissectCoordinates(rotateOrder[direction])
    if board[baseRow + row][baseColumn + column] == CLEAR:
        board[baseRow + row][baseColumn + column] = symbol
        baseRow, baseColumn = (baseRow + row), (baseColumn + column)
        direction = 0
        if willStep == "yes": 
            printBoard(board)
        autoFill(board, rotateOrder, direction, symbol, baseRow, baseColumn, willStep)
        return autoFill(board, rotateOrder, direction + 1, symbol, baseRow, baseColumn, willStep)
    else: return autoFill(board, rotateOrder, direction + 1, symbol, baseRow, baseColumn, willStep)
    
# printBoard() prints the current board layout as a readable board
# Input: the current board
# Output: a readable board
def printBoard(board):
    for row in board:
        for column in row:
            print(column.strip("\n"), end = "")
        print()

# checkInput() determines whether or not an inputed value is valid
# Input: the user's input, a max row/column value (if applicable), what kind of value is being validated,
#        and a comment that determines what is being asked for
# Output: a valid response
def checkInput(response, rowMax, columnMax, whatToCheck, askFor):
    response = str(input("Please enter " + str(askFor)))
    # checks for text file inputs
    if whatToCheck == "textFile" and (response[-4:] == ".dat" or response[-4:] == ".txt"): 
        return response
    elif whatToCheck == "textFile": 
        print("\tInvalid file name!\n\tFile name must end in either '.dat' or '.txt'.")
    # checks for coordinates entered
    if whatToCheck == "coordinates":
        if response == "Q": 
            return response
        rowNum, columnNum = dissectCoordinates(response)
        if rowNum >= 0 and columnNum >= 0 and rowNum <= rowMax and columnNum <= columnMax: 
            return response
        if rowNum < 0 or rowNum > rowMax: 
            print("\t", str(rowNum), "is not a valid row value; please enter a value\n\tbetween 0 and", str(rowMax), "inclusive.") 
        if columnNum < 0 or columnNum > columnMax: 
            print("\t", str(columnNum), " is not a valid column value; please enter a value\n\tbetween 0 and", str(columnMax), "inclusive.")
    # checks for the symbol being used (cannot use multple characters)
    if whatToCheck == "symbol" and len(response) == 1: 
        return response
    elif whatToCheck == "symbol": 
        print("\tIncorrect Input!\n\tSymbol used must have only one character.")
    # checks if a valid 'yes' or 'no' was used
    if whatToCheck == "yes/no" and (response == "yes" or response == "no"): 
        return response
    elif whatToCheck == "yes/no": 
        print("\tIncorrect Input!\n\tResponse must be either 'yes' or 'no' in all lowercase")
    return checkInput(response, rowMax, columnMax, whatToCheck, askFor)
        
# dissectCoordinates takes in coordinates as a string and splits them into individual 'row' and 'column' variables
# Input: the coordinates in the format of a string
# Output: the coordinates in the format of individual variables
def dissectCoordinates(response):
    coordinates = response.split(",")
    rowNum, columnNum = int(coordinates[0]), int(coordinates[1])
    return rowNum, columnNum

main()
