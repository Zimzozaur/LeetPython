# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Find number using binary search in the rotated array
        :param nums:
        :param target:
        :return:

        1 2 3 4 5 6 7
        2 3 4 5 6 7 1
        3 4 5 6 7 1 2
        4 5 6 7 1 2 3
        5 6 7 1 2 3 4
        6 7 1 2 3 4 5
        7 1 2 3 4 5 6

        left  = 1 2 3 4 5 6 7
        mid   = 4 5 6 7 1 2 3
        right = 7 1 2 3 4 5 6

        """

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            # right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.search([5, 6, 0, 1, 2, 3, 4], 0))

