"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


import random
import sys
import json
import itertools
import prompts


# def game():
#     rows = 10
#     columns = 10
#     board = make_board(rows, columns)
#     character = make_character("Player name")
#     achieved_goal = False
#     while is_alive(character) and not achieved_goal:
#         # Tell the user where they are describe_current_location(board, character)
#         direction = get_user_choice()
#         valid_move = validate_move(board, character, direction)
#         if valid_move:
#             move_character(character)
#             describe_current_location(board, character)
#             there_is_a_challenge = check_for_challenges()
#             if there_is_a_challenge:
#                 execute_challenge_protocol(character)
#                 if character_has_leveled():
#                     execute_glow_up_protocol()
#             achieved_goal = check_if_goal_attained(board, character)
#         else:
#             # Tell the user they can't go in that direction
#     # Print end of game (congratulations or sorry you died)
#
#
#     # create dictionary w tuples as key
#     # list as value, first thing string that describes location, second thing some event/character/question
#     # enumerated list to give users a selection of answers so they can type as little as possible
#     # picked from enumerated list if they want to go N, S, E, W: return true if they can move is valid, false if illegal


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
        # print(board)
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

    # Print end of game (congratulations or sorry you died)


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

# character = make_character('Chris')


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
            # board[(row, column)] = board(row, column)

            # text += f"{row * column} \t"

            board[(row, column)] = ['None', 'None']

            # print('{:3}'.format(x * y), end=' ')
            # board[(row, column)] = ["Welcome to the pit of doom", None]

    # for key, value in board.items:
    #     if value == 'Empty':

    return board


# board = make_board(10, 10)


def filtering_fixed_coordinates(coordinate):
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

    # board[(3, 3)][1] = 'battle_four'
    # board[(5, 8)][1] = 'battle_five'
    # board[(8, 3)][1] = 'battle_six'
    # board[(10, 10)][1] = 'battle_final'

    board[(3, 3)][1], board[(5, 8)][1], board[(8, 3)][1], board[(10, 10)][1] = \
        'battle_four', 'battle_five', 'battle_six', 'battle_final'

    list_of_coordinate = list(filter(filtering_fixed_coordinates, list_of_coordinate))

    # list_of_coordinate = [filter(filtering_fixed_coordinates, coordinate) for coordinate in list_of_coordinate]

    # list_of_coordinate = [coordinate for coordinate in list_of_coordinate
    #                       if coordinate not in [(1, 1), (10, 10), (3, 3), (5, 8), (8, 3)]]




    # while True:
    #     trivia = random.sample(list_of_coordinate, 5)
    #     if trivia != (1, 1) and trivia != (10, 10):
    #         break

    # print(random_trivia_coordinates)

    list_trivias = ['trivia_one', 'trivia_two', 'trivia_three', 'trivia_four', 'trivia_five']
    random_trivia_coordinates = random.sample(list_of_coordinate, len(list_trivias) * 2)
    iterator_trivias = itertools.cycle(list_trivias)

    for coordinate in random_trivia_coordinates:
        board[coordinate][1] = next(iterator_trivias)
        list_of_coordinate.remove(coordinate)


    # for coordinate in random_trivia_coordinates:
    #     board[coordinate][1] = random.choice(['trivia_1', 'trivia_2', 'trivia_3', 'trivia_4', 'trivia_5'])

    # print(board)



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
    # board = make_board(rows, columns)
    text = ''

    # for key in board:
    #     if key[0]

    special_cases = ['battle_four', 'battle_five', 'battle_six', 'battle_final']

    for row in range(1, rows + 1):

        text += str(row) + '\t'
        for column in range(1, columns + 1):
            # text += f"{board[(column, row)]} \t"

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
    # print(board_visual(board, 10, 10, character))


def get_user_choice():
    """
    Gets user's choice of which direction they want to move.

    :return:
    """
    directions = ['North', 'South', 'West', 'East']
    # enumerate_directions = list(enumerate(directions))

    # response = ''
    print("Which direction would you like to go?")
    for number, direction in enumerate(directions, start=1):
        print(f"{number}:\t {direction}")
    # response = input(f"Where do u wanna go broski? \n{enumerate_directions} \n")
    response = input("Please enter the number of your answer: ")
    quit_game(response)
    get_user_choice_check_input(response)
    # while response not in ['1', '2', '3', '4']:
    #     print("Which direction would you like to go?")
    #     for number, direction in enumerate(directions, start=1):
    #         print(f"{number}:\t {direction}")
    #     response = input("Please enter the number of your answer: ")
    #     quit_game(response)

    return response


