"""
Nibrus Chowdhury
10/21/24
Period 5-6
Description: User guesses a random number from 1 to 10 and the computer responds if that is high or low until the user gets the answer 
"""
import random

ran_num = random.randint(1,10)
attempts = 0

def attempt(ran_num, attempts):
    user_guess = int(input("What is your guess? 1-10"))
    if user_guess == ran_num:
        print(f"It took you: {attempts} attempts to guess the number")
    else:
        attempts += 1
        if user_guess > ran_num:
            print("Too high")
            attempt(ran_num, attempts)
        else:
            print("Too low")
            attempt(ran_num, attempts)
attempt(ran_num, attempts)
