"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


# def game():
#     rows = 10
#     columns = 10
#     board = make_board(rows, columns)
#     character = make_character("Player name")
#     achieved_goal = False
#     while not achieved_goal:
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

def make_character(name):
    """
    Creates and returns a dictionary that contains key:value pairs.

    :param name: a string
    :return: dictionary that contains key:value pairs
    """
    character_dictionary = {"Name": name, "x_coordinate": 1,
                            "y_coordinate": 1, "Current HP": 5, "Max HP": 5}

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

            board[(row, column)] = 'None'

            # print('{:3}'.format(x * y), end=' ')
            # board[(row, column)] = ["Welcome to the pit of doom", None]

    # for key, value in board.items:
    #     if value == 'Empty':

    return board


# board = make_board(10, 10)

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
            text += f"{board[(row, column)]} \t"
            # if (row, column) in board:

    return text


def describe_current_location(board, character):
    """

    :param board:
    :param character:
    :return:
    """
    board[(character["x_coordinate"], character["y_coordinate"])] = 'current location'
    print(board_visual(board, 10, 10))







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





def main():
    character = make_character('Chris')
    print(make_board(10, 10))
    board = make_board(10, 10)
    print(board_visual(board, 10, 10))
    describe_current_location(board, character)
    # print(board_visual(board, 10, 10))

if __name__ == "__main__":
    main()
