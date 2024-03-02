# https://leetcode.com/problems/squares-of-a-sorted-array/description/?envType=daily-question&envId=2024-03-02
from collections import deque

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """Two pointers comparing absolute value of number"""
        one = 0
        two = len(nums) - 1
        res = deque([])

        for i in range(len(nums)):
            if abs(nums[one]) > abs(nums[two]):
                res.appendleft(nums[one] ** 2)
                one += 1
            else:
                res.appendleft(nums[two] ** 2)
                two -= 1

        return list(res)

