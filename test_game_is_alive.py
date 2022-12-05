"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


from unittest import TestCase
import game


class TestGameIsAlive(TestCase):

    def test_is_alive_Chris(self):
        character_chris = {"Name": 'Chris', "x_coordinate": 1,
                     "y_coordinate": 1, "Current_HP": 100,
                     "Max_HP": 100, "Experience_Points": 0,
                     "Level": 1, "trivia_one": 0, "trivia_two": 0,
                     "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                     "battle_one": 0, "battle_two": 0, "battle_three": 0,
                     "battle_four": 0, "battle_five": 0, "battle_six": 0,
                     "battle_final": 0}
        actual = game.is_alive(character_chris)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_not_alive_Chris(self):
        character_chris = {"Name": 'Chris', "x_coordinate": 1,
                     "y_coordinate": 1, "Current_HP": 0,
                     "Max_HP": 100, "Experience_Points": 0,
                     "Level": 1, "trivia_one": 0, "trivia_two": 0,
                     "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                     "battle_one": 0, "battle_two": 0, "battle_three": 0,
                     "battle_four": 0, "battle_five": 0, "battle_six": 0,
                     "battle_final": 0}
        actual = game.is_alive(character_chris)
        expected = False
        self.assertEqual(expected, actual)
