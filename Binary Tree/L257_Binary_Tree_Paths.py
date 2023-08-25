# https://leetcode.com/problems/binary-tree-paths/description/
from typing import Optional
from TreeNode import *


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        """Backtrack every path from root to leaf and return array with paths"""

        track_list = []
        nums_list = []
        not_remove = root

        def dfs(root: Optional[TreeNode]) -> Optional[TreeNode]:
            """Traverse and add to list root to a leaf path"""

            # Base case
            if not root:
                return

            nums_list.append(root.val)

            if not root.left and not root.right:
                path = ""
                for num in nums_list:
                    path += str(num) + "->"
                track_list.append(path[:len(path) - 2])

            dfs(root.left)
            dfs(root.right)

            nums_list.pop()

        dfs(root)

        return track_list


if __name__ == '__main__':

    def create_binary_tree(array, index=0):
        if index >= len(array) or array[index] is None:
            return None

        root = TreeNode(array[index])
        root.left = create_binary_tree(array, 2 * index + 1)
        root.right = create_binary_tree(array, 2 * index + 2)

        return root

    # Given array
    array = [1,2,3,None,5]

    # Create binary tree from array
    root = create_binary_tree(array)

    sol = Solution()
    print(sol.binaryTreePaths(root))

