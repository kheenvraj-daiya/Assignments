import random

user_score = 0
computer_score = 0
tie_score = 0

choices = ['rock', 'paper', 'scissors']

print("Welcome to Rock, Paper, Scissors!")
print("Type 'exit' anytime to quit.\n")

while True:
    user_input = input("Choose rock, paper, or scissors: ").lower()
    
    if user_input == 'exit':
        break
    if user_input not in choices:
        print("Invalid choice. Try again.\n")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!\n")
        tie_score += 1
    elif (user_input == 'rock' and computer_choice == 'scissors') or \
         (user_input == 'scissors' and computer_choice == 'paper') or \
         (user_input == 'paper' and computer_choice == 'rock'):
        print("You win!\n")
        user_score += 1
    else:
        print("Computer wins!\n")
        computer_score += 1

print("\nGame Over!")
print(f"Your Wins: {user_score}")
print(f"Computer Wins: {computer_score}")
print(f"Ties: {tie_score}")


