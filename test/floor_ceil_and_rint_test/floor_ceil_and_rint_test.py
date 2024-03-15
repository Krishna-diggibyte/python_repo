import unittest
from src.floor_ceil_and_rint.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = floor_ceil()
        expected_output ='''(array([ 1.,  2.,  3.,  4.,  5.]),
 array([ 2.,  3.,  4.,  5.,  6.]),
 array([ 1.,  2.,  3.,  4.,  6.]))'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input
        1.1 2.2 3.3 4.4 5.5
        '''

    def test2(self):
        actual_input = floor_ceil()
        expected_output = '''(array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.]),
 array([  2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.,  10.]),
 array([  1.,   2.,   3.,   4.,   6.,   7.,   8.,   9.,  10.]))'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input
        1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
        '''

    def test3(self):
        actual_input = floor_ceil()
        expected_output = '''(array([ 1.,  8.,  2.,  9.,  3.]),
 array([  2.,   9.,   3.,  10.,   4.]),
 array([  1.,   9.,   2.,  10.,   3.]))'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input
        1.1 8.8 2.2 9.9 3.3
        '''

if __name__ == '__main__':
    unittest.main()
