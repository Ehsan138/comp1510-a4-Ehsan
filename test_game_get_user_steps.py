"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


from unittest import TestCase
from unittest.mock import patch
from game import get_user_steps


class TestGameGetUserSteps(TestCase):

    @patch('builtins.input', side_effect=['3'])
    def test_get_user_steps_1(self, mock_input):
        actual = get_user_steps()
        expected = '3'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['9'])
    def test_get_user_steps_2(self, mock_input):
        actual = get_user_steps()
        expected = '9'
        self.assertEqual(expected, actual)
