# https://leetcode.com/problems/find-pivot-index/description/


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        total = sum(nums)

        for index, num in enumerate(nums):
            left += num
            if left == total:
                return index
            total -= num

        return - 1


