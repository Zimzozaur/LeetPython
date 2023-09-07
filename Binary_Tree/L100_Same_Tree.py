# https://leetcode.com/problems/same-tree/
import random
from typing import Optional
from TreeNode import *
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Check if they are the same."""
        """
        Recu Function that needs as input p and q
        """
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

        return dfs_check(p, q)


if __name__ == '__main__':
    print([random.randint(-5000, 5000) for num in range(100)])