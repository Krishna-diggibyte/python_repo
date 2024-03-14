import unittest
from src.mean_var_and_std.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = mean_var()
        expected_output = '''[1.5 3.5]
[1. 1.]
1.11803398875'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2 2
1 2
3 4
        '''

    def test2(self):
        actual_input = mean_var()
        expected_output = '''[4.5 3.5]
[4. 1.]
1.87082869339'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2 2
7 2
3 4
        '''

    def test3(self):
        actual_input = mean_var()
        expected_output = '''[2.66666667 4.33333333]
[0.25 2.25 0.25]
1.8929694486'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2 3
1 2 5
2 5 6
        '''

if __name__ == '__main__':
    unittest.main()
