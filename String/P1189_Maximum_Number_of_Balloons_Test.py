import unittest
from P1189_Maximum_Number_of_Balloons import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        text = "nlaebolko"
        res = self.s.maxNumberOfBalloons(text)
        self.assertEqual(1, res)

    def test_2(self):
        text = "loonbalxballpoon"
        res = self.s.maxNumberOfBalloons(text)
        self.assertEqual(2, res)

    def test_4(self):
        text = 'leetcode'
        res = self.s.maxNumberOfBalloons(text)
        self.assertEqual(0, res)

    def test_1_correct_every_letter_separate_by_x(self):
        text = "bxaxlxlxoxoxn"
        res = self.s.maxNumberOfBalloons(text)
        self.assertEqual(1, res)

    def test_strange_word(self):
        text = 'hpitp'
        res = self.s.maxNumberOfBalloons(text)
        self.assertEqual(0, res)