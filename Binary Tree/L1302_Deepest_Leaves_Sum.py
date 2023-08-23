# https://leetcode.com/problems/deepest-leaves-sum/
from collections import deque
from typing import Optional
from TreeNode import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """Return sum of leaves on the lowes level of the tree"""

        """
        Use breadth first search to find lowes leaves
        """

        stack_nodes = deque([root])  # Hold current level
        stack_values = deque()  # Hold values of current level

        while stack_nodes:
            stack_values.clear()
            new_nodes_stack = deque()

            # Loop over stack and put nodes from the next level and add to 2nd stack
            while stack_nodes:
                node = stack_nodes.pop()
                stack_values.append(node.val)

                if node.right:
                    new_nodes_stack.append(node.right)
                if node.left:
                    new_nodes_stack.append(node.left)

            stack_nodes = new_nodes_stack

        return sum(stack_values)


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)

    sol = Solution()
    print(sol.deepestLeavesSum(root))

