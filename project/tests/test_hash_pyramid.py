from staircase.stair_hash import hash_pyramid
import unittest

class PyramidHash(unittest.TestCase):

    def test_give_4_with_hash_should_be_hh(self):
        #arrange
        n = 4
        expected_output =  \
        "#\n" + \
        "##\n" + \
        "###\n" + \
        "####"

        #act
        result = hash_pyramid(n)

        #assert
        self.assertEqual(result, f"\n{expected_output}")