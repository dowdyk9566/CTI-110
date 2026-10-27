# Name: Kenneth Dowdy
# Date: 10/27/2026
# Assignment: P4HW2
# Description: Collects scores and calculates the average and final letter grade.

"""
Pseudocode:
1. Input: Prompt the user to enter the number of scores they want to input.
2. Decision: Check if the input is a positive integer. If not, display an error message and prompt again.
3. Input: Prompt the user to enter each score one by one.
4. Find the lowest score and remove it from the list of scores.
5. Calculate the average of the remaining scores.
6. Decision: Determine the final letter grade based on the average score using the following scale:
   - A: 90-100
   - B: 80-89
   - C: 70-79
   - D: 60-69
   - F: Below 60
7. Output: Display the average score and the corresponding letter grade to the user.
"""

# Ask the user for the number of scores they want to input
while True:
    try:
        num_scores = int(input("Enter the number of scores you want to input: "))
        if num_scores > 0:
            break
        else:
            print("\nINVALID INPUT! Please enter a positive integer.")
    except ValueError:
        print("\nINVALID INPUT! Please enter a positive integer.")

print()
score_list = []

# Loop to collect the scores from the user
for i in range(1, num_scores + 1):
    while True:
        try:
            score = float(input(f"Enter score #{i}: "))
            if 0 <= score <= 100:
                score_list.append(score)
                break
            else:
                print("\nINVALID SCORE! Please enter a score between 0 and 100.")
        except ValueError:
            print("\nINVALID SCORE! Please enter a score between 0 and 100.")

print()

# ----- Data Processing and Calculation -----
lowest_score = min(score_list)

# Remove the lowest score from the list
if len(score_list) > 1:
    modified_list = score_list.copy()
    modified_list.remove(lowest_score)

    # Calculate the average of the remaining scores
    average_score = sum(modified_list) / len(modified_list)

    # Determine the final letter grade based on the average score
    if average_score >= 90:
        letter_grade = "A"
    elif average_score >= 80:
        letter_grade = "B"
    elif average_score >= 70:
        letter_grade = "C"
    elif average_score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print("------------------------")
    print(f"Lowest Score : {lowest_score}")
    print(f"Modified List : {modified_list}")
    print(f"Average Score : {average_score:.2f}")
    print(f"Letter Grade : {letter_grade}")
    print("------------------------")
else:
    print("Not enough scores to calculate an average after removing the lowest score. Please enter at least two scores.")