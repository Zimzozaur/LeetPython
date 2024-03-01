# https://leetcode.com/problems/encode-and-decode-strings/
from collections import deque


class Codec:
    def encode(self, strs: list[str]) -> str:
        res = ''
        for s in strs:
            res += f'{s}#{len(s)}#'
        return res

    def decode(self, s: str) -> list[str]:
        deck = deque([])
        end = 1
        start = 1
        while -start > -len(s):
            start += 1
            if s[-start] == '#':
                num = int(s[-start + 1:-end])
                if num > 0:
                    deck.appendleft(s[-start - num:-start])
                else:
                    deck.appendleft('')
                end = start = start + num + 1
        return list(deck)
