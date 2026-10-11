
# Name: Kenneth Dowdy
# Date: 10/10/2026
# Assignment: P3LAB - Money Counting
# Description: Calculate the dollars and coins needed to make an amount of money.

# Pseudocode:
# Ask the user to enter an amount of money.
# Convert the amount to cents.
# Calculate the number of dollars using floor division.
# Subtract the dollar value from the remaining cents.
# Repeat for quarters, dimes, nickels, and pennies.
# Display only denominations that are needed.
# Use singular names for one and plural names for more than one.

# Get the amount of money from the user
amount = float(input("Enter the amount of money: "))

# Convert dollars to cents
cents = int(round(amount * 100))

# Calculate dollars
dollars = cents // 100
cents = cents - (dollars * 100)

# Calculate quarters
quarters = cents // 25
cents = cents - (quarters * 25)

# Calculate dimes
dimes = cents // 10
cents = cents - (dimes * 10)

# Calculate nickels
nickels = cents // 5
cents = cents - (nickels * 5)

# Remaining cents are pennies
pennies = cents

# Display dollars
if dollars > 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(f"{dollars} dollars")

# Display quarters
if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(f"{quarters} quarters")

# Display dimes
if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(f"{dimes} dimes")

# Display nickels
if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(f"{nickels} nickels")

# Display pennies
if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")