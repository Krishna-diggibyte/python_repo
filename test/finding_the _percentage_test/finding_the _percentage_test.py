import unittest
from src.finding_the_percentage.util import *
class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = find_percentage()
        expected_output = 26.50
        self.assertEqual(actual_input, expected_output)  # add assertion here

        '''
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
        '''
    def test2(self):
        actual_input = find_percentage()
        expected_output = 60.00
        self.assertEqual(actual_input, expected_output)  # add assertion here

        '''
3
Riya 52 93 20
Rencho 69 65 62
Hbtg 52 60 68
Hbtg
        '''
    def test3(self):
        actual_input = find_percentage()
        expected_output = 56.00
        self.assertEqual(actual_input, expected_output)  # add assertion here
        '''
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
        '''


if __name__ == '__main__':
    unittest.main()
