import math
r = int(input("What is the radius of your circle?"))
C = 2*r*math.pi
A = math.pi*r**2
print("C=",C," A=",A)
rCyl = int(input("What is the radius of the cylinder?"))
h = int(input("What is the height of the cylinder?"))
v = rCyl**2*math.pi*h
print("V=",v)
