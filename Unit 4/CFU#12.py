"""
Nibrus Chowdhury
10/29/24
Period 5-6
Description: Asks the user for a password and if the password is not correct then it asks again until the user gets the password. Only 3 Chances.
"""

password = input("Enter Password: ")
password1(password)
global chance
chance = 0
def chance():
    if chance == 3:
        print("Too many tries.")
    else:
        password1(password)
def password1(password):
    while password != "simonsnyc":
        print("Wrong Password!")
        password = input("Enter Password: ")
        chance += 1
        chance()
    print("Correct! You may enter...")
