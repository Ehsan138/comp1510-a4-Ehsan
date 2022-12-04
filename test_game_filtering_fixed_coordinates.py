"""
Ehsan Emadi A01291627
Michelle Kwok A01323329
"""


from unittest import TestCase
from game import filtering_fixed_coordinates


class TestGameFilteringFixedCoordinates(TestCase):
    def test_filtering_fixed_coordinates_false(self):
        actual = filtering_fixed_coordinates((3, 3))
        expected = False
        self.assertEqual(expected, actual)

    def test_filtering_fixed_coordinates_true(self):
        actual = filtering_fixed_coordinates((1, 10))
        expected = True
        self.assertEqual(expected, actual)
