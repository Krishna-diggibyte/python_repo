import unittest
from src.word_order.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = word_order()
        expected_output ='''3
2 1 1'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
4
bcdef
abcdefg
bcde
bcdef
        '''

    def test2(self):
        actual_input = word_order()
        expected_output = '''2
3 1'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
4
bcdef
bcdef
bcde
bcdef
        '''

    def test3(self):
        actual_input = word_order()
        expected_output = '''4
1 1 1 1'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
4
bcdef
abcdefg
bcde
adcdef
        '''

if __name__ == '__main__':
    unittest.main()