def get_user_choice_check_input(response):
    directions = ['North', 'South', 'West', 'East']
    while response not in ['1', '2', '3', '4']:
        print("Which direction would you like to go?")
        for number, direction in enumerate(directions, start=1):
            print(f"{number}:\t {direction}")
        # response = input(f"Where do u wanna go broski? \n{enumerate_directions} \n")
        response = input("This direction is not reachable.\n"
                         "The number that you choose must be between 1 and 4.\n"
                         "Please enter the number of your answer: ")
        quit_game(response)

    # board[(0, 0)] = adfkjdfklj


# def board(coordinate_x , coordinate_y):
#     """
#
#     :param coordinate_x:
#     :param coordinate_y:
#     :return:
#     """
#
#     return 'Empty'


# def describe_current_location():
#
#
# def get_user_choice():
#
#
# def validate_move():


# def is_alive(character):
#     if HP > 0:
#         return True
#     else:
#         return False


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


# def pre_validate_move()


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


    # if int(direction) == 0 and character['y_coordinate'] - 1 >= 1:
    #     character['y_coordinate'] -= 1
    #     return True
    # elif int(direction) == 1 and character['y_coordinate'] + 1 <= 10:
    #     character['y_coordinate'] += 1
    #     return True
    # elif int(direction) == 2 and character['x_coordinate'] - 1 >= 1:
    #     character['x_coordinate'] -= 1
    #     return True
    # elif int(direction) == 3 and character['x_coordinate'] + 1 <= 10:
    #     character['x_coordinate'] += 1
    #     return True
    # else:
    #     return False


def move_character(character, direction, steps):
    if int(direction) == 1:
        character['y_coordinate'] -= int(steps)
    elif int(direction) == 2:
        character['y_coordinate'] += int(steps)
    elif int(direction) == 3:
        character['x_coordinate'] -= int(steps)
    elif int(direction) == 4:
        character['x_coordinate'] += int(steps)


