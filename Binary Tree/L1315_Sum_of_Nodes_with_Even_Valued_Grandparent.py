# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
import random
from TreeNode import TreeNode


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        Return the sum of values of nodes with an even-valued grandparent.
        If there are no nodes with an even-valued grandparent, return 0.
        """
        def dfs(root, parent=None, grandparent=None) -> int:
            result = 0
            if not root:
                return 0
            if isinstance(grandparent, TreeNode):
                if grandparent.val % 2 == 0:
                    result += root.val
            if isinstance(parent, TreeNode):
                grandparent = parent

            left = dfs(root.left, root, grandparent)
            right = dfs(root.right, root, grandparent)

            return left + right + result

        return dfs(root)


if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(3)

    print(sol.sumEvenGrandparent(tree))
    print([random.randint(1,100) for i in range(1000)])
