import random
import time
import json
import os
import pdb

with open('rps_bonus.json', 'r') as file:
    MESSAGE = json.load(file)

GAME_MODE_DICT = {
    "single" : ["1", "one", "single", "singleround"],
"three" : ["2", "3", "three", "best", "best-of-three", "bestofthree", "ultimateshowdown"]
}

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

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def prompt(message):
    print(f"====> {message}")

def messages(message):
    return MESSAGE[message]

def get_name():
    prompt(messages("input_name"))
    PLAYER_NAME = input().strip()
    return PLAYER_NAME

def check_no_name(PLAYER_NAME):
    if PLAYER_NAME == "":
        PLAYER_NAME = "Anonymous"
        prompt(messages("empty_seperator"))
        prompt("Oooo, how mysterious!\n")
        time.sleep(1)
    return PLAYER_NAME

def display_welcome_message(PLAYER_NAME):
    prompt(f"Welcome, {PLAYER_NAME}, to Rock, Paper, Scissors, Lizard, Spock!")
    prompt(messages("seperator"))
    prompt(messages("empty_seperator"))

def not_valid_mode(game_mode):
    for accepted_inputs in GAME_MODE_DICT.values():
        if game_mode in accepted_inputs:
            return False
    return True

def not_valid_choice(player_input):
    if (player_input not in VALID_CHOICE_DICT
    and player_input not in VALID_CHOICE_DICT.values()):
        return True
    return False
        
def get_game_mode():
    prompt("""Select your game mode:
    
        1. Single Round
        2. Best-of-three Ultimate Showdown
        """)
    game_mode = input().replace(" ", "").lower()
    return game_mode

def display_game_mode(game_mode, GAME_MODE_DICT):
    if game_mode in GAME_MODE_DICT["single"]:
        prompt("Single Round selected.")
    else:
        prompt("My word...what courage! Ultimate Showdown selected!")


def display_countdown(ROUND_NUMBER):
    prompt(f"<-------ROUND {ROUND_NUMBER} /// "
    +  messages("countdown_message") + "--------->")
    time.sleep(1)
    prompt("")
    for _, value in VALID_CHOICE_DICT.items():
        if value == "lizard":
            prompt(f"{value.capitalize()}...??")
        elif value == "spock":
            prompt(f"{value.capitalize()}..?!?!")
        else:
            prompt(f"{value.capitalize()}...")
        time.sleep(0.3)
    prompt("SHOOT!!!!!!!")
    time.sleep(0.6)

def get_move_choice():
    prompt("""Please make your selection:
        
        1. 'R' for Rock
        2. 'P' for Paper
        3. 'S' for Scissors
        4. 'L' for Lizard
        5. 'SP' for Spock
        """)
    player_choice = input().strip().lower()
    return player_choice

def assign_choice_as_dict_value(player_choice):
    if player_choice not in VALID_CHOICE_DICT.values():
        player_choice = VALID_CHOICE_DICT[player_choice]
    return player_choice

def get_computer_choice():
    computer_choice = random.choice(list(WINNING_MOVES))
    return computer_choice

def display_choices(player_choice, computer_choice):
    prompt(f"You chose {player_choice.capitalize()}, "
    f"Computer chose {computer_choice.capitalize()}.")

def decide_winner(player_choice, computer_choice):
    if computer_choice in WINNING_MOVES[player_choice]:
        result = "player"
    elif player_choice in WINNING_MOVES[computer_choice]:
        result = "computer"
    else:
        result = "tie"
    return result

def display_result(result):
    if result == "player":
        return (messages("winning_message"))
    elif result == "computer":
        return (messages("losing_message"))
    return ("It's a tie!")
    
def set_scores(result, scores):
    if result == "player":
        scores["player"] += 1
    elif result == "computer":
        scores["computer"] += 1

def display_scores(scores, PLAYER_NAME):
    prompt(messages("seperator"))
    prompt("$C0RE_B0RED")
    prompt(f"{PLAYER_NAME}: {scores['player']}  //  Computer: {scores['computer']}")
    prompt(messages("seperator"))

