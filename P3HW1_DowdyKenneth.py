
# Name: Kenneth Dowdy
# Date: 10/10/2026
# Assignment: P3HW1
# Description: This program accepts six grades and calculates the
# lowest grade, highest grade, sum, average, and letter grade.

# Pseudocode:
# 1. Create an empty list to store six grades.
# 2. Ask the user to enter six grades.
# 3. Find the lowest and highest grades.
# 4. Calculate the sum and average of the grades.
# 5. Determine the letter grade using the average.
# 6. Display the results.

# Create an empty list
grades = []

# Get six grades from the user
for i in range(1, 7):
    grade = float(input(f"Enter grade {i}: "))
    grades.append(grade)

# Calculate grade information
lowest_grade = min(grades)
highest_grade = max(grades)
total = sum(grades)
average = total / len(grades)

# Determine the letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results
print()
print("------------Results------------")
print(f"{'Lowest Grade:':<20} {lowest_grade:.1f}")
print(f"{'Highest Grade:':<20} {highest_grade:.1f}")
print(f"{'Sum of Grades:':<20} {total:.1f}")
print(f"{'Average:':<20} {average:.2f}")
print(f"{'Letter Grade:':<20} {letter_grade}")
print("--------------------------------")