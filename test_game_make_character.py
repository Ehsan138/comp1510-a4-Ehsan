"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


from unittest import TestCase
from unittest.mock import patch
import game


class TestGameMakeCharacter(TestCase):

    @patch('builtins.input', side_effect=['Chris'])
    def test_make_character_Chris(self, mock_input):
        actual = game.make_character()
        expected = {"Name": 'Chris', "x_coordinate": 1, "y_coordinate": 1, "Current_HP": 100,
                                          "Max_HP": 100, "Experience_Points": 0, "Level": 1, "trivia_one": 0,
                                          "trivia_two": 0, "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                                          "battle_one": 0, "battle_two": 0, "battle_three": 0, "battle_four": 0,
                                          "battle_five": 0, "battle_six": 0, "battle_final": 0}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Hoda'])
    def test_make_character_Hoda(self, mock_input):
        actual = game.make_character()
        expected = {"Name": 'Hoda', "x_coordinate": 1, "y_coordinate": 1, "Current_HP": 100,
                    "Max_HP": 100, "Experience_Points": 0, "Level": 1, "trivia_one": 0,
                    "trivia_two": 0, "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                    "battle_one": 0, "battle_two": 0, "battle_three": 0, "battle_four": 0,
                    "battle_five": 0, "battle_six": 0, "battle_final": 0}
        self.assertEqual(expected, actual)
