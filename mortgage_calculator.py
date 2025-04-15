# Mortgage Calculator v5.0
# note v1.0
# note v2.0
# note v3.0
# note v4.0
# note 5.0 implements changes suggested by LSBot

import json

with open('mortgage_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(statement):
    return input("===> " + statement)

def is_invalid_input(user_input):
    try:
        float(user_input)
    except ValueError:
        print(MESSAGES['invalid_input'])
        return True
    return False

def is_negative(entered_number):
    if float(entered_number) < 0:
        print(MESSAGES['number_is_negative'])
        return True
    return False

def get_valid_number_input(prompt_message, replace_chars=""):
    while True:
        user_input = prompt(prompt_message)
        for char in replace_chars:
            user_input = user_input.replace(char,"")
        if not is_invalid_input(user_input) and not is_negative(user_input):
            return float(user_input)

def calculate_monthly_payment(entered_loan_amount):
    if monthly_interest_rate > 0:
        return entered_loan_amount * (monthly_interest_rate / (
            1 - (1 + monthly_interest_rate) ** (-loan_duration_in_months)))
    return entered_loan_amount / loan_duration_in_months

while True:
# Obtain necessary inputs
    print()
    loan_amount = (get_valid_number_input
                              (MESSAGES['enter_loan_amount'], ",$"))
    annual_percentage_rate = (get_valid_number_input
                              (MESSAGES['enter_annual_rate'], "%"))
    loan_duration_in_years = (get_valid_number_input
                              (MESSAGES['enter_loan_duration']))

# Make calculations
    monthly_interest_rate = (annual_percentage_rate / 100) / 12
    loan_duration_in_months = loan_duration_in_years * 12
    monthly_payment_amount = calculate_monthly_payment(loan_amount)

# Print results
    print()
    print("You requested the monthly payment amount for a loan with a "
          f"principla amount of ${loan_amount:,.2f}, an annual interest "
          f"rate of {annual_percentage_rate}%, and a duration of "
          f"{loan_duration_in_years} years. Here are the details of that "
          "loan:\n")
    if annual_percentage_rate > 0:
        print(MESSAGES['monthly_rate'] + f"{monthly_interest_rate:.4f}%.")
    else:
        print(MESSAGES['interest_free'])
    print(MESSAGES['duration_in_months'] + f"{loan_duration_in_months:.0f}.")
    print(MESSAGES['monthly_payment'] + f"${monthly_payment_amount:,.2f}!")
    print()

    user_response = prompt(MESSAGES['another_calculation'])
    if user_response[0].lower() != 'y':
        break