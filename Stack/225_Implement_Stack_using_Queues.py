# https://leetcode.com/problems/implement-stack-using-queues/
import queue


class MyStack:
    """
    Stack implementation using only Queue:
        Push add at the end O(n)
        Empty check is there element O(n)
        Pop - pop and add elements len - 1 times and return additional pop O(n)
        Top - pop and add elements len - 1 times and return additional pop  O(n)
    """

    def __init__(self):
        self.stack_queue = queue.Queue()

    def push(self, x: int) -> None:
        """Add an element at the end of a Queue"""
        self.stack_queue.put(x)

    def pop(self) -> int:
        """Loop over the Queue and remove last element"""
        for i in range(self.stack_queue.qsize() - 1):
            self.stack_queue.put(self.stack_queue.get())
        return self.stack_queue.get()

    def top(self) -> int:
        """Return a top element of the stack"""
        for i in range(self.stack_queue.qsize() - 1):
            self.stack_queue.put(self.stack_queue.get())
        num = self.stack_queue.get()
        self.stack_queue.put(num)
        return num

    def empty(self) -> bool:
        """Check is Stack empty"""
        return self.stack_queue.empty()
