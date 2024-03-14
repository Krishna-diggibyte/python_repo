import unittest
from src.piling_up.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = pilling_up()
        expected_output = '''Yes
No
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2
6
4 3 2 1 3 4
3
1 3 2
        '''

    def test2(self):
        actual_input = pilling_up()
        expected_output ='''Yes
No
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2
6
4 3 2 1 3 4
3
1 3 2
        '''

    def test3(self):
        actual_input = pilling_up()
        expected_output = '''No
Yes
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2
3
1 3 2
6
4 3 2 1 3 4
        '''

if __name__ == '__main__':
    unittest.main()
