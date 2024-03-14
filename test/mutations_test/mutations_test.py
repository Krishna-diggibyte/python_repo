import unittest

from src.mutations.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input=mutate_string()
        expected_output='abrackdabra'
        self.assertEqual(actual_input,expected_output)

        '''
        abracadabra
5 k
        '''
    def test2(self):
        actual_input=mutate_string()
        expected_output='Tannu'
        self.assertEqual(actual_input,expected_output)
        '''
        Kannu
0 T
        '''
    def test3(self):
        actual_input=mutate_string()
        expected_output="asedrft"
        self.assertEqual(actual_input,expected_output)
        '''
        asddrft
2 e
        '''

MyTestCase()