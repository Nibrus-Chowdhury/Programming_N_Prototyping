"""
Nibrus Chowdhury
10/29/24
Period 5-6
Description: Asks the user for a password and if the password is not correct then it asks again until the user gets the password. Only 3 Chances.
"""

option = int(input("Which version do you want to play? (Enter 1 or 2)"))

if option == 1:
    password = "simonsnyc"
    user = input("Enter password: ")
    while user != "simonsnyc":
        print("Wrong Password!")
        user = input("Enter passowrd: ")
    print("Correct! You may enter...")
else:
    def check(password1):
        correct = "simonsnyc"
        if password1 == correct:
            print("Correct! You may enter...")
        else:
            print("Wrong Password!")
    def attempts():
        attempts = 0
        while attempts < 3:
            password1 = input("Enter the password: ")
            check(password1)
            if password1 == "simonsnyc":
                attempts = 3 
            else:
                attempts += 1
            if attempts == 3 and password1 != "simonsnyc":
                print("Access denied. No more attempts left.")
    attempts()
