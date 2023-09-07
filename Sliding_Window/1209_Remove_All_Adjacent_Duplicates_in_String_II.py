# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Return the final string after all such duplicate removals have been made.
        It is guaranteed that the answer is unique.
        :param s:
        :param k:
        :return:
        We need to use stack

        Add to stack if added the same element k times pop from stack,
        When adding an element if stack is empty,
        Check is last element the same k time if the same remove


        """

        stack = []

        for char in s:

            if stack:
                



if __name__ == '__main__':
    sol = Solution()
    x = "deeedbbcccbdaa"
    print(sol.removeDuplicates(x, 3))
