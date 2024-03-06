import unittest
from P783_Minimum_Distance_Between_BST_Nodes import Solution
from TreeNode import TreeNode

class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        root = TreeNode(4)
        root.left, root.right = TreeNode(2), TreeNode(6)
        root.left.left, root.left.right = TreeNode(1), TreeNode(3)
        res = self.s.minDiffInBST(root)
        self.assertEqual(1, res)

    def test_2(self):
        root = TreeNode(1)
        root.left, root.right = TreeNode(0), TreeNode(48)
        root.right.left, root.right.right = TreeNode(12), TreeNode(49)
        res = self.s.minDiffInBST(root)
        self.assertEqual(1, res)

