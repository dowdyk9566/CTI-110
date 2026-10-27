# Name: Kenneth Dowdy
# Date: 10/27/2026
# Assignment: P4LAB2
# Description: This program displays a multiplication table form 1 to 12 for a given non-negative interger input by the user. The program will continue to prompt the user for a valid input until a non-negative integer is provided. The multiplication table will be displayed in a formatted manner.
# It rejects negative inputs and loops based on user preference.

#PseudoCode:
#1. Input: Prompt the user to enter a non-negative integer.
#2. Decision: Check if the input is a non-negative integer. If not, display an error message and prompt again.
#3. Multiplication Table: Once a valid input is received, generate and display the multiplication table from 1 to 12 for the given integer.
#4. Repeat/runn-again: Ask the user if they want to enter another number. If yes, repeat the process; if no, exit the program.
#5. Program exit condtions: The program will exit when the user chooses not to enter another number or if the user inputs a negative integer.

run_again = "yes"

# One while loop to allow the user to run the program multiple times
while run_again.strip().lower() in ("yes", "y"):
    while True:
        try:
            user_num = int(input("Please enter a non-negative integer: "))
            if user_num < 0:
                print("Error: Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid non-negative integer.")

    for i in range(1, 13):
        print(f"{user_num} * {i} = {user_num * i}")
    print()
    run_again = input("Would you like to enter another number? (yes/no): ")
print("Exiting the program. Goodbye!")