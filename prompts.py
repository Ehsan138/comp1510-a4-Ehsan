from game import game
import sys


def game_intro_1() -> None:
    """
    Print welcome statement for the game.
    """
    print("""                          
                                       ,'\ 
         _.----.        ____         ,'  _\  ___    ___     ____
     _,-'       `.     |    |  /`.   \,-'   |   \  /   |   |    \  |`. .
     \      __    \    '-.  | /   `.  ___   |    \/    |   '-.   \ |   |
      \.    \ \   |  __  |  |/    ,','_  `. |          | __  |    \|   |
       \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |   |
        \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \   |     |
         \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  |  |\    |
          \    \ \      /       `-.`.___,-' |  |\  /| \      /   | |   |
           \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|   | |   |
            \_.-'       |__|    `-._ |              '-.|     '-. | |   |
                                    `'                             '-._|
    """)
    print("Welcome to Pokémon Pikachu Edition!")


def game_intro_2(character: dict) -> None:
    """
    Print the game's instructions.

    :param character: a dictionary where keys are strings of letters
    :precondition: character must be a dictionary where each key is a string of letters
    :postcondition: the function correctly prints the intro, without changing character
    """
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠒⠛⠛⣁⣽⠖⠲⢤⣀⣠⣴⠄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡞⠃⠀⢀⣤⣞⣿⡟⣠⠴⣚⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠉⡾⠁⢠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠝⣦⣄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠂⠀⣼⣵⣾⣿⣿⣿⣿⣿⣿⢻⣟⣿⣿⣿⣿⣁⢆⣄⣈⢷⡄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠤⠄⣰⣾⣿⠿⣫⣿⢯⡟⣿⡟⠃⣼⣿⡯⣿⣿⣿⣿⣾⣿⠿⣶⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⣠⣾⣏⢨⣷⣾⣿⡿⠫⣴⣿⣷⣿⣿⣿⣅⢸⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡴⢫⣿⣿⣿⣿⡿⠋⣿⡟⣿⣿⡿⡿⣃⣿⣿⣿⣦⣿⠿⣿⣿⣿⣿⣿⣄⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⢿⣿⣿⠁⠁⠀⠋⠸⣽⠟⠘⠹⡇⢹⣿⣿⢿⣿⠀⢸⠛⠛⠋⠁⢸⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡸⣿⡇⠀⢀⠀⠀⠐⠁⠀⠀⠀⠀⢸⣿⣿⠀⣿⠀⠀⢳⡖⠒⠒⢿⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣷⣬⣥⡜⢹⠀⠀⢤⣀⠀⠀⠀⠀⢸⠃⠇⠀⠁⠀⠀⠈⡇⠀⠀⠘⡆⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠙⣟⠁⠀⢸⡀⠀⠀⠈⠉⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⢻⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⣿⡄⠀⣾⠉⠲⣤⣠⡤⠖⠉⠉⣩⣿⣀⡤⠶⢦⡀⠀⣸⠀⠀⠀⠀⠇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢶⡚⠉⠉⠉⠉⠹⣄⢸⣆⠀⠈⡷⣄⠀⠀⡼⢳⡄⠁⢠⠷⠶⠿⠶⠿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠁⠀⠙⢦⠀⠀⠀⠀⠈⠾⡇⠻⢷⣶⣞⢧⣸⠁⠀⢧⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠈⣆⠀⠀⠀⠀⠀⢹⢷⣶⠀⠀⢨⢿⠀⠀⢸⠀⠈⣇⣀⣀⣀⡤⠤⠤⠴⠶⠋
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡗⠲⠦⣄⡀⠀⠀⠀⣸⢀⣀⣀⠀⢤⣸⣾⣿⠀⠀⠋⠘⢇⠀⠈⡇⠀⠘⣦⡼⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⡾⠉⠳⣄⠀⣷⡿⠉⠀⠀⡸⠀⠉⠉⠀⠀⠀⠀⠈⣆⠀⠹⡍⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⢈⣷⡟⠀⠀⠀⢠⢇⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⢀⣾⡏⠀⠀⠀⠀⡞⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⣲⠏⡞⠀⠀⠀⠀⡼⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⡿⣧⡀⠘⢇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠙⢦⡉⢿⣓⡦⠤⢄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡶⣿⠟⢹⠟⠓⢦⣀⠀⠀⣰⠋⡼⠁⠀⠀⠀⡼⠁⠀⠀⠀⠀⠙⢄⠀⠀⠀⠀⠀⠀⣷⢿⣳⡄⠘⣆⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠘⣎⢿⣿⣿⣶⣤⣍⣉⡛⠒⠦⠤⠤⣀⣠⣞⡿⣰⢣⡴⠃⣀⣴⠛⠉⣹⣴⣣⠾⢅⡀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠈⠳⢄⠀⠀⠀⠀⣟⠳⢿⢿⣄⠸⡆⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠹⡜⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣤⣼⠛⠉⣩⡝⣛⡋⠈⠙⣿⣿⣿⠗⠦⣀⣹⠂⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⣿⣷⠃⠳⠙⣦⣹⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠙⢌⡻⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⢿⣿⡾⣷⡄⠀⠀⠀⢻⡀⠀⣨⠃⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡉⢀⣀⠀⠉⢳⣳⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠙⠦⣕⡦⢌⣉⠁⠙⠛⠙⢽⠀⠀⠐⠢⠌⠉⠉⠉⠀⠀⠀⠀⢀⣣⢠⠇⠀⣸⢤⣴⠒⠛⠋⠉⠉⠉⠉⠙⠛⢻⠒⠤⢄⣀⢰⡗⣲⡤⠬⢥⣀⣻⣧⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠺⠽⠷⣶⠶⠛⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠋⠀⢰⢧⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢻⣁⣠⠤⠈⢽⣿⣿⣡⣼⡇⠀⠉⢿⡆⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠈⠓⠀⣠⠾⣄⡀⡞⣸⠁⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠛⣁⣀⣀⣀⣘⣿⣿⣿⣿⡇⠀⠀⠩⡿⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⣀⡠⣀⠔⢛⡆⠀⠀⠀⠀⠀⠀⠀⣀⡠⠾⣟⠢⣀⢹⡟⣿⡴⠚⠁⠀⠀⠀⠀⡰⣿⣟⣴⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⠃⠀⠀⠀⠀⠀⠀
    ⣀⣀⠠⠤⠤⠤⠤⠤⣀⣀⣘⣃⣈⣩⣝⣋⣁⡤⠚⠀⠀⠀⠀⠀⢀⡴⠚⢻⡀⠀⠸⡀⠈⢻⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⡟⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⠋⠀⠀⠀⠀⠀⠀⠀
    ⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠸⣟⣄⠀⡇⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⢸⡇⢟⣿⣿⠟⠋⠁⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠈⠈⠻⠇⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⢸⠃⠘⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀
    """)
    print(f"Pleased to make your acquaintance, {character['Name']} \nListen carefully to these instructions: \nTo "
          f"battle the final boss (🐲️), you must be at least Level 3 and have battled (🐍🐱🐆) in that order. \nOn top "
          f"of the battles shown on the board, there are hidden random battles and trivia that will give you rewards "
          f"so try finding them. \nIf your HP reaches 0, you will die. \nYou gain EXP after each battle and level up "
          f"every 1000 EXP. \nWhen you level up, your Max HP will increase and your Current HP will be fully restored."
          f"\nTo move, you will have to first enter the number of the direction and then the number of "
          f"steps you wish to take. \nOn the board, 💥 shows your current location and 🟨 shows your past locations. "
          f"\nPlease note that if you've already been to the 🐍🐱🐆 spaces, those spaces will change to 🟨 after "
          f"you leave the space. \nFleeing a battle will deduct 100 EXP. If you want to re-attempt a fled battle, you "
          f"must leave that space and go back to it in order for the battle to happen. \nType quit at any time to stop "
          f"the game.")


def succeed_game(character):
    """
    Print message upon successful completion of the game and stats.

    :param character: a dictionary where keys are strings of letters
    :precondition: character must be a dictionary where each key is a string of letters
    :postcondition: the function correctly prints the intro, without changing character
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
    Print message upon failure of the game before asking user if they want to restart.

    A function that call the game function again if the player wants to keep playing
    or quit the script if they don't want to continue.
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
    pass


if __name__ == "__main__":
    main()
