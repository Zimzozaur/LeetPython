# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Finds the biggest difference between two numbers in array
        (num[i] & num[j]: i < j)
        :param prices:
        :return:
        Constrains
        1 <= prices.length <= 105
        0 <= prices[i] <= 104
        """

        array_len = len(prices)

        if array_len < 2:  # Allways zero
            return 0

        biggest = prices[-1]  # Holds biggest number
        best_difference = 0  # Holds biggest difference

        # Loops from back to begging but skip the last element
        for price in prices[array_len - 2::-1]:
            # Finds biggest difference
            if biggest - price > best_difference:
                best_difference = biggest - price
            # Finds biggest number
            if biggest < price:
                biggest = price

        return best_difference


if __name__ == '__main__':
    sol = Solution()
    x = [1, 3, 0, 4]
    print(sol.maxProfit(x))
