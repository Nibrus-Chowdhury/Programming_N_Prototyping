'''
Nibrus Chowdhury
Period: 5-6
1/2/2025
Description: A review of built in formatting functions in Python and creating/running functions.
'''

# Function & Variable Declaration
box = "bRead"

def formatting(box):
    userInput = int(input("Choice? (1,2,3,4,5,6,7)"))
    if userInput == 1:
        # Capitalize function
        print(box.capitalize())
    elif userInput == 2:
        # Find and return the position of a value in the string
        print(box.find("a"))
    elif userInput == 3:
        # Return true if the variable is a number
        print(box.isdigit())
    elif userInput == 4:
        # Output the variable all lowercase
        print(box.lower())
    elif userInput == 5:
        # Output the variable all uppercase
        print(box.upper())
    elif userInput == 6:
        # Replace an index item for another item
        print(box.replace("d","g"))
    else:
        print("not a valid option")

formatting(box)
