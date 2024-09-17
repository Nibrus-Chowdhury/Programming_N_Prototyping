# Greetings
name=input("Hi user, what is your name?")
print("Hi,",name+"!","Great to see you!")

# Addition
addFirst=int(input("Let me show you a neat trick! Give me a number"))
addSecond=int(input("Give me one more number"))

print("\nThese are the numbers added together:")
print(addFirst,"+",addSecond,"=",addFirst+addSecond)

# Subtraction
minuend=int(input("How about a different trick? Give me a number"))
subtrahend=int(input("Give me one more number"))

print("\nThese are the numbers subtracted:")
print(minuend,"-",subtrahend,"=",minuend-subtrahend)

# Multiplication
factor1=int(input("How about we get more complex? Give me a number"))
factor2=int(input("Give me one more number"))

print("\nThese are the numbers multiplied:")
print(factor1,"*",factor2,"=",factor1*factor2)

# Division
numerator=int(input("How about the opposite of what we just did? Give me a numerator"))
denominator=int(input("Give me a denominator"))

print("\nThese are the numbers divided by each other:")
print(numerator,"/",denominator,"=",numerator/denominator)

# Mod
mod1=int(input("Lets spice it up, no more simple operations. Give me a numerator"))
mod2=int(input("Give me a denominator"))

print("\nThis is the remainder of this operation:")
print(mod1,"%",mod2,"=",mod1%mod2)

# Change
addSecond=int(input("Lets change one of the numbers in the addition operation, give me a new number"))
print("\nThese are the NEW numbers added together:")
print(addFirst,"+",addSecond,"=",addFirst+addSecond)

subtrahend=int(input("Lets change one of the numbers in the subtraction operation, give me a new number"))
print("\nThese are the NEW numbers subtracted:")
print(minuend,"-",subtrahend,"=",minuend-subtrahend)

factor2=int(input("Lets change one of the numbers in the multiplication operation, give me a new number"))
print("\nThese are the NEW numbers multiplied:")
print(factor1,"*",factor2,"=",factor1*factor2)

denominator=int(input("Lets change one of the numbers in the division operation, give me a new number"))
print("\nThese are the NEW numbers divided by each other:")
print(numerator,"/",denominator,"=",numerator/denominator)

mod2=int(input("Lets change one of the numbers in the mod operation, give me a new number"))
print("\nThis is the NEW remainder of this operation:")
print(mod1,"%",mod2,"=",mod1%mod2)

print("Thank you for playing with me,",name+"!")
