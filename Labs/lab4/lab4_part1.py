# File:        lab4_part1.py
# Author:      Edward Hanson
# Date:        9/22/15
# Section:     18
# E-mail:      ehanson1@umbc.edu
# Description: Describes the weather using an inputted temperature.


def main():
    temp = int(input("Please enter the current temperature (Farenheit): "))
    if temp < 25:
        print("It's freezing outside.")
    elif temp >= 25 and temp <= 49:
        print("It's a bit chilly, remember to bundle up.")
    elif temp > 49 and temp <= 79:
        print("The weather is wonderful!")
    elif temp > 79 and temp <= 100:
        print("It's pretty hot outside.")
    else:
        print("It is way too hot.")

main()
