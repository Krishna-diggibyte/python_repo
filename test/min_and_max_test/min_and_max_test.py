import unittest
from src.min_and_max.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = min_max()
        expected_output = 3
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
4 2
2 5
3 7
1 3
4 0
        '''

    def test2(self):
        actual_input = min_max()
        expected_output = 3
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
4 3
2 5 4
3 7 6
1 3 3
4 0 1
        '''

    def test3(self):
        actual_input = min_max()
        expected_output = 2
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
3 3
2 5 4
3 7 0
1 3 4
        '''

if __name__ == '__main__':
    unittest.main()
