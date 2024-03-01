import unittest
from P128_Longest_Consecutive_Sequence import Solution


class LeetCodeTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_leetcode_1(self):
        nums = [100, 4, 200, 1, 3, 2]
        res = self.sol.longestConsecutive(nums)
        self.assertEqual(4, res)

    def test_leetcode_2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        res = self.sol.longestConsecutive(nums)
        self.assertEqual(9, res)

    def test_empty_arr(self):
        nums = []
        res = self.sol.longestConsecutive(nums)
        self.assertEqual(0, res)

    def test_1_num(self):
        nums = [0]
        res = self.sol.longestConsecutive(nums)
        self.assertEqual(1, res)

    def test_2_num_1_len(self):
        nums = [100, 200]
        res = self.sol.longestConsecutive(nums)
        self.assertEqual(1, res)

    def test_2_num_2_len(self):
        nums = [1, 2]
        res = self.sol.longestConsecutive(nums)
        self.assertEqual(2, res)

