import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"\nComputer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}\n")

# Start the game
play_game()

