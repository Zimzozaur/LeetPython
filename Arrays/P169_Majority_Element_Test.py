import unittest
from P169_Majority_Element import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        arr = [3, 2, 3]
        res = self.s.majorityElement(arr)
        self.assertEqual(3, res)

    def test_2(self):
        arr = [2, 2, 1, 1, 1, 2, 2]
        res = self.s.majorityElement(arr)
        self.assertEqual(2, res)

    def test_8_len(self):
        arr = [1, 1, 2, 1, 3, 3, 1]
        res = self.s.majorityElement(arr)
        self.assertEqual(1, res)

    def tes_8_len_reversed(self):
        arr = [1, 3, 3, 1, 2, 1, 1]
        res = self.s.majorityElement(arr)
        self.assertEqual(1, res)

