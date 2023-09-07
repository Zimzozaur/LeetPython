# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for pointer in points:
            pointer1 = math.sqrt(pointer[0] ** 2 + pointer[1] ** 2)
            tup = [pointer1, pointer]
            heapq.heappush(heap, tup)

        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == '__main__':
    sol = Solution()
    points = [[1, 3], [-2, 2]]
    k = 2
    x = sol.kClosest(points, k)
    print(x)
