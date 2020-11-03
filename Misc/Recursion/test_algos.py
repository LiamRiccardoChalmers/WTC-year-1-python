import unittest
from super_algos import find_min
from super_algos import sum_all
from super_algos import find_possible_strings

class TestSuper_Algos(unittest.TestCase):

    def test_find_min(self):
        self.assertEqual(find_min([-5,-8,-10,20,30]), -10)
        self.assertEqual(find_min([1,2,3,4,5]), 1)
        self.assertEqual(find_min([-5,-8,-10,-20,-30]), -30)
        self.assertEqual(find_min([1.5, 1.4, 1.6, 1.7, 1.3]), -1)
    def test_sum_all(self):
        self.assertEqual(sum_all([-5,-8,-10,20,30]), 27)
        self.assertEqual(sum_all([1,2,3,4,5]), 15)
        self.assertEqual(sum_all([-5,-8,-10,-20,-30]), -73)
        self.assertEqual(sum_all([1.5, 1.4, 1.6, 1.7, 1.3]), -1)
    def test_find_strings(self):
        result = find_possible_strings(['x', 'y', 'z'], 1)
        self.assertEqual(['x','y','z'], result)
        result = find_possible_strings(['c','d'], 3)
        self.assertEqual(['ccc', 'ccd', 'cdc', 'cdd', 'dcc', 'dcd', 'ddc', 'ddd'], result)
        result = find_possible_strings([], 3)
        self.assertEqual([], result)
        result = find_possible_strings([1,2,3,4], 3)
        self.assertEqual([], result)
    