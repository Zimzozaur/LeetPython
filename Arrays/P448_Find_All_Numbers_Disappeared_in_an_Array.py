# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums_set = set(nums)
        return [num for num in range(1, len(nums) + 1) if num not in nums_set]
