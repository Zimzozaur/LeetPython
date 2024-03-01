# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        The key is to find number that starts a sequence
        Number that starts a sequence is n - 1 not in set
        When look up in set until end of sequence

        Worst case is loop over whole list and last is one that
        starts a sequence, so again we loop over whole set
        """

        nums_set = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in nums_set:
                i = 1
                while (num + i) in nums_set:
                    i += 1
                longest = max(longest, i)
        return longest
