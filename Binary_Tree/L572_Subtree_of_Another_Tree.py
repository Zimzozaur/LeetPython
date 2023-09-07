# https://leetcode.com/problems/subtree-of-another-tree/description/
from typing import Optional
from TreeNode import *
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subRoot):
            if not root:
                return False

            if not dfs_check(root, subRoot):
                if dfs(root.left, subRoot):
                    return True
                if dfs(root.right, subRoot):
                    return True
                return False
            else:
                return True

        def dfs_check(p, q):
            if not p and not q:
                return True
            if not p and q or p and not q:
                return False
            if p.val != q.val:
                return False

            flag1 = dfs_check(p.left, q.left)
            flag2 = dfs_check(p.right, q.right)

            if not flag1 or not flag2:
                return False

            return True

        return dfs(root, subRoot)
