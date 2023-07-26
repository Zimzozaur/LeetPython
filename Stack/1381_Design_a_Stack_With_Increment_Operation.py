# https://leetcode.com/problems/design-a-stack-with-increment-operation/
class CustomStack:
    """
    Builds a stack that supports increment operations on its elements.
    """

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        """
        Adds element one the top of the stack if limit is not reached.
        :param x: Value of the element
        :return: None
        """
        if self.size != self.maxSize:
            self.stack.append(x)
            self.size += 1

    def pop(self) -> int:
        """
        Removes last element from the stack if stack is empty returns -1
        :return: Value of an element or -1
        """
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        """
        Increments elements of a stack from beginning to end.
        :param k: Number of elements to increase
        :param val: Number of values to increment
        :return: None
        """
        if k > self.size:
            for i in range(self.size):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val


if __name__ == '__main__':
    stk = CustomStack(3)                  # Stack is Empty []
    stk.push(1)                           # stack becomes [1]
    stk.push(2)                           # stack becomes [1, 2]
    stk.pop()                             # return 2 --> Return top of the stack 2, stack becomes [1]
    stk.push(2)                           # stack becomes [1, 2]
    stk.push(3)                           # stack becomes [1, 2, 3]
    stk.push(4)                           # stack still [1, 2, 3], Do not add another elements as size is 4
    stk.increment(5, 100)                 # stack becomes [101, 102, 103]
    stk.increment(2, 100)                 # stack becomes [201, 202, 103]
    stk.pop()                             # return 103 --> Return top of the stack 103, stack becomes [201, 202]
    stk.pop()                             # return 202 --> Return top of the stack 202, stack becomes [201]
    stk.pop()                             # return 201 --> Return top of the stack 201, stack becomes []
    stk.pop()                             # return -1 --> Stack is empty return -1

