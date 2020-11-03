import unittest
from io import StringIO
from unittest.mock import patch
import robot

class TestRobot(unittest.TestCase):

    @patch("sys.stdin", StringIO("Hal\nHAL\nhAL"))
    def test_get_name(self):
        self.assertEqual(robot.get_name(), "Hal")
        self.assertEqual(robot.get_name(), "HAL")
        self.assertEqual(robot.get_name(), "hAL")
    

    @patch("sys.stdin", StringIO("off\nOFF\nOff \n off "))
    def test_get_command(self):
        self.assertEqual(robot.get_command('k'), "off")
        self.assertEqual(robot.get_command('k'), "off")
        self.assertEqual(robot.get_command('k'), "off")
        self.assertEqual(robot.get_command('k'), "off")


    def test_do_off(self):
        self.assertEqual(robot.do_off('off','k', 'a', 'off', (0,0)), "k: Shutting down..")
        self.assertEqual(robot.do_off('off','l', 'a', 'off', (0,0)), "l: Shutting down..")
        self.assertEqual(robot.do_off('off','a','a', 'off', (0,0)), "a: Shutting down..")
        self.assertEqual(robot.do_off('off','S','a', 'off', (0,0)), "S: Shutting down..")
        self.assertEqual(robot.do_off('off','Dan','a', 'off', (0,0)), "Dan: Shutting down..")


    def test_do_help(self):
        command = {
        "off": ['Shut down robot'],
        "help": ['provide information about commands'], 
        }
        test = ''
        x = ' ' * 4
        for i in command:
            test += i.upper()+ x[len(i):] + ' - ' + command[i][0] + '\n'
        self.assertEqual(robot.do_help(command, 'k', 1, 'help', (0,0)), test)

    def test_do_forward(self):
        self.assertEqual(robot.do_forward('forward', 'k', '10', (0,0), 1 ), (0, 0))
        self.assertEqual(robot.do_forward('forward', 'k', '10', (0,0),  1 ), (0, 0))
        self.assertEqual(robot.do_forward('forward', 'k', '20', (0,0),  1 ), (0, 0))
        self.assertEqual(robot.do_forward('forward', 'k', '20', (0,0), 1 ), (0, 0))

    def test_do_back(self):
        self.assertEqual(robot.do_back('back', 'k', '10', (0,0),  1), (0, 0))
        self.assertEqual(robot.do_back('back', 'k', '10', (0,0), 1), (0, 0))
        self.assertEqual(robot.do_back('back', 'k', '20', (0,0), 1), (0, 0))
        self.assertEqual(robot.do_back('back', 'k', '20', (0,0), 1), (0, 0))

    def test_do_location(self):
        self.assertEqual(robot.do_location('forward', 'k', '10', (0,0),  1 ), (0, 0))
        self.assertEqual(robot.do_location('forward', 'k', '10', (0,-10), 1 ), (0, -10))
        self.assertEqual(robot.do_location('forward', 'k', '20', (0,0),  1 ), (0, 0))
        self.assertEqual(robot.do_location('forward', 'k', '20', (0,-10),  1 ), (0, -10))
        self.assertEqual(robot.do_location('back', 'k', '10', (0,0),  1 ), (0, 0))
        self.assertEqual(robot.do_location('back', 'k', '10', (0,-10),  1 ), (0, -10))
        self.assertEqual(robot.do_location('back', 'k', '20', (0,0),  1 ), (0, 0))
        self.assertEqual(robot.do_location('back', 'k', '20', (0,-10),  1 ), (0, -10))

    def test_do_right(self):
        self.assertEqual(robot.do_right('right', 'k', 'b', 'right', (0,0)), '-a')
        self.assertEqual(robot.do_right('right', 'k', '-b', 'right', (0,0)), 'a')
        self.assertEqual(robot.do_right('right', 'k', 'a', 'right', (0,0)), 'b')
        self.assertEqual(robot.do_right('right', 'k', '-a', 'right', (0,0)), '-b')

    def test_do_left(self):
        self.assertEqual(robot.do_left('left', 'k', 'b', 'left', (0,0)), 'a')
        self.assertEqual(robot.do_left('left', 'k', '-b', 'left', (0,0)), '-a')
        self.assertEqual(robot.do_left('left', 'k', 'a', 'left', (0,0)), '-b')
        self.assertEqual(robot.do_left('left', 'k', '-a', 'left', (0,0)), 'b')

    def test_check_range(self):
        self.assertTrue(robot.check_range((0,101), 1, 'b', 1))
        self.assertTrue(robot.check_range((0,101), 1, '-b', 1))
        self.assertTrue(robot.check_range((0,101), 1, 'a', 1))
        self.assertTrue(robot.check_range((0,101), 1, '-a', 1))
