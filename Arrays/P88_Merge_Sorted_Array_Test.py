import unittest
from P88_Merge_Sorted_Array import Solution


class LeetCodeTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_leetcode_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.sol.merge(nums1, m, nums2, n)
        answer = [1, 2, 2, 3, 5, 6]
        self.assertEqual(answer, nums1)

    def test_leetcode_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        self.sol.merge(nums1, m, nums2, n)
        answer = [1]
        self.assertEqual(answer, nums1)

    def test_leetcode_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        self.sol.merge(nums1, m, nums2, n)
        answer = [1]
        self.assertEqual(answer, nums1)

    def test_m0_n4(self):
        nums1 = [0, 0, 0, 0]
        m = 0
        nums2 = [1, 2, 3, 4]
        n = 4
        self.sol.merge(nums1, m, nums2, n)
        answer = [1, 2, 3, 4]
        self.assertEqual(answer, nums1)

    def test_8_num(self):
        nums1 = [1, 2, 4, 7, 0, 0, 0, 0]
        m = 4
        nums2 = [2, 2, 5, 6]
        n = 4
        self.sol.merge(nums1, m, nums2, n)
        answer = [1, 2, 2, 2, 4, 5, 6, 7]
        self.assertEqual(answer, nums1)





