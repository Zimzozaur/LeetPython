import unittest
from P918_Maximum_Sum_Circular_Subarray import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        arr = [1, -2, 3, -2]
        res = self.s.maxSubarraySumCircular(arr)
        self.assertEqual(3, res)

    def test_2(self):
        arr = [5, -3, 5]
        res = self.s.maxSubarraySumCircular(arr)
        self.assertEqual(10, res)

    def test_3(self):
        arr = [-3, -2, -3]
        res = self.s.maxSubarraySumCircular(arr)
        self.assertEqual(-2, res)

    def test_3_subs_2_holes(self):
        arr = [5, 3, -9, 7, 2, -10, 5, 3]
        res = self.s.maxSubarraySumCircular(arr)
        self.assertEqual(16, res)

    def test_3_positive(self):
        arr = [5, 5, 5]
        res = self.s.maxSubarraySumCircular(arr)
        self.assertEqual(15, res)

    def test_4(self):
        arr = [3, -1, 2, -1]
        res = self.s.maxSubarraySumCircular(arr)
        self.assertEqual(4, res)

    def test_5(self):
        arr = [5, -6, 5, -4]
        res = self.s.maxSubarraySumCircular(arr)
        self.assertEqual(6, res)

    def test_6(self):
        arr = [9, -4, -7, 9]
        res = self.s.maxSubarraySumCircular(arr)
        self.assertEqual(18, res)

    def test_7(self):
        arr = [-2, 3, -4, 3]
        res = self.s.maxSubarraySumCircular(arr)
        self.assertEqual(4, res)

    def test_8(self):
        arr = [1, -6, -7, 4]
        res = self.s.maxSubarraySumCircular(arr)
        self.assertEqual(5, res)

    def test_9(self):
        arr = [8, -8, 8, -8]
        res = self.s.maxSubarraySumCircular(arr)
        self.assertEqual(8, res)
