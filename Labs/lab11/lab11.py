# File:        lab11.py
# Written By:  Edward Hanson
# Date:        11/17/15
# Section:     18
# E-mail:      ehanson1@umbc.edu
# Description: Translates english words into the "Ong" language.


def main():
    word = str(input("Please enter a word to translate into Ong: "))
    myWord = ong(word)
    myWord.translateOng()

class ong:
    def __init__(self, word):
        self.word = word

    def isVowel(self, letter):
        vowels = ["a", "e", "i", "o", "u"]
        for vowel in vowels:
            if letter.lower() == vowel:
                return True
        return False

    def translateOng(self):
        for letter in self.word:
            if self.isVowel(letter):
                print(letter, end = "")
            else:
                print(letter, end = "ong")
        print()
main()
