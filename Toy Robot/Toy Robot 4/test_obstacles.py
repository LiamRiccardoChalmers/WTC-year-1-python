import unittest
import world.obstacles



class TestObstacles(unittest.TestCase):

    def test_step1_get_obstacles(self):
        world.obstacles.random.randint = lambda a, b: 0
        obstacle = len(world.obstacles.get_obstacles())
        self.assertEqual(obstacle,0)

    def test_step2_obstacles_position_list(self):
        test_list = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
        function_list = world.obstacles.obstacles_position_list((1,1))
        self.assertEqual(test_list, function_list)

    def test_step3_is_position_blocked(self):
        world.obstacles.obstacles_list = ((1,1),(10,10),(-1,10))
        is_it = world.obstacles.is_position_blocked(1,1)
        self.assertEqual(True, is_it)
        is_it = world.obstacles.is_position_blocked(10,100)
        self.assertEqual(False, is_it)

    def  test_step4_is_path_blocked(self):
        world.obstacles.obstacles_list = ((-1,10),(10,10),(-1,10))
        is_it = world.obstacles.is_path_blocked(0,0,0,20)
        self.assertEqual(True, is_it)
        is_it = world.obstacles.is_path_blocked(0,0,10,0)
        self.assertEqual(False, is_it)