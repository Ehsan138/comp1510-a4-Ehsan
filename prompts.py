
def game_intro_1():
    print("""                          
                                       ,'\ 
         _.----.        ____         ,'  _\  ___    ___     ____
     _,-'       `.     |    |  /`.   \,-'   |   \  /   |   |    \  |`.
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


def game_intro_2(character):
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
    print(f"Pleased to make your acquaintance, {character['Name']}"
    "\nListen carefully to these instructions: \nTo battle the final boss (㊙), you must be at least Level 3 and have "
    "battled (🐍🐱🐆) in that order. \nOn top of the battles shown on the board, there are hidden random battles and " \
    "trivia that will give you rewards so try finding them. \nIf your HP reaches 0, you will die. \nYou gain EXP " \
    "after each battle and level up every 1000 EXP. \nTo move, you will have to first enter the number of the " \
    "direction and then the number of steps you wish to take. \nOn the board, ⚡ shows your current location and 🟨 " \
    "shows your past locations. \nPlease note that even if you've already been to the 🐍🐱🐆 spaces, those spaces will" \
    " not change to 🟨. \nFleeing a battle will deduct 50 EXP. If you want to re-attempt a fled battle, you " \
    "must leave that space and go back to it in order for the battle to happen.")


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
    game_fail()


if __name__ == "__main__":
    main()






