# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2024-03-08
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        c = Counter(nums)
        biggest = max(c.values())
        return sum(filter(lambda x: x == biggest, c.values()))



