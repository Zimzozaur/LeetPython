# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/?envType=daily-question&envId=2024-03-05


class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        end = len(s) - 1

        while True:
            if start < end and s[start] == s[end]:
                char = s[start]
                while start <= end and s[start] == char:
                    start += 1
                while start <= end and s[end] == char:
                    end -= 1
            else:
                break

        return end - start + 1 if end >= start else 0
