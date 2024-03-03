import unittest
from ListNode import list_generator, compare_ll


class CompareLLTest(unittest.TestCase):
    def setUp(self):
        self.node3 = list_generator([1, 2, 3])
        self.node3_diff = list_generator([1, 2, 2])
        self.node2 = list_generator([1, 2])

    def test_3_node_2_node(self):
        res = compare_ll(self.node3, self.node2)
        self.assertEqual(False, res)


    def test_2_node_3_node(self):
        res = compare_ll(self.node2, self.node3)
        self.assertEqual(False, res)


    def test_3_node_3_node(self):
        res = compare_ll(self.node3, self.node3)
        self.assertEqual(True, res)

    def test_3_node_3_node_diff_val(self):
        res = compare_ll(self.node3, self.node3_diff)
        self.assertEqual(False, res)