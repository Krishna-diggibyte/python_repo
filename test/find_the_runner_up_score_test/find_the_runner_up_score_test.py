import unittest
from src.find_the_runner_up_score.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = find_runner_up()
        expected_output = 5
        self.assertEqual(actual_input, expected_output)
        '''
        5
2 3 6 6 5
        '''

    def test2(self):
        actual_input = find_runner_up()
        expected_output = 6
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
        6
5 6 4 7 5 3
        '''

    def test3(self):
        actual_input = find_runner_up()
        expected_output = 7
        self.assertEqual(actual_input, expected_output)
        '''
        7
4 6 5 7 4 9 6
        '''

if __name__ == '__main__':
    unittest.main()
