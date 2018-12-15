# Shawn Potter
# 12/15/2018
# passgen.py
# simple password generator

import random

#initial interface
def interface():
    print("Welcome to Password Generator!")
    
    while True:
        try:
            passLength = int(input("Please enter how many characters you would like your password to be: "))
            if passLength > 64:
                print("Choose a number lower than 64")
                continue
            elif passLength <= 0:
                print("Choose a number greater than 0")
                continue
            else:
                break
        except:
            print("You must enter a number!")
    
    while True:
        try:
            specialChar = str(input("Do you want to use special characters? (Y/N): "))
            specialChar = specialChar.lower()
            break
        except:
            print("Type 'Y' or 'N'")
    
    generator(passLength, specialChar)

#generate the password
def generator(length, special):
    if special == "y":
        charList = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    else:
        charList = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    password = "".join(random.sample(charList,length))
    print("Password: " + password)
    tryAgain(length, special)

#create function to ask if the user wants to generate another password
def tryAgain(length, special):
    again = str(input("Do you want to generate another password? (Y/N): "))
    again = again.lower()
    if again == "y":
        generator(length, special)
    else:
        print("Thanks for using Password Generator!")

#execute        
interface()