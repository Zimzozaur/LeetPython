# https://leetcode.com/problems/binary-tree-pruning/description/
from typing import Optional
from TreeNode import TreeNode


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root.left:
                root.left = dfs(root.left)
            if root.right:
                root.right = dfs(root.right)

            if not root.left and not root.right and root.val == 0:
                return None
            elif not root.left and not root.right and root.val == 1:
                return root

            return root

        return dfs(root)