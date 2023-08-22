# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        """Return the sorted string in decreasing order based on the frequency of the characters."""

        return_string = ""
        frequency_dict = {}

        for char in s:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

        keys = list(frequency_dict.keys())

        while frequency_dict:
            biggest = -1
            biggest_index = -1
            for index, char in enumerate(keys):
                if frequency_dict.get(char) > biggest:
                    biggest = frequency_dict.get(char)
                    biggest_index = index

            char = keys[biggest_index]
            return_string += char * frequency_dict.get(char)

            frequency_dict.pop(char)
            keys.pop(biggest_index)

        return return_string






