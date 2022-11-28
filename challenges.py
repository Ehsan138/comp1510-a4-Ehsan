
def trivia_one():
    options = ["Electric, Ground, and Poison", "Grass, Water, and Fire", "Fighting, Psychic, and Ghost", "Dragon, "
                                                                                                         "Flying, and "
                                                                                                         "Normal"]
    print("What are the three types of starter Pokémon?")
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer:")
    if answer == '2':
        print("That's correct!As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
        if character_dictionary["Current HP"] < character_dictionary["Max HP"]:
            character_dictionary["Current HP"] *= 1.10
        else:
            print("Oh, actually, your Pikachu is well rested.")
    else:
        print("Oops, you got that wrong.")


def trivia_two():
    options = ["Evolution stone", "Lightning stone", "Thunder stone", "Leveling up to Lvl 14"]
    print("How do you evolve a Pikachu?")
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer:")
    if answer == '3':
        print("That's correct!As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
        if character_dictionary["Current HP"] < character_dictionary["Max HP"]:
            character_dictionary["Current HP"] *= 1.10
        else:
            print("Oh, actually, your Pikachu is well rested.")
    else:
        print("Oops, you got that wrong.")


def trivia_three():
    options = ["Psychic", "Fighting", "Fairy", "Dark"]
    print("What type of Pokémon is Mewtwo?")
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer:")
    if answer == '1':
        print("That's correct! Few people know anything about Mewtwo so I'm surprised you got it so easily. Your "
              "Pikachu looks so tired. Let me heal him up for ya.")
        if character_dictionary["Current HP"] < character_dictionary["Max HP"]:
            character_dictionary["Current HP"] = character_dictionary["Max HP"]
        else:
            print("Oh, actually, your Pikachu is well rested.")
    else:
        print("Oops, you got that wrong.")


def trivia_four():
    options = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"]
    print("Who is #1 in the Pokédex?")
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer:")
    if answer == '4':
        print("That's correct! As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
        if character_dictionary["Current HP"] < character_dictionary["Max HP"]:
            character_dictionary["Current HP"] *= 1.10
        else:
            print("Oh, actually, your Pikachu is well rested.")
    else:
        print("Oops, you got that wrong.")


def trivia_five():
    options = ["Onix", "Rhydon", "Charizard", "Diglet"]
    print("Which Pokémon can live in molten lava of 3600 degrees?")
    for count, options in enumerate(options, start=1):
        print(count, options)
    answer = input("Please enter the number of the correct answer:")
    if answer == '2':
        print("That's correct! As a reward, I'll feed your Pikachu this Oran Berry which will help restore his HP.")
        if character_dictionary["Current HP"] < character_dictionary["Max HP"]:
            character_dictionary["Current HP"] *= 1.10
        else:
            print("Oh, actually, your Pikachu is well rested.")
    else:
        print("Oops, you got that wrong.")


def battle_one():
    options = ["Battle", "Flee"]
    print("Youngster Allen looks like he wants to battle with you.")
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("What do you want to do?")
    if will_battle == "1":
        print("'If you have Pokemon with you, then you're an official Pokemon trainer! You can't say no to my challenge"
              "!'\nYoungster Allen sent out Wurmple (Lvl 1)! \nGo Pikachu! \nPikachu used Thunder Shock! \nWurmple's hp"
              " went down 30hp! \nFoe Wurmple used String Shot! \nPikachu's SPEED was harshly lowered! \nPikachu used "
              "Thunder Shock! \nWurmple fainted! \nPikachu gained 20 EXP Points! \nPikachu grew to Level 2! \nPikachu "
              "learned the new move Spark! \nPlayer defeated Youngster Allen. \n'I called you because I thought I could"
              " beat you... I can tell you're new to battling. Let me give you some advice. \nWhen Pokemon battle, they"
              " eventually level up and become stronger. If the Pokemon with you become stronger, you'll be able to go "
              "farther away from here.'")
    else:
        move_character()


def battle_two():
    options = ["Battle", "Flee"]
    print("Team Rocket Jessie is looking to start a fight.")
    for count, options in enumerate(options, start=1):
        print(count, options)
    will_battle = input("Will you take her on?")
    if will_battle == "1":
        print("'To protect the world from devastation! To unite all people within our nation! To denounce the evils of "
              "truth and love!' \nTeam Rocket Jessie sends out Ekans! \nGo Pikachu! \nPikachu used Spark! \nEkans' hp "
              "went down 40hp! \nFoe Ekans used Bite! \nPikachu's hp went down 30hp! \nPikachu used Spark! \nEkans' hp "
              "went down 50hp! \nEkans fainted! \nPikachu gained 30 EXP Points! \nPikachu grew to Level 3! \nPikachu "
              "learned the new move Thunderbolt! \nPlayer defeated Team Rocket Jessie! \n'Just you wait! Our Team "
              "Rocket Leader Giovanni has something BIG in store for you...All I can say is a powerful Pokemon will "
              "help us achieve great things!'")
    else:
        move_character()


def battle_three():
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
        print("Go Pikachu! \nPikachu used Thunderbolt! \nOh no, Mewtwo dodged it. \nMewtwo used Confusion! \nPikachu is"
              " confused! \nPikachu hurt himself in his confusion! \nMewtwo used Ice Beam! \nPikachu lost 50 hp! "
              "\nPikachu snapped out of his confusion. \nPikachu used Thunderbolt! \nMewtwo's hp decreased by 30 hp! "
              "\nMewtwo used Flamethrower! \nPikachu's hp went down by 35 hp! \nPikachu used Thunderbolt! \nMewtwo's hp"
              " decreased by 40 hp! \nMewtwo used Confusion! \nPikachu moved out of the way just in time. \nPikachu"
              "looks at you waiting to be complimented. \nPikachu used Thunderbolt! \nMewtwo's hp decreased by 30 hp! "
              "... \nMewtwo fainted! \n...)


def main():
    battle_three()


if __name__ == "__main__":
    main()
