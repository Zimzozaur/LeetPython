# https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Boyer–Moore majority vote algorithm
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        counter = 0
        integer = None

        for num in nums:
            if counter == 0:
                integer = num
            counter += (1 if num == integer else -1)

        return integer


