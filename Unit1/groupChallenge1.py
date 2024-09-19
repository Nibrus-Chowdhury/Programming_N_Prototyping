#Challenge 1
print("Challenge #1:\n")
length = int(input("Give me the length of the rectangle"))
width = int(input("Give me the width of the rectangle"))
perimeter = (length+width)*2
print("Perimeter of a",length,"x",width,"rectangle is",perimeter)

#Challenge 2
print("\nChallenge #2:\n")
faren = int(input("Give me a Farenheit temperature"))
celcius = (faren-32)*(5/9)
print(faren,"°F is",celcius,"°C")

#Challenge 3
print("\nChallenge #3:\n")
initVertVelo = int(input("Give me the initial vertical velocity of the object"))
time = int(input("How long did this object go up for?"))
vertDistance = (initVertVelo*time)-(1/2)*9.8*time**2
print("The vertical distance of the projectile is",vertDistance,"meters")

#Bonus Challenge:
print("\nBonus Challenge:\n")
xCoor1 = int(input("Give me the x coordinate of one point"))
yCoor1 = int(input("Give me the y coordinate of one point"))
xCoor2 = int(input("Give me the x coordinate of another point"))
yCoor2 = int(input("Give me the y coordinate of another point"))
distance = ((xCoor2-xCoor1)**2+(yCoor2-yCoor1)**2)**0.5
print("The distance between these two points is",distance,"units")
