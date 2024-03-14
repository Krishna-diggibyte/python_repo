import unittest
from src.validating_email_addresses_with_a_filter.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = validating_email()
        expected_output = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
        '''

    def test2(self):
        actual_input = validating_email()
        expected_output = ['Amit@diggibyte.com', 'Basheer@diggibyte.com', 'Krishna@diggibyte.com']
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
3
Krishna@diggibyte.com
Basheer@diggibyte.com
Amit@diggibyte.com
        '''

    def test3(self):
        actual_input = validating_email()
        expected_output = ['kalai@diggibyte.com', 'prathibha@diggibyte.com']
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2
kalai@diggibyte.com
prathibha@diggibyte.com
        '''

if __name__ == '__main__':
    unittest.main()
