import unittest
from P229_Majority_Element_II import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        arr = [3, 2, 3]
        res = self.s.majorityElement(arr)
        self.assertEqual([3], res)

    def test_2(self):
        arr = [1]
        res = self.s.majorityElement(arr)
        self.assertEqual([1], res)

    def test_3(self):
        arr = [1, 2]
        res = self.s.majorityElement(arr)
        self.assertEqual([1, 2], res)

    def test_7_len_1_good(self):
        arr = [1, 2, 1, 2, 3, 3, 3]
        res = self.s.majorityElement(arr)
        self.assertEqual([3], res)

    def test_8_len_2_good(self):
        arr = [1, 2, 1, 2, 1, 3, 3, 3]
        res = self.s.majorityElement(arr)
        self.assertEqual([1, 3], res)

    def test_5_len_2_good(self):
        arr = [1, 2, 2, 3, 3]
        res = self.s.majorityElement(arr)
        self.assertEqual([2, 3], res)