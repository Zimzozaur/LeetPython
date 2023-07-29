# https://leetcode.com/problems/truncate-sentence/
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Takes string of words divided by spaces.
        Returns k words.
        :param s:
        :param k:
        :return:

        Splits string
        Return string that is the length of a k index.
        """

        new_string = s.split()
        new_word = ""

        for i in range(k):
            new_word += new_string[i] + " "  # Builds new string and adds spaces.

        return new_word[:len(new_word) - 1]  # Cuts last space.
