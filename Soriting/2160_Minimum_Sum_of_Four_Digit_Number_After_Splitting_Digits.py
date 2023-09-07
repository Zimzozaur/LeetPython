# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
class Solution:
    def minimumSum(self, num: int) -> int:
        """
        Creates two numbers from int and returns a sum of those 2
        :param num:
        :return:

        Convert int to array
        Use radix sort on array
        Create two numbers by adding digits from the smallest alternately to both numbers.
        """
