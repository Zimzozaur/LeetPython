# https://leetcode.com/problems/path-sum/
from collections import deque
from typing import Optional
from TreeNode import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Return true if the sum of root-to-leaf path if equal to target"""
        """
        I want to go from root to leaf and then check is equal if not go to next leaf
        """
        if not root:
            return False

        stack = deque()

        if traverse(root, targetSum, stack):
            return True

        return False


def traverse(root, target, nodes):

    if not root:
        return False

    nodes.append(root.val)

    if not root.left and not root.right:
        if sum(nodes) == target:
            return True

    if traverse(root.left, target, nodes):
        return True
    if traverse(root.right, target, nodes):
        return True

    nodes.pop()
    return False


if __name__ == '__main__':

    def create_binary_tree(array, index=0):
        if index >= len(array) or array[index] is None:
            return None

        root = TreeNode(array[index])
        root.left = create_binary_tree(array, 2 * index + 1)
        root.right = create_binary_tree(array, 2 * index + 2)

        return root


    # Given array
    array = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 1]

    # Create binary tree from array
    root = create_binary_tree(array)

    sol = Solution()
    print(sol.hasPathSum(root, 18))
