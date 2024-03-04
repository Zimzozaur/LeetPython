# https://leetcode.com/problems/bag-of-tokens/description/?envType=daily-question&envId=2024-03-04
from collections import deque


class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        deck = deque(sorted(tokens))
        max_score = 0
        curr = 0

        while deck:
            first = deck.popleft()
            if power >= first:
                power -= first
                curr += 1
                max_score = max(max_score, curr)
                continue
            deck.appendleft(first)
            if curr > 0:
                power += deck.pop()
                curr -= 1
            else:
                break

        return max_score
