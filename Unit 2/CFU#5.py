num_pennies = int(input("Enter the number of pennies: "))
num_nickels = int(input("Enter the number of nickels: "))
num_dimes = int(input("Enter the number of dimes: "))
num_quarters = int(input("Enter the number of quarters: "))
num_loonies = int(input("Enter the number of loonies: "))
num_toonies = int(input("Enter the number of toonies: "))

total_value = (num_pennies + 5*num_nickels + 10*num_dimes + 25*num_quarters + 100*num_loonies + 200*num_toonies)/100
#total_value is calculated by finding the total number of cents, then dividing that number by 100 to get the amount in dollars and cents
#this prevants rounding errors resulting from pythons float imprecision

print()
print("Number of pennies:", num_pennies) 
print("Number of nickels:", num_nickels) 
print("Number of dimes:", num_dimes) 
print("Number of quarters:", num_quarters)
print("Number of loonies:", num_loonies) 
print("Number of toonies:", num_toonies)
print("Total value of coins: $"+"{:.2f}".format(total_value)) # The {.2f} is used to format a float to two decimal places

change = (total_value-total_value//1)*100

quarters = int(change/25)
dimes = int((change%25)/10)
nickels = int(((change%25)%10)/5)
pennies = int(((change%25)%10)%5)

print("$"+str(total_value//1),f"and {quarters} quarters, {dimes} dime, {nickels} nickel, {pennies} cents")
