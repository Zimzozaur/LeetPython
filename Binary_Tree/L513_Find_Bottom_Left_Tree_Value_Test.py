import unittest
from TreeNode import TreeNode
from tree_generator import tree_generate
from L513_Find_Bottom_Left_Tree_Value import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_class_exits(self):
        assert isinstance(self.sol, Solution), 'Class does not exist'

    def test_one_node_tree(self):
        tree = TreeNode(1)
        res = self.sol.findBottomLeftValue(tree)
        self.assertEqual(1, res)

    def test_3_node_tree(self):
        tree = tree_generate([1, 2, 3])
        res = self.sol.findBottomLeftValue(tree)
        self.assertEqual(2, res)

    def test_9_node_tree(self):
        tree = tree_generate([1, 2, 3, 4, None, 5, 6, None, None, None, 7, None, 8, None, None, 9, None, 10])
        res = self.sol.findBottomLeftValue(tree)
        self.assertEqual(10, res)

