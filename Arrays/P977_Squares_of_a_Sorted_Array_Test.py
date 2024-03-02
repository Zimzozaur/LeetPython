import unittest
from P977_Squares_of_a_Sorted_Array import Solution


class LeetCodeTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1_leetcode(self):
        nums = [-4, -1, 0, 3, 10]
        answer = [0, 1, 9, 16, 100]
        res = self.sol.sortedSquares(nums)
        self.assertEqual(answer, res)

    def test_2_leetcode(self):
        nums = [-7, -3, 2, 3, 11]
        answer = [4, 9, 9, 49, 121]
        res = self.sol.sortedSquares(nums)
        self.assertEqual(answer, res)

    def test_2_nums(self):
        nums = [-2, 3]
        answer = [4, 9]
        res = self.sol.sortedSquares(nums)
        self.assertEqual(answer, res)

    def test_3_nums(self):
        nums = [-2, 1, 3]
        answer = [1, 4, 9]
        res = self.sol.sortedSquares(nums)
        self.assertEqual(answer, res)

    def test_6_nums(self):
        nums = [-3, -2, -1, 1, -2, -3]
        answer = [1, 1, 4, 4, 9, 9]
        res = self.sol.sortedSquares(nums)
        self.assertEqual(answer, res)
