import unittest

import unittesting

def check(x):
    if x % 2 ==0:
        return "even"
    else:
        return 'odd'

def add(x, y):

    return x+y
class EvenorOddApp(unittest.TestCase):
    def test_case_even_check(self):
        x=10
        result = check(x)
        self.assertEqual("even", result)

    def test_case_odd_check(self):
        x=11
        result = check(x)
        self.assertEqual("odd", result)


