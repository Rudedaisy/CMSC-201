# File:        hw2.py
# Written by:  Edward Hanson
# Date:        9/13/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: This program demonstrates the use of different operations
#              in an expression.


# Question 1: 
# Expected output: 24
num1 = (7 + 1) * 3
print("Question 1 evaluates to:", num1)
# Actual output: 24
# Explanation: Parentheses first (8), then multiplication (24).

# Question 2:
# Expected output: 2
num2 = (12 % 5)
print("Question 2 evaluates to:", num2)
# Actual output: 2
# Explanation: The remainder of 12 / 5 is 2. Therefore, 12 % 5 is 2.

# Question 3:
# Expected output: 21
num3 = (21 % 49)
print("Question 3 evaluates to:", num3)
# Actual output: 21
# Explanation: 21 cannot be divided a single time by 49 without resulting
#              in a non-integer quotient. For this reason, 21 / 49 would
#              result in a remainder of 21. Thus, 21 % 49 is 21.

# Question 4:
# Expected output: 2
num4 = (5 - 3) + (10 - 5) * (8 % 2)
print("Question 4 evaluates to:", num4)
# Actual output: 2
# Explanation: Parentheses first (2 + 5 * 0), then multiplication (0),
#              then addition (2).

# Question 5:
# Expected output: 34
num5 = 6.5 + 5 / 2 * (4 + 7)
print("Question 5 evaluates to:", num5)
# Actual output: 34.0
# Explanation: Parentheses first (11), then division (2.5), then 
#              multiplication (27.5), then addition (34.0)
#              My mistake was not taking into consideration that the
#              final value is now a float, not an integer.

# Question 6:
# Expected output: 5.0
num6 = 9 / 3 + 18 - 4 * 4
print("Question 6 evaluates to:", num6)
# Actual output: First is division (3.0) and multiplication (16),
#                then addition (21.0), then subtraction (5.0).

# Question 7:
# Expected output: 22
num7 = 8 % 3 + 5 * 4
print("Question 7 evaluates to:", num7)
# Actual output: 22
# Explanation: First is modulo (2) and multiplication (20), then
#              addition 22.

# Question 8: 
# Expected output: 79.91428571428571
num8 = 81.3 / 2.1 + ((51.5 % 65.2) * 2 / 2.5)
print("Question 8 evaluates to:", num8)
# Actual output: 79.91428571428571
# Explanation: Inner parentheses first (51.5), then multiplication within
#              the outer parentheses (103), then division within the 
#              outer parentheses (41.2), then division (38.71428571428571),
#              then addition (79.91428571428571).

# Question 9:
# Given equation: 100 - 8 * 8 + 1 / 0.5
# Solved equation: 100 - (8 * 8 + 1) / 0.5
# Target number: -30
num9 = 100 - (8 * 8 + 1) / 0.5
print("Question 9 evaluates to:", num9, "and should be", -30)

# Question 10:
# Given equation: 84 / 10 + 11 - 4 * 4
# Solved equation: (84 / (10 + 11) - 4) * 4
# Target number: 0
num10 = (84 / (10 + 11) - 4) * 4
print("Question 10 evaluates to:", num10, "and should be", 0)
