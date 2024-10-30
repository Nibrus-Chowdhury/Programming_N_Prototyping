"""
Nibrus Chowdhury
10/29/24
Period 5-6
Description: Asks the user for a password and if the password is not correct then it asks again until the user gets the password. Only 3 Chances.
"""

def check(password):
    correct = "simonsnyc"
    if password == correct:
        print("Correct! You may enter...")
    else:
        print("Wrong Password!")
def attempts():
    attempts = 0
    while attempts < 3:
        password = input("Enter the password: ")
        check(password)
        if password == "simonsnyc":
            attempts = 3 
        else:
            attempts += 1
        if attempts == 3 and password != "simonsnyc":
            print("Access denied. No more attempts left.")
attempts()
