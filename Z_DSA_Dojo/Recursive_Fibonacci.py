
def fibonacci(n):
    """Count nth element of Fibonacci sequence"""

    if n < 3:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(19))

