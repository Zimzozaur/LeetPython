import unittest
from P496_Next_Greater_Element_I import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        res = self.s.nextGreaterElement(nums1, nums2)
        self.assertEqual([-1, 3, -1], res)

    def test_2(self):
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        res = self.s.nextGreaterElement(nums1, nums2)
        self.assertEqual([3, -1], res)

    def test_3(self):
        nums1 = [3, 1, 7]
        nums2 = [2, 3, 5, 1, 0, 7]
        res = self.s.nextGreaterElement(nums1, nums2)
        self.assertEqual([5, 7, -1], res)
