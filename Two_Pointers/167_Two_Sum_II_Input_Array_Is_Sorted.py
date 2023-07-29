# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
import random


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Findex index of two numbers which sum is equal to target.
        Numbers are 1-indexed
        :param numbers:
        :param target:
        :return:

        Two pointers one starts at the beginning and the second at the end
        if sum is greater 2nd goes down
        if sum is smaller 1st goes up.
        """

        pointer1 = 0
        pointer2 = len(numbers) - 1

        while pointer1 < pointer2:
            if numbers[pointer1] + numbers[pointer2] < target:  # Move the pointer up when too small
                pointer1 += 1
            elif numbers[pointer1] + numbers[pointer2] > target:  # Move the pointer down when too big
                pointer2 -= 1
            else:
                return [pointer1 + 1, pointer2 + 1]

