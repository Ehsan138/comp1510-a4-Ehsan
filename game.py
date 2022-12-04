"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


import random
import sys
import itertools
import prompts
import challenges
import json


def game() -> None:
    """

    :return:
    """
    prompts.game_intro_1()
    rows = 10
    columns = 10
    with open('package.json', encoding="utf-8") as file:
        data = json.load(file)
    board = make_board(rows, columns)
    character = make_character()
    placing_challenges(board, rows, columns)
    achieved_goal = False
    prompts.game_intro_2(character)
    while is_alive(character) and not achieved_goal:
        describe_current_location(board, character)
        print(board_visual(board, rows, columns, character))
        direction = get_user_choice()
        steps = get_user_steps()
        valid_move = validate_move(character, direction, steps, rows, columns)
        if valid_move:
            move_character(character, direction, steps)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges(board, character)
            if there_is_a_challenge and first_time_challenge(character):
                level = character["Level"]
                execute_challenge_protocol(board, character, data)
                current_level(character)
                if character_has_leveled(character, level):
                    execute_glow_up_protocol(character)
            achieved_goal = check_if_goal_attained(character)
        else:
            print("Sorry, that's out of bounds. Try somewhere else.")

    if not is_alive(character):
        prompts.fail_game()
    elif achieved_goal:
        prompts.succeed_game(character)


def quit_game(answer: str) -> None:
    """
    End the game if the player types 'quit'.

    :param answer: a string
    :precondition: answer must be a string
    :postcondition: the function correctly ends the script
    """
    if answer.lower() == 'quit':
        sys.exit()


def make_character() -> dict:
    """
    Ask user for their name and return a dictionary that contains key:value pairs.

    :return: a dictionary that contains key:value pairs, where keys are strings
    """
    name = input("Please enter your name: ")
    quit_game(name)
    character_dictionary = {"Name": name, "x_coordinate": 1,
                            "y_coordinate": 1, "Current_HP": 100,
                            "Max_HP": 100, "Experience_Points": 0,
                            "Level": 1, "trivia_one": 0, "trivia_two": 0,
                            "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                            "battle_one": 0, "battle_two": 0, "battle_three": 0,
                            "battle_four": 0, "battle_five": 0, "battle_six": 0,
                            "battle_final": 0}

    return character_dictionary


def make_board(rows: int, columns: int) -> dict:
    """
    Return a board based on specified rows and columns.

    :param rows: number of rows desired
    :param columns: number of columns desired
    :precondition: rows and columns must be positive non-zero integers
    :postcondition: correctly returns a board with the specified number of rows and columns
    :return: a board which is a dictionary

    >>> make_board(3, 3)
    {(1, 1): ['None', 'None'], (1, 2): ['None', 'None'], (1, 3): ['None', 'None'], (2, 1): ['None', 'None'], (2, 2): ['None', 'None'], (2, 3): ['None', 'None'], (3, 1): ['None', 'None'], (3, 2): ['None', 'None'], (3, 3): ['None', 'None']}
    """
    board = {}
    text = ''
    for row in range(1, rows + 1):
        text += '\n'
        for column in range(1, columns + 1):
            board[(row, column)] = ['None', 'None']
    return board


def filtering_fixed_coordinates(coordinate: tuple) -> bool:
    """
    Return True if tuple coordinate is not in list_of_fixed_coordinates, else False.

    :param coordinate: a tuple of coordinates
    :precondition: coordinate must be a tuple of two positive non-zero integers
    :postcondition: returns the correct boolean expression, True if tuple
    coordinate is not in list_of_fixed_coordinates, else False
    correctly returns tuples of coordinates not in the fixed events
    :return: a boolean expression, True if tuple coordinate is not
    in list_of_fixed_coordinates, else False
    """
    list_of_fixed_coordinates = [(1, 1), (10, 10), (3, 3), (5, 8), (8, 3)]
    return coordinate not in list_of_fixed_coordinates


