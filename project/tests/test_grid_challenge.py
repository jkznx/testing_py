import unittest
from Grid.grid_Challenge import gridChallenge

class TestGrid(unittest.TestCase):
    def test_1_grid_challenge(self):
        grid = ['abcde', 'fghij', 'olkmn', 'trpqs', 'xywuv']
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_2_grid_challenge(self): 
        grid = ['nmjf','abcd','nmsf']
        self.assertEqual(gridChallenge(grid), "NO")

    def test_3_LongText_grid_challenge(self):
        grid = [
            'jkcgahsotypovnxzvnhfeywertr'
            'asjiywevbmnmoptujgirhgyeujv'
            'yvndgctehskkmkrwqpovmfjdkcu'
            'iovxyvtrbnhchsjvndfsjchyiew'
            'zvioxucslhfldosoeyofhvoyofh'
        ]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_4_RepeatText_grid_challenge(self):
        grid=['ooo','ttt','ooo']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_5_grid_challenge(self):
        grid=['red','med','pig']
        self.assertEqual(gridChallenge(grid), 'NO')
