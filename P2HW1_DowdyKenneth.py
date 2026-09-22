# Kenneth Dowdy
# September 22, 2026
# P1HW1
# This program calculates an exponent and performs an addition
# and subtraction calculation using integers entered by the user.

# Calculate Exponents
base_value = int(input("Enter an integer as the base value: "))
exponent_value = int(input("Enter an integer as the exponent: "))

exponent_result = base_value ** exponent_value

print()
print("-----Calculating Exponents----")
print(f"{base_value} raised to the power of {exponent_value} is {exponent_result} !!")

# Addition and Subtraction
starting_integer = int(input("Enter an integer to add: "))
second_integer = int(input("Enter an integer to add: "))
subtract_integer = int(input("Enter an integer to subtract: "))

calculation_result = starting_integer + second_integer - subtract_integer

print()
print("-----Addition and Subtraction----")
print(f"{starting_integer} + {second_integer} - {subtract_integer} is {calculation_result}")