# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        """
        You are given a positive integer array nums.
            The element sum is the sum of all the elements in nums.
            The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
        Return the absolute difference between the element sum and digit sum of nums
        :param nums:
        :return:

        Loop over array sum numbers and convert them to string
        Sum all digits in string
        return absolute value
        """

        sum1 = 0
        sum2 = 0
        string_int = ""

        for num in nums:  # Counts the sum of ints and convert them to one string
            sum1 += num
            string_int += str(num)

        for i in range(len(string_int)):  # Counts sum value of digits
            sum2 += int(string_int[i])

        return abs(sum2 - sum1)
