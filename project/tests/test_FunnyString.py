import unittest
from FunnyString.funny_String import funnyString

class TestFunny(unittest.TestCase):
    def test_funny_string(self):
        self.assertEqual(funnyString("abcd"), 'Funny')
        self.assertEqual(funnyString("acxz"), 'Funny')

    def test_single_character_string(self):
        self.assertEqual(funnyString("a"), 'Funny')
        self.assertEqual(funnyString("b"), 'Funny')

    def test_empty_string(self):
        self.assertEqual(funnyString(""), 'Funny')

    def test_long_string(self):
        self.assertEqual(funnyString("ljvnsljgljsllkdjkdshgsdlldgvnwerotuouoojlswljljgisjlolbhhosdhinbvywjejsid"), 'Not Funny')

    def test_verylong_string(self):
        self.assertEqual(funnyString("skibidigreaihfhihhdlnbritainenlianffantansieoofhouhhnkddsupersjjfusnldjfinlosnjustjutsukaisensfjsjuvhkhudjnhksheroacademiafjdojolnansfbonepuchmanfjsjhfanimeeplodesjlsjfhloajvkhdjfflacalllmeabyyuasnamelkjfkdivjlv;dofjdjllrigjdlfgjl"), 'Funny')

