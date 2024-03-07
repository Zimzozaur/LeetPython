import unittest
from ListNode import *
from P876_Middle_of_the_Linked_List import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        res = self.s.middleNode(ListNode(1))
        self.assertEqual([1], [res.val])

    def test_two(self):
        arr = [1, 2]
        head = list_generator(arr)
        res = self.s.middleNode(head)
        res_arr = [res.val]
        self.assertEqual([2], res_arr)

    def test_three(self):
        arr = [1, 2, 3]
        head = list_generator(arr)
        res = self.s.middleNode(head)
        res_arr = [res.val, res.next.val]
        self.assertEqual([2, 3], res_arr)

    def test_four(self):
        arr = [1, 2, 3, 4]
        head = list_generator(arr)
        res = self.s.middleNode(head)
        res_arr = [res.val, res.next.val]
        self.assertEqual([3, 4], res_arr)

    def test_five(self):
        arr = [1, 2, 3, 4, 5]
        head = list_generator(arr)
        res = self.s.middleNode(head)
        res_arr = [res.val, res.next.val, res.next.next.val]
        self.assertEqual([3, 4, 5], res_arr)

    def test_six(self):
        arr = [1, 2, 3, 4, 5, 6]
        head = list_generator(arr)
        res = self.s.middleNode(head)
        res_arr = [res.val, res.next.val, res.next.next.val]
        self.assertEqual([4, 5, 6], res_arr)


