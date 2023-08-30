# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
from typing import Optional
from TreeNode import *
from tree_generator import tree_generate


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        """
        Return the number of nodes where
        the value of the node is equal to
        the average of the values in its subtree.
        """
        def dfs(root):
            if not root:
                return 0, 0, 0

            tup1 = dfs(root.left)
            tup2 = dfs(root.right)

            value = tup1[0] + tup2[0] + root.val
            nodes = tup1[1] + tup2[1] + 1
            if value // nodes == root.val:
                correct = tup1[2] + tup2[2] + 1
            else:
                correct = tup1[2] + tup2[2]

            return value, nodes, correct

        return dfs(root)[2]


if __name__ == '__main__':
    sol = Solution()
    x = [4,8,5,0,1,None,6]
    tree = tree_generate(x)
    print(sol.averageOfSubtree(tree))


