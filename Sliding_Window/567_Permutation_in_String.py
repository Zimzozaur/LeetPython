# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Returns true if one of s1's permutations is the substring of s2.
        :param s1:
        :param s2:
        :return:

        Uses the sliding window and HashMap to compare frequencies of characters.
        """

        dict1_freq = {}  # Keeps frequency of s1
        dict2_freq = {}  # Keeps frequency of Windows

        len_s1 = len(s1)

        if len_s1 > len(s2):  # Always false
            return False

        for char in s1:  # Counts frequency of s1
            dict1_freq[char] = dict1_freq.get(char, 0) + 1

        for i in range(len_s1):  # Counts frequency of the initial window
            dict2_freq[s2[i]] = dict2_freq.get(s2[i], 0) + 1

        if dict1_freq == dict2_freq:  # if s1 equal to window
            return True

        for i in range(len_s1, len(s2)):

            # Removes an element before the window if equal to 1
            if dict2_freq.get(s2[i - len_s1]) == 1:
                dict2_freq.pop(s2[i - len_s1])
            else:
                # Decreases by one
                dict2_freq[s2[i - len_s1]] = dict2_freq.get(s2[i - len_s1]) - 1

            # Add a new element to window
            dict2_freq[s2[i]] = dict2_freq.get(s2[i], 0) + 1

            if dict1_freq == dict2_freq:  # Check is s1 equal to the window
                return True

        return False  # They are not equal


if __name__ == '__main__':
    sol = Solution()
    s1 = "a"
    s2 = "b"
    print(sol.checkInclusion(s1, s2))

