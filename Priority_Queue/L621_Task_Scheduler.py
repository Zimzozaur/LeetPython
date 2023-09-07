# https://leetcode.com/problems/task-scheduler/
import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequency = {}
        for task in tasks:
            frequency[task] = frequency.get(task, 0) + 1
        heap = [-value for key, value in frequency.items()]

        heapq.heapify(heap)
        queue = deque([])
        ops = 0
        while heap or queue:
            if heap:
                task = heapq.heappop(heap)
                task += 1
                if task < 0:
                    queue.append([ops + n, task])
            if queue and queue[0][0] == ops:
                heapq.heappush(heap, queue.popleft()[1])
            ops += 1
        return ops

    # This is Big Brain Solution
    # c = Counter(tasks)
    # mostCom = c.most_common(1)
    # k, v = mostCom[0]
    # count = 0
    # for item in c:
    #     if c[item] == v:
    #         count = count + 1
    # minlen = len(tasks)

    # return max(minlen, (n + 1) * (v - 1) + count)


if __name__ == '__main__':
    x = ["A", "A", "A", "B", "B", "B"]
    n = 2
    sol = Solution()
    print(sol.leastInterval(x, n))
