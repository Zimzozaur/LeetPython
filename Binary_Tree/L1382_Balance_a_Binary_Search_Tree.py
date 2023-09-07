# https://leetcode.com/problems/balance-a-binary-search-tree/
from TreeNode import *
from tree_generator import *

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        Return a balanced binary search tree with the same node values.
        If there is more than one answer, return any of them.
        """
        nodes_arr = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nonlocal nodes_arr
            nodes_arr.append(root.val)
            inorder(root.right)

        def build_tree(arr):
            if len(arr) == 0:
                return

            mid = len(arr) // 2
            groot = TreeNode(arr[mid])
            groot.left = build_tree(arr[0:mid].copy())
            groot.right = build_tree(arr[mid + 1:].copy())

            return groot
            
        inorder(root)
        return build_tree(nodes_arr)


if __name__ == '__main__':
    sol = Solution()
    x = [1000,900,2000,800,950,None,3000,700,None,None,None,2500,4000,600,None,None,None,None,None,None,650]
    y = tree_generate(x)
    z = sol.balanceBST(y)
    print()