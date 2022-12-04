"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


from unittest import TestCase
import game


class TestGameIsAlive(TestCase):

    def test_is_alive_Chris(self):
        character_chris = {"Name": 'Chris', "x_coordinate": 1, "y_coordinate": 1, "Current_HP": 100, "Max_HP": 100}
        actual = game.is_alive(character_chris)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_not_alive_Chris(self):
        character_chris = {"Name": 'Chris', "x_coordinate": 1, "y_coordinate": 1, "Current_HP": 0, "Max_HP": 100}
        actual = game.is_alive(character_chris)
        expected = False
        self.assertEqual(expected, actual)
