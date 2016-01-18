# File:        hw3_part5.py
# Written by:  Edward Hanson
# Date:        9/19/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Determines the day of the week using a day of the month.


def main():
     SUNDAY = 0
     MONDAY = 1
     TUESDAY = 2
     WEDNESDAY = 3
     THURSDAY = 4
     FRIDAY = 5
     SATURDAY = 6

     dayOfMonth = int(input("Please enter the day of the month: "))
     if (dayOfMonth <1) or (dayOfMonth > 31):
         print("Invalid day.")
     else:
         dayOfWeek = dayOfMonth % 7
         if dayOfWeek == SUNDAY:
             print("Today is Sunday!")
         if dayOfWeek == MONDAY:
             print("Today is Monday!")
         if dayOfWeek == TUESDAY:
             print("Today is Tuesday!")
         if dayOfWeek == WEDNESDAY:
             print("Today is Wednesday!")
         if dayOfWeek == THURSDAY:
             print("Today is Thursday!")
         if dayOfWeek == FRIDAY:
             print("Today is Friday!")
         if dayOfWeek == SATURDAY:
             print("Today is Saturday!")

main()