def best_of_three(game_mode, GAME_MODE_DICT):
    if game_mode in GAME_MODE_DICT["three"]:
        return True

def next_round_check(game_mode, GAME_MODE_DICT, scores):
    if (best_of_three(game_mode, GAME_MODE_DICT) is True
    and (scores["player"] < 3 and scores["computer"] < 3)):
        prompt("Press 'enter' to continue to the next round or 'q' to quit.")
        next_round_choice = input().strip().lower()
        return next_round_choice

def display_grandmaster(scores, PLAYER_NAME):
    if scores["player"] == 3:
        prompt(messages("empty_seperator"))
        prompt(f"***!!!CONGRATULATIONS, {PLAYER_NAME.upper()}!!!***")
        prompt("By winning three games, "
        "you have been declared the RPSLSP Grandmaster!")
        prompt(messages("empty_seperator"))
    if scores["computer"] == 3:
        prompt(messages("empty_seperator"))
        prompt("Oh dear...by winning three games, "
        "Computer has been declared the RPSLSP Grandmaster!")
        prompt("Challenge them again to take the title!")
        prompt(messages("empty_seperator"))

def score_round_reset(ROUND_NUMBER, scores):    
            ROUND_NUMBER = 0
            scores["player"] = 0
            scores["computer"] = 0

def ask_play_again():
    prompt(messages("not_valid"))
    prompt("Please enter 'y' or 'n'")
    play_again = input().lower().strip()

def play_again_valid(play_again):
    if play_again.startswith('y') or play_again.startswith('n'):
        return True
    return False

def dont_play_again(play_again_valid, play_again):
    while play_again_valid is False:
        ask_play_again()
    if play_again.startswith('n'):
        return True
    return False

def play_game():
    clear_screen()
    
    scores = {
        "player" : 0,
        "computer" : 0
    }
    
    player_score = 0
    computer_score = 0
    ROUND_NUMBER = 1
    
    PLAYER_NAME = get_name()
    clear_screen()
    
    PLAYER_NAME = check_no_name(PLAYER_NAME)
    
    display_welcome_message(PLAYER_NAME)
    
    game_mode = get_game_mode()
    
    while not_valid_mode(game_mode) is True:
        clear_screen()
        prompt(messages("not_valid"))
        game_mode = get_game_mode()
    
    display_game_mode(game_mode, GAME_MODE_DICT)
    
    time.sleep(2)
    clear_screen()
    
    #MAIN LOOP
    while True:
    
        player_choice = get_move_choice()
        clear_screen()
    
        while not_valid_choice(player_choice) is True:
            prompt(messages("not_valid"))
            player_choice = get_move_choice()
            clear_screen()
    
        prompt(messages("seperator"))
        
        player_choice = assign_choice_as_dict_value(player_choice)
    
        computer_choice = get_computer_choice()
    
        clear_screen()
        display_countdown(ROUND_NUMBER)
        clear_screen()
    
        display_choices(player_choice, computer_choice)
        
        result = decide_winner(player_choice, computer_choice)
        
        prompt(display_result(result))

        set_scores(result, scores)
        
        display_scores(scores, PLAYER_NAME)
        
        if best_of_three(game_mode, GAME_MODE_DICT) is True:
            display_grandmaster(scores, PLAYER_NAME)
        
        next_round_choice = next_round_check(game_mode, GAME_MODE_DICT, scores)
            
        if next_round_choice == "q":
            prompt(messages("thanks"))
            break
        else:
            play_again = 'y'
            clear_screen()
        
        if scores["player"] == 3 or scores["computer"] == 3:
            prompt(f"Would you like to play again, {PLAYER_NAME}? (y/n)")
            play_again = input().lower().strip()
            score_round_reset(ROUND_NUMBER, scores)
    
        if game_mode in GAME_MODE_DICT["single"]:
            prompt(f"Would you like to play again, {PLAYER_NAME}? (y/n)")
            play_again = input().lower().strip()
        
        ROUND_NUMBER += 1
        clear_screen()
    
        #If player doesn't want to play again, quit.
        if dont_play_again(play_again_valid, play_again) is True:
            prompt(messages("thanks"))
            break

play_game()
