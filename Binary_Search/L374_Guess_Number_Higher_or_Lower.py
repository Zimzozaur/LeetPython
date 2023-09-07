# https://leetcode.com/problems/guess-number-higher-or-lower/

class Solution:

    def guessNumber(self, n: int) -> int:
        """
        Return picked number in range from one to n where bool about
        picked number is returned by guess function
        """
        start = 1
        end = n

        while start <= end:

            mid = (start + end) // 2
            api_return = guess(mid)

            if api_return > 0:
                start = mid + 1
            elif api_return < 0:
                end = mid - 1
            else:
                return mid

def guess(n):

    pick = 2543

    if n > pick:
        return -1
    elif n < pick:
        return 1
    else:
        return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.guessNumber(1000000000))
