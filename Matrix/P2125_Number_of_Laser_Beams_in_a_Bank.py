# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
from collections import Counter

class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        """
        Create array with number of lasers on levels with laser
        multiply them and return
        """
        lasers = []
        for arr in bank:
            c = Counter(arr)
            if '1' in c:
                lasers.append(c['1'])

        if len(lasers) == 0:
            return 0

        counter = 0
        first = lasers[0]
        for laser in lasers[1:]:
            counter += first * laser
            first = laser

        return counter

