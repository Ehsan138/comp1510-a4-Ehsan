"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


import random
import sys
import json
import itertools
import prompts


def game():
    prompts.game_intro_1()
    rows = 10
    columns = 10
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
                execute_challenge_protocol(board, character)
                current_level(character)
                if character_has_leveled(character, level):
                    execute_glow_up_protocol(character)
            achieved_goal = check_if_goal_attained(character)
        else:
            print("Sorry, that's out of bounds. Try somewhere else.")

    if not is_alive(character):
        fail_game()
    elif achieved_goal:
        succeed_game(character)


def quit_game(answer):
    if answer.lower() == 'quit':
        sys.exit()


def make_character():
    """
    Creates and returns a dictionary that contains key:value pairs.

    :precondition:
    :postcondition
    :return: dictionary that contains key:value pairs
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


def make_board(rows, columns):
    """
    Makes a board based on specified rows and columns.

    :param rows: number of rows desired
    :param columns: number of columns desired
    :precondition:
    :postcondition:
    :return:
    """
    board = {}
    text = ''

    for row in range(1, rows + 1):
        text += '\n'

        for column in range(1, columns + 1):
            board[(row, column)] = ['None', 'None']

    return board


def filtering_fixed_coordinates(coordinate):
    """

    :param coordinate:
    :return:
    """
    list_of_fixed_coordinates = [(1, 1), (10, 10), (3, 3), (5, 8), (8, 3)]
    return coordinate not in list_of_fixed_coordinates


def placing_challenges(board, rows, columns):
    """
    Places challenges on the board.

    :param board:
    :param rows:
    :param columns:
    :precondition:
    :postcondition:
    :return:
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


def board_visual(board, rows, columns, character):
    """
    Makes the visuals of the board.

    :param rows:
    :param columns:
    :precondition:
    :postcondition:
    :return:
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


def describe_current_location(board, character):
    """
    Describes character's current location.

    :param board:
    :param character:
    :precondition:
    :postcondition:

    """
    for coordinate in board:
        if board[coordinate][0] == 'current':
            board[coordinate][0] = 'past_location'

    board[(character["x_coordinate"], character["y_coordinate"])][0] = 'current'


def get_user_choice():
    """
    Gets user's choice of which direction they want to move.

    :return:
    """
    directions = ['North', 'South', 'West', 'East']
    print("Which direction would you like to go?")
    for number, direction in enumerate(directions, start=1):
        print(f"{number}:\t {direction}")
    response = input("Please enter the number of your answer: ")
    quit_game(response)
    get_user_choice_check_input(response)

    return response


def get_user_choice_check_input(response):
    directions = ['North', 'South', 'West', 'East']
    while response not in ['1', '2', '3', '4']:
        print("Which direction would you like to go?")
        for number, direction in enumerate(directions, start=1):
            print(f"{number}:\t {direction}")
        response = input("This direction is not reachable.\n"
                         "The number that you choose must be between 1 and 4.\n"
                         "Please enter the number of your answer: ")
        quit_game(response)


def get_user_steps():
    """
    Asks user how many steps they want to take.

    :return:
    """
    steps = ''
    while steps not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print("How many steps do you want to take? (This number must be between 1 and 9)")
        steps = input("Please enter your answer: ")
        quit_game(steps)
        if steps not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Sorry, that's out of bounds. Try another number.")

    return steps


def validate_move(character, direction, steps, rows, columns):
    """

    :param character:
    :param direction:
    :param steps:
    :param rows:
    :param columns:
    :return:
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


def move_character(character, direction, steps):
    if int(direction) == 1:
        character['y_coordinate'] -= int(steps)
    elif int(direction) == 2:
        character['y_coordinate'] += int(steps)
    elif int(direction) == 3:
        character['x_coordinate'] -= int(steps)
    elif int(direction) == 4:
        character['x_coordinate'] += int(steps)


