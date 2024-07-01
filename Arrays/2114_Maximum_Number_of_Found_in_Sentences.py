# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        """
        Counts words in every sentence in array and return number of word in the longest sentence
        :param sentences:
        :return:

        Loop over every sentence
            Split word
            count word
            if greater than max length change
            else continue
        """
        return max(len(sentences.split()) for sentences in sentences)
