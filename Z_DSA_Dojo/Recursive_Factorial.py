
def factorial(n):

    # Base Case
    if n < 2:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':

    nums = [1,1,2,6,24,120,720,5040,40320,362880,3628800]

    for i in range(1, 11):
        if nums[i] != factorial(i):
            print("FALSE")
    print("DONE")
