import unittest
from src.calendar_module.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = find_day()
        expected_output = 'WEDNESDAY'
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
        08 05 2015
        '''

    def test2(self):
        actual_input = find_day()
        expected_output = 'SATURDAY'
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
        10 06 2012
        '''

    def test3(self):
        actual_input = find_day()
        expected_output = 'MONDAY'
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
        12 07 2020
        '''

if __name__ == '__main__':
    unittest.main()
