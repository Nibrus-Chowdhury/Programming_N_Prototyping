"""
Nibrus Chowdhury
10/19/2024
Period 5-6
Description: This program rolls a dice through the random library and the user guesses a number from 1 to 6 and if they get it right then they get +6 points and if they get it wrong they get -1 point and the total is written at the end.
"""
import random

def randomNum():
    return random.randint(1,6)

def guess(total):
    user_guess = int(input("What's your guess? "))
    roll = randomNum()
    print(f"You rolled a {roll}")
    
    if user_guess == roll:
        total += 6
        print("Correct guess! +6 points.")
    else:
        total -= 1
        print("Incorrect guess! -1 point.")
  
    return total

def rolls(num_rolls, total):
    if num_rolls == 0:
        return total
    else:
        total = guess(total)
        return rolls(num_rolls - 1, total)
    
    
num_rolls = int(input("Let's play dice! How many times do you want to roll the dice?"))
total = 0
final_total = rolls(num_rolls, total)
print(f"The total score is: {final_total}")
