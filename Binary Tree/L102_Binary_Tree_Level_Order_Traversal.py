# https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque
from typing import Optional
from TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """Return sum of leaves on the lowes level of the tree"""

        if not root:
            return []

        queue_nodes = deque([root])
        values = []

        while queue_nodes:
            new_chunk = []
            for i in range(len(queue_nodes)):
                node = queue_nodes.popleft()
                new_chunk.append(node.val)

                if node.right:
                    queue_nodes.append(node.right)
                if node.left:
                    queue_nodes.append(node.left)

            values.append(new_chunk)

        return values


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)

    sol = Solution()
    print(sol.levelOrder(root))

