import random
import time
import json

with open('rps_bonus.json', 'r') as file:
    MESSAGE = json.load(file)

VALID_CHOICE_DICT = {
    "r" : "rock",
    "p" : "paper",
    "s" : "scissors",
    "l" : "lizard",
    "sp" : "spock",
}

WINNING_MOVES = {
    "rock" : ["scissors", "lizard"],
    "paper" : ["rock", "spock"],
    "scissors" : ["paper", "lizard"],
    "lizard" : ["spock", "paper"],
    "spock" : ["scissors", "rock"],
}

def prompt(message):
    print(f"====> {message}")

def not_valid_choice(player_input):
    if player_input not in VALID_CHOICE_DICT:
        return True
    return False

def menu_selection():
    prompt("""Please make your selection:
    
        1. 'R' for Rock
        2. 'P' for Paper
        3. 'S' for Scissors
        4. 'L' for Lizard
        5. 'SP' for Spock
        """)

def countdown():
    prompt(">:OOO !!!GET READY TO BATTLE!!! >:OOO")
    time.sleep(2)
    prompt("")
    for key in VALID_CHOICE_DICT:
        prompt(f"{VALID_CHOICE_DICT[key].capitalize()}...")
        time.sleep(0.5)
    prompt("SHOOT!")
    time.sleep(1)


def display_winner(player, computer):
    if player == "rock" and computer in WINNING_MOVES["rock"]:
        result_message = "$$** You win! :D **$$"
    elif player == "paper" and computer in WINNING_MOVES["paper"]:
        result_message = "$$** You win! :D **$$"
    elif player == "scissors" and computer in WINNING_MOVES["scissors"]:
        result_message = "$$** You win! :D **$$"
    elif player == "lizard" and computer in WINNING_MOVES["lizard"]:
        result_message = "$$** You win! :D **$$"
    elif player == "spock" and computer in WINNING_MOVES["spock"]:
        result_message = "$$** You win! :D **$$"
    elif player == computer:
        result_message = "It's a tie!"
    else:
        result_message = "Sorry, you lose! :*("
    return result_message

def decide_score(result):
    if result == "$$** You win! :D **$$":
        return "player"
    if result == "Sorry, you lose! :*(":
        return "computer"
    return None

def display_grandmaster(p_score, c_score):
    if p_score == 3:
        prompt("")
        prompt(f"***!!!CONGRATULATIONS, {player_name.upper()}!!!***")
        prompt("By winning three games, "
        "you have been declared the RPSLSP Grandmaster!")
        prompt("")
    if c_score == 3:
        prompt("")
        prompt("@!#!* OH NO!!! *!#!@")
        prompt("By winning three games, "
        "Computer has been declared the RPSLSP Grandmaster!\n"
        "Challenge them again to take the title!")
        prompt("")

#START welcome message
prompt("What's your name?")
player_name = input()

prompt(f"Welcome, {player_name}, to Rock, Paper, Scissors, Lizard, Spock!")
prompt("---------------------------------")

player_score = 0
computer_score = 0

#main loop
while True:

    #GET user choice
    menu_selection()
    player_choice = input().strip().lower()

    #READ user choice and validate
    while not_valid_choice(player_choice) is True:
        prompt("Your choice isn'nt valid!")
        menu_selection()
        player_choice = input().strip().lower()

    prompt("---------------------------------")


    #SET player_choice as a VALID_CHOICE_DICT key
    player_choice = VALID_CHOICE_DICT[player_choice]

    #GET computer choice
    computer_choice = random.choice(list(WINNING_MOVES))

    #PRINT countdown
    countdown()
    prompt("")

    #PRINT choices
    prompt(f"You chose {player_choice.capitalize()}, "
    f"Computer chose {computer_choice.capitalize()}.")

    #READ computer's and player's choices and PRINT winner
    prompt(display_winner(player_choice, computer_choice))
    prompt("")

    #SET scoreboard variables
    if (decide_score(display_winner(player_choice, computer_choice))
    == "player"):
        player_score += 1
    elif (decide_score(display_winner(player_choice, computer_choice))
    == "computer"):
        computer_score += 1

    #PRINT scoreboard
    prompt(f"{player_name}: {player_score}  //  Computer: {computer_score}")

    #PRINT the Grandmaster
    display_grandmaster(player_score, computer_score)

    #SET score reset
    if computer_score == 3 or player_score == 3:
        computer_score = 0
        player_score = 0

    #GET input asking if user wants to play again
    prompt("Would you like to play again, {player_name}? (y/n)")
    play_again = input().lower().strip()

    #validate input
    while True:
        if play_again.startswith('y') or play_again.startswith('n'):
            break
        prompt("Please enter 'y' or 'n'")
        play_again = input().lower().strip()

    if play_again.startswith('n'):
        prompt("Ok, thanks for playing Rock, Paper, Scissors, Lizard, Spock!")
        break

#END