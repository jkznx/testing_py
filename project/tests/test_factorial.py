import unittest
from Factorial.factorial import factorial

class FactorialTest(unittest.TestCase):
    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_negative(self):
        self.assertIsNone(factorial(-1))

    def test_factorial_of_6(self):
        self.assertEqual(factorial(6), 720)

    

if __name__ == '__main__':
    unittest.main()