# File:        lab7.py
# Author:      Edward Hanson
# Date:        10/13/2015
# Section:     18
# E-mail:      ehanson1@umbc.edu
# Description: 


def main():
    items = ["shoes", "socks", "hat", "belt", "blouse", "dress", "tie"]
    prices = [ 54.99, 7.11, 6.49, 22.58, 21.73, 38.99, 14.83]
    LISTLENGTH = 7
    cash = 100.00
    response = ""
    print("Welcome to our online store!")
    while response != 0:
        print("You have $ " + str(cash) + " in funds available.")
        for element in range(0, LISTLENGTH):
            print(str(element+1) + " - " + items[element] + " \t$ " + str(prices[element]))
        response = int(input("Please choose an item number to purchase, or '0' to quit: "))
        for option in range(1, LISTLENGTH + 1):
            if response == option:
                cash = cash - prices[option - 1]
                if cash < 0:
                    print("Sorry, but you are unable to afford that item\n")
                    cash = cash + prices[option - 1]
                else:
                    print("Thank you for purchasing: "+ items[option - 1]+"\n")
    print("Thank you for visiting our store!")

main()
