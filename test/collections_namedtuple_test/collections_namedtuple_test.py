import unittest
from src.collections_namedtuple.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = avg_marks()
        expected_output = 78.0
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6
        '''

    def test2(self):
        actual_input = avg_marks()
        expected_output = 90.8
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
5
MARKS      CLASS      NAME       ID
94         2          Krishna    1
88         5          Basheer    2
93         2          Amit       3
87         8          Kuldeep    4
92         2          Prathibha  5
        '''

    def test3(self):
        actual_input = avg_marks()
        expected_output = 81.0
        self.assertEqual(actual_input, expected_output)
        '''
5
MARKS      CLASS      NAME       ID
92         2          Calum      1
82         5          Scott      2
94         2          Jason      3
55         8          Glenn      4
82         2          Fergus     5
        '''

if __name__ == '__main__':
    unittest.main()
