# https://leetcode.com/problems/average-of-levels-in-binary-tree/
from collections import deque
from typing import Optional
from TreeNode import TreeNode
from tree_generator import tree_generate

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        """
        BSF
        result - array
        counter - int
        """

        arr = deque([root])
        result = []
        while arr:
            sum_val = 0
            counter = 0
            for _ in range(len(arr)):
                node = arr.popleft()
                sum_val += node.val
                counter += 1
                if node.left:
                    arr.append(node.left)
                if node.right:
                    arr.append(node.right)
            result.append(round(sum_val / counter, 5))

        return result


if __name__ == '__main__':
    sol = Solution()
    x = [-630, -403, 522, -485, -564, 652, 572, 277, -472, 12, 351, 385, 482, 164, -251]
    y = sol.averageOfLevels(tree_generate(x))
    print(y)