def check_for_challenges(board, character):
    """
    Checks if there is a challenge in that space.

    :param board:
    :param character:
    :return:
    """
    list_of_challenges = ["trivia_one", "trivia_two", "trivia_three", "trivia_four",
                          "trivia_five", "battle_one", "battle_two", "battle_three",
                          "battle_four", "battle_five", "battle_six", "battle_final"]
    for challenge in list_of_challenges:
        if board[(character["x_coordinate"], character["y_coordinate"])][1] == challenge:
            return True

    return False


def is_alive(character):
    """
    Checks if the character is alive.

    :param character:
    :return:
    """
    return character['Current_HP'] > 0


def first_time_challenge(character):
    """
    Checks if it is the first time the character is doing the challenge.

    :param board:
    :param character:
    :return:
    """
    special_cases = ['battle_four', 'battle_five', 'battle_six', 'battle_final']
    for challenge in special_cases:
        if character[challenge] == 0:
            return True
    return False


def execute_challenge_protocol(board, character):
    """

    :param board:
    :param character:
    :return:
    """
    challenge = board[(character["x_coordinate"], character["y_coordinate"])][1]
    if challenge in ['battle_one', 'battle_two', 'battle_three']:
        random_battles(challenge, character)
    elif challenge in ['battle_four', 'battle_five', 'battle_six']:
        if character[challenge] == 0:
            fixed_battles(challenge, character)
    elif challenge == 'battle_final':
        if character[challenge] == 0:
            battle_final(character)
    elif challenge in ['trivia_one', 'trivia_two', 'trivia_three', 'trivia_four', 'trivia_five']:
        trivias(challenge, character)


def character_has_leveled(character, level):
    """
    Checks if character has leveled up.

    :param character:
    :param level:
    :return:
    """
    if character['Level'] - level == 1:
        return True
    else:
        return False


