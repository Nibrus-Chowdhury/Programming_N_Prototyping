import random
# Salutations
name = input("What is your name user?")
print(f"Hello {name}, I am glad you could be here to join me in this Random Number activity!\nFirst off I ask you to input a number and I shall generate a random number.")

# Random Numbers
userNumber = int(input("Please enter a number: "))
randNumber = random.randint(1,100)

print(f"\nRandom number generated: {randNumber}")
print(f"User picked number: {userNumber}")

# Results
print("\nResults:")
print(f"\nSum: {randNumber} + {userNumber} =",randNumber+userNumber)
print(f"Difference: {randNumber} - {userNumber} =",randNumber-userNumber)
print(f"Product: {randNumber} * {userNumber} =",randNumber*userNumber)
print(f"Quotient: {randNumber} / {userNumber} =",randNumber/userNumber)
print(f"Remainder: {randNumber} % {userNumber} =",randNumber%userNumber)
print(f"Square Root of Random Number: sqrt({randNumber}) =",randNumber**0.5)
print(f"Your Number to the Power of Random Number: {userNumber}^{randNumber} =",userNumber**randNumber)
