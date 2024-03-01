import unittest
from P1570_Dot_Product_of_Two_Sparse_Vectors import SparseVector


class ListToDictConversionTest(unittest.TestCase):
    def test_1_dict(self):
        d = [0, 0, 1]
        inst = SparseVector(d)
        answer = {2: 1}
        self.assertEqual(answer, inst.has_map)

    def test_2_dict(self):
        d = [1, 2, 3, 0, 5]
        inst = SparseVector(d)
        answer = {0: 1, 1: 2, 2: 3, 4: 5}
        self.assertEqual(answer, inst.has_map)

    def test_iteration(self):
        d = [1, 2, 3, 0, 5]
        inst = SparseVector(d)
        answer = {0: 1, 1: 2, 2: 3, 4: 5}
        res = {key: value for key, value in inst.has_map.items()}
        self.assertEqual(answer, res)


class LeetCodeTest(unittest.TestCase):
    def test_leetcode_1(self):
        nums1 = [1, 0, 0, 2, 3]
        nums2 = [0, 3, 0, 4, 0]
        inst1 = SparseVector(nums1)
        inst2 = SparseVector(nums2)
        res = inst1.dotProduct(inst2)
        self.assertEqual(8, res)

    def test_leetcode_2(self):
        nums1 = [0, 1, 0, 0, 0]
        nums2 = [0, 0, 0, 0, 2]
        inst1 = SparseVector(nums1)
        inst2 = SparseVector(nums2)
        res = inst1.dotProduct(inst2)
        self.assertEqual(0, res)

    def test_leetcode_3(self):
        nums1 = [0, 1, 0, 0, 2, 0, 0]
        nums2 = [1, 0, 0, 0, 3, 0, 4]
        inst1 = SparseVector(nums1)
        inst2 = SparseVector(nums2)
        res = inst1.dotProduct(inst2)
        self.assertEqual(6, res)

    def test_2_len(self):
        nums1 = [1, 4]
        nums2 = [3, 4]
        inst1 = SparseVector(nums1)
        inst2 = SparseVector(nums2)
        res = inst1.dotProduct(inst2)
        self.assertEqual(19, res)









