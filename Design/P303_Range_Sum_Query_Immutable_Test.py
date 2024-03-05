import unittest
from P303_Range_Sum_Query_Immutable import NumArray


class BasicTest(unittest.TestCase):

    def test_correct_init(self):
        arr = NumArray([1, 2, 3])
        self.assertEqual([1, 3, 6], arr.arr)

    def test_1(self):
        arr = NumArray([-2, 0, 3, -5, 2, -1])
        res = arr.sumRange(0, 2)
        self.assertEqual(1, res)
        res = arr.sumRange(2, 5)
        self.assertEqual(-1, res)
        res = arr.sumRange(0, 5)
        self.assertEqual(-3, res)

    def test_2(self):
        arr = NumArray([6, 3, 4, 1, 2, 9])
        res = arr.sumRange(0, 2)
        self.assertEqual(13, res)
        res = arr.sumRange(2, 5)
        self.assertEqual(16, res)
        res = arr.sumRange(0, 5)
        self.assertEqual(25, res)
        res = arr.sumRange(1, 3)
        self.assertEqual(8, res)
