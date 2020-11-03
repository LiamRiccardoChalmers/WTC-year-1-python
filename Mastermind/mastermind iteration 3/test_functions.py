from mastermind import create_code
from mastermind import check_correctness
from mastermind import take_turn
from mastermind import get_answer_input
from mastermind import check_in_range
from unittest.mock import patch
from io import StringIO
import unittest

class TestMastermind(unittest.TestCase):

    def test_create_code(self):

        for i in range(100):
            code = create_code()
            for x in code:
                self.assertEqual(code.count(x), 1)
                if 0 in code or 9 in code:
                    print("Error 0 and 9 in code")
    
    def test_check_correctness(self):
        correct = check_correctness(12, 3, 1, False)
        if correct == True:
            print("Error: True returned instead of of False")
        correct = check_correctness(12, 4, 0, True)
        if correct == False:
            print("Error: False returned instead of of True")
    
    @patch("sys.stdin", StringIO("5487643\n369\nliam3456\naaaa\n0000\n9999\n1234\n"))
    def test_get_input(self):
        self.assertEqual(get_answer_input(), "1234")
    

    @patch("sys.stdin", StringIO("1111\n1256\n1161\n5642\n5624\n5426"))
    def test_take_turn(self):
        self.assertEqual(take_turn([5, 4, 2, 6]), tuple([0,0]))
        self.assertEqual(take_turn([5, 4, 2, 6]), tuple([1,2]))
        self.assertEqual(take_turn([5, 4, 2, 6]), tuple([0,1]))
        self.assertEqual(take_turn([5, 4, 2, 6]), tuple([1,3]))
        self.assertEqual(take_turn([5, 4, 2, 6]), tuple([2,2]))
        self.assertEqual(take_turn([5, 4, 2, 6]), tuple([4,0]))

    def test_check_in_range(self):
        inrange = check_in_range(['1', '2', '3', '4', '5', '6', '7', '8'], [1,2,3,4])
        if inrange == False:
                print ("error: false instead of true")
        inrange = check_in_range(['5', '6', '7', '8'], [1,2,3,4])
        if inrange == True:
                print ("error: true instead of false")