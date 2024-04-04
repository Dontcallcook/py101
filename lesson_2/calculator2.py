import json

with open('calculator_messages.json', 'r') as file:
    MESSAGE = json.load(file)


def prompt(message):
    print(f"---> {message}")

def not_valid(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False
    
def messages(message, lang='en'):
    return MESSAGE[lang][message]

LANGUAGE = 'es'

prompt(messages("welcome_message", LANGUAGE))

while True:
    prompt(messages("first_value", LANGUAGE))
    value_1 = input()
    
    while not_valid(value_1) is True:
        prompt(messages("not_a_number", LANGUAGE))
        value_1 = input()
    
    prompt(messages("second_value", LANGUAGE))
    value_2 = input()
    
    while not_valid(value_2) is True:
        prompt(messages("not_a_number", LANGUAGE))
        value_2 = input()
    
    prompt(messages("choose_operator", LANGUAGE))
    operation = input()
    
    while operation not in ["1", "2", "3", "4"]:
        prompt(messages("not_operator", LANGUAGE))
        operation = input()
    
    if operation == "4":
        try:
            int(value_1) / int(value_2)
        except ZeroDivisionError:
            prompt(messages("zero_division_error", LANGUAGE))
            operation = input()

    match operation:
        case '1':
            output = float(value_1) + float(value_2)
        case '2': 
            output = float(value_1) - float(value_2)
        case '3':
            output = float(value_1) * float(value_2)
        case '4':
            output = float(value_1) / float(value_2)
    
    prompt(f"Your calculation evaluates to {output}.")

    print("Would you like to perform another calculation?\nY/N")
    new_calc = input().upper()
    if new_calc and new_calc[0] != "Y":
        prompt(messages("goodbye_message", LANGUAGE))
        break