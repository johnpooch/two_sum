import unittest

from two_sum import two_sum


class TesTwoSum(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_this_thing_on(self):
        self.assertTrue(True)

    def test_returns_array_1(self):
        self.assertEqual(two_sum([1, 1], 2), (0, 1))

    def test_returns_array_2(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))