def placing_challenges(board: dict, rows: int, columns: int) -> None:
    """
    Place challenges on the board.

    :param board: a dictionary
    :param rows: an integer
    :param columns: an integer
    :precondition: rows and columns must be positive non-zero integers, must the same number
    :precondition: board must be a tuple of two positive non-zero integers
    :postcondition: correctly places challenges on the board
    """
    list_of_coordinate = [(x_coordinate, y_coordinate)
                          for x_coordinate in range(1, columns + 1) for y_coordinate in range(1, rows + 1)]

    board[(3, 3)][1], board[(5, 8)][1], board[(8, 3)][1], board[(10, 10)][1] = \
        'battle_four', 'battle_five', 'battle_six', 'battle_final'

    list_of_coordinate = list(filter(filtering_fixed_coordinates, list_of_coordinate))

    list_trivias = ['trivia_one', 'trivia_two', 'trivia_three', 'trivia_four', 'trivia_five']
    random_trivia_coordinates = random.sample(list_of_coordinate, len(list_trivias) * 2)
    iterator_trivias = itertools.cycle(list_trivias)

    for coordinate in random_trivia_coordinates:
        board[coordinate][1] = next(iterator_trivias)
        list_of_coordinate.remove(coordinate)

    list_random_battles = ['battle_one', 'battle_two', 'battle_three']
    random_battle_coordinates = random.sample(list_of_coordinate, len(list_random_battles) * 4)
    iterator_random_battles = itertools.cycle(list_random_battles)

    for coordinate in random_battle_coordinates:
        board[coordinate][1] = next(iterator_random_battles)
        list_of_coordinate.remove(coordinate)


def board_visual(board: dict, rows: int, columns: int, character: dict) -> str:
    """
    Return the visual format of the board.

    :param board: a dictionary
    :param rows: an integer
    :param columns: an integer
    :param character: a dictionary
    :precondition: rows and columns must be positive non-zero integers, must the same number
    :precondition: board must be a tuple of two positive non-zero integers
    :precondition: character must be a dictionary where each key is a string of letters
    :postcondition: correctly displays board as emojis
    :return: a string which is the visual format of the board⬜️
    """
    text = ''
    special_cases = ['battle_four', 'battle_five', 'battle_six', 'battle_final']

    for row in range(1, rows + 1):

        text += str(row) + '\t'
        for column in range(1, columns + 1):

            if board[(column, row)][0] == 'None' and board[(column, row)][1] not in special_cases:
                text += "⬜️"
            elif board[(column, row)][0] == 'current' and board[(column, row)][1] not in special_cases:
                text += "💥"
            elif board[(column, row)][0] == 'current' and board[(column, row)][1] in special_cases and \
                    character[board[(column, row)][1]] == 1:
                text += "💥"
            elif board[(column, row)][0] == 'past_location' and board[(column, row)][1] not in special_cases:
                text += "🟨️"
            elif board[(column, row)][0] == 'past_location' and board[(column, row)][1] in special_cases and \
                    character[board[(column, row)][1]] == 1:
                text += "🟨️"
            elif board[(column, row)][1] == 'battle_four':
                text += "🐍"
            elif board[(column, row)][1] == 'battle_five':
                text += "🐱"
            elif board[(column, row)][1] == 'battle_six':
                text += "🐆"
            elif board[(column, row)][1] == 'battle_final':
                text += "🐲️"
        text += '\n'

    return text


def describe_current_location(board: dict, character: dict) -> None:
    """
    Update character's current location in board dictionary.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a tuple of two positive non-zero integers
    :precondition: character must be a dictionary where each key is a string of letters
    :postcondition: correctly updates character's current location in board dictionary
    """
    for coordinate in board:
        if board[coordinate][0] == 'current':
            board[coordinate][0] = 'past_location'

    board[(character["x_coordinate"], character["y_coordinate"])][0] = 'current'


def get_user_choice() -> str:
    """
    Get user's choice of which direction they want to move.

    :return: a string which is a number between 1 and 4
    """
    directions = ['North', 'South', 'West', 'East']
    print("Which direction would you like to go?")
    for number, direction in enumerate(directions, start=1):
        print(f"{number}:\t {direction}")
    response = input("Please enter the number of your answer: ")
    quit_game(response)
    get_user_choice_check_input(response)

    return response


def get_user_choice_check_input(response: str) -> None:
    """
    Check if user's answer is in the range of 1 to 4.

    :param response: a string which is a number between 1 and 4
    :precondition: response must be a string which is a number between 1 and 4
    :postcondition: correctly checks if user's answer is in the range of 1 to 4
    """
    directions = ['North', 'South', 'West', 'East']
    while response not in ['1', '2', '3', '4']:
        print("Which direction would you like to go?")
        for number, direction in enumerate(directions, start=1):
            print(f"{number}:\t {direction}")
        response = input("This direction is not reachable.\nThe number that you choose must be between 1 and 4.\nPlease"
                         " enter the number of your answer: ")
        quit_game(response)


