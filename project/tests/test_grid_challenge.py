from Grid.grid_Challenge import gridChallenges
import unittest

class TestGrid(unittest.TestCase):
    def test_1_grid_challenge(self):
        grid = ['abcde', 'fghij', 'olkmn', 'trpqs', 'xywuv']
        self.assertEqual(gridChallenges(grid), 'YES')

    def test_2_grid_challenge(self): 
        grid = ['nmjf','abcd','nmsf']
        self.assertEqual(gridChallenges(grid), "NO")

    def test_3_LongText_grid_challenge(self):
        grid = [
            'jkcgahsotypovnxzvnhfeywertr'
            'asjiywevbmnmoptujgirhgyeujv'
            'yvndgctehskkmkrwqpovmfjdkcu'
            'iovxyvtrbnhchsjvndfsjchyiew'
            'zvioxucslhfldosoeyofhvoyofh'
        ]
        self.assertEqual(gridChallenges(grid), "YES")

    def test_4_RepeatText_grid_challenge(self):
        grid=['ooo','ttt','ooo']
        self.assertEqual(gridChallenges(grid), "YES")

    def test_5_grid_challenge(self):
        grid=['red','med','pig']
        self.assertEqual(gridChallenges(grid), 'NO')
