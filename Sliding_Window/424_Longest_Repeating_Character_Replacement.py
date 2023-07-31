# https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the longest substring where every character is the same
        But you can change k times any char to make it longer.
        :param s:
        :param k:
        :return:
        """
        # This solution uses two pointers / dynamic sliding window

        frequency = {}  # Holds frequency of each character
        longest = 0  # Longest length
        curr_len = 0  # Current length
        i = 0  # Pointer 1
        j = 0  # Pointer 2

        while j < len(s):
            frequency[s[j]] = frequency.get(s[j], 0) + 1  # +1 to char
            curr_len += 1
            j += 1

            while sum(frequency.values()) - max(frequency.values()) > k:  # If more chars to change than K
                frequency[s[i]] = frequency.get(s[i]) - 1  # -1 to current char.
                curr_len -= 1
                i += 1  # Moves i by one

            if curr_len > longest:  # Check is longer
                longest = curr_len

        return longest


if __name__ == '__main__':
    sol = Solution()
    x = "IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR"
    print(sol.characterReplacement(x, 2))
