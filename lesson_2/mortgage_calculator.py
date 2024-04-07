def not_valid(user_input):
    try:
        if user_input == "0":
            return True
        float(user_input)
    except ValueError:
        return True
    return False

def prompt(message):
    print(f"---> {message}")

#START
#PRINT welcome message
prompt("Welcome to Mortgage Calculator!\n")

#main loop
while True:
    #GET loan_amount
    prompt("How much would you like to borrow? ")
    loan_amount = input()
    while not_valid(loan_amount) is True:
        prompt("Hmm, that doesn't appear to be a valid number.")
        prompt("Please enter a positive number.")
        loan_amount = input()

    #GET interest rate and convert to monthly rate
    prompt("What's the annual interest rate?")
    apr = input()
    while not_valid(apr) is True:
        prompt("Hmm, that doesn't appear to be a valid number.")
        prompt("Please input a number, for example, 5 for 5%.")
        apr = input()
    annual_rate = float(apr) / 100
    monthly_rate = float(annual_rate) / 12

    #GET loan duration and calculate total months
    prompt("What's the loan duration? ")
    loan_duration = input()
    while not_valid(loan_duration) is True:
        prompt("Hmm, that doesn't appear to be a valid number of years.")
        prompt("Please enter a positive number.")
        loan_duration = input()
    monthly_duration = int(loan_duration) * 12

    #PRINT monthly_payment amount
    monthly_payments = (float(loan_amount) *
    (monthly_rate / (1 - (1 + monthly_rate) ** (-monthly_duration))))
    print(f"Your monthly payments will be: ${monthly_payments:.2f}")

    #check whether to loop
    print("""------------------------------------------------""")
    prompt("Would you like to calculate a new mortgage?")
    answer = input()
    if answer not in ["y", "yes"]:
        prompt("Thanks for using Mortgage Calculator. Goodbye!")
        break
#END