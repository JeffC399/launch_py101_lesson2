import json

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

print(messages('welcome'))

while True:
    while True:
        prompt(messages('number_prompt_1'))
        number1 = input()

        if not invalid_number(number1):
            break

        prompt(messages('invalid_number'))

    while True:
        prompt(messages('number_prompt_2'))
        number2 = input()

        if not invalid_number(number2):
            break

        prompt(messages('invalid_number'))

    while True:
        prompt(messages('operation_prompt'))
        operation = input()

        if operation in ["1", "2", "3", "4"]:
            break

        prompt(messages('invalid_operation'))

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    output = round(output, 2)  # Round the result to two decimals

    prompt(messages('result').format(output=output))

    prompt(messages('another_operation'))
    answer = input()
    if answer[0].lower() != 'y':
        break