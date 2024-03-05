import unittest
from P53_Maximum_Subarray import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        res = self.s.maxSubArray(arr)
        self.assertEqual(6, res)

    def test_2(self):
        arr = [1]
        res = self.s.maxSubArray(arr)
        self.assertEqual(1, res)

    def test_3(self):
        arr = [5, 4, -1, 7, 8]
        res = self.s.maxSubArray(arr)
        self.assertEqual(23, res)

    def test_all_negative(self):
        arr = [-1, -2, -3, -4, -5]
        res = self.s.maxSubArray(arr)
        self.assertEqual(-1, res)

    def test_duplicate_number(self):
        arr = [3, -2, -3, -3, 1, 3, 0]
        res = self.s.maxSubArray(arr)
        self.assertEqual(4, res)

    def test_3_same_numbers(self):
        arr = [2, -3, 1, 3, -3, 2, 2, 1]
        res = self.s.maxSubArray(arr)
        self.assertEqual(6, res)
