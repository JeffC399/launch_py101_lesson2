# Rock, Paper, Scissors Game
# v1 Basic Game

import random
import json

VALID_CHOICES = ['rock', 'paper', 'scissors']

with open('rock_paper_scissors_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def calculate_winner(user_choice, computer_choice):
    if ((user_choice == 'rock' and computer_choice == 'scissors') or 
        (user_choice == 'paper' and computer_choice == 'rock') or 
        (user_choice == 'scissors' and computer_choice == 'paper')):
        return "You win!"
    elif((computer_choice == 'rock' and user_choice == 'scissors') or 
        (computer_choice == 'paper' and user_choice == 'rock') or
        (computer_choice == 'scissors' and user_choice == 'paper')):
        return "Computer wins!"
    else:
        return "It's a tie!"

while True:
    # Obtain User Input
    prompt(f"Choose one: {", ".join(VALID_CHOICES)}")
    user_choice = input().lower()

    while user_choice not in VALID_CHOICES:
        prompt(MESSAGES['invalid_choice'])
        user_choice = input().lower()

    # Obtain Computer Input
    computer_choice = random.choice(VALID_CHOICES)

    # Calculate and Display Results
    prompt(f"You chose {user_choice}, computer chose {computer_choice}...")
    prompt(calculate_winner(user_choice, computer_choice))

    # Play Again?
    while True:
        prompt(MESSAGES['another_game'])
        play_again = input().lower()

        if play_again.startswith('n') or play_again.startswith('y'):
            break
        else:
            prompt(MESSAGES['another_invalid_choice'])
        
    if play_again[0] == 'n':
        break