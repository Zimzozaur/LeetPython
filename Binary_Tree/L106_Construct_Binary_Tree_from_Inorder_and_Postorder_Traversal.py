# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from collections import deque
from typing import Optional
from TreeNode import TreeNode
from tree_generator import tree_generate


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:

        if len(inorder) < 1 and len(postorder) < 1:
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])

        return root


def in_order(root):
    arr = []
    stack = deque([root])

    while stack:
        if stack[-1] is None:
            stack.pop()
            if stack:
                arr.append(stack[-1].val)
                stack.append(stack.pop().right)
        else:
            stack.append(stack[-1].left)

    return arr


def post_order(root):
    arr = []

    def traverse(root):
        if root:
            traverse(root.left)
            traverse(root.right)
            arr.append(root.val)

    traverse(root)
    return arr


if __name__ == '__main__':
    x = [num for num in range(1, 80)]
    # x = [3,9,20,None,None,15,7]
    tree = tree_generate(x)
    post = post_order(tree)
    ino = in_order(tree)

    print(post)
    print(ino)

    sol = Solution()
    z = sol.buildTree(ino, post)
    print()
