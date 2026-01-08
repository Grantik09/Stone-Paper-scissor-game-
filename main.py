import random

"""
Stone = -1
Paper = 1
Scissor = 0
"""

choices = {"s": -1, "p": 1, "c": 0
reverse_choices = {-1: "Stone", 1: "Paper", 0: "Scissor"}

# Computer choice
computer_choice = random.choice([-1, 1, 0])

# User input with validation
while True:
    user_input = input("Enter your choice (s = Stone, p = Paper, c = Scissor): ").strip().lower()
    if user_input in choices:
        break
    print("Invalid input! Please enter s, p, or c.")

user_choice = choices[user_input]

print(f"\nYou chose: {reverse_choices[user_choice]}")
print(f"Computer chose: {reverse_choices[computer_choice]}")

# Game logic
if computer_choice == user_choice:
    print("It's a Draw!")
elif (
    (user_choice == -1 and computer_choice == 0) or
    (user_choice == 1 and computer_choice == -1) or
    (user_choice == 0 and computer_choice == 1)
):
    print("You Win!")
else:
    print("You Lose!")
