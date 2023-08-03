# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Removes duplicates of letters in a string.
        :param s:
        :return:

        Create a stack if char is the same as on top do not pop from stack.
        """

        stack = []

        for char in s:
            # When the stack is empty or the char is not the same
            if not stack or char != stack[-1]:
                stack.append(char)
            else:
                # Same so pop
                stack.pop()

        return "".join(stack)
