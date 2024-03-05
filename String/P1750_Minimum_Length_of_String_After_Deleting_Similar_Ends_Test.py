import unittest
from P1750_Minimum_Length_of_String_After_Deleting_Similar_Ends import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        s = 'ca'
        res = self.s.minimumLength(s)
        self.assertEqual(2, res)

    def test_2(self):
        s = 'cabaabac'
        res = self.s.minimumLength(s)
        self.assertEqual(0, res)

    def test_3(self):
        s = "aabccabba"
        res = self.s.minimumLength(s)
        self.assertEqual(3, res)

    def test_all_the_same_letters(self):
        s = 'aaaaa'
        res = self.s.minimumLength(s)
        self.assertEqual(0, res)

    def test_5_chars_4_remove(self):
        s = 'abcba'
        res = self.s.minimumLength(s)
        self.assertEqual(1, res)

    def test_1_char(self):
        s = 'a'
        res = self.s.minimumLength(s)
        self.assertEqual(1, res)