import unittest
import world.text.world as text
#import world.turtle.world as turtle

class TestText(unittest.TestCase):


    def test_step1_boot_up(self):
        text.position_x = 100
        text.position_y = 100
        text.boot_up(1)
        x = text.position_x
        y = text.position_y
        self.assertEqual(x,0)
        self.assertEqual(y,0)


    def test_step2_is_position_allowed(self):
        is_it = text.is_position_allowed(201,100)
        self.assertEqual(False, is_it)
        is_it = text.is_position_allowed(90,100)
        self.assertEqual(True, is_it)
        is_it = text.is_position_allowed(50,400)
        self.assertEqual(False, is_it)
        is_it = text.is_position_allowed(50,100)
        self.assertEqual(True, is_it)


    def test_step3_check_blocked(self):
        text.a = True
        text.b = False
        is_it = text.check_blocked(1,1)
        self.assertEqual(True, is_it)

    def test_step4_update_position(self):
        x = text.update_position(201,'forward')
        self.assertEqual(x[0], False)
        x = text.update_position(20,'forward')
        self.assertEqual(x[0], False)
