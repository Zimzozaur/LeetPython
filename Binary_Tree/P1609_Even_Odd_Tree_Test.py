# https://leetcode.com/problems/even-odd-tree/?envType=daily-question&envId=2024-02-29
import unittest
from tree_generator import tree_generate
from P1609_Even_Odd_Tree import *


class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one_node_tree_odd(self):
        tree = TreeNode(1)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(True, res)

    def test_one_node_tree_even(self):
        tree = TreeNode(2)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(False, res)

    def test_leetcode_1(self):
        tree_arr = [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]
        tree = tree_generate(tree_arr)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(True, res)

    def test_leetcode_2(self):
        tree_arr = [5, 4, 2, 3, 3, 7]
        tree = tree_generate(tree_arr)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(False, res)

    def test_leetcode_3(self):
        tree_arr = [5, 9, 1, 3, 5, 7]
        tree = tree_generate(tree_arr)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(False, res)

    def test_my_1(self):
        tree_arr = [5, 6, 4, 1]
        tree = tree_generate(tree_arr)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(True, res)











