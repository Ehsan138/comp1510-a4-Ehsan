"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


from unittest import TestCase
from game import make_board


class TestGameMakeBoard(TestCase):
    def test_make_board_3x3(self):
        actual = make_board(3, 3)
        expected = {(1, 1): ['None', 'None'], (1, 2): ['None', 'None'], (1, 3): ['None', 'None'],
                    (2, 1): ['None', 'None'], (2, 2): ['None', 'None'], (2, 3): ['None', 'None'],
                    (3, 1): ['None', 'None'], (3, 2): ['None', 'None'], (3, 3): ['None', 'None']}
        self.assertEqual(expected, actual)

    def test_make_board_5x5(self):
        actual = make_board(5, 5)
        expected = {(1, 1): ['None', 'None'], (1, 2): ['None', 'None'], (1, 3): ['None', 'None'],
                    (1, 4): ['None', 'None'], (1, 5): ['None', 'None'], (2, 1): ['None', 'None'],
                    (2, 2): ['None', 'None'], (2, 3): ['None', 'None'], (2, 4): ['None', 'None'],
                    (2, 5): ['None', 'None'], (3, 1): ['None', 'None'], (3, 2): ['None', 'None'],
                    (3, 3): ['None', 'None'], (3, 4): ['None', 'None'], (3, 5): ['None', 'None'],
                    (4, 1): ['None', 'None'], (4, 2): ['None', 'None'], (4, 3): ['None', 'None'],
                    (4, 4): ['None', 'None'], (4, 5): ['None', 'None'], (5, 1): ['None', 'None'],
                    (5, 2): ['None', 'None'], (5, 3): ['None', 'None'], (5, 4): ['None', 'None'],
                    (5, 5): ['None', 'None']}
        self.assertEqual(expected, actual)
