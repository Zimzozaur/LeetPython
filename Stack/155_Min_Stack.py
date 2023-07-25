# https://leetcode.com/problems/min-stack/description/
class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Adds int to stack
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        # Pops int from stack
        val = self.stack.pop()
        if self.min_stack[-1] >= val:
            self.min_stack.pop()

    def top(self) -> int:
        # Returns last value in Stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Returns the smallest value in stack
        return self.min_stack[-1]


if __name__ == '__main__':
    sol = MinStack()
    sol.push(-2)
    sol.push(0)
    sol.push(3)
    sol.pop()
    print(sol.top())
    print(sol.getMin())

