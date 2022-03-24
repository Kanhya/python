import unittest


def checkDivisibilityby7(x):
    if x%7 == 0:
        return True
    else:
        return False

class CheckDivisible(unittest.TestCase):
    def test_case_DIVISIBLE(self):
        X = 14
        result = checkDivisibilityby7()
        self.assertTrue(result)

    def test_case_divisible1(self):
        x=9
        result = checkDivisibilityby7(x)
        self.assertTrue(result)



