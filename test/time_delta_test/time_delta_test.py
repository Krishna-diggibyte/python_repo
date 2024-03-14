import unittest
from src.time_delta.util import *

class MyTestCase(unittest.TestCase):

    def test1(self):
        actual_input = time_diff()
        expected_output = '''61200
'''
        self.assertEqual(actual_input, expected_output)
        '''
1
Sun 10 May 2015 13:54:36 -0700
Sun 11 May 2015 13:54:36 -0000
        '''

    def test2(self):
        actual_input = time_diff()
        expected_output = '''172800
'''
        self.assertEqual(actual_input, expected_output)
        '''
1
Sun 03 May 2015 13:54:36 -0000
Fri 01 May 2015 13:54:36 -0000
        '''

    def test3(self):
        actual_input = time_diff()
        expected_output = '''25200
88200
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
'''

if __name__ == '__main__':
    unittest.main()
