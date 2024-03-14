import unittest
from src.no_idea.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = no_idea()
        expected_output = 1
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
3 2
1 5 3
3 1
5 7
        '''

    def test2(self):
        actual_input = no_idea()
        expected_output = 1
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
3 2
8 5 3
3 8
5 7
        '''

    def test3(self):
        actual_input = no_idea()
        expected_output = 0
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
3 2
1 5 8
3 1
5 7
        '''

if __name__ == '__main__':
    unittest.main()
