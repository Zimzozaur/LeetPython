from collections import deque
from itertools import combinations


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.allCombinations = list(combinations(characters, combinationLength))
        self.count = 0

    def next(self) -> str:
        self.count += 1
        return "".join(self.allCombinations[self.count - 1])

    def hasNext(self) -> bool:
        return self.count < len(self.allCombinations)


# class CombinationIterator:
#     def __init__(self, characters: str, combinationLength: int):
#         self.string = characters
#         self.positions = deque([i for i in range(combinationLength)])
#         self.limits = [i for i in range(len(characters) - combinationLength, len(characters))]
#         self.has_next = True
#
#     def next(self) -> str:
#         """return string and move pointers to next position"""
#         result = ''.join([self.string[i] for i in self.positions])
#         popped_deck = deque()
#         limits_deck = deque(self.limits)
#         flag = False
#         while limits_deck:
#             popped = self.positions.pop()
#             limit = limits_deck.pop()
#             if popped + 1 <= limit and not flag:
#                 popped_deck.append(popped + 1)
#                 self.positions.extend(popped_deck)
#                 return result
#             elif popped + 1 <= limit and flag:
#                 self.positions.append(popped + 1)
#                 for num in range(1, len(popped_deck) + 1):
#                     self.positions.append(popped + 1 + num)
#                 return result
#
#             popped_deck.appendleft(popped)
#             flag = True
#         self.has_next = False
#         return result
#
#     def hasNext(self) -> bool:
#         return self.has_next

