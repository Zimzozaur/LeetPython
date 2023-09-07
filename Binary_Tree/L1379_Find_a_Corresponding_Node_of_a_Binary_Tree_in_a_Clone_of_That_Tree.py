# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
from TreeNode import *

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """DFS on two trees in the same time"""

        def dfs(root, groot, target):
            if not root:
                return
            if root.val == target.val:
                return groot

            node_left = dfs(root.left, groot.left, target)
            node_right = dfs(root.right, groot.right, target)

            if isinstance(node_left, TreeNode):
                return node_left
            if isinstance(node_right, TreeNode):
                return node_right

        return dfs(original, cloned, target)


if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(7)
    tree.left = TreeNode(4)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(19)

    bree = TreeNode(7)
    bree.left = TreeNode(4)
    bree.right = TreeNode(3)
    bree.right.left = TreeNode(6)
    bree.right.right = TreeNode(19)

    print(sol.getTargetCopy(tree, bree, tree.right).val)
