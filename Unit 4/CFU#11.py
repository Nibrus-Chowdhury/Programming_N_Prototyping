"""
Nibrus Chowdhury
10/25/24
Period 5-6
Description: This code allows the user to print out options 1 through 3 with each of them doing something different and unique.
"""
num = int(input("What function do you want to run?"))

if num == 1:
    # Option 1
    for i in range(10,71,10):
        print(i)
elif num == 2:
    # Option 2
    for i in range(0,21):
        print(i/2)
else:
    # Option 3
    for i in range(99,0,-1):  
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print("Take one down and pass it around,")
        if i > 1:
            print(f"{i-1} bottles of beer on the wall.\n")
        else:
            print("No more bottles of beer on the wall.")
        
