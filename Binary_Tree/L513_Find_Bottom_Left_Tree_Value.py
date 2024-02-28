from TreeNode import TreeNode
from typing import Optional
from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        BFS than first node will be correct
        Use 2 queue one for current and one for next
        if next is empty take return 1st from current
        """
        current, coming = deque([root]), deque()
        while True:
            for node in current:
                if node.left:
                    coming.append(node.left)
                if node.right:
                    coming.append(node.right)
            if not coming:
                return current.popleft().val
            else:
                current.clear()
                for _ in range(len(coming)):
                    current.append(coming.popleft())


