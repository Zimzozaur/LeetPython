# https://leetcode.com/problems/implement-queue-using-stacks/
from collections import deque


class MyQueue:
    """Create Queue implemented using two Deques behaving like Stack"""

    def __init__(self):
        self.deque_push = deque([])
        self.deque_pop = deque([])

    def push(self, x: int) -> None:
        """
        Push data to tail of Queue
        If needed moves data from pop to push deck
        """
        if not self.deque_pop:
            self.deque_push.append(x)
        else:
            for i in range(len(self.deque_pop)):
                self.deque_push.append(self.deque_pop.pop())
            self.deque_push.append(x)

    def pop(self) -> int:
        """
        Pop data from head of Queue
        If needed moves data from push to pop deck
        """
        if self.deque_push:
            for i in range(len(self.deque_push) - 1):
                self.deque_pop.append(self.deque_push.pop())
            return self.deque_push.pop()
        else:
            return self.deque_pop.pop()

    def peek(self) -> int:
        """
        Look up data from head of Queue
        If needed moves data from push to pop deck
        """
        if self.deque_pop:
            return self.deque_pop[-1]
        else:
            return self.deque_push[0]

    def empty(self) -> bool:
        """Check is Queue empty"""
        if self.deque_push or self.deque_pop:
            return False
        else:
            return True


if __name__ == '__main__':
    que = MyQueue()
    print(que.push(1))
    print(que.push(2))
    print(que.push(3))
    print(que.push(4))
    print(que.pop())
    print(que.push(5))
    print(que.pop())
    print(que.pop())
    print(que.pop())
    print(que.pop())
