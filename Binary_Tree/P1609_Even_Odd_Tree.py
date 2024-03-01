# https://leetcode.com/problems/even-odd-tree/?envType=daily-question&envId=2024-02-29
from TreeNode import TreeNode
from typing import Optional
from collections import deque


def helper(asc_decs_fn, odd_even_fn, deck: deque[TreeNode]):
    """Returns bool about is level complain with rules"""
    for node in deck:
        if not odd_even_fn(node.val):
            return False
    if not asc_decs_fn(deck):
        return False
    return True


def is_ascending(deck: deque[TreeNode]):
    coming = deck.popleft()
    deck.append(coming)
    for i in range(len(deck) - 1):
        curr = coming
        coming = deck.popleft()
        deck.append(coming)
        if curr.val >= coming.val:
            return False
    return True


def is_descending(deck: deque[TreeNode]):
    coming = deck.popleft()
    deck.append(coming)
    for i in range(len(deck) - 1):
        curr = coming
        coming = deck.popleft()
        deck.append(coming)
        if curr.val <= coming.val:
            return False
    return True


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).

        For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
        """
        curr = deque([root])
        odd = True
        while curr:
            if odd:
                res = helper(is_ascending, is_odd, curr)
            else:
                res = helper(is_descending, is_even, curr)
            if not res:
                return False
            coming = deque([])
            for r in curr:
                if r.left:
                    coming.append(r.left)
                if r.right:
                    coming.append(r.right)
            odd = not odd
            curr = coming
        return True
