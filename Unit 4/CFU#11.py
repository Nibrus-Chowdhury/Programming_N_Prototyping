"""
Nibrus Chowdhury
10/25/24
Period 5-6
Description: This code allows the user to print out options 1 through 3 with each of them doing something different and unique.
"""
ask = int(input("Which function do you want to run? (1, 2, or 3)"))
if ask == 1:
    # Option 1
    for i in range(10,71,10):
    print(i)
elif ask == 2:
    # Option 2
    for i in range(0,21):
    print(i/2)
else:
    # Option 3
    for i in range(99,-1,-1):
    print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
    print("Take one down and pass it around,")
    print(f"{i-1} bottles of beer on the wall.\n")
