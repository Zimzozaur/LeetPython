# https://leetcode.com/problems/first-bad-version/
class Solution:
    def firstBadVersion(self, n: int) -> int:
        """Find smaller number that inputted to isBadVersion returns True"""
        """
        Find highest stat stay False
        
        if False remember the number go up
        if True go down
        """
        start = 1
        end = n
        highest = 0

        while start <= end:

            mid = (start + end) // 2
            api_return = isBadVersion(mid)

            if api_return is True:
                end = mid - 1
            else:
                highest = mid
                start = mid + 1

        return highest + 1


def isBadVersion(version: int) -> bool:
    first_bad = 1

    if version < first_bad:
        return False
    else:
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstBadVersion(10))
