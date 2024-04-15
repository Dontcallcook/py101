import random
import time
import json
import os

with open('rps_bonus.json', 'r') as file:
    MESSAGE = json.load(file)

GAME_MODES = {
    "single" : ["1", "one", "single", "singleround"],
    "three" : ["2", "3", "three", "best",
               "best-of-three", "bestofthree", "ultimateshowdown"]
}

VALID_CHOICES = {
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
    player_name = input().strip()
    return player_name

def check_no_name(player_name):
    if player_name == "":
        player_name = "Anonymous"
        prompt(messages("empty_seperator"))
        prompt("Oooo, how mysterious!\n")
        time.sleep(1)
    return player_name

def display_welcome_message(player_name):
    prompt(f"Welcome, {player_name}, to Rock, Paper, Scissors, Lizard, Spock!")
    prompt(messages("seperator"))
    prompt(messages("empty_seperator"))

def not_valid_mode(game_mode):
    for accepted_inputs in GAME_MODES.values():
        if game_mode in accepted_inputs:
            return False
    return True

def get_game_mode():
    prompt("""Select your game mode:
    
        1. Single Round
        2. Best-of-three Ultimate Showdown
        """)
    game_mode = input().replace(" ", "").lower()
    return game_mode

def display_game_mode(game_mode):
    if game_mode in GAME_MODES["single"]:
        prompt("Single Round selected.")
    else:
        prompt("My word...WHAT COURAGE! Ultimate Showdown selected!")

def display_round(round_number):
    prompt(f"<------- /// ROUND {round_number} /// --------->")
    time.sleep(1)

def display_countdown():
    prompt(f"<------- /// {messages('countdown_message')} /// --------->")
    time.sleep(1)
    prompt("")
    for _, value in VALID_CHOICES.items():
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
    prompt("""/// MOVE SELECT ///
    
    Please make your selection:
        
        1. 'R' for Rock
        2. 'P' for Paper
        3. 'S' for Scissors
        4. 'L' for Lizard
        5. 'SP' for Spock
        """)
    player_choice = input().strip().lower()
    return player_choice

def not_valid_choice(player_input):
    if (player_input not in VALID_CHOICES
    and player_input not in VALID_CHOICES.values()):
        return True
    return False

def get_valid_choice():
    clear_screen()
    prompt(messages("not_valid"))
    time.sleep(1)
    clear_screen()
    player_choice = get_move_choice()
    clear_screen()
    return player_choice

def assign_choice_as_dict_value(player_choice):
    if player_choice not in VALID_CHOICES.values():
        player_choice = VALID_CHOICES[player_choice]
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
        return messages("winning_message")
    if result == "computer":
        return messages("losing_message")
    return "It's a tie!"

def set_scores(result, scores):
    if result == "player":
        scores["player"] += 1
    elif result == "computer":
        scores["computer"] += 1

def display_scores(scores, player_name):
    prompt(messages("seperator"))
    prompt("$C0RE_B0RED")
    prompt(f"{player_name}: {scores['player']}  "
    f"//  Computer: {scores['computer']}")
    prompt(messages("seperator"))

def next_round_check():
    prompt("Press 'enter' to continue to the next round or 'q' to quit.")
    next_round_choice = input().strip().lower()
    return next_round_choice

def determine_grandmaster(scores):
    if scores["player"] == 3:
        return "player"
    if scores["computer"] == 3:
        return "computer"
    return None

def display_grandmaster(grandmaster, player_name):
    if grandmaster == "player":
        prompt(messages("empty_seperator"))
        prompt(f"***!!!CONGRATULATIONS, {player_name.upper()}!!!***")
        prompt("By winning three games, "
        "you have been declared the RPSLSP Grandmaster!")
        prompt(messages("empty_seperator"))
    if grandmaster == "computer":
        prompt(messages("empty_seperator"))
        prompt("Oh dear...by winning three games, "
        "Computer has been declared the RPSLSP Grandmaster!")
        prompt("Challenge them again to take the title!")
        prompt(messages("empty_seperator"))

def determine_game_mode(game_mode, game_modes):
    if game_mode in game_modes["single"]:
        return "single"
    return "three"

def showdown_complete(scores):
    return scores["player"] == 3 or scores["computer"] == 3

def display_choose_play_again(player_name):
    prompt(f"Would you like to play again, {player_name}? (y/n)")

def get_play_again():
    play_again = input().lower().strip()
    return play_again

def play_again_valid(play_again):
    if play_again.startswith('y') or play_again.startswith('n'):
        return True
    return False

def display_play_again_not_valid():
    prompt(messages("not_valid"))
    prompt(messages("enter_y_n"))

def ensure_play_again_valid(play_again):
    while play_again_valid(play_again) is False:
        display_play_again_not_valid()
        play_again = input().lower().strip()

def play_again_check(play_again):
    if play_again == 'n':
        return False
    return True

def exit_game():
    prompt(messages("goodbye"))

def game_init(): #resets round number and scores
    scores = {
        "player" : 0,
        "computer" : 0,
    }
    round_number = 0
    return scores, round_number

def name_select():
    clear_screen()
    player_name = get_name()
    clear_screen()
    player_name = check_no_name(player_name)
    display_welcome_message(player_name)
    return player_name

def mode_select(): #resets scores gets name and game mode
    game_mode = get_game_mode()

    while not_valid_mode(game_mode):
        clear_screen()
        prompt(messages("not_valid"))
        game_mode = get_game_mode()

    display_game_mode(game_mode)
    time.sleep(2)
    clear_screen()
    return game_mode

def main_loop(player_name, game_mode):

    scores = {
        "player" : 0,
        "computer" : 0,
    }
    round_number = 1

    while True:

        player_choice = get_move_choice()
        clear_screen()

        while not_valid_choice(player_choice):
            player_choice = get_valid_choice()

        prompt(messages("seperator"))

        player_choice = assign_choice_as_dict_value(player_choice)

        computer_choice = get_computer_choice()

        clear_screen()
        display_round(round_number)
        display_countdown()
        clear_screen()
        display_choices(player_choice, computer_choice)

        result = decide_winner(player_choice, computer_choice)

        prompt(display_result(result))

        set_scores(result, scores)

        display_scores(scores, player_name)

        if game_mode in GAME_MODES["single"]:
            display_choose_play_again(player_name)
            play_again = get_play_again()
            ensure_play_again_valid(play_again)

            if play_again_check(play_again) is False:
                exit_game()
                break

        if (game_mode in GAME_MODES["three"]
        and (scores["player"] < 3 and scores["computer"] < 3)):
            next_round_choice = next_round_check()
            if next_round_choice == "q":
                exit_game()
                break
            play_again = 'y'

        if (game_mode in GAME_MODES["three"]
        and showdown_complete(scores)):
            grandmaster = determine_grandmaster(scores)
            display_grandmaster(grandmaster, player_name)

            display_choose_play_again(player_name)
            play_again = get_play_again()
            ensure_play_again_valid(play_again)

            scores, round_number = game_init()

            if play_again_check(play_again) is True:
                clear_screen()
                game_mode = mode_select()

        round_number += 1
        clear_screen()

        if play_again_check(play_again) is False:
            exit_game()
            break

def play_game():
    player_name = name_select()
    game_mode = mode_select()
    main_loop(player_name, game_mode)

play_game()
    