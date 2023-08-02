# https://leetcode.com/problems/left-and-right-sum-differences/
class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        """
        Takes sum of every index after i (right) and before i (left)
        Builds array of indexes = | left - right |
        :param nums:
        :return:

        Create two arrays right and result
        Loop from right to left and put sum into right array
        Loop form left to right and perform math operation
            Put result into result array
        """

        limit = len(nums)
        right = []
        result = []
        sum_right = 0
        for i in range(limit - 1, -1, -1):
            # Adds sum of element before i
            right.insert(0, sum_right)
            sum_right += nums[i]

        sum_left = 0
        for index, num in enumerate(nums):
            # Adds results of operations to result array
            equation = right[index] - sum_left
            if equation < 0:
                # Performs absolute value
                equation *= -1
            result.append(equation)
            sum_left += nums[index]

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.leftRightDifference([1, 2, 3, 4]))
