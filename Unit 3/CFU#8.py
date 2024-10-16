""" 
Nibrus Chowdhury
10/15/2024
Period 5-6
Description: A program that asks if you ordered delivery and then calculates the cost per person if you did and split the bill.
"""
#Version 1
print("Version 1:\n")
ordDev = input("Did you order delivery? Yes or No")
if ordDev == "Yes":
    print("Great!")
elif ordDev == "No":
    print("NO!? So who is cooking?")
else:
    print("Incorrect reponse, please type Yes or No")
    
#Version 2
print("\nVersion 2:\n")
ordDev2 = input("Did you order delivery? Yes or No")
if ordDev == "Yes":
    cost = int(input("How much did the food cost?"))
    people = int(input("How many people are splitting the order?"))
    print("The cost per person is","$"+str(cost/people))
elif ordDev == "No":
    print("NO!? So who is cooking?")
else:
    print("Incorrect reponse, please type Yes or No")
