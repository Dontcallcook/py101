import json

with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f"---> {message}")

def not_valid(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt(data["welcome_message"])

while True:

    prompt("First value: ")
    value_1 = input()
    
    while not_valid(value_1) is True:
        prompt("Hmm...that doesn't seem to be a number.")
        value_1 = input()
    
    prompt("Second value: ")
    value_2 = input()
    
    while not_valid(value_2) is True:
        prompt("Hmm...that doesn't seem to be a number.")
        value_2 = input()
    
    prompt("Choose your operator:\n1.Plus 2.Minus 3.Multiply 4.Divide: ")
    operation = input()
    
    while operation not in ["1", "2", "3", "4"]:
        prompt("Please enter 1, 2, 3, or 4")
        operation = input()
    
    if operation == "4":
        try:
            int(value_1) / int(value_2)
        except ZeroDivisionError:
            prompt("You can't divide by zero. Pick a new operation.")
            operation = input()
    
    if operation == "1":
        prompt(f"Your calculation evaluates to {int(value_1) + int(value_2)}.")
    elif operation == "2":
        prompt(f"Your calculation evaluates to {int(value_1) - int(value_2)}.")
    elif operation == "3":
        prompt(f"Your calculation evaluates to {int(value_1) * int(value_2)}.")
    elif operation == "4":
        prompt(f"Your calculation evaluates to {int(value_1) // int(value_2)}.")

    print("Would you like to perform another calculation?\nY/N")
    new_calc = input().upper()
    if new_calc and new_calc[0] != "Y":
        prompt("Goodbye!")
        break