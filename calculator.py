# Ask the user for the first number
# Ask the user for the second number
# Ask the user for an operation to perform
# Perform the operation on the two numbers
# Print the result to the terminal

import json

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Now 'data' contains the contents of the JSON file as a Python dictionary or list

while True:

    def prompt(message):
        print(f"=> {message}")

    def invalid_number(number_str):
        try:
            int(number_str)
        except ValueError:
            return True

        return False

    prompt(MESSAGES['welcome'])

    prompt("What\'s the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_number'])
        number1 = input()

    prompt('What\'s the second number?')
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    prompt( 'What operation would you like to perform?'
            '\n1) Add 2) Subtract 3) Multipy 4) Divide')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("You must choose 1, 2, 3, or 4.")
        operation = input()

    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)

    prompt(f'The result is: {output:,}')
    prompt("Would you like to run another calculation?")
    another_calculation = input().upper()

    while another_calculation not in ['Y', 'YES', 'N', 'NO']:
        prompt("That is not a valid response. Try again.")
        prompt("Would you like to run another calculation?")
        another_calculation = input().upper()

    if another_calculation in ['N', "NO"]:
        break
