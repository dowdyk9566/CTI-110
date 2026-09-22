# Kenneth Dowdy
# September 22, 2026
# P2LAB2
# This program uses a dictionary to store vehicle MPG information
# and calculates the gallons of gas needed for a given distance.

# Pseudocode:
# Create a dictionary containing vehicle names and their MPG.
# Get the keys from the dictionary.
# Display the keys.
# Ask the user to enter a vehicle.
# Display the MPG for the selected vehicle.
# Ask the user to enter the number of miles they will drive.
# Calculate gallons needed by dividing miles by MPG.
# Display the gallons needed rounded to two decimal places.

vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicles.keys()

print(keys)

vehicle = input("Enter a vehicle to see its MPG: ")

print(f"The {vehicle} gets {vehicles[vehicle]} MPG.")

miles = float(input(f"How many miles will you drive the {vehicle}? "))

gallons = miles / vehicles[vehicle]

print(f"{gallons:.2f} gallons of gas are needed.")