"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


from unittest import TestCase
from game import board_visual, make_board, make_character


class TestGameBoardVisual(TestCase):
    def test_board_visual_3x3(self):
        board = make_board(3, 3)
        character = {"Name": 'Chris', "x_coordinate": 1,
                        "y_coordinate": 1, "Current_HP": 100,
                        "Max_HP": 100, "Experience_Points": 0,
                        "Level": 1, "trivia_one": 0, "trivia_two": 0,
                        "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                        "battle_one": 0, "battle_two": 0, "battle_three": 0,
                        "battle_four": 0, "battle_five": 0, "battle_six": 0,
                        "battle_final": 0}
        actual = board_visual(board, 3, 3, character)
        expected = """1\t⬜⬜⬜\n2\t⬜⬜⬜\n3\t⬜⬜⬜\n"""
        self.assertEqual(expected, actual)

    def test_board_visual_5x5(self):
        board = make_board(5, 5)
        character = {"Name": 'Chris', "x_coordinate": 1,
                        "y_coordinate": 1, "Current_HP": 100,
                        "Max_HP": 100, "Experience_Points": 0,
                        "Level": 1, "trivia_one": 0, "trivia_two": 0,
                        "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                        "battle_one": 0, "battle_two": 0, "battle_three": 0,
                        "battle_four": 0, "battle_five": 0, "battle_six": 0,
                        "battle_final": 0}
        actual = board_visual(board, 5, 5, character)
        expected = """1\t⬜⬜⬜⬜⬜\n2\t⬜⬜⬜⬜⬜\n3\t⬜⬜⬜⬜⬜\n4\t⬜⬜⬜⬜⬜\n5\t⬜⬜⬜⬜⬜\n"""
        self.assertEqual(expected, actual)
