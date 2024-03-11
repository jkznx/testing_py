import unittest
from Factorial.factorial import factorials

class FactorialTest(unittest.TestCase):
    def test_factorial_of_0(self):
        self.assertEqual(factorials(0), 1)

    def test_factorial_of_1(self):
        self.assertEqual(factorials(1), 1)

    def test_factorial_of_negative(self):
        self.assertIsNone(factorials(-1))

    def test_factorial_of_6(self):
        self.assertEqual(factorials(6), 720)

    

if __name__ == '__main__':
    unittest.main()