# https://leetcode.com/problems/maximum-number-of-balloons/description/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Count frequency of letters
        Remove every set of letters needed to create new word
        """
        balloon = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for char in text:
            if char in balloon:
                balloon[char] += 1

        balloon['l'] //= 2
        balloon['o'] //= 2
        return min(balloon.values())
