# https://leetcode.com/problems/maximum-odd-binary-number/

from collections import Counter

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter = Counter(s)
        res = ''.join(('1' for _ in range(counter['1']-1)))
        res += ''.join(('0' for _ in range(counter['0'])))
        return res + '1'


