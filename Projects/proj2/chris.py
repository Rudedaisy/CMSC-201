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
    board = [[character for character in line.strip()] for line in boardFile.readlines()]
    printBoard(board)
    fillCoordinates(board)
    boardFile.close()

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
        autofill(board, row, column,symbol, willStep)
        if willStep == "no":
            printBoard(board)
        return fillCoordinates(board)

def autofill(board,row,column,symbol, willStep):
    if not board[row][column]!=" " or row<0 or row>len(board) or column<0 or column>len(board[0]):
        board[row][column]=symbol
        if willStep=="yes":printBoard(board)
        [autofill(board,row+mod[0],column+mod[1],symbol,willStep) for mod in [[-1,0],[0,1],[1,0],[0,-1]]]
        #autofill(board,row-1,column,symbol,willStep)
        #autofill(board,row,column+1,symbol,willStep)
        #autofill(board,row+1,column,symbol,willStep)
        #autofill(board,row,column-1,symbol,willStep)
         
def printBoard(board):
    for row in board:
        for column in row:
            print(column.strip("\n"), end = "")
        print()

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
        if rowNum < 0 or rowNum > rowMax  :
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
        
def dissectCoordinates(response):
    coordinates = response.split(",")
    rowNum, columnNum = int(coordinates[0]), int(coordinates[1])
    return rowNum, columnNum

main()
