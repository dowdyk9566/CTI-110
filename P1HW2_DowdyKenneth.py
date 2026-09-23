# Kenneth Dowdy
# September 22, 2026
# P1HW2 - Travel Budget
# This program calculates the total travel expenses and
# subtracts them from the user's travel budget.

# Pseudocode:
# 1. Ask the user to enter their travel budget.
# 2. Ask the user to enter their travel destination.
# 3. Ask the user to enter the amount they will spend on gas.
# 4. Ask the user to enter the amount they will spend on accommodation.
# 5. Ask the user to enter the amount they will spend on food.
# 6. Add the gas, accommodation, and food expenses.
# 7. Subtract the total expenses from the budget.
# 8. Display the destination, budget, expenses, and remaining balance.

# Get the user's travel budget
budget = float(input("Enter your budget: $"))

# Get the user's travel destination
destination = input("Enter your travel destination: ")

# Get the user's travel expenses
gas = float(input("Enter the amount you will spend on gas: $"))
accommodation = float(input("Enter the amount you will spend on accommodation: $"))
food = float(input("Enter the amount you will spend on food: $"))

# Calculate the total expenses
total_expenses = gas + accommodation + food

# Calculate the remaining budget
remaining_budget = budget - total_expenses

# Display the results
print("\n-------- Travel Budget Results --------")
print(f"Destination: {destination}")
print(f"Budget: ${budget:.2f}")
print(f"Gas: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
print("---------------------------------------")