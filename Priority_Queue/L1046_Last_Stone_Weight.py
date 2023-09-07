# https://leetcode.com/problems/last-stone-weight/
import heapq
import random


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """

        """
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 < stone2:
                heapq.heappush(stones, stone1 - stone2)

        stones.append(0)
        return abs(stones[0])


if __name__ == '__main__':
    sol = Solution()
    x = [random.randint(1, 1000) for num in range(30)]
    print(x)
    print(sol.lastStoneWeight(x))
