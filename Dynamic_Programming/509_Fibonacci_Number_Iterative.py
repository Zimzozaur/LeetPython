# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        """Count nth Fibonacci Number"""
        fib_sum = 0
        fib1 = 0  # Start at 0th
        fib2 = 1  # Start at 1st
        for i in range(n - 1):
            fib_sum = fib2 + fib1
            fib1 = fib2
            fib2 = fib_sum

        return fib_sum


if __name__ == '__main__':
    sol = Solution()
    print(sol.fib(2))

