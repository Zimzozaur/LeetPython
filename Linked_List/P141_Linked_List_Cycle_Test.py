import unittest
from ListNode import *
from P141_Linked_List_Cycle import Solution


class BasicTest(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        ll: ListNode = list_generator([3, 2, 0, -4])
        ll.next.next.next.next = ll.next
        res = self.s.hasCycle(ll)
        self.assertEqual(True, res)

    def test_2(self):
        ll: ListNode = list_generator([1, 2])
        ll.next.next = ll
        res = self.s.hasCycle(ll)
        self.assertEqual(True, res)

    def test_3(self):
        ll: ListNode = list_generator([-1])
        res = self.s.hasCycle(ll)
        self.assertEqual(False, res)

    def test_no_cycle(self):
        ll: ListNode = list_generator([1, 2, 3, 4, 5])
        res = self.s.hasCycle(ll)
        self.assertEqual(False, res)

