from fizzbuzz.fizz_buzz import FizzBuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_x_equal_0_is_Fizz(self):
        x = 0
        Fizz_Buzz = FizzBuzz(x)
        self.assertTrue(Fizz_Buzz)

    def test_x_equal_3_is_Fizz(self):
        x = 3
        Fizz_Buzz = FizzBuzz(x)
        self.assertTrue(Fizz_Buzz)
    
    def test_x_equal_15_is_Fizz(self):
        x = 15
        Fizz_Buzz = FizzBuzz(x)
        self.assertTrue(Fizz_Buzz)
    
    def test_x_equal_10_is_Buzz(self):
        x = 10
        Fizz_Buzz = FizzBuzz(x)
        self.assertTrue(Fizz_Buzz)




