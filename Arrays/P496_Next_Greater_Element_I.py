# https://leetcode.com/problems/next-greater-element-i/description/


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        hash_map = {}

        for num in nums2:
            while stack and stack[-1] < num:
                hash_map[stack.pop()] = num
            stack.append(num)

        return [hash_map.get(num, -1) for num in nums1]
