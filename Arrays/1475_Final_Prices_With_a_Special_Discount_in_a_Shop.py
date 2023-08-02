class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        """
        Checks is any number starting from index + 1 same or smaller
        If yes subtract this value from the number
        prices[i] = int
        Discount -> prices[i] - prices[j]
        j > i and prices[j] <= prices[i].
        Return answer[i]
        :param prices:
        :return:
        """

        result = [prices[-1]]

        for i in range(len(prices) - 2, -1, -1):
            # Loops backward
            executed = False
            for j in range(i + 1, len(prices)):
                # Loop forward to compare numbers
                if prices[i] >= prices[j]:
                    # Subtract value and insert in array
                    result.append(prices[i] - prices[j])
                    executed = True
                    break

            if not executed:
                result.append(prices[i])

        result.reverse()  # Revers to correct order
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.finalPrices([8,7,4,2,8,1,7,7,10,1]))