def get_user_steps() -> str:
    """
    Return the user's desired steps.

    :return: a string which is a number between 1 and 9
    """
    steps = ''
    while steps not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print("How many steps do you want to take? (This number must be between 1 and 9)")
        steps = input("Please enter your answer: ")
        quit_game(steps)
        if steps not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Sorry, that's out of bounds. Try another number.")
    return steps


def validate_move(character: dict, direction: str, steps: str, rows: int, columns: int) -> bool:
    """
    Return True if user's move is valid, else False.

    :param character: a dictionary
    :param direction: a string
    :param steps: a string
    :param rows: an integer
    :param columns: an integer
    :precondition: rows and columns must be positive non-zero integers, must the same number
    :precondition: board must be a tuple of two positive non-zero integers
    :precondition: character must be a dictionary where each key is a string of letters
    :precondition: direction must be a string which is a number between 1 and 4
    :precondition: steps must be a string which is a number between 1 and 9
    :postcondition: return the correct boolean expression
    :return: a boolean expression, True if user's move is valid, else False
    """
    if int(direction) == 1 and character['y_coordinate'] - int(steps) >= 1:
        return True
    elif int(direction) == 2 and character['y_coordinate'] + int(steps) <= rows:
        return True
    elif int(direction) == 3 and character['x_coordinate'] - int(steps) >= 1:
        return True
    elif int(direction) == 4 and character['x_coordinate'] + int(steps) <= columns:
        return True
    else:
        return False


def move_character(character: dict, direction: str, steps: str) -> None:
    """
    Update the current location coordinates of the character dictionary.

    :param character: a dictionary
    :param direction: a string
    :param steps: a string
    :precondition: character must be a dictionary where each key is a string of letters
    :precondition: direction must be a string which is a number between 1 and 4
    :precondition: steps must be a string which is a number between 1 and 9
    :postcondition: correctly updates the current location coordinates of the character dictionary
    """
    if int(direction) == 1:
        character['y_coordinate'] -= int(steps)
    elif int(direction) == 2:
        character['y_coordinate'] += int(steps)
    elif int(direction) == 3:
        character['x_coordinate'] -= int(steps)
    elif int(direction) == 4:
        character['x_coordinate'] += int(steps)


def check_for_challenges(board: dict, character: dict) -> bool:
    """
    Return True if player is on a space that has a challenge, else False.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a tuple of two positive non-zero integers
    :precondition: character must be a dictionary where each key is a string of letters
    :postcondition: returns the correct boolean expression, True if player is on
    a space that has a challenge, else False
    :return: a boolean expression, True if player is on a space that has a challenge, else False
    """
    list_of_challenges = ["trivia_one", "trivia_two", "trivia_three", "trivia_four",
                          "trivia_five", "battle_one", "battle_two", "battle_three",
                          "battle_four", "battle_five", "battle_six", "battle_final"]
    for challenge in list_of_challenges:
        if board[(character["x_coordinate"], character["y_coordinate"])][1] == challenge:
            return True
    return False


def is_alive(character: dict) -> bool:
    """
    Return True if the character is alive, else False.

    :param character: a dictionary
    :precondition: character must be a dictionary where each key is a string of letters
    :postcondition: returns the correct boolean expression, True if the character is alive, else False
    :return: a boolean expression, True if the character is alive, else False

    >>> character_chris = {"Name": 'Chris', "x_coordinate": 1, "y_coordinate": 1, "Current_HP": 100, "Max_HP": 100}
    >>> is_alive(character_chris)
    True
    >>> character_hoda = {"Name": 'Hoda', "x_coordinate": 1, "y_coordinate": 1, "Current_HP": 0, "Max_HP": 100}
    >>> is_alive(character_hoda)
    False
    """
    return character['Current_HP'] > 0


