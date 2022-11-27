"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character("Player name")
    achieved_goal = False
    while not achieved_goal:
        # Tell the user where they are describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges()
            if there_is_a_challenge:
                execute_challenge_protocol(character)
                if character_has_leveled():
                    execute_glow_up_protocol()
            achieved_goal = check_if_goal_attained(board, character)
        else:
            # Tell the user they can't go in that direction
    # Print end of game (congratulations or sorry you died)


    # create dictionary w tuples as key
    # list as value, first thing string that describes location, second thing some event/character/question
    # enumerated list to give users a selection of answers so they can type as little as possible
    # picked from enumerated list if they want to go N, S, E, W: return true if they can move is valid, false if illegal

def make_character(name):
    """
    Creates and returns a dictionary that contains key:value pairs.

    :param name: a string
    :return: dictionary that contains key:value pairs
    """


def make_board():
    board = {}
    # for row in rows:
    #     for column in columns:
    #         board[(row, column)] = ["Welcome to the pit of doom", None]
    board[(0, 0)] = adfkjdfklj


def describe_current_location():


def get_user_choice():


def validate_move():





def main():
    game()


if __name__ == "__main__":
    main()
