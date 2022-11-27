"""


Youngster Allen looks like he wants to battle with you. Accept?
Youngster Allen:
"If you have Pokemon with you, then you're an official Pokemon trainer! You can't say no to my challenge!"
Youngster Allen would like to battle!
Youngster Allen sent out Wurmple (Lvl 1)!
Go Pikachu!
Pikachu used Thunder Shock!
Wurmple's hp went down 30hp!
Foe Wurmple used String Shot!
Pikachu's SPEED was harshly lowered!
Pikachu used Thunder Shock!
Wurmple fainted!
Pikachu gained 15 EXP Points!
Youngster Allen sends out Taillow (Lvl 1)!
Pikachu used Thunder Shock!
opponent's hp
Foe Taillow used Peck!
Pikachu's hp went down 35hp!
Pikachu used Thunder Shock!
Foe Taillow fainted!
Pikachu gained 18 EXP Points!
Pikachu grew to Level 2!
Pikachu learned the new move Spark!
Player defeated Youngster Allen.
"I called you because I thought I could beat you..."
__player__ got $5.
"I can tell you're new to battling. Let me give you advice. When Pokemon battle, they eventually level up and become
stronger. If the Pokemon with you become stronger, you'll be able to go farther away from here."


Team Rocket Jessie:
'To protect the world from devastation! To unite all people within our nation! To denounce the evils of truth and love!'
Team Rocket Jessie sends out Ekans!
Go Pikachu!
Pikachu used Spark!
Ekans' hp went down 40hp!
Foe Ekans used Bite!
Pikachu's hp went down 30hp!
Pikachu used Spark!
Ekans' hp went down 50hp!
Pikachu grew to Level 3!
Pikachu learned the new move Thunderbolt!
Player defeated Team Rocket Jessie.
'Just you wait! Our Team Rocket Leader Giovanni has something BIG in store for you...All I can say is such a powerful
Pokemon will help us achieve great things!'


There is a menacing pokemon towering over you, blocking the only path you can take. Upon closer inspection, it is
legendary pokemon Mewtwo! Mewtwo makes eye contact with you. It seems you must battle Mewtwo to pass.
Pikachu seems a little bit worried about being able to battle.
Go Pikachu!
Pikachu used Thunderbolt!

"""


def game_intro():
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
    character_name = input("Please enter your name.")
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
    print("Pleased to make your acquaintance,", character_name)


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
