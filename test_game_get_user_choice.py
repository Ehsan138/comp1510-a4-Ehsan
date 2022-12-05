"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class TestGameGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_1(self, mock_input):
        actual = get_user_choice()
        expected = '1'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_get_user_choice_2(self, mock_input):
        actual = get_user_choice()
        expected = '4'
        self.assertEqual(expected, actual)
