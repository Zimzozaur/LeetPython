# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        """
        Proceses string in a way that removes all starts and letter before star
        :param s:
        :return:

        loop over the string
        add letters to stack if * pop letter
        loop over a stack to create string and return it.
        """

        stack = []

        for char in s:
            if char == '*':
                stack.pop()  # Pops char
            else:
                stack.append(char)  # Adds char

        return "".join(stack)  # Merge chars

