# File:        hw3_part2.py
# Written by:  Edward Hanson
# Date:        9/19/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Calculates the user's final grade using multiple 
#              assigment grades.


def main():
     hwWeight = float(input("Please enter homework's weight: "))
     hwGrade = int(input("Please enter homework grade: "))
     examWeight = float(input("Please enter exam's weight: "))
     examGrade = int(input("Please enter exam grade: "))
     discussionWeight = float(input("Please enter discussion's weight: "))
     discussionGrade = int(input("Please enter discussion grade: "))

     hwPoints = hwWeight * hwGrade
     examPoints = examWeight * examGrade
     discussionPoints = discussionWeight * discussionGrade
     finalGrade = hwPoints + examPoints + discussionPoints

     print("The final numerical grade is:", finalGrade)
     if finalGrade >=90:
          print("This earns you an A in the class.")
     elif finalGrade >= 80 and finalGrade < 90:
          print("This earns you a B in the class.")
     elif finalGrade >= 70 and finalGrade < 80:
          print("This earns you a C in the class.")
     elif finalGrade >=60 and finalGrade < 70:
          print("This earns you a D in the class.")
     else:
          print("This earns you an E in the class.")

main()
