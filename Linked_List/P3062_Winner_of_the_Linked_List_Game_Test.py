import unittest
from ListNode import list_generator
from P3062_Winner_of_the_Linked_List_Game import Solution


class LeetCode(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        arr = [2, 1]
        ll = list_generator(arr)
        res = self.s.gameResult(ll)
        self.assertEqual("Even", res)

    def test_2(self):
        arr = [2, 5, 4, 7, 20, 5]
        ll = list_generator(arr)
        res = self.s.gameResult(ll)
        self.assertEqual("Odd", res)

    def test_3(self):
        arr = [4, 5, 2, 1]
        ll = list_generator(arr)
        res = self.s.gameResult(ll)
        self.assertEqual("Tie", res)