def current_level(character):
    """

    :param character:
    :return:
    """
    character["Level"] = (character["Experience_Points"] // 1000) + 1


def execute_glow_up_protocol(character):
    """
    Executes what happens when character levels up.

    :param character:
    :return:
    """
    character["Max_HP"] += 100
    character["Current_HP"] = character["Max_HP"]
    print(f"Congratulations on leveling up! \nYou've done excellent work!\n"
          f"{character['Name']}, these are your current stats:\n"
          f"Level: {character['Level']} \n"
          f"Current HP: {character['Current_HP']} \n"
          f"Max HP: {character['Max_HP']} \n"
          f"Experience Points: {character['Experience_Points']} \n")


def check_if_goal_attained(character):
    """
    Checks if the character has

    :param board:
    :param character:
    :param rows:
    :param columns:
    :return:
    """
    return character['battle_final'] == 1


#############################################################################################


def fixed_battles(challenge_name, character):
    """
    Executes fixed battles.

    :param challenge_name:
    :param character:
    :return:
    """
    file = open('package.json')
    data = json.load(file)

    options = ("Battle", "Flee")
    print(data[challenge_name]["opponent_introduction"])
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("What do you want to do? (Any key other than 1 will Flee): ")
    quit_game(will_battle)
    check_fixed_battles_conditions(challenge_name, character, will_battle, data)


def check_fixed_battles_conditions(challenge_name, character, will_battle, data):
    """

    :param challenge_name:
    :param character:
    :param will_battle:
    :param data:
    :return:
    """
    if will_battle == "1":
        if challenge_name == 'battle_five' and character["battle_four"] == 0:
            print(data[challenge_name]["is_not_ready"])
        elif challenge_name == 'battle_six' and (character["battle_four"] == 0 or character["battle_five"] == 0):
            print(data[challenge_name]["is_not_ready"])
        else:
            character["Experience_Points"] += random.randint(500, 650)
            new_randomize_hp = 1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"]
            if character["Current_HP"] - new_randomize_hp >= 0:
                character["Current_HP"] -= new_randomize_hp
                character[challenge_name] = 1
                print(data[challenge_name]["battle_statement"].format(health=character["Current_HP"],
                                                                      experience=character["Experience_Points"]))
            else:
                character["Current_HP"] = 0
                print("Uh oh! Pikachu has fainted!")
    else:
        if character["Experience_Points"] - 100 >= 0:
            character["Experience_Points"] -= 100
            print("You lose 100 EXP Points for fleeing from battle.\nPikachu now has {experience} EXP Points!".format(
                experience=character["Experience_Points"]))
        else:
            character["Experience_Points"] = (character["Experience_Points"] // 1000) * 1000
            print('Now you have zero EXP for your current level, sorry not sorry :)')


def random_battles(challenge_name, character):
    """
    Executes random battles.

    :param challenge_name:
    :param character:
    :return:
    """
    file = open('package.json')
    data = json.load(file)

    options = ("Battle", "Flee")
    print(data[challenge_name]["opponent_introduction"])
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("What do you want to do? (Any key other than 1 will Flee): ")
    quit_game(will_battle)
    check_random_battles_conditions(challenge_name, character, will_battle, data)


def check_random_battles_conditions(challenge_name, character, will_battle, data):
    """

    :param challenge_name:
    :param character:
    :param will_battle:
    :param data:
    :return:
    """
    if will_battle == "1":
        character["Experience_Points"] += random.randint(200, 300)
        new_randomize_hp = 1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"]
        if character["Current_HP"] - new_randomize_hp >= 0:
            character["Current_HP"] -= new_randomize_hp
            character[challenge_name] = 1
            print(data[challenge_name]["battle_statement"].format(health=character["Current_HP"],
                                                                  experience=character["Experience_Points"]))
        else:
            character["Current_HP"] = 0
            print("Uh oh! Pikachu has fainted!")
    else:
        if character["Experience_Points"] - 100 >= 0:
            character["Experience_Points"] -= 100
            print("You lose 100 EXP for fleeing from battle.\nPikachu now has {experience} EXP!".format(
                experience=character["Experience_Points"]))
        else:
            character["Experience_Points"] = (character["Experience_Points"] // 1000) * 1000
            print('Attention! Looks like you have 0 EXP left!')


def trivias(trivia_name, character):
    """
    Executes trivia questions.

    :param trivia_name:
    :param character:
    :return:
    """
    file = open('package.json')
    data = json.load(file)

    options = data[trivia_name]["options"]
    print(data[trivia_name]["question"])
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer: ")
    quit_game(answer)
    check_trivias_conditions(trivia_name, character, answer, data)


def check_trivias_conditions(trivia_name, character, answer, data):
    """

    :param trivia_name:
    :param character:
    :param answer:
    :param data:
    :return:
    """
    if answer == data[trivia_name]["right_answer"]:
        if trivia_name == 'trivia_three':
            character["Experience_Points"] += 500
        else:
            character["Experience_Points"] += 100
        character[trivia_name] = 1
        print(data[trivia_name]['award'].format(health=character["Current_HP"]))
        if (character["Current_HP"] < character["Max_HP"]) and trivia_name == 'trivia_three':
            character["Current_HP"] = character["Max_HP"]
        elif (character["Current_HP"] < character["Max_HP"]) and trivia_name != 'trivia_three':
            character["Current_HP"] *= 1.10
        else:
            print("Oh, actually, your Pikachu is well rested.")
    else:
        print("Oops, you got that wrong.")


def battle_final(character):
    """
    Executes the final battle.

    :param character:
    :return:
    """
    file = open('package.json')
    data = json.load(file)
    print(data['battle_final']['narration'])
    print("""
                              ⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣷⠀⠀⠀⠀⣸⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡞⣿⣷⣮⣻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡝⢿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⠸⣸⣻⣏⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⡿⡀⠀⠀⠀⠀⠀⣾⡞⡝⣿⢿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠩⣾⣿⣶⢦⣤⣀⠸⠻⢭⣥⡻⣧⠀⡙⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⢠⣴⣾⣿⣿⣿⣏⣶⣾⡽⣿⣷⣟⣿⣿⣿⣻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣀⣀⣀⠀⠀⠀⠸⣿⡿⠘⠻⢿⣿⣿⠟⠛⠿⠿⠃⢍⣿⣿⢸⣿⣿⣿⡽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣰⣟⠛⠛⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣜⢿⣿⡿⡷⡿⣼⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢰⣿⠃⠀⠀⠀⠈⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣯⣾⣿⡀⠀⠙⠻⢿⣶⣄⠀⠀⠀⠀⠀⠀⠀
    ⢸⣿⠀⠀⠀⠀⠀⠀⢻⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣧⡀⠀⠀⠀⠙⢿⣧⡀⠀⠀⠀⠀⠀
    ⢸⣿⡀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣬⣽⣿⣿⢟⣛⣳⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠀⠀
    ⠀⣿⣇⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣷⢻⣾⣿⣿⣷⡽⣄⠀⠀⢀⣾⣿⣷⣄⠀⠀
    ⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣷⣄⡀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⢹⣦⠀⢸⣇⠀⠹⣏⢧⡀
    ⠀⠀⠹⣿⣷⡀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⡆⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⢸⣿⡄⠈⠛⠀⣶⠟⠼⠇
    ⠀⠀⠀⠹⣿⣿⣷⣤⡀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣿⣿⣿⡿⣾⣿⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠙⣿⣿⣿⣿⣶⣄⠀⠀⠈⠻⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⡿⣱⣿⣿⣿⣿⢟⣼⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣧⡀⠀⠀⠈⠻⢿⣿⢸⣿⣿⣿⡿⢟⣫⣾⣿⣿⠿⣛⣵⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢈⣾⣿⡟⠙⠚⠛⠛⠋⠉⠀⠘⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠁⠀⠀⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⡏⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣯⢻⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠋⠘⠻⣿⣿⣷⣶⣒⣒⢢⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⣏⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠟⠈⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡿⠿⠿⠿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    print(data['battle_final']['opponent_introduction'])
    options = ("Battle", "Flee")
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("Will you battle Mewtwo? ")
    quit_game(will_battle)
    check_battle_final_conditions(character, will_battle, data)


def check_battle_final_conditions(character, will_battle, data):
    if will_battle == "1":
        if character["battle_four"] == 1 and character["battle_four"] == 1 and character["battle_four"] == 1 and \
                character["Level"] >= 3:
            character["Experience_Points"] += random.randint(500, 650)
            character["Current_HP"] -= (1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"])
            character["battle_final"] = 1
            print(data['battle_final']['battle_statement'])
        elif character["battle_four"] == 0 or character["battle_five"] == 0 or character["battle_six"] == 0:
            print(data['battle_final']['not_complete_all_fixed_battles'])
        elif character["Level"] < 3:
            print(data['battle_final']['not_level_three'])

    else:
        character["Experience_Points"] -= 100
        print("You lose 100 EXP Points for fleeing from battle.")

#################################################################################################################


def succeed_game(character):
    """
    Prints message upon successful completion of the game.

    :return:
    """
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡆
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡇⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠿⠋⠁⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          ⣀⠴⠋⢳⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠤⠔⠒⠒⠚⣻⣿⣿⣿⣷⣶⠆⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠈⡆⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⠉⠁⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⢣⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⢀⡟⢀⣀⣀⡤⠤⠤⢄⣀⣀⡀⠀⠀⠀⣠⠴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠿⠋⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⢸⡆
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣠⠴⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠛⠁⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇
    ⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠁⠀⠀⠀⠀⠀⠀⠀⢀⡴⠶⣤⣀⠀⠀⠀⠠⡀⠀⠀⠀⠀⣀⣀⣠⠤⠔⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
    ⠀⠀⠀⠀⠀⠀⠀⣴⢃⣤⡄⠀⠀⠀⠀⠀⠀⠀⠸⣷⣤⣿⣿⠄⠀⠀⠀⠉⠛⢼⣿⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
    ⠀⠀⠀⠀⠀⠀⢠⣷⣾⣠⡇⢀⡀⠀⠀⠀⠀⠀⠀⠉⠻⠿⠋⠀⠀⠀⠀⠀⠀⠀⠉⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⣀⣀⠀⠄⠀⠀⠀⢀⣠⠶⠋
    ⠀⠀⠀⠀⠀⠀⣸⠸⠿⠏⠀⢈⡁⠀⠀⠀⣤⡆⠀⠀⠀⢀⡴⠟⠛⠶⣄⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣋⣠⠤⠶⠒⠒⠛⠉⠁⠀⠀⠀⠀⢀⣠⠔⠋⠁
    ⠀⠀⠀⠀⠀⣰⡿⡄⠀⠐⢺⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢾⠁⢠⣤⡀⣹⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠋
    ⠀⠀⠀⠀⠀⣟⠀⣷⠀⠀⠈⢻⣿⣿⣿⣿⣿⠀⠀⠀⠀⠘⢷⣤⣈⣶⠟⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⣀⡤⠞⠋
    ⠀⠀⠀⠀⠀⢻⣶⠏⠀⠀⠀⠀⠹⣏⠁⠀⢹⡇⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⡏
    ⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠙⢦⣀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡀⠀⠀⠀⣿
    ⠀⠀⠀⠀⠀⠀⠀⢈⣢⡀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡾⢭⣠⡈⡉⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⢹
    ⠀⠀⢀⣠⠤⠒⠛⠉⠁⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠾⠁⠀⠀⠀⠉⠇⠀⠀⠀⢿⣆⠀⠀⠀⠀⠀⠀⣠⠖⠋⠀⠀⠀⢸⡇
    ⢰⡖⠉⠁⠀⠀⠀⠀⠀⠀⠀⢙⠀⠀⠠⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠏⠳⡄⠀⣠⡴⠚⠁⠀⠀⠀⣠⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀
    ⣻⠁⠻⠁⠀⠀⠀⠀⠀⠀⠀⠀⢣⡀⠀⠈⠳⣄⣀⣠⠄⠀⠀⠀⠀⠀⢳⣄⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠈⢧⡈⠳⣄⠀⠀⢰⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢹⣧⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢭⣉⣉⣟⡿⠁⠀⠀⠀⠀⠀⠀⢱⣄⠙⢧⣰⣯⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠉⠛⠒⠤⠤⠤⣄⣀⣀⣀⣀⣹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⣀⣹⣿⣿⣿⣦⡀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠈⢻⣿⣿⠿⠟⠛⠁
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣏⠁
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣻⣷⡦
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠛⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠁⢠⠇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⢀⣠⠴⠒⠚⢻⣭⣥⣤⣀⡀⠀⠒⠒⠒⠒⠒⠋⠉⠀⠀⢠⡟
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⢤⣄⣊⣉⣁⣤⠴⠚⠉⠁⠀⠀⠈⠉⠓⠲⠤⣤⣀⣀⣀⣀⣠⡴⢻⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⣴⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⡆⠀⢸⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣹⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣦⢦⣧
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣂⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⡏
    """)
    print(f"Congratulations on beating the game! \nYou've done excellent work. "
          f"{character['Name']}, these are your current stats:\n"
          f"Level: {character['Level']} \n"
          f"Current HP: {character['Current_HP']} \n"
          f"Max HP: {character['Max_HP']} \n"
          f"Experience Points: {character['Experience_Points']}"
          f"\nYou've really proved yourself as a Pokémon Trainer. "
          f"\nI will be expecting great things from you here on out."
          f"\nKeep battling with Pikachu and you'll go far."
          f"\nUntil next time...")


def fail_game():
    """
    Prints message upon failure of the game before asking user if they want to restart.

    :return:
    """
    print("""
    ⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
    ⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
    ⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
    ⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
    """)
    print("Oh no! \nPikachu has fainted from running out of HP! \nYou must heal him up before he can do any more "
          "battles. \nMewtwo is still blocking the path so you must go back to the beginning if you want to pass.")
    options = ["Restart", "Quit"]
    for count, options in enumerate(options, start=1):
        print(count, options)
    restart_game = input("Would you like to restart? ")
    if restart_game == "1":
        game()
    else:
        sys.exit()


def main():
    """
    Drives the program.
    """
    game()


if __name__ == "__main__":
    main()
