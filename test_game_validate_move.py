"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


from unittest import TestCase
from game import validate_move


class TestGameValidateMove(TestCase):
    def test_validate_move_possible(self):
        character = {"Name": 'Chris', "x_coordinate": 1,
                     "y_coordinate": 1, "Current_HP": 100,
                     "Max_HP": 100, "Experience_Points": 0,
                     "Level": 1, "trivia_one": 0, "trivia_two": 0,
                     "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                     "battle_one": 0, "battle_two": 0, "battle_three": 0,
                     "battle_four": 0, "battle_five": 0, "battle_six": 0,
                     "battle_final": 0}
        actual = validate_move(character, '2', '3', 10, 10)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_impossible_direction(self):
        character = {"Name": 'Chris', "x_coordinate": 1,
                     "y_coordinate": 1, "Current_HP": 100,
                     "Max_HP": 100, "Experience_Points": 0,
                     "Level": 1, "trivia_one": 0, "trivia_two": 0,
                     "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                     "battle_one": 0, "battle_two": 0, "battle_three": 0,
                     "battle_four": 0, "battle_five": 0, "battle_six": 0,
                     "battle_final": 0}
        actual = validate_move(character, '1', '7', 10, 10)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_impossible_steps(self):
        character = {"Name": 'Chris', "x_coordinate": 1,
                     "y_coordinate": 1, "Current_HP": 100,
                     "Max_HP": 100, "Experience_Points": 0,
                     "Level": 1, "trivia_one": 0, "trivia_two": 0,
                     "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                     "battle_one": 0, "battle_two": 0, "battle_three": 0,
                     "battle_four": 0, "battle_five": 0, "battle_six": 0,
                     "battle_final": 0}
        actual = validate_move(character, '2', '10', 10, 10)
        expected = False
        self.assertEqual(expected, actual)
