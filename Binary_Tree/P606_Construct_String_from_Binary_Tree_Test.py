import unittest
from P606_Construct_String_from_Binary_Tree import Solution
from tree_generator import *


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        tree = tree_generate([1, 2, 3, 4])
        res = self.s.tree2str(tree)
        answer = "1(2(4))(3)"
        self.assertEqual(answer, res)

    def test_2(self):
        tree = tree_generate([1, 2, 3, None, 4])
        res = self.s.tree2str(tree)
        answer = "1(2()(4))(3)"
        self.assertEqual(answer, res)

    def test_one_node(self):
        tree = tree_generate([1])
        res = self.s.tree2str(tree)
        answer = "1"
        self.assertEqual(answer, res)

    def test_two_nodes(self):
        tree = tree_generate([1, 2])
        res = self.s.tree2str(tree)
        answer = "1(2)"
        self.assertEqual(answer, res)

    def test_two_nodes_one_right(self):
        tree = tree_generate([1, None, 2])
        res = self.s.tree2str(tree)
        answer = "1()(2)"
        self.assertEqual(answer, res)

    def test_big_tree(self):
        tree = tree_generate([1,2,3,3,2,1,5,None, 1, None, 5, None, None, 2,4, None, 2, 3, 4])
        res = self.s.tree2str(tree)
        answer = "1(2(3()(1()(2)))(2()(5(3)(4))))(3(1)(5(2)(4)))"
        self.assertEqual(answer, res)