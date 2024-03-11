import unittest
from staircase.stair_hash import hash_pyramids

class TestHashPyramid(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        # arrange
        n = 2
        pattern = '#'
        expected_output = "#\n##"

        # act
        result = hash_pyramids(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_0_with_hash_should_be_hh(self):
        # arrange
        n = 0
        pattern = '#'
        expected_output = ""

        # act
        result = hash_pyramids(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

if __name__ == "__main__":
    unittest.main()
