def prompt(statement):
    return input("=>" + statement)

def invalid_input(user_input):
    try:
        float(user_input)
    except ValueError:
        print("Invalid input. Try again.")
        return True
    return False

# Obtain necessary inputs
while True:
    loan_amount = prompt("Enter the total amount of your loan: ")
    if not invalid_input(loan_amount):
        break

while True:
    annual_percentage_rate = prompt("Enter the annual percentage"
                                    " rate of your loan: ")
    if not invalid_input(annual_percentage_rate):
        break

while True:
    loan_duration_in_years = prompt("Enter the total duration of"
                                    " your loan in years: ")
    if not invalid_input(loan_duration_in_years):
        break

# Make calculations
monthly_interest_rate = (float(annual_percentage_rate) / 100) / 12
print(f"The monthly interest rate is {monthly_interest_rate:.4f}%.")
loan_duration_in_months = float(loan_duration_in_years) * 12
print(f"The duration of the loan in months is {loan_duration_in_months:.0f}.")
monthly_payment_amount = float(loan_amount) * (monthly_interest_rate / (
    1 - (1 + monthly_interest_rate) ** (-loan_duration_in_months)))
print(f"Your monthly payment is ${monthly_payment_amount:,.2f}!")
