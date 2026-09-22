#Kenneth Dowdy
#September 22, 2026
#P2HW2 - Lists
#This program collects six module grades and calculates the lowest,
#highest, sum, and average of the grades.

# Pseudocode:
# Ask the user to enter a grade for Modules 1 through 6.
# Store all six grades in a list.
# Find the lowest grade.
# Find the highest grade.
# Find the sum of the grades.
# Calculate the average.
# Display the results.

module1 = float(input('Enter grade for Module 1: '))
module2 = float(input('Enter grade for Module 2: '))
module3 = float(input('Enter grade for Module 3: '))
module4 = float(input('Enter grade for Module 4: '))
module5 = float(input('Enter grade for Module 5: '))
module6 = float(input('Enter grade for Module 6: '))

grades = [module1, module2, module3, module4, module5, module6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print()
print('------------Results------------')
print(f'Lowest Grade:        {lowest_grade:.1f}')
print(f'Highest Grade:       {highest_grade:.1f}')
print(f'Sum of Grades:       {sum_of_grades:.1f}')
print(f'Average:             {average_grade:.2f}')
print('--------------------------------')