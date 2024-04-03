def prompt(message):
    print(f"---> {message}")

prompt("Welcome to Calculator!\n")

while True:
    value_1 = input("First value: ")
    if value_1.isdigit():
        break
    prompt(f"\nError. '{value_1}' is not a number.\n")

while True:
    value_2 = input("\nSecond value: ")
    if value_2.isdigit():
        break
    prompt(f"Error. '{value_2}' is not a number.\n")

while True:
    operation = input("\nChoose your operator:"
    "\n1.Plus 2.Minus 3.Multiply 4.Divide: ")
    if operation.isdigit():
        break
    prompt("Please input 1, 2, 3 or 4 to select an operator.\n")

if operation == "1":
    prompt(f"Your calculation evaluates to {int(value_1) + int(value_2)}.")
elif operation == "2":
    prompt(f"Your calculation evaluates to {int(value_1) - int(value_2)}.")
elif operation == "3":
    prompt(f"Your calculation evaluates to {int(value_1) * int(value_2)}.")
elif operation == "4":
    prompt(f"Your calculation evaluates to {int(value_1) // int(value_2)}.")
