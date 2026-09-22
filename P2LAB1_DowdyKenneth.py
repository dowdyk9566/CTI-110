# Kenneth Dowdy
# September 22, 2026
# P2LAB1 - Circle Calculations
# This program calculates the diameter, circumference, and area
# of a circle using a radius entered by the user.

# Pseudocode:
# 1. Ask the user to enter the radius of the circle.
# 2. Calculate the diameter by multiplying the radius by 2.
# 3. Calculate the circumference using 2 * pi * radius.
# 4. Calculate the area using pi * radius squared.
# 5. Display the diameter with 1 decimal place.
# 6. Display the circumference with 2 decimal places.
# 7. Display the area with 3 decimal places.

import math

radius = float(input("Enter the radius of the circle: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")