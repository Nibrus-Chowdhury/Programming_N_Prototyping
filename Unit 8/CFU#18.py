'''
Nibrus Chowdhury
1/7/2024
Period: 5-6
Description: This is a program that asks the user for a list of items and their prices then gives the user a tally of the items the user entered as well as the price and at the bottom the final price of all the items using lists.
'''
items = []
prices = []
total = 0
num = int(input("How many prices do you want to add?"))
for i in range(num):
    y = input("Enter item name: ")
    items.append(y)
    x = float(input("Enter a price: "))
    prices.append(x)
    total = total + x
print("Item:		Cost:")
for i in range(num):
    print(f"{i+1}. {items[i]} - ${prices[i]}")
print(f"\nThe total cost of all your items is ${total}.")
