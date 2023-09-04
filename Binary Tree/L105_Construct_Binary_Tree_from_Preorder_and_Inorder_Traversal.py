# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
import math
from typing import Optional
from TreeNode import TreeNode
from tree_generator import tree_generate


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return
        root = TreeNode(preorder[0])
        ino = 0
        for index, val in enumerate(preorder):
            if val == inorder[0]:
                ino = index

        root.left = self.buildTree(preorder[1:ino + 1], inorder[:ino])
        root.right = self.buildTree(preorder[ino + 1:], inorder[ino + 1:])

        return root
def in_order(root):
    arr = []

    def traverse(root):
        if root:
            traverse(root.left)
            arr.append(root.val)
            traverse(root.right)
    traverse(root)
    return arr


def pre_order(root):
    arr = []

    def traverse(root):
        if root:
            arr.append(root.val)
            traverse(root.left)
            traverse(root.right)
    traverse(root)
    return arr

if __name__ == '__main__':
    sol = Solution()
    x = [num for num in range(1, 6)]
    tree = tree_generate(x)
    pre = pre_order(tree)
    bino = in_order(tree)

    print(pre)
    print(bino)
    z = sol.buildTree(pre, bino)
    print()

"""
Tworzę drzewo w lewo aż liczba będzie równa ino
wtedy pcham ino do następnej której nnie był 
"""