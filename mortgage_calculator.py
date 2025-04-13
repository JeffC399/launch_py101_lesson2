# Mortgage Calculator v3.0
# Prohibit the entry of negative interest rate values.
# Note: v4.0 to allow entry of partial years.
# Note: v5.0 to carefully refactor the entire project before checking solution.

def prompt(statement):
    return input("=>" + statement)

def invalid_input(user_input):
    try:
        float(user_input)
    except ValueError:
        print("Invalid input. Try again.")
        return True
    return False

def is_non_negative(entered_interest_rate):
    if convert_to_float(entered_interest_rate) < 0:
        print("Error. The interest rate cannot be less than zero. Try again.")
        return False
    return True

def calculate_monthly_payment(entered_loan_amount):
    if monthly_interest_rate > 0:
        return entered_loan_amount * (monthly_interest_rate / (
            1 - (1 + monthly_interest_rate) ** (-loan_duration_in_months)))
    return entered_loan_amount / loan_duration_in_months

def convert_to_float(string_value):
    return float(string_value)

# Obtain necessary inputs
while True:
    loan_amount = prompt("Enter the total amount of your loan: ")
    if not invalid_input(loan_amount):
        loan_amount = convert_to_float(loan_amount)
        break

while True:
    annual_percentage_rate = prompt("Enter the annual percentage"
                                    " rate of your loan: ")
    if not invalid_input(annual_percentage_rate) and is_non_negative(annual_percentage_rate):
        annual_percentage_rate = convert_to_float(annual_percentage_rate)
        break

while True:
    loan_duration_in_years = prompt("Enter the total duration of"
                                    " your loan in years: ")
    if not invalid_input(loan_duration_in_years):
        loan_duration_in_years = convert_to_float(loan_duration_in_years)
        break

# Make calculations
monthly_interest_rate = (annual_percentage_rate / 100) / 12
loan_duration_in_months = loan_duration_in_years * 12
monthly_payment_amount = calculate_monthly_payment(loan_amount)

# Print results
if annual_percentage_rate > 0:
    print(f"The monthly interest rate is {monthly_interest_rate:.4f}%.")
else:
    print("This loan is an interest-free loan. Lucky you.")
print(f"The duration of the loan in months is {loan_duration_in_months:.0f}.")
print(f"Your monthly payment is ${monthly_payment_amount:,.2f}!")