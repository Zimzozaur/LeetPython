# https://leetcode.com/problems/koko-eating-bananas/
import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Returns the minimum integer k such that Koko can eat all the bananas within h hours.
        Array is a pile of bananas. Even if she eats faster than the size of a pile, she spends one hour

        To solve this, we need to find the greatest element in piles
        Create a range from 1 to this element
        Perform binary search on this array and check is element the minimum speed
        :param piles:
        :param h:
        :return:
        """

        min_speed = max(piles)

        # Pointers are values and indexes of a virtual array
        left, right = 1, min_speed

        while left <= right:

            k = math.ceil((left + right) / 2)  # Counts k

            hours_needed = 0
            for pile in piles:  # Checks how many hour Koko needs
                hours_needed += math.ceil(pile / k)

            if hours_needed > h:
                left = k + 1
            else:
                min_speed = k
                right = k - 1

        return min_speed


if __name__ == '__main__':
    sol = Solution()
    x = [30,11,23,4,20]
    h = 6
    print(sol.minEatingSpeed(x, h))
