import unittest


def add(x, y):

    return x+y

def checkDivisibility7(x):
    if x%7 == 0:
        return True
    else:
        false

class MyApp(unittest.TestCase):

    def test_case1(self):
        a = 10
        b = 22
        result = add(a,b)
        self.assertEqual(a+b, result)

    def test_case2(self):
        a = 12.5
        b = 12.9
        result = add(a, b)
        self.assertEqual(a+b, result)

    if __name__==" main ":
        unittest.main()

