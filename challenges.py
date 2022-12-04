"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


import random
import game


def fixed_battles(challenge_name: str, character: dict, data: dict) -> None:
    """
    Execute a fixed battle based on the challenge_name that is given to the function.

    :param challenge_name: a string
    :param data: a dictionary
    :param character: a dictionary
    :precondition: challenge_name must be a string of letters which should be in character
    dictionary and package.json file
    :precondition: character and data must be dictionaries where each key is a string of letters
    :postcondition: Execute the correct fixed battle based on the
    challenge_name that is given to the function
    """
    options = ("Battle", "Flee")
    print(data[challenge_name]["opponent_introduction"])
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("What do you want to do? (Any key other than 1 will Flee): ")
    game.quit_game(will_battle)
    check_fixed_battles_conditions(challenge_name, character, will_battle, data)


def check_fixed_battles_conditions(challenge_name: str, character: dict, will_battle: str, data: dict) -> None:
    """
    Update character dictionary and print differnt game scripts based on the value of will_battle.

    :param challenge_name: a string
    :param character: a dictionary
    :param will_battle: a string
    :param data: a dictionary
    :precondition: challenge_name must be a string of letters which should be in character
    dictionary and package.json file
    :precondition: character and data must be dictionaries where each key is a string of letters
    postcondition: correctly updates character dictionary and print differnt game scripts
    based on the value of will_battle
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
            print('Attention! Looks like you have 0 EXP left!')


def random_battles(challenge_name: str, character: dict, data: dict) -> None:
    """
    Execute a random battle based on the challenge_name that is given to the function.

    :param challenge_name: a string
    :param character: a dictionary
    :param data: a dictionary
    :precondition: challenge_name must be a string of letters which should be in character
    dictionary and package.json file
    :precondition: character and data must be dictionaries where each key is a string of letters
    :postcondition: Execute the correct random battle based on the
    challenge_name that is given to the function
    """
    options = ("Battle", "Flee")
    print(data[challenge_name]["opponent_introduction"])
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("What do you want to do? (Any key other than 1 will Flee): ")
    game.quit_game(will_battle)
    check_random_battles_conditions(challenge_name, character, will_battle, data)


def check_random_battles_conditions(challenge_name: str, character: dict, will_battle: str, data: dict) -> None:
    """
    Update character dictionary and print differnt game scripts based on the value of will_battle.

    :param challenge_name: a string
    :param character: a dictionary
    :param will_battle: a string
    :param data: a dictionary
    :precondition: challenge_name must be a string of letters which should be in character
    dictionary and package.json file
    :precondition: character and data must be dictionaries where each key is a string of letters
    postcondition: correctly updates character dictionary and print differnt game scripts
    based on the value of will_battle
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


def trivia(trivia_name: str, character: dict, data: dict) -> None:
    """
    Execute a trivia based on the trivia_name that is given to the function.

    :param trivia_name: a string
    :param character: a dictionary
    :param data: a dictionary
    :precondition: trivia_name must be a string of letters which should be in character
    dictionary and package.json file
    :precondition: character and data must be dictionaries where each key is a string of letters
    :postcondition: execute the correct random battle based on the
    trivia_name that is given to the function
    """
    options = data[trivia_name]["options"]
    print(data[trivia_name]["question"])
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer: ")
    game.quit_game(answer)
    check_trivia_conditions(trivia_name, character, answer, data)


def check_trivia_conditions(trivia_name: str, character: dict, answer: str, data: dict) -> None:
    """
    Update character dictionary and print differnt game scripts based on the value of answer.

    :param trivia_name: a string
    :param character: a dictionary
    :param answer: a string
    :param data: a dictionary
    :precondition: trivia_name must be a string of letters which should be in character
    dictionary and package.json file
    :precondition: character and data must be dictionaries where each key is a string of letters
    postcondition: correctly updates character dictionary and print differnt game scripts
    based on the value of answer
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


def battle_final(character: dict, data: dict) -> None:
    """
    Execute the final battle.

    :param character: a dictionary
    :param data: a dictionary
    :precondition: character and data must be dictionaries where each key is a string of letters
    :postcondition: Execute the final battle correctly
    """
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
    game.quit_game(will_battle)
    check_battle_final_conditions(character, will_battle, data)


def check_battle_final_conditions(character: dict, will_battle: str, data: dict) -> None:
    """
    Update character dictionary and print differnt game scripts based on the value of will_battle.

    :param character: a dictionary
    :param will_battle: a string
    :param data: a dictionary
    :precondition: character and data must be dictionaries where each key is a string of letters
    postcondition: correctly updates character dictionary and print differnt game scripts
    based on the value of will_battle
    """
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


def main():
    pass


if __name__ == "__main__":
    main()
