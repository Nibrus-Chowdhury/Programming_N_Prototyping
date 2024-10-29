"""
Nibrus Chowdhury
10/29/24
Period 5-6
Description: Asks the user for a password and if the password is not correct then it asks again until the user gets the password. Only 3 Chances.
"""

password = input("Enter Password: ")
chance = 0
while chance != 3:
        if password == "simonsnyc":
            print("Correct! You may enter...")
            chance = 3
        else:
            print("Wrong Password!")
            password = input("Enter Password: ")
            chance += 1
            if chance == 3:
                print("Too many chances.")
