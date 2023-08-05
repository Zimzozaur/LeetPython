# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Return list of ints that are common for both lists"""
        one = set(nums1)
        two = set(nums2)

        return list(one.intersection(two))


if __name__ == '__main__':
    sol = Solution()
    one = [4,9,5]
    two = [9,4,9,8,4]
    print(sol.intersection(one, two))