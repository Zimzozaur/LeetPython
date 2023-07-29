# https://leetcode.com/problems/strictly-palindromic-number/description/
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        """
        An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive),
        the string representation of the integer n in base b is palindromic.

        Given an integer n, return true if n is strictly palindromic and false otherwise.

        A string is palindromic if it reads the same forward and backward.

        Input: n = 9
        Output: false
        Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
        In base 3: 9 = 100 (base 3), which is not palindromic.
        Therefore, 9 is not strictly palindromic so we return false.
        Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.

        Constraints:

        4 <= n <= 105

        For those who do not understand the question or why - false is always the right answer.

        When you scroll down to the "Related Topics" section,
        you will see that this question is tagged as "Brainteaser".
        Which means that this question probably is not about DSA, but about logic.

        When you look closely at examples 1 & 2, you will see that for n equal to 4 answer if false.

        So it does not matter how big n is because you will always include n equal to 4
        (Constraints: 4 <= n <= 105, and "for every base b between 2 and n - 2 (inclusive)"),
        which is false, so for every n >= 4 answer will be false.
        :param n:
        :return:
        """
        return False
