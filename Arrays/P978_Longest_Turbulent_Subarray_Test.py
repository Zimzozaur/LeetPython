import unittest
from P978_Longest_Turbulent_Subarray import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
        res = self.s.maxTurbulenceSize(arr)
        self.assertEqual(5, res)

    def test_2(self):
        arr = [4, 8, 12, 16]
        res = self.s.maxTurbulenceSize(arr)
        self.assertEqual(2, res)

    def test_3(self):
        arr = [100]
        res = self.s.maxTurbulenceSize(arr)
        self.assertEqual(1, res)

    def test_4(self):
        arr = [3, 8, 5, 2, 7, 9, 4]
        res = self.s.maxTurbulenceSize(arr)
        self.assertEqual(3, res)

    def test_5(self):
        arr = [5, 5, 5]
        res = self.s.maxTurbulenceSize(arr)
        self.assertEqual(1, res)

    def test_6(self):
        arr = [5, 5, 6,]
        res = self.s.maxTurbulenceSize(arr)
        self.assertEqual(2, res)