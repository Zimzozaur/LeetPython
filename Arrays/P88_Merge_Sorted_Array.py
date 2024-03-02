# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        3 pointers are needed:
            One starts at the end of first arr - m
            Two starts at the end of numbers in first arr - n
            Three starts at the end of numbers in second arr - o (m+n)

        if one and two > 0 - compare
        elif one > 0 - return
        else - input all from 2
        """
        if n == 0:
            return None

        one = m - 1
        two = n - 1

        for i in range(1, m + n + 1):
            if one >= 0 and two >= 0 and nums1[one] > nums2[two]:
                nums1[-i] = nums1[one]
                one -= 1
            elif two >= 0:
                nums1[-i] = nums2[two]
                two -= 1
            else:
                return
