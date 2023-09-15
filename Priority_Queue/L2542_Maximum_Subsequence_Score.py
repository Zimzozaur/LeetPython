# https://leetcode.com/problems/maximum-subsequence-score/


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        zipped = zip(nums1, nums2)

        

