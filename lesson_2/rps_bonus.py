import random

VALID_CHOICES = ["rock", "paper", "scissors"]

def prompt(message):
    print(f"====> {message}")

def not_valid_choice(player_input):
    if player_input not in VALID_CHOICES:
        return True
    return False

def display_winner(player, computer):
    if ((player == "rock" and computer == "scissors") or
    (player == "paper" and computer == "rock") or
    (player == "scissors" and computer == "paper")):
        prompt("You win! :D")
    elif player == computer:
        prompt("It's a tie!")
    else:
        prompt("Sorry, you lose! >:(")

#START
prompt("Welcome to Rock, Paper, Scissors!")
prompt("---------------------------------")

replay = True
while replay is True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    player_choice = input()

    while not_valid_choice(player_choice) is True:
        prompt("Your choice isn't valid!")
        prompt("Please type rock, paper, or scissors.")
        player_choice = input()

    #GET computer choice
    computer_choice = random.choice(VALID_CHOICES)
    prompt(f"""You chose {player_choice},
    computer chose {computer_choice}.""")

    #READ computer and player choices and PRINT winner
    display_winner(player_choice, computer_choice)

    #GET input asking if user wants to play again
    prompt("Would you like to play again? (y/n)")
    play_again = input().lower().strip()

    #validate input
    while True:
        if play_again.startswith('y') or play_again.startswith('n'):
            break
        prompt("Please enter 'y' or 'n'")
        play_again = input().lower().strip()

    if play_again.startswith('n'):
        prompt('Ok, thanks for playing!')
        replay = False
