import unittest
from P448_Find_All_Numbers_Disappeared_in_an_Array import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        res = self.s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
        self.assertEqual([5, 6], res)

    def test_2(self):
        res = self.s.findDisappearedNumbers([1, 1])
        self.assertEqual([2], res)

    def test_5_ones(self):
        res = self.s.findDisappearedNumbers([1, 1, 1, 1, 1])
        self.assertEqual([2, 3, 4, 5], res)

