"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


def game():
    rows = 10
    columns = 10
    # create dictionary w tuples as key
    # list as value, first thing string that describes location, second thing some event/character/question
    # enumerated list to give users a selection of answers so they can type as little as possible
    board = make_board(rows, columns)
    character = make_character("Player name")
    # picked from enumerated list if they want to go N, S, E, W: return true if they can move is valid, false if illegal


def make_board():
    board = {}
    # for row in rows:
    #     for column in columns:
    #         board[(row, column)] = ["Welcome to the pit of doom", None]
    board[(0, 0)] = adfkjdfklj


def main():
    game()


if __name__ == "__main__":
    main()
