# File:        lab10.py
# Written By:  Edward Hanson
# Date:        11/3/15
# Section:     18
# E-mail:      ehanson1@umbc.edu
# Description: Utilizes a Caesar Cipher to encrypt/decrypt a message.


def main():
    option = int(input("What would you like to do?\n1. Encrypt String\n2. Decrypt String\nEnter '1' or '2': "))
    shift = int(input("How much would you like to shift? (1-26): "))
    if option == 1:
        encrypt(shift)
    elif option == 2:
        decrypt(shift)
    else:
        print("You have to choose between Encrypt or Decrypt!")

def encrypt(shift):
    phrase = str(input("Enter plain text message: "))
    newPhrase = ""
    newChar = ""
    for character in phrase:
        newChar = ord(character) + shift
        if newChar > ord("Z"):
            newChar = newChar - 26
        newPhrase += chr(newChar)
    print("Your encrypted message is:", newPhrase)
def decrypt(shift):
    phrase = str(input("Enter encrypted message: "))
    newPhrase = ""
    newChar = ""
    for character in phrase:
        newChar = ord(character) - shift
        if newChar < ord("A"):
            newChar = newChar + 26
        newPhrase += chr(newChar)
    print("Your plain text message is:", newPhrase)
main()
