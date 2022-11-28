"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


import random
import sys


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
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    while is_alive(character) and not achieved_goal:
        describe_current_location(board, character)
        board_visual(board, rows, columns)
        direction = get_user_choice()
        steps = get_user_steps()
        valid_move = validate_move(character, direction, steps, rows, columns)
        if valid_move:
            move_character(character, direction, steps)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges(board, character)
            if there_is_a_challenge and first_time_challenge(board, character):
                level = character["Level"]
                execute_challenge_protocol(board, character)
                level_up(character)
                if character_has_leveled(character, level):
                    execute_glow_up_protocol(character)
            achieved_goal = check_if_goal_attained(board, character, rows, columns)
        else:
            print("Tell the user they can't go in that direction.")

    if not is_alive(character):
        game_fail()
    elif achieved_goal:
        game_succeed()

    # Print end of game (congratulations or sorry you died)



def make_character():
    """
    Creates and returns a dictionary that contains key:value pairs.

    :return: dictionary that contains key:value pairs
    """
    name = input("Name: ")
    character_dictionary = {"Name": name, "x_coordinate": 1,
                            "y_coordinate": 1, "Current_HP": 100,
                            "Max_HP": 100, "Experience_Points": 0,
                            "Level": 1, "trivia_one": 0, "trivia_two": 0,
                            "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                            "battle_one": 0, "battle_two": 0, "battle_three": 0,
                            "battle_four": 0, "battle_final": 0}

    return character_dictionary

# character = make_character('Chris')


def make_board(rows, columns):
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


def placing_challenges(board, rows, columns):
    list_of_coordinate = [(x_coordinate, y_coordinate)
                          for x_coordinate in range(1, columns + 1) for y_coordinate in range(1, rows + 1)]

    while True:
        challenge_1 = random.sample(list_of_coordinate, 5)
        if challenge_1 != (1, 1) and challenge_1 != (10, 10):
            break

    print(challenge_1)

    for coordinate in challenge_1:
        board[coordinate][1] = f"challenge"

    # print(board)



def board_visual(board, rows, columns):
    """

    :param rows:
    :param columns:
    :return:
    """
    # board = make_board(rows, columns)
    text = ''

    # for key in board:
    #     if key[0]

    for row in range(1, rows + 1):
        text += '\n'
        for column in range(1, columns + 1):
            text += f"{board[(column, row)]} \t"
            # if (row, column) in board:

    return text


def describe_current_location(board, character):
    """

    :param board:
    :param character:
    :return:
    """
    board[(character["x_coordinate"], character["y_coordinate"])][0] = 'current'
    print(board_visual(board, 10, 10))


def get_user_choice():
    directions = ['North', 'South', 'West', 'East']
    # enumerate_directions = list(enumerate(directions))

    response = ''
    while response not in ['0', '1', '2', '3']:
        print("Where do u wanna go broski")
        for number, direction in enumerate(directions):
            print(f"{number}:\t {direction}")
        # response = input(f"Where do u wanna go broski? \n{enumerate_directions} \n")
        response = input("Please enter the number of the correct answer: ")

    return response

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
    steps = ''
    while steps not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print("How many steps do u wanna take? (this number must be 1 and 9)")
        steps = input("Please enter your answer here: ")

    return steps


def validate_move(character, direction, steps, rows, columns):
    if int(direction) == 0 and character['y_coordinate'] - int(steps) >= 1:
        return True
    elif int(direction) == 1 and character['y_coordinate'] + int(steps) <= rows:
        return True
    elif int(direction) == 2 and character['x_coordinate'] - int(steps) >= 1:
        return True
    elif int(direction) == 3 and character['x_coordinate'] + int(steps) <= columns:
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
    if int(direction) == 0:
        character['y_coordinate'] -= int(steps)
    elif int(direction) == 1:
        character['y_coordinate'] += int(steps)
    elif int(direction) == 2:
        character['x_coordinate'] -= int(steps)
    elif int(direction) == 3:
        character['x_coordinate'] += int(steps)


# def update_current_location(board, character):
#     board[(character["x_coordinate"], character["y_coordinate"])][0] = 'current'


def check_for_challenges(board, character):
    if board[(character["x_coordinate"], character["y_coordinate"])][1] == 'challenge':
        return True
    else:
        return False


def is_alive(character):
    if character['Current_HP'] > 0:
        return True
    else:
        return False


def first_time_challenge(board, character):
    if character[board[(character["x_coordinate"], character["y_coordinate"])][1]] == 0:
        return True
    else:
        return False



def execute_challenge_protocol(board, character):
    if board[(character["x_coordinate"], character["y_coordinate"])][1] == 'trivia_one':
        trivia_one(character)
    elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'trivia_two':
        trivia_two(character)
    elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'trivia_three':
        trivia_three(character)
    elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'trivia_four':
        trivia_four(character)
    elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'trivia_five':
        trivia_five(character)
    elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'battle_one':
        battle_one()
    elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'battle_two':
        battle_two()
    elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'battle_three':
        battle_three()
    elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'battle_four':
        battle_four()
    elif board[(character["x_coordinate"], character["y_coordinate"])][1] == 'battle_final':
        battle_final()


