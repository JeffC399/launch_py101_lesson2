# Rock, Paper, Scissors Game
# v1.0 Basic Game
# v2.0 Added Bonus Features Other Than Shortened Input
# v3.0 Added Shortened Input

import os
import random
import json

VALID_CHOICES = ['r', 'p', 's', 'l', 'o']
BEST_OUT_OF = 5
MESSAGES_WHEN_TIED = [
    "You mean you couldn't outsmart your own computer? Lame.",
    "What kind of man are you?",
    "You'd better up your game, mister.",
    "Well, you coulda been a contender...but you weren't.",
    "Put down the peace pipe and FOCUS!"
]
CONVERT_CHOICE = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors',
    'l': 'Lizard',
    'o': 'Spock'
}

was_a_tie = True
no_winner = True
game_count = 0
match_count = 0
matches_won_by_player = 0
matches_won_by_computer = 0

with open('rock_paper_scissors_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt(message):
    print(f"==> {message}")

def boundary():
    print("-------------------------------------------------"
          "-----------------------")

def display_welcome():
    clear_screen()
    prompt(MESSAGES['welcome'])
    print(MESSAGES['heading_rules'])
    boundary()
    print(MESSAGES['game_rules1'])
    print()
    print(MESSAGES['game_rules2'])
    boundary()
    print()

def return_correct_action(u, c):
    if   (u == 'r' and c == 'p') or (u == 'p' and c == 'r'):
        return "Paper covers Rock."
    elif (u == 'r' and c == 's') or (u == 's' and c == 'r'):
        return "Rock smashes Scissors."
    elif (u == 'r' and c == 'l') or (u == 'l' and c == 'r'):
        return "Rock crushes Lizard."
    elif (u == 'r' and c == 'o') or (u == 'o' and c == 'r'):
        return "Spock vaporizes Rock."
    elif (u == 'p' and c == 's') or (u == 's' and c == 'p'):
        return "Scissors cut Paper."
    elif (u == 'p' and c == 'l') or (u == 'l' and c == 'p'):
        return "Lizard eats Paper."
    elif (u == 'p' and c == 'o') or (u == 'o' and c == 'p'):
        return "Paper disproves Spock."
    elif (u == 's' and c == 'l') or (u == 'l' and c == 's'):
        return "Scissors decapitate Lizard."
    elif (u == 's' and c == 'o') or (u == 'o' and c == 's'):
        return "Spock smashes Scissors."
    elif (u == 'l' and c == 'o') or (u == 'o' and c == 'l'):
        return "Spock smashes Scissors."
    else:
        return "This round was a tie."

def calculate_winner_of_round(user_choice, computer_choice):
    global was_a_tie
    global user_wins
    global computer_wins
    global game_count

    game_count += 1

    if user_choice == computer_choice:
        was_a_tie = True
        tied_message = random.choice(MESSAGES_WHEN_TIED)
        return tied_message
    elif((user_choice == 'r' and computer_choice in ['p', 'o']) or
         (user_choice == 'p' and computer_choice in ['s', 'l']) or
         (user_choice == 's' and computer_choice in ['o', 'r']) or
         (user_choice == 'o' and computer_choice in ['l', 'p']) or
         (user_choice == 'l' and computer_choice in ['r', 's'])):
        computer_wins += 1
        was_a_tie = False
        return "Computer won this round."
    else:
        user_wins += 1
        was_a_tie = False
        return f"{user_name} won this round!"

def display_match_results(user_wins, computer_wins):
    global no_winner
    global match_count
    global matches_won_by_player
    global matches_won_by_computer

    no_winner = False
    match_count += 1

    print()
    boundary()

    if user_wins >= ((BEST_OUT_OF // 2) + 1):
        print(MESSAGES['end_of_match'])
        print(f"{user_name} won the match against Computer by "
              f"a score of {user_wins} to {computer_wins}!")
        matches_won_by_player += 1
    else:
        print(MESSAGES['end_of_match'] + f"Computer won the match, "
              f"beating {user_name} by a score of {computer_wins} "
              f"to {user_wins}. Bummer.")
        matches_won_by_computer += 1

    boundary()
    print()

def display_final_results():
    clear_screen()
    print()
    boundary()

    if match_count == 1:
        print(f"Thank you for playing one match (consisting of "
              f"{game_count} games) of Rock, Paper, \n"
              "Scissors, Lizard, Spock!\n")
    else:
        print(f"Thank you for playing a total of {match_count} "
              f"matches (consisting of {game_count} games) of \n"
              "Rock, Paper, Scissors, Lizard, Spock!\n")

    if matches_won_by_player == 0:
        if matches_won_by_computer == 1:
            print("Pathetic. You lost the only match you played "
                  "against the computer."
                  "\nWhere is your human pride?")
        else:
            print(f"Unfortunately, you didn't win a single match, "
                  f"and the computer blanked \nyou {matches_won_by_computer}"
                   "to zero. Ouch.")
    elif matches_won_by_computer == 0:
        if matches_won_by_player == 1:
            print("You won the only match you played against the "
                  "computer. Ho hum.")
        else:
            print("You thrashed your digital overlord by winning "
                  f"all {matches_won_by_player} matches you played. \n"
                  "Congrats, but watch your back!")
    elif matches_won_by_player > matches_won_by_computer:
        print("You dominated, crushing the puny digital brain by "
              f"{matches_won_by_player} to "
              f"{matches_won_by_computer}. Go humans!")
    elif matches_won_by_computer > matches_won_by_player:
        print(f"Are you sure you're actually human? Losing by "
              f"{matches_won_by_computer} to {matches_won_by_player} "
              "is... sad, and might \nmean that you have more homo erectus "
              "DNA than homo sapiens DNA.")
    else:
        print(f"The match was tied {matches_won_by_player} to "
              f"{matches_won_by_computer}. "
              "Very unsatisfying result.")
    print()
    print(f"{user_name}, " + MESSAGES['final_message'])
    boundary()
    print()

# Welcome and Rules
display_welcome()

# Get Player's Name and Confirm His Readiness
while True:
    prompt(MESSAGES['enter_name'])
    user_name = input()
    print()

    if len(user_name) > 0 and len(user_name) < 20 and user_name[0] != " ":
        break
    prompt(MESSAGES['user_name_error'])

while True:
    user_answer = input("Press <enter> to start the game!").strip()

    if user_answer == "":
        clear_screen()
        break
    prompt(MESSAGES['wrong_choice_to_start_game'])

# Main Game Loop
while True:
    user_wins = 0
    computer_wins = 0

    while no_winner:
        # Obtain User Input
        prompt("Enter your choice: 'r'=Rock, 'p'=Paper, 's'=Scissors, "
               "'l'=Lizard, 'o'=SpOck.")
        user_choice = input().strip().lower()
        print()

        while user_choice not in VALID_CHOICES:
            prompt(MESSAGES['invalid_choice'])
            user_choice = input().strip().lower()

        # Obtain Computer Input
        computer_choice = random.choice(VALID_CHOICES)

        # Calculate and Display Results
        prompt(f"{user_name} chose {CONVERT_CHOICE[user_choice]}, computer "
               f"chose {CONVERT_CHOICE[computer_choice]}...")
        prompt(return_correct_action(user_choice, computer_choice))
        prompt(calculate_winner_of_round(user_choice,
                                         computer_choice))

        if (computer_wins < ((BEST_OUT_OF // 2) + 1) and 
            user_wins < ((BEST_OUT_OF // 2) + 1)):
            prompt(f"Currently, the score is {user_name}: "
                   f"{user_wins}, Computer: {computer_wins}\n")
        else:
            display_match_results(user_wins, computer_wins)

    # Play Again?
    while True:
        prompt(MESSAGES['another_game'])
        play_again = input().lower()

        if play_again.startswith('n') or play_again.startswith('y'):
            no_winner = True
            clear_screen()
            break
        prompt(MESSAGES['another_invalid_choice'])

    if play_again[0] == 'n':
        clear_screen()
        display_final_results()
        break