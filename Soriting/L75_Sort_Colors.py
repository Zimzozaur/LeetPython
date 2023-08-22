# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Use Bucket sort
        """
        colors = [0, 0, 0]

        for num in nums:
            colors[num] += 1

        start = 0
        val = 0
        for i in range(3):
            for j in range(colors[i]):
                nums[start] = val
                start += 1
            val += 1

