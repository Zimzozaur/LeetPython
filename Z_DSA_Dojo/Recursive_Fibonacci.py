import time


def fibonacci(n):
    """Count nth element of Fibonacci sequence"""

    if n < 3:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)


def fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    return result


def fibonacci_memoized(n):
    memo = [None] * (n + 1)
    return fib(n, memo)


def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]


if __name__ == '__main__':

    nth = 1500

    start_time_1 = time.time()
    for _ in range(nth):
        fib_bottom_up(nth)
    end_time_1 = time.time()
    execution_time_1 = end_time_1 - start_time_1

    print(f"Function 1 execution time: {execution_time_1} seconds")


