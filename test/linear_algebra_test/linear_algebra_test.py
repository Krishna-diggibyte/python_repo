import unittest
from src.linear_algebra.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = linear_alg()
        expected_output = 0.0
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2
1.1 1.1
1.1 1.1
        '''

    def test2(self):
        actual_input = linear_alg()
        expected_output = 0.11
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2
1.1 1.1
1.1 1.2
        '''

    def test3(self):
        actual_input = linear_alg()
        expected_output = 0.01
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2
1.2 1.3
1.1 1.2

        '''

if __name__ == '__main__':
    unittest.main()
