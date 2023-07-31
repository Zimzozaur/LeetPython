# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        """
        Returns the number of sub-arrays that are of size k and average greater than or equal to the threshold.
        :param arr:
        :param k:
        :param threshold:
        :return:
        """

        if threshold == 0:  # Avoids 0 divisions.
            threshold = 1

        return_int = 0  # Holds the number of arrays that pass a threshold
        window_sum = 0  # Holds a sum of the window

        for i in range(k):  # Creates a first window
            window_sum += arr[i]

        if window_sum / threshold >= k:  # Checks do window pass
            return_int += 1

        for i in range(k, len(arr)):  # Moves a window by one
            window_sum -= arr[i - k]
            window_sum += arr[i]

            if window_sum / threshold >= k:  # Checks do window pass
                return_int += 1

        return return_int


if __name__ == '__main__':
    sol = Solution()
    k = 3
    thresh = 5
    x = [11,13,17,23,29,31,7,5,2,3]
    print(sol.numOfSubarrays(x, k, thresh))