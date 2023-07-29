# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        """
        Given an array of positive integers arr,
        return the sum of all possible odd-length sub-arrays of arr.
        A subarray is a contiguous subsequence of the array.
        :param arr:
        :return:

        prefix sum with sliding window approach:
            count all sums
            loop arr.len / 2 times
                use slide fixed size sliding window

            count all sums
            loop n times where n is arr.len / 2
                every time use slide windows starting size 3 and add +2 every iteration.
        """
        result_sum = 0  # Holds a sum of all subarrays

        prefix_sum_array = []  # Contains all prefixes
        prefix_sum = 0  # Holds prefix sum
        for num in arr:
            # Count all prefix sums
            prefix_sum += num
            prefix_sum_array.append(prefix_sum)

        result_sum += prefix_sum  # Adds the sum to the end result.

        array_size = len(arr)  # Holds size to count once

        i = 3  # First odd window

        while i <= array_size:
            # Loops with sliding windows of size i when i is not greater than arr.len
            prefix_sum = prefix_sum_array[i - 1]
            result_sum += prefix_sum

            for j in range(i, array_size):
                # Adds value of a window to result
                prefix_sum = prefix_sum_array[j] - prefix_sum_array[j - i]
                result_sum += prefix_sum

            i += 2  # Increase a window to the next size

        return result_sum


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 1, 1, 1, 1, 1]
    print(sol.sumOddLengthSubarrays(arr))

