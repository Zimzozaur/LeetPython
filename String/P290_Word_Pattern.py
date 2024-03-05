# https://leetcode.com/problems/word-pattern/description/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(' ')
        if len(arr) != len(pattern):
            return False

        word_letter = {}
        letter_word = {}

        for let, word in zip(pattern, arr):
            if word not in word_letter and let not in letter_word:
                word_letter[word] = let
                letter_word[let] = word
            elif word in word_letter and word_letter[word] == let:
                continue
            else:
                return False
        return True


