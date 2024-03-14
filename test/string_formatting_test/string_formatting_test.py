import unittest
from src.string_formatting.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = print_formatted()
        expected_output ='''   1    1    1    1
   2    2    2   10
   3    3    3   11
   4    4    4  100
   5    5    5  101
   6    6    6  110
   7    7    7  111
   8   10    8 1000
   9   11    9 1001
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
9
        '''

    def test2(self):
        actual_input = print_formatted()
        expected_output = '''  1   1   1   1
  2   2   2  10
  3   3   3  11
  4   4   4 100
  5   5   5 101
  6   6   6 110
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
6
        '''

    def test3(self):
        actual_input = print_formatted()
        expected_output = '''   1    1    1    1
   2    2    2   10
   3    3    3   11
   4    4    4  100
   5    5    5  101
   6    6    6  110
   7    7    7  111
   8   10    8 1000
   9   11    9 1001
  10   12    A 1010
  11   13    B 1011
  12   14    C 1100
  13   15    D 1101
  14   16    E 1110
  15   17    F 1111
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
15
        '''

if __name__ == '__main__':
    unittest.main()