# def update_current_location(board, character):
#     board[(character["x_coordinate"], character["y_coordinate"])][0] = 'current'


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
    if character['Current_HP'] > 0:
        return True
    else:
        return False


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
    challenge = board[(character["x_coordinate"], character["y_coordinate"])][1]
    if challenge in ['battle_one', 'battle_two', 'battle_three']:
        get_user_choice_random_battles(challenge, character)
    elif challenge in ['battle_four', 'battle_five', 'battle_six']:
        if character[challenge] == 0:
            get_user_choice_fixed_battles(challenge, character)
    elif challenge == 'battle_final':
        if character[challenge] == 0:
            battle_final(character)
    elif challenge in ['trivia_one', 'trivia_two', 'trivia_three', 'trivia_four', 'trivia_five']:
        get_user_answer_trivia(challenge, character)



    # if board[(character["x_coordinate"], character["y_coordinate"])][1] == 'trivia_one':
    #     trivia_one(character)
    # elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'trivia_two':
    #     trivia_two(character)
    # elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'trivia_three':
    #     trivia_three(character)
    # elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'trivia_four':
    #     trivia_four(character)
    # elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'trivia_five':
    #     trivia_five(character)
    # elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'battle_one':
    #     battle_one()
    # elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'battle_two':
    #     battle_two()
    # elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'battle_three':
    #     battle_three()
    # elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'battle_four':
    #     battle_four()
    # elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'battle_final':
    #     battle_final()


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
    character["Level"] = (character["Experience_Points"] // 1000) + 1
    # if 0 <= character["Experience_Points"] < 1000:
    #     character["Level"] = 1
    #     character["Max_HP"] += 100
    #     character["Current_HP"] = character["Max_HP"]
    # elif 1000 <= character["Experience_Points"] < 2000:
    #     character["Level"] = 2
    #     character["Max_HP"] += 100
    #     character["Current_HP"] = character["Max_HP"]
    # elif 2000 <= character["Experience_Points"] < 3000:
    #     character["Level"] = 3
    #     character["Max_HP"] += 100
    #     character["Current_HP"] = character["Max_HP"]


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


# def check_if_goal_attained(board, character):
#     if character[board[(character["x_coordinate"], character["y_coordinate"])][1]] == 1:
#         return True
#     else:
#         return False

def check_if_goal_attained(character):
    """
    Checks if the character has

    :param board:
    :param character:
    :param rows:
    :param columns:
    :return:
    """
    # return character[board[(rows, columns)][1]] == 1
    return character['battle_final'] == 1


#############################################################################################


def get_user_choice_fixed_battles(challenge_name, character):
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
    execute_fixed_battles(challenge_name, character, will_battle, data)
    # if will_battle == "1":
    #     if challenge_name == 'battle_five' and character["battle_four"] == 0:
    #         print(data[challenge_name]["is_not_ready"])
    #     elif challenge_name == 'battle_six' and (character["battle_four"] == 0 or character["battle_five"] == 0):
    #         print(data[challenge_name]["is_not_ready"])
    #     else:
    #         character["Experience_Points"] += random.randint(500, 650)
    #         new_randomize_hp = 1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"]
    #         if character["Current_HP"] - new_randomize_hp >= 0:
    #             character["Current_HP"] -= new_randomize_hp
    #             character[challenge_name] = 1
    #             print(data[challenge_name]["battle_statement"].format(health=character["Current_HP"],
    #                                                                   experience=character["Experience_Points"]))
    #         else:
    #             character["Current_HP"] = 0
    #             print("Uh oh! Pikachu has fainted!")
    # else:
    #     if character["Experience_Points"] - 100 >= 0:
    #         character["Experience_Points"] -= 100
    #         print("You lose 50 EXP Points for fleeing from battle.\nPikachu now has {experience} EXP Points!".format(
    #             experience=character["Experience_Points"]))
    #     else:
    #         character["Experience_Points"] = (character["Experience_Points"] // 1000) * 1000
    #         print('Now you have zero EXP for your current level, sorry not sorry :)')


def execute_fixed_battles(challenge_name, character, will_battle, data):
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




def get_user_choice_random_battles(challenge_name, character):
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
    execute_random_battles(challenge_name, character, will_battle, data)
    # if will_battle == "1":
    #     character["Experience_Points"] += random.randint(200, 300)
    #     new_randomize_hp = 1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"]
    #     if character["Current_HP"] - new_randomize_hp >= 0:
    #         character["Current_HP"] -= new_randomize_hp
    #         character[challenge_name] = 1
    #         print(data[challenge_name]["battle_statement"].format(health=character["Current_HP"],
    #                                                               experience=character["Experience_Points"]))
    #     else:
    #         character["Current_HP"] = 0
    #         print("Uh oh! Pikachu has fainted!")
    # else:
    #     if character["Experience_Points"] - 100 >= 0:
    #         character["Experience_Points"] -= 100
    #         print("You lose 100 EXP for fleeing from battle.\nPikachu now has {experience} EXP!".format(
    #             experience=character["Experience_Points"]))
    #     else:
    #         character["Experience_Points"] = (character["Experience_Points"] // 1000) * 1000
    #         print('Attention! Looks like you have 0 EXP left!')


def execute_random_battles(challenge_name, character, will_battle, data):
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


def get_user_answer_trivia(trivia_name, character):
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
    execute_trivia_protocol(trivia_name, character, answer, data)
    # if answer == data[trivia_name]["right_answer"]:
    #     if trivia_name == 'trivia_three':
    #         character["Experience_Points"] += 500
    #     else:
    #         character["Experience_Points"] += 100
    #     character[trivia_name] = 1
    #     print(data[trivia_name]['award'].format(health=character["Current_HP"]))
    #     if (character["Current_HP"] < character["Max_HP"]) and trivia_name == 'trivia_three':
    #         character["Current_HP"] = character["Max_HP"]
    #     elif (character["Current_HP"] < character["Max_HP"]) and trivia_name != 'trivia_three':
    #         character["Current_HP"] *= 1.10
    #     else:
    #         print("Oh, actually, your Pikachu is well rested.")
    # else:
    #     print("Oops, you got that wrong.")


def execute_trivia_protocol(trivia_name, character, answer, data):
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




#
# def trivia_one(character):
#     options = ["Electric, Ground, and Poison", "Grass, Water, and Fire", "Fighting, Psychic, and Ghost", "Dragon, "
#                                                                                                          "Flying, and "
#                                                                                                          "Normal"]
#     print("What are the three types of starter Pokémon?")
#     for count, options in enumerate(options, start=1):
#         print(count, options)
#     answer = input("Please enter the number of the correct answer:")
#     if answer == '2':
#         character["Experience_Points"] += 100
#         character["trivia_one"] = 1
#         print("That's correct!As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
#         if character["Current_HP"] < character["Max_HP"]:
#             character["Current_HP"] *= 1.10
#         else:
#             print("Oh, actually, your Pikachu is well rested.")
#     else:
#         print("Oops, you got that wrong.")
#
#
# def trivia_two(character):
#     options = ["Evolution stone", "Lightning stone", "Thunder stone", "Leveling up to Lvl 14"]
#     print("How do you evolve a Pikachu?")
#     for count, options in enumerate(options, start=1):
#         print(count, options)
#     answer = input("Please enter the number of the correct answer:")
#     if answer == '3':
#         character["Experience_Points"] += 100
#         character["trivia_two"] = 1
#         print("That's correct!As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
#         if character["Current_HP"] < character["Max_HP"]:
#             character["Current_HP"] *= 1.10
#         else:
#             print("Oh, actually, your Pikachu is well rested.")
#     else:
#         print("Oops, you got that wrong.")
#
#
# def trivia_three(character):
#     options = ["Psychic", "Fighting", "Fairy", "Dark"]
#     print("What type of Pokémon is Mewtwo?")
#     for count, options in enumerate(options, start=1):
#         print(count, options)
#     answer = input("Please enter the number of the correct answer:")
#     if answer == '1':
#         character["Experience_Points"] += 500
#         character["trivia_three"] = 1
#         print("That's correct! Few people know anything about Mewtwo so I'm surprised you got it so easily. Your "
#               "Pikachu looks so tired. Let me heal him up for ya.")
#         if character["Current_HP"] < character["Max_HP"]:
#             character["Current_HP"] = character["Max_HP"]
#         else:
#             print("Oh, actually, your Pikachu is well rested.")
#     else:
#         print("Oops, you got that wrong.")
#
#
# def trivia_four(character):
#     options = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"]
#     print("Who is #1 in the Pokédex?")
#     for count, options in enumerate(options, start=1):
#         print(count, options)
#     answer = input("Please enter the number of the correct answer:")
#     if answer == '4':
#         character["Experience_Points"] += 100
#         character["trivia_four"] = 1
#         print("That's correct! As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
#         if character["Current_HP"] < character["Max_HP"]:
#             character["Current_HP"] *= 1.10
#         else:
#             print("Oh, actually, your Pikachu is well rested.")
#     else:
#         print("Oops, you got that wrong.")
#
#
# def trivia_five(character):
#     options = ["Onix", "Rhydon", "Charizard", "Diglet"]
#     print("Which Pokémon can live in molten lava of 3600 degrees?")
#     for count, options in enumerate(options, start=1):
#         print(count, options)
#     answer = input("Please enter the number of the correct answer:")
#     if answer == '2':
#         character["Experience_Points"] += 100
#         character["trivia_five"] = 1
#         print("That's correct! As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
#         if character["Current_HP"] < character["Max_HP"]:
#             character["Current_HP"] *= 1.10
#         else:
#             print("Oh, actually, your Pikachu is well rested.")
#     else:
#         print("Oops, you got that wrong.")


# def battle_one(character):
#     options = ("Battle", "Flee")
#     print("Youngster Allen looks like he wants to battle with you.")
#     for count, options in enumerate(options, start=1):
#         print(count, options)
#     will_battle = input("What do you want to do?")
#     if will_battle == "1":
#         character["Experience_Points"] += random.randint(200, 300)
#         character["Current_HP"] -= (1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"])
#         character["battle_one"] = 1
#         print("'If you have Pokemon with you, then you're an official Pokemon trainer! You can't say no to my challenge"
#               "!'\nYoungster Allen sent out Wurmple (Lvl 1)! \nGo Pikachu! \nPikachu used Thunder Shock! \nWurmple's hp"
#               " went down 30hp! \nFoe Wurmple used String Shot! \nPikachu's SPEED was harshly lowered! \nPikachu used "
#               "Thunder Shock! \nWurmple fainted! \nPikachu gained 20 EXP Points! \nPikachu grew to Level 2! \nPikachu "
#               "learned the new move Spark! \nPlayer defeated Youngster Allen. \n'I called you because I thought I could"
#               " beat you... I can tell you're new to battling. Let me give you some advice. \nWhen Pokemon battle, they"
#               " eventually level up and become stronger. If the Pokemon with you become stronger, you'll be able to go "
#               "farther away from here.'")
#     else:
#         character["Experience_Points"] -= 50
#
#
# def battle_two(character):
#     options = ("Battle", "Flee")
#     print("Team Rocket Jessie is looking to start a fight.")
#     for count, options in enumerate(options, start=1):
#         print(count, options)
#     will_battle = input("Will you take her on?")
#     if will_battle == "1":
#         character["Experience_Points"] += random.randint(500, 650)
#         character["Current_HP"] -= (1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"])
#         character["battle_two"] = 1
#         print("'To protect the world from devastation! To unite all people within our nation! To denounce the evils of "
#               "truth and love!' \nTeam Rocket Jessie sends out Ekans! \nGo Pikachu! \nPikachu used Spark! \nEkans' hp "
#               "went down 40hp! \nFoe Ekans used Bite! \nPikachu's hp went down 30hp! \nPikachu used Spark! \nEkans' hp "
#               "went down 50hp! \nEkans fainted! \nPikachu gained 30 EXP Points! \nPikachu grew to Level 3! \nPikachu "
#               "learned the new move Thunderbolt! \nPlayer defeated Team Rocket Jessie! \n'Just you wait! Our Team "
#               "Rocket Boss Giovanni has something BIG in store for you...All I can say is a powerful Pokemon will help "
#               "us achieve great things!'")
#     else:
#         character["Experience_Points"] -= 50
#
#
# def battle_three(character):
#     options = ("Battle", "Flee")
#     print("Team Rocket James is looking to start a fight.")
#     for count, options in enumerate(options, start=1):
#         print(count, options)
#     will_battle = input("Will you take him on?")
#     if will_battle == "1" and character["battle_two"] == 1:
#         character["Experience_Points"] += random.randint(500, 650)
#         character["Current_HP"] -= (1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"])
#         character["battle_three"] = 1
#         print("'You may have defeated Jessie but I will avenge her! Get ready to cry at my feet!' \nTeam Rocket "
#               "James sends out Meowth! \nGo Pikachu! \nPikachu used Spark! \nMeowth's hp went down 40hp! \nFoe "
#               "Meowth used Pay Day! \nPikachu's hp went down 30hp! \nPikachu used Spark! \nMeowth's hp went down "
#               "50hp! \nMeowth fainted! \nPikachu gained 30 EXP Points! \nPikachu grew to Level 3! \nPikachu learned"
#               " the new move Thunderbolt! \nPlayer defeated Team Rocket James! \n'Okay...You may have defeated me "
#               "too BUT we will NEVER give up! \nNot until our goal is achieved!'")
#     elif will_battle == "1" and character["battle_two"] == 0:
#         print("Oh nevermind, go find Team Rocket Jessie first before battling me.")
#     else:
#         character["Experience_Points"] -= 50
#         print("You lose 50 EXP Points for fleeing from battle.")
#
#
# def battle_four(character):
#     options = ("Battle", "Flee")
#     print("Team Rocket Boss Giovanni is furiously glaring at you.")
#     for count, options in enumerate(options, start=1):
#         print(count, options)
#     will_battle = input("Will you battle him?")
#     if will_battle == "1" and character["battle_three"] == 1:
#         character["Experience_Points"] += random.randint(500, 650)
#         character["Current_HP"] -= (1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"])
#         character["battle_four"] = 1
#         print("'I heard about what happened from my underlings. If you are so adamant on opposing us, show me your "
#               "power!' \nTeam Rocket Boss Giovanni sends out Persian! \nGo Pikachu! \nPikachu used Spark! \nPersian's "
#               "hp went down 40hp! \nFoe Persian used Assurance! \nPikachu's hp went down 30hp! \nPikachu used Spark! \n"
#               "Persian's hp went down 50hp! \nPersian fainted! \nPikachu gained 30 EXP Points! \nPikachu grew to Level "
#               "3! \nPikachu learned the new move Thunderbolt! \nPlayer defeated Team Rocket Boss Giovanni! \n'I lost "
#               "because of bad luck. Next time I will battle you with better Pokémon. \nNow I just need to look for "
#               "Mewtwo...'")
#     elif will_battle == "1" and character["battle_three"] == 0:
#         print("Oh nevermind, go find Team Rocket James first before battling me.")
#     else:
#         character["Experience_Points"] -= 50
#         print("You lose 50 EXP Points for fleeing from battle.")


def battle_final(character):
    """
    Executes the final battle.

    :param character:
    :return:
    """
    print("There is a menacing pokemon towering over you, blocking the only path you can take.", """
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
    print("\nUpon closer inspection it is legendary pokemon Mewtwo! \nMewtwo makes eye contact with you. It seems you "
          "must battle Mewtwo to pass. \nPikachu seems a little bit worried about being able to battle.")
    options = ("Battle", "Flee")
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("Will you battle Mewtwo? ")
    quit_game(will_battle)
    if will_battle == "1":
        if character["battle_four"] == 1 and character["battle_four"] == 1 and character["battle_four"] == 1 and \
                character["Level"] >= 3:
            character["Experience_Points"] += random.randint(500, 650)
            character["Current_HP"] -= (1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"])
            character["battle_final"] = 1
            print("Go Pikachu! \nPikachu used Thunderbolt! \nOh no, Mewtwo dodged it. \nMewtwo used Confusion! "
                  "\nPikachu is confused! \nPikachu hurt himself in his confusion! \nMewtwo used Ice Beam! \nPikachu "
                  "is dazed from the impact! \nPikachu snapped out of his confusion. \nPikachu used Thunderbolt! "
                  "\nMewtwo's HP sharply dropped! \nMewtwo used Flamethrower! \nPikachu's health is now {health} HP "
                  "Points! \nPikachu used Thunderbolt! \nIt was a critical hit! \nMewtwo used Confusion! \nPikachu "
                  "moved out of the way just in time. \nPikachu looks at you waiting to be complimented. \nPikachu "
                  "used Thunderbolt! \nMewtwo fainted! \nYou have defeated Mewtwo!")
        elif character["battle_four"] == 0 or character["battle_five"] == 0 or character["battle_six"] == 0:
            print("Oh, seems like Mewtwo deems you unworthy of battle. Maybe go find Team Rocket Jessie 🐍, Team Rocket"
                  " James 🐱, and Team Rocket Boss Giovanni 🐆 first.")
        elif character["Level"] < 3:
            print("You must be at least Level 3 to challenge Mewtwo.")

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



def access_jason(name):
    file = open('package.json')
    data = json.load(file)
    print(data[name]["opponent_introduction"])





def main():
    """
    Drives the program.
    """
    # character = make_character()
    # print(make_board(10, 10))
    # board = make_board(10, 10)
    # placing_challenges(board, 10, 10)
    # # print(board_visual(board, 10, 10))
    # describe_current_location(board, character)
    # print(board)
    # print(character)
    #
    # direction = get_user_choice()
    # print(direction)
    # steps = get_user_steps()
    #
    # print(character)
    # print(board)
    # print(validate_move(character, direction, steps, 10, 10))
    # move_character(character, direction, steps)
    #
    # print(character)
    # print(board)
    # print(board[(8, 3)][1] == 'battle_six')


    #
    # # print(board_visual(board, 10, 10))
    #
    # direction = get_user_choice()
    # print(direction)
    # steps = get_user_steps()
    # print(validate_move(character, direction, steps))
    # move_character(character, direction, steps)
    # update_current_location(board, character)
    # # print(character)
    # # print(board)
    # # print(board_visual(board, 10, 10))
    # there_is_a_challenge = check_for_challenges(board, character)
    # print(there_is_a_challenge)

    game()


if __name__ == "__main__":
    main()
