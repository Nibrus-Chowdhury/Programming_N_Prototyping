# Math
import math
r = int(input("What is the radius of your circle?"))
C = 2*r*math.pi
A = math.pi*r**2
print("C=",C," A=",A)
rCyl = int(input("What is the radius of the cylinder?"))
h = int(input("What is the height of the cylinder?"))
v = rCyl**2*math.pi*h
print("V=",int(v))

# Conditionals
x = int(input("Give me a number: "))
if x >= 5:
    print("Greater than or equal to 5!")
else:
    print("This number is less than 5")