def first_time_challenge(character: dict) -> bool:
    """
    Return True if it is the first time the character is doing one of the
    fixed challenges, else False.

    :param character: a dictionary
    :precondition: character must be a dictionary where each key is a string of letters
    :postcondition: returns the correct boolean expression, True if it is the first time
    the character is doing one of the fixed challenges, else False
    :return: a boolean expression, True if it is the first time the character is doing
    one of the fixed challenges, else False
    >>> test_1 = {"battle_three": 0, "battle_four": 0, "battle_five": 0, "battle_six": 0, "battle_final": 0}
    >>> first_time_challenge(test_1)
    True
    >>> test_2 = {"battle_three": 0, "battle_four": 1, "battle_five": 1, "battle_six": 1, "battle_final": 1}
    >>> first_time_challenge(test_2)
    False
    """
    special_cases = ['battle_four', 'battle_five', 'battle_six', 'battle_final']
    for challenge in special_cases:
        if character[challenge] == 0:
            return True
    return False


def execute_challenge_protocol(board: dict, character: dict, data: dict) -> None:
    """
    Return the challenge functions based on the current event on the board.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a tuple of two positive non-zero integers
    :precondition: character must be a dictionary where each key is a string of letters
    :postcondition: returns the correct challenge function based on the current
    event on the board
    """
    challenge = board[(character["x_coordinate"], character["y_coordinate"])][1]
    if challenge in ['battle_one', 'battle_two', 'battle_three']:
        challenges.random_battles(challenge, character, data)
    elif challenge in ['battle_four', 'battle_five', 'battle_six']:
        if character[challenge] == 0:
            challenges.fixed_battles(challenge, character, data)
    elif challenge == 'battle_final':
        if character[challenge] == 0:
            challenges.battle_final(character, data)
    elif challenge in ['trivia_one', 'trivia_two', 'trivia_three', 'trivia_four', 'trivia_five']:
        challenges.trivia(challenge, character, data)


def character_has_leveled(character: dict, level: int) -> bool:
    """
    Return True if character has leveled up, else False.

    :param character: a dictionary
    :param level: a positive non-zero integer
    :precondition: character must be a dictionary where each key is a string of letters
    :precondition: level must be a positive non-zero integer
    :postcondition: returns the correct boolean expression, True if character has leveled up, else False
    :return: a boolean expression, True if character has leveled up, else False

    >>> character_1 = {"Level": 3}
    >>> level_1 = 2
    >>> character_has_leveled(character_1, level_1)
    True
    >>> character_2 = {"Level": 3}
    >>> level_2 = 1
    >>> character_has_leveled(character_2, level_2)
    False
    """
    return character['Level'] - level == 1


def current_level(character):
    """
    Update the character's current level.

    :param character: a dictionary
    :precondition: character must be a dictionary where each key is a string of letters
    :postcondition: correctly updates the character's current level

    >>> character_1 = {"Level": 0, "Experience_Points": 456}
    >>> current_level(character_1)
    >>> character_1["Level"] == 1
    True
    >>> character_2 = {"Level": 1, "Experience_Points": 2674}
    >>> current_level(character_2)
    >>> character_2["Level"] == 3
    True
    """
    character["Level"] = (character["Experience_Points"] // 1000) + 1


def execute_glow_up_protocol(character: dict) -> None:
    """
    Update character's HP stats and print their new level, HP, and EXP stats.

    :param character: a dictionary
    :precondition: character must be a dictionary where each key is a string of letters
    :postcondition: correctly updates character's HP stats and print their
    new level, HP, and EXP stats
    """
    character["Max_HP"] += 100
    character["Current_HP"] = character["Max_HP"]
    print(f"Congratulations on leveling up! \nYou've done excellent work!\n"
          f"{character['Name']}, these are your current stats:\n"
          f"Level: {character['Level']} \n"
          f"Current HP: {character['Current_HP']} \n"
          f"Max HP: {character['Max_HP']} \n"
          f"Experience Points: {character['Experience_Points']} \n")


def check_if_goal_attained(character: dict) -> bool:
    """
    Return True if the character has completed battle_final, else False.

    :param character: a dictionary
    :precondition: character must be a dictionary where each key is a string of letters
    :postcondition: returns the correct boolean expression, True if the
    character has completed battle_final, else False
    :return: a boolean expression, True if the character has completed battle_final, else False

    >>> character_1 = {"battle_final": 0, "Experience_Points": 456}
    >>> check_if_goal_attained(character_1)
    False
    >>> character_2 = {"battle_final": 1, "Experience_Points": 2674}
    >>> check_if_goal_attained(character_2)
    True
    """
    return character['battle_final'] == 1


def main():
    """
    Drives the program.
    """
    game()


if __name__ == "__main__":
    main()
