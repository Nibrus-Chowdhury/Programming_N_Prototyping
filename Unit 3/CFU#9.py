"""
Nibrus Chowdhury
10/17/2024
Period 5-6
"""

import random

rolls = int(input("How many rolls do you want to do? In this game you have to guess the dice roll of the computer"))
points = 0

for i in range(rolls):
    def round():
        x = random.randint(1,6)
        global points
        guess = int(input("What is your guess?"))
        if guess == x:
            points = points + 6
            print("You are correct! +6 points")
        else:
            points = points - 1
            print("You are incorrect! -1 points")
    round()
print("Your final score is: "+str(points))
