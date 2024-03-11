from Guess.guess_int_float import guess_int, guess_float
import unittest

class TestGuessFunctions(unittest.TestCase):
    def test_guess_int(self):
        int_result = guess_int(1, 10)
        self.assertIsInstance(int_result, int)
        self.assertTrue(1 <= int_result <= 10)

    def test_guess_float(self):
        float_result = guess_float(1.0, 10.0)
        self.assertIsInstance(float_result, float)
        self.assertTrue(1.0 <= float_result <= 10.0)

if __name__ == '__main__':
    unittest.main()
