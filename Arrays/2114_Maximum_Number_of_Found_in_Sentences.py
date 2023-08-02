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

        # return max([len(sentences.split()) for sentences in sentences]) Or using list comprehension

        maxWords = 0
        for sentence in sentences:
            sentence = sentence.split()  # Split sentence to words
            words = 0
            for _ in sentence:
                # Counts words
                words += 1
            if words > maxWords:
                # Compares max to current length
                maxWords = words

        return maxWords


if __name__ == '__main__':
    sol = Solution()
    print(sol.mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"]))