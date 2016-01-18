# File:        lab5.py
# Author:      Edward Hanson
# Date:        9/29/15
# Section:     18
# E-mail:      ehanson1@umbc.edu
# Description: Tests a word on whether or not it is a palindrome.


def main():
    word = input("Please enter a word: ")
    word = word.lower()
    reverseWord = ""
    for char in range(len(word), 0, -1):
        reverseWord = reverseWord + word[char - 1]
    if word == reverseWord:
        print(word, "is a palindrome.")
    else:
        print(word, "is not a palindrome.", word, "reversed is '" +  reverseWord + "'.")

main()
