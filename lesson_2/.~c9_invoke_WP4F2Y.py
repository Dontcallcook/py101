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

def messages(message):
    return MESSAGE[message]

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
    prompt(messages("countdown_message"))
    time.sleep(2)
    prompt("")
    for _, value in VALID_CHOICE_DICT.items():
        if value == "lizard":
            prompt(f"{value.capitalize()}...??")
        elif value == "spock":
            prompt(f"{value.capitalize()}..?!?!")
        else:
            prompt(f"{value.capitalize()}...")
        time.sleep(0.5)
    prompt("SHOOT!!!!!!!")
    time.sleep(1)

#Reads the player's and computer's choice
#Returns a string declaring winner
def decide_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    if computer in WINNING_MOVES[player]:
        return messages("winning_message")
    return messages("losing_message")

def set_score(result):
    if result == messages("winning_message"):
        return "player"
    if result == messages("losing_message"):
        return "computer"
    return None

def display_grandmaster():
    if PLAYER_SCORE == 3:
        prompt("")
        prompt(f"***!!!CONGRATULATIONS, {PLAYER_NAME.upper()}!!!***")
        prompt("By winning three games, "
        "you have been declared the RPSLSP Grandmaster!")
        prompt("")
    if COMPUTER_SCORE == 3:
        prompt("")
        prompt("Oh dear...by winning three games, "
        "Computer has been declared the RPSLSP Grandmaster!")
        prompt("Challenge them again to take the title!")
        prompt("")

#START
#SET score
PLAYER_SCORE = 0
COMPUTER_SCORE = 0

#GET player's name'
prompt(messages("input_name"))
PLAYER_NAME = input()

#READ name and check for empty string
if PLAYER_NAME == "":
    PLAYER_NAME = "Anonymous"
    prompt("Oooo, how mysterious!\n")
    time.sleep(1)

#PRINT welcome message
prompt(f"Welcome, {PLAYER_NAME}, to Rock, Paper, Scissors, Lizard, Spock!")
prompt(messages("seperator"))

#main loop
while True:

    #GET user choice
    menu_selection()
    player_choice = input().strip().lower()

    #READ user choice and validate
    while not_valid_choice(player_choice) is True:
        prompt(messages("not_valid"))
        menu_selection()
        player_choice = input().strip().lower()

    prompt(messages("seperator"))


    #SET player_choice as a VALID_CHOICE_DICT key
    player_choice = VALID_CHOICE_DICT[player_choice]

    #GET computer choice
    computer_choice = random.choice(list(WINNING_MOVES))

    #PRINT countdown
    countdown()
    prompt(messages("empty_seperator"))

    #PRINT choices
    prompt(f"You chose {player_choice.capitalize()}, "
    f"Computer chose {computer_choice.capitalize()}.")

    #READ computer's and player's choices and PRINT winner
    prompt(decide_winner(player_choice, computer_choice))
    prompt(messages("empty_seperator"))

    #SET scoreboard variables
    if (set_score(decide_winner(player_choice, computer_choice))
    == "player"):
        PLAYER_SCORE += 1
    elif (set_score(decide_winner(player_choice, computer_choice))
    == "computer"):
        COMPUTER_SCORE += 1

    #PRINT scoreboard
    prompt(messages("seperator"))
    prompt("$C0RE_B0RED")
    prompt(f"{PLAYER_NAME}: {PLAYER_SCORE}  //  Computer: {COMPUTER_SCORE}")
    prompt(messages("seperator"))

    #PRINT the Grandmaster
    display_grandmaster()
    
    #PRINT next round
    prompt("ROUND str(PLAYER_SCORE + COMPUTER_SCORE + 1:
    
    #SET score reset
    if COMPUTER_SCORE == 3 or PLAYER_SCORE == 3:
        COMPUTER_SCORE = 0
        PLAYER_SCORE = 0

    #GET input asking if user wants to play again
        prompt(f"Would you like to play again, {PLAYER_NAME}? (y/n)")
        play_again = input().lower().strip()

        #validate input
        while True:
            if play_again.startswith('y') or play_again.startswith('n'):
                break
            prompt(messages("not_valid"))
            prompt("Please enter 'y' or 'n'")
            play_again = input().lower().strip()
        #PRINT goodbye message
        if play_again.startswith('n'):
            prompt(messages("thanks"))
            break

#END