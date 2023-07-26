# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Check how many parentheses are needed to add to make strings valid.

        A parentheses string is valid if and only if:
            It is an empty string,
            It can be written as AB (A concatenated with B), where A and B are valid strings, or
            It can be written as (A), where A is a valid string.
        :param s:
        :return:

        The right order is:
            open, close, open, close or
            open, open, close, close


        """
        stack = []   # holds brackets closed not correctly
        for char in s:
            if char is "(":
                stack.append('(')
            elif char is ")" and len(stack) > 0 and stack[-1] is '(':
                # if a list is empty or the bracket is not closing, it will not be valid.
                stack.pop()
            else:
                stack.append(')')

        return len(stack)
