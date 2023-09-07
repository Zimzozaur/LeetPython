# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
from collections import deque
from tree_generator import tree_generate
from TreeNode import *


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, val, stack=None):
            flag = False
            nonlocal result
            if not root:
                return stack
            if stack is None:
                stack = deque([])
            if not stack or stack[-1] <= root.val:
                flag = True
                stack.append(root.val)
                result += 1
            stack = dfs(root.left, val, stack)
            stack = dfs(root.right, val, stack)
            if flag:
                stack.pop()
            return stack

        result = 0
        dfs(root, root.val)
        return result

if __name__ == '__main__':
    sol = Solution()
    arr = [59, 34, 5, 26, 87, 51, 13, 67, 84, 56, 22, 3, 87, 36, 50, 45, 7, 10, 37, 41, 96, 61, 6, 41, 81, 42, 75, 29, 72, 50, 4, 69, 70, 39, 87, 35, 79, 60, 58, 58, 67, 100, 4, 68, 30, 36, 60, 56, 17, 2, 93, 100, 17, 50, 78, 37, 4, 82, 1, 83, 93, 4, 77, 66, 100, 100, 31, 88, 56, 64, 51, 21, 53, 61, 69, 36, 21, 70, 76, 93, 60, 73, 77, 28, 37, 67, 42, 84, 90, 53, 98, 87, 11, 83, 39, 35, 92, 8, 69, 83]
    tree = tree_generate(arr)

    print(sol.goodNodes(tree))
