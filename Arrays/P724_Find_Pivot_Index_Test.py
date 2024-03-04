import unittest
from P724_Find_Pivot_Index import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        nums = [1, 7, 3, 6, 5, 6]
        res = self.s.pivotIndex(nums)
        self.assertEqual(3, res)

    def test_2(self):
        nums = [1, 2, 3]
        res = self.s.pivotIndex(nums)
        self.assertEqual(-1, res)

    def test_3(self):
        nums = [2, 1, -1]
        res = self.s.pivotIndex(nums)
        self.assertEqual(0, res)

    def test_4(self):
        nums = [2, 1, 0, 3]
        res = self.s.pivotIndex(nums)
        self.assertEqual(2, res)

