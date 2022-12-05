"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


from unittest import TestCase
from game import first_time_challenge


class TestGameFirstTimeChallenge(TestCase):
    def test_first_time_challenge_true(self):
        character = {"Name": 'Chris', "x_coordinate": 1,
                     "y_coordinate": 1, "Current_HP": 100,
                     "Max_HP": 100, "Experience_Points": 0,
                     "Level": 1, "trivia_one": 0, "trivia_two": 0,
                     "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                     "battle_one": 0, "battle_two": 0, "battle_three": 0,
                     "battle_four": 1, "battle_five": 1, "battle_six": 1,
                     "battle_final": 0}
        actual = first_time_challenge(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_first_time_challenge_false(self):
        character = {"Name": 'Chris', "x_coordinate": 1,
                     "y_coordinate": 1, "Current_HP": 100,
                     "Max_HP": 100, "Experience_Points": 0,
                     "Level": 1, "trivia_one": 0, "trivia_two": 0,
                     "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                     "battle_one": 0, "battle_two": 0, "battle_three": 0,
                     "battle_four": 1, "battle_five": 1, "battle_six": 1,
                     "battle_final": 1}
        actual = first_time_challenge(character)
        expected = False
        self.assertEqual(expected, actual)
