# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Input is a sorted rotated array nums of unique elements,
        returns the minimum element of this array.

        Key if to find the biggest number coz next is the smallest
        :param nums:
        :return:
        """

        if len(nums) == 1:  # When len 1
            return nums[0]

        if nums[0] < nums[-1]:  # When without rotation
            return nums[0]

        left = 0
        right = len(nums) - 1

        while True:

            mid = (left + right) // 2  # Count the mid-point

            if nums[mid] > nums[mid + 1]:  # When found the biggest
                return nums[mid + 1]

            if nums[mid] < nums[left]:
                # Compares edges to the mid and narrows the range
                right = mid - 1
            else:
                left = mid + 1


if __name__ == '__main__':
    sol = Solution()
    arr = [3, 4, 5, 1, 2]

    print(sol.findMin(arr))