def character_has_leveled(character, level):
    if character['Level'] - level == 1:
        return True
    else:
        return False


def level_up(character):
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
    character["Max_HP"] += 100
    character["Current_HP"] = character["Max_HP"]
    print(f"Name: {character['Name']} \n"
          f"Level: {character['Level']} \n"
          f"Current HP: {character['Current_HP']} \n"
          f"Max HP: {character['Max_HP']} \n"
          f"Experience Points: {character['Experience_Points']} \n")


# def check_if_goal_attained(board, character):
#     if character[board[(character["x_coordinate"], character["y_coordinate"])][1]] == 1:
#         return True
#     else:
#         return False

def check_if_goal_attained(board, character, rows, columns):
    return character[board[(rows, columns)][1]] == 1


#############################################################################################

def trivia_one(character):
    options = ["Electric, Ground, and Poison", "Grass, Water, and Fire", "Fighting, Psychic, and Ghost", "Dragon, "
                                                                                                         "Flying, and "
                                                                                                         "Normal"]
    print("What are the three types of starter Pokémon?")
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer:")
    if answer == '2':
        character["Experience_Points"] += 100
        character["trivia_one"] = 1
        print("That's correct!As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
        if character["Current_HP"] < character["Max_HP"]:
            character["Current_HP"] *= 1.10
        else:
            print("Oh, actually, your Pikachu is well rested.")
    else:
        print("Oops, you got that wrong.")


def trivia_two(character):
    options = ["Evolution stone", "Lightning stone", "Thunder stone", "Leveling up to Lvl 14"]
    print("How do you evolve a Pikachu?")
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer:")
    if answer == '3':
        character["Experience_Points"] += 100
        character["trivia_two"] = 1
        print("That's correct!As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
        if character["Current_HP"] < character["Max_HP"]:
            character["Current_HP"] *= 1.10
        else:
            print("Oh, actually, your Pikachu is well rested.")
    else:
        print("Oops, you got that wrong.")


def trivia_three(character):
    options = ["Psychic", "Fighting", "Fairy", "Dark"]
    print("What type of Pokémon is Mewtwo?")
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer:")
    if answer == '1':
        character["Experience_Points"] += 500
        character["trivia_three"] = 1
        print("That's correct! Few people know anything about Mewtwo so I'm surprised you got it so easily. Your "
              "Pikachu looks so tired. Let me heal him up for ya.")
        if character["Current_HP"] < character["Max_HP"]:
            character["Current_HP"] = character["Max_HP"]
        else:
            print("Oh, actually, your Pikachu is well rested.")
    else:
        print("Oops, you got that wrong.")


def trivia_four(character):
    options = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"]
    print("Who is #1 in the Pokédex?")
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer:")
    if answer == '4':
        character["Experience_Points"] += 100
        character["trivia_four"] = 1
        print("That's correct! As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
        if character["Current_HP"] < character["Max_HP"]:
            character["Current_HP"] *= 1.10
        else:
            print("Oh, actually, your Pikachu is well rested.")
    else:
        print("Oops, you got that wrong.")


def trivia_five(character):
    options = ["Onix", "Rhydon", "Charizard", "Diglet"]
    print("Which Pokémon can live in molten lava of 3600 degrees?")
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer:")
    if answer == '2':
        character["Experience_Points"] += 100
        character["trivia_five"] = 1
        print("That's correct! As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
        if character["Current_HP"] < character["Max_HP"]:
            character["Current_HP"] *= 1.10
        else:
            print("Oh, actually, your Pikachu is well rested.")
    else:
        print("Oops, you got that wrong.")


def battle_one(character):
    options = ["Battle", "Flee"]
    print("Youngster Allen looks like he wants to battle with you.")
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("What do you want to do?")
    if will_battle == "1":
        character["Experience_Points"] += random.randint(500, 650)
        character["Current_HP"] -= (1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"])
        character["battle_one"] = 1
        print("'If you have Pokemon with you, then you're an official Pokemon trainer! You can't say no to my challenge"
              "!'\nYoungster Allen sent out Wurmple (Lvl 1)! \nGo Pikachu! \nPikachu used Thunder Shock! \nWurmple's hp"
              " went down 30hp! \nFoe Wurmple used String Shot! \nPikachu's SPEED was harshly lowered! \nPikachu used "
              "Thunder Shock! \nWurmple fainted! \nPikachu gained 20 EXP Points! \nPikachu grew to Level 2! \nPikachu "
              "learned the new move Spark! \nPlayer defeated Youngster Allen. \n'I called you because I thought I could"
              " beat you... I can tell you're new to battling. Let me give you some advice. \nWhen Pokemon battle, they"
              " eventually level up and become stronger. If the Pokemon with you become stronger, you'll be able to go "
              "farther away from here.'")
    else:
        character["Experience_Points"] -= 50


def battle_two(character):
    options = ["Battle", "Flee"]
    print("Team Rocket Jessie is looking to start a fight.")
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("Will you take her on?")
    if will_battle == "1":
        character["Experience_Points"] += random.randint(500, 650)
        character["Current_HP"] -= (1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"])
        character["battle_two"] = 1
        print("'To protect the world from devastation! To unite all people within our nation! To denounce the evils of "
              "truth and love!' \nTeam Rocket Jessie sends out Ekans! \nGo Pikachu! \nPikachu used Spark! \nEkans' hp "
              "went down 40hp! \nFoe Ekans used Bite! \nPikachu's hp went down 30hp! \nPikachu used Spark! \nEkans' hp "
              "went down 50hp! \nEkans fainted! \nPikachu gained 30 EXP Points! \nPikachu grew to Level 3! \nPikachu "
              "learned the new move Thunderbolt! \nPlayer defeated Team Rocket Jessie! \n'Just you wait! Our Team "
              "Rocket Boss Giovanni has something BIG in store for you...All I can say is a powerful Pokemon will help "
              "us achieve great things!'")
    else:
        character["Experience_Points"] -= 50


def battle_three(character):
    options = ["Battle", "Flee"]
    print("Team Rocket James is looking to start a fight.")
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("Will you take him on?")
    if will_battle == "1":
        character["Experience_Points"] += random.randint(500, 650)
        character["Current_HP"] -= (1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"])
        character["battle_three"] = 1
        print("'You may have defeated Jessie but I will avenge her! Get ready to cry at my feet!' \nTeam Rocket James "
              "sends out Meowth! \nGo Pikachu! \nPikachu used Spark! \nMeowth's hp went down 40hp! \nFoe Meowth used "
              "Pay Day! \nPikachu's hp went down 30hp! \nPikachu used Spark! \nMeowth's hp went down 50hp! \nMeowth "
              "fainted! \nPikachu gained 30 EXP Points! \nPikachu grew to Level 3! \nPikachu learned the new move "
              "Thunderbolt! \nPlayer defeated Team Rocket James! \n'Okay...You may have defeated me too BUT we will "
              "NEVER give up! \nNot until our goal is achieved!'")
    else:
        character["Experience_Points"] -= 50


def battle_four(character):
    options = ["Battle", "Flee"]
    print("Team Rocket Boss Giovanni is furiously glaring at you.")
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("Will you battle him?")
    if will_battle == "1":
        character["Experience_Points"] += random.randint(500, 650)
        character["Current_HP"] -= (1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"])
        character["battle_four"] = 1
        print("'I heard about what happened from my underlings. If you are so adamant on opposing us, show me your "
              "power!' \nTeam Rocket Boss Giovanni sends out Persian! \nGo Pikachu! \nPikachu used Spark! \nPersian's "
              "hp went down 40hp! \nFoe Persian used Assurance! \nPikachu's hp went down 30hp! \nPikachu used Spark! \n"
              "Persian's hp went down 50hp! \nPersian fainted! \nPikachu gained 30 EXP Points! \nPikachu grew to Level "
              "3! \nPikachu learned the new move Thunderbolt! \nPlayer defeated Team Rocket Boss Giovanni! \n'I lost "
              "because of bad luck. Next time I will battle you with better Pokémon. \nNow I just need to look for "
              "Mewtwo...'")
    else:
        character["Experience_Points"] -= 50


def battle_final(character):
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
    options = ["Battle", "Flee"]
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("Will you battle Mewtwo?")
    if will_battle == "1":
        character["Experience_Points"] += random.randint(500, 650)
        character["Current_HP"] -= (1 + round(random.uniform(0.10, 0.25), 2) * character["Max_HP"])
        character["battle_final"] = 1
        print("Go Pikachu! \nPikachu used Thunderbolt! \nOh no, Mewtwo dodged it. \nMewtwo used Confusion! \nPikachu is"
              " confused! \nPikachu hurt himself in his confusion! \nMewtwo used Ice Beam! \nPikachu lost 50 hp! "
              "\nPikachu snapped out of his confusion. \nPikachu used Thunderbolt! \nMewtwo's hp decreased by 30 hp! "
              "\nMewtwo used Flamethrower! \nPikachu's hp went down by 35 hp! \nPikachu used Thunderbolt! \nMewtwo's hp"
              " decreased by 40 hp! \nMewtwo used Confusion! \nPikachu moved out of the way just in time. \nPikachu"
              "looks at you waiting to be complimented. \nPikachu used Thunderbolt! \nMewtwo's hp decreased by 30 hp! "
              "... \nMewtwo fainted! \n...")

#################################################################################################################


def game_succeed():
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
    print("Congratulations on beating the game! \nYou've done excellent work. \nYou've really proved yourself as a "
          "Pokémon Trainer. \nI will be expecting great things from you here on out. \nKeep battling with Pikachu and "
          "you'll go far. \nUntil next time...")


def game_fail():
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
    restart_game = input("Would you like to restart?")
    if restart_game == "1":
        game()
    else:
        sys.exit()




def main():
    # character = make_character('Chris')
    # print(make_board(10, 10))
    # board = make_board(10, 10)
    # placing_challenges(board)
    # print(board_visual(board, 10, 10))
    # describe_current_location(board, character)
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
