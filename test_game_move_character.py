"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


from unittest import TestCase
from game import move_character


class TestGameMoveCharacter(TestCase):
    def test_move_character_south(self):
        character = {"Name": 'Chris', "x_coordinate": 1,
                     "y_coordinate": 1, "Current_HP": 100,
                     "Max_HP": 100, "Experience_Points": 0,
                     "Level": 1, "trivia_one": 0, "trivia_two": 0,
                     "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                     "battle_one": 0, "battle_two": 0, "battle_three": 0,
                     "battle_four": 0, "battle_five": 0, "battle_six": 0,
                     "battle_final": 0}
        move_character(character, '2', '3')
        actual = character['y_coordinate']
        expected = 4
        self.assertEqual(expected, actual)

    def test_move_character_north(self):
        character = {"Name": 'Chris', "x_coordinate": 1,
                     "y_coordinate": 7, "Current_HP": 100,
                     "Max_HP": 100, "Experience_Points": 0,
                     "Level": 1, "trivia_one": 0, "trivia_two": 0,
                     "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                     "battle_one": 0, "battle_two": 0, "battle_three": 0,
                     "battle_four": 0, "battle_five": 0, "battle_six": 0,
                     "battle_final": 0}
        move_character(character, '1', '5')
        actual = character['y_coordinate']
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_east(self):
        character = {"Name": 'Chris', "x_coordinate": 1,
                     "y_coordinate": 7, "Current_HP": 100,
                     "Max_HP": 100, "Experience_Points": 0,
                     "Level": 1, "trivia_one": 0, "trivia_two": 0,
                     "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                     "battle_one": 0, "battle_two": 0, "battle_three": 0,
                     "battle_four": 0, "battle_five": 0, "battle_six": 0,
                     "battle_final": 0}
        move_character(character, '4', '9')
        actual = character['x_coordinate']
        expected = 10
        self.assertEqual(expected, actual)

    def test_move_character_west(self):
        character = {"Name": 'Chris', "x_coordinate": 4,
                     "y_coordinate": 7, "Current_HP": 100,
                     "Max_HP": 100, "Experience_Points": 0,
                     "Level": 1, "trivia_one": 0, "trivia_two": 0,
                     "trivia_three": 0, "trivia_four": 0, "trivia_five": 0,
                     "battle_one": 0, "battle_two": 0, "battle_three": 0,
                     "battle_four": 0, "battle_five": 0, "battle_six": 0,
                     "battle_final": 0}
        move_character(character, '3', '2')
        actual = character['x_coordinate']
        expected = 2
        self.assertEqual(expected, actual)
