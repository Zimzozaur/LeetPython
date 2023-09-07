# https://leetcode.com/problems/kth-largest-element-in-a-stream/
import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            if self.heap[0] < val:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
            return self.heap[0]
        heapq.heappush(self.heap, val)
        return self.heap[0]




if __name__ == '__main__':
    x = [4, 5, 8, 2]
    size = 3
    sol = KthLargest(size, x)
    vals = [3, 5, 10, 9, 4]
    for num in vals:
        print(sol.add(num))
