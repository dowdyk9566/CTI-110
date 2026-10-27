# Name: Kenneth Dowdy
# Date: 10/27/2026
# Assignment: P4HW2
# Description: Processes salary information for multiple employees until "Done" is entered.

# Initialize accumulators for the final summary totals
total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Prompt for employees until the sentinel value is entered
while True:
    name = input('Enter employee name or "Done" to terminate: ')

    # Terminate only when the name is exactly "Done"
    if name == "Done":
        break

    rate = float(input(f"Enter hourly rate for {name}: "))
    hours = float(input(f"Enter hours worked for {name}: "))

    # Calculate regular and overtime pay
    if hours > 40:
        regular_hours = 40
        overtime_hours = hours - 40
    else:
        regular_hours = hours
        overtime_hours = 0

    regular_pay = regular_hours * rate
    overtime_pay = overtime_hours * rate * 1.5
    gross_pay = regular_pay + overtime_pay

    # Accumulate totals across all employees
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Display the employee's pay information
    print(f"\nEmployee Name: {name}")
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Regular Pay':<15}{'Overtime Pay':<15}{'Gross Pay':<15}")
    print("-" * 75)
    print(f"{hours:<15.2f}{rate:<15.2f}{regular_pay:<15.2f}{overtime_pay:<15.2f}{gross_pay:<15.2f}\n")

# Display final summary totals
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular pay: ${total_regular_pay:.2f}")
print(f"Total amount paid for gross pay: ${total_gross_pay:.2f}")