# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        """
        Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
        :param word1:
        :param word2:
        :return:

        Use array comparison to merge strings into one word and compare them
        """

        done1 = ""
        done2 = ""
        for word in word1:
            done1 += word
        for word in word2:
            done2 += word

        return done1 == done2
