from staircase.stair_hash import hash_pyramid
import unittest

class PyramidHash(unittest.TestCase):

    def test_give_2_with_hash_should_be_hh(self):
        #arrange
        n = 2
        expected_output = "#\n"+"##"

        #act
        result = hash_pyramid(n)

        #assert
        self.assertEqual(result, expected_output)