"""
Nibrus Chowdhury
10/29/24
Period 5-6
Description: Asks the user for a password and if the password is not correct then it asks again until the user gets the password.
"""

password = input("Enter Password: ")
while password != "simonsnyc":
    print("Wrong Password!")
    password = input("Enter Password: ")
print("Correct! You may enter...")
    
