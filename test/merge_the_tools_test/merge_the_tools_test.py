import unittest

from src.merge_the_tools.util import merge_the_tools

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input=merge_the_tools()
        expected_output="""AB
CA
AD
"""
        self.assertEqual(actual_input,expected_output)
        '''
AABCAAADA
3
        '''


    def test2(self):
        actual_input = merge_the_tools()
        expected_output = '''AC
BCA
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
ACABCA
3
        '''

    def test3(self):
        actual_input = merge_the_tools()
        expected_output = '''A
DA
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
AADA
2
        '''

if __name__ == '__main__':
    unittest.main()